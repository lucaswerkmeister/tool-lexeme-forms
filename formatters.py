"""A collection of formatters for i18n messages.

You usually want to use I18nFormatter, which combines all the other
formatters in this module. Create it like this:

    formatter = I18nFormatter(locale_identifier='en',
                              get_gender=lambda arg: 'n')

And then use format strings such as:

    formatter.format('You have {count!p:one=one message:other={count} messages} from {users!l}.',
                     count=len(messages),
                     users=set(users))
    formatter.format('Reply to {user!g:m=him:f=her:n=them}?',
                     user=user)

See the documentation of the other formatter classes for details on
the supported conversions.

If the markupsafe module is available, then all the formatters defined
in this module become MarkupSafe-aware: if the format string is
Markup, then the returned formatted value will also be Markup, and any
non-Markup arguments will be escaped."""


import babel
import babel.lists
import string


try:
    import markupsafe
except ModuleNotFoundError:
    markup_type = str

    class BaseI18nFormatter(string.Formatter):
        """Base class of our i18n formatters."""

        type_of_format_string = str

        def __init__(self, **kwargs):
            """Strip away all constructor arguments.

            string.Formatter complains if it gets any constructor
            arguments, but our individual constructors need to pass
            through their constructor arguments so the classes can be
            combined freely, so we throw away the arguments here."""
            super().__init__()

        def escape(self, s):
            """No-op function with a signature matching the escape below.

            Used by HyperlinkFormatter / _Hyperlink."""
            return s
else:
    markup_type = markupsafe.Markup  # type: ignore

    class BaseI18nFormatter(markupsafe.EscapeFormatter):  # type: ignore
        """Base class of our i18n formatters."""

        """Empty base class stripping away constructor arguments and passing
        the right escape method to MarkupSafe’s EscapeFormatter."""

        type_of_format_string = None

        def __init__(self, **kwargs):
            """Use a context-sensitive escape function.

            EscapeFormatter calls the escape function on all fields,
            since it expects to be reached through Markup.format(),
            i.e. we know we’ll want to produce Markup and escape
            strings. We change this so that fields are only escaped if
            the format string was Markup in the first place.

            Also, throw away other constructor arguments, so that
            string.Formatter doesn’t complain about them."""

            def escape(s):
                if issubclass(self.type_of_format_string, markupsafe.Markup):
                    return markupsafe.Markup.escape(s)
                else:
                    return s

            super().__init__(escape=escape)

        def vformat(self, format_string, args, kwargs):
            """Store the type of the format string and apply it to the result.

            string.Formatter is partially implemented in C, so the
            format spec when formatting individual fields is always a
            string, never a Markup object. To still allow fields to
            properly format themselves as markup, store the type of
            the format string here. Also, apply it to the final result
            of string formatting."""

            self.type_of_format_string = type(format_string)
            try:
                ret = super().vformat(format_string, args, kwargs)
                return self.type_of_format_string(ret)
            finally:
                self.type_of_format_string = None


class PluralFormatter(BaseI18nFormatter):
    """A string formatter supporting a !p plural conversion.

    Format string examples:

        "I ate {count!p:0=no apples:one={count} apple:other={count} apples}."
        "{size} (0x{size:04X}) {size!p:one=bajt:two=bajtaj:few=bajty:other=bajtow}"

    For numeric values converted with !p, the format spec is
    interpreted differently: it consists of a set of key=text specs,
    separated by colons. The key should be one of the CLDR plural rule
    tags, currently “zero”, “one”, “two”, “few”, “many”, or “other”,
    or an explicit value. The text for the matching value or tag,
    according to the plural rules of the locale specified in the
    constructor, is substituted into the message. Attempting to
    convert non-numeric values with !p is an error.

    Note that most languages do not use all possible tags, and only
    exactly those tags used in a language should occur in the format
    string. For example, even though there is a “zero” tag, English
    only uses the “one” and “other” ones, and to make a special case
    for a value of zero with a PluralFormatter('en'), you need to use
    the key “0”, not “zero”. On the other hand, failing to specify all
    tags used in a language may make the formatter raise a KeyError:
    for instance, if the first example above used the key “1” instead
    of “one”, then it would fail when given a count of -1 or 1.0.

    Value keys always take precedence over tag keys, no matter in
    which order they are specified in the format spec. To match the
    value, they must be identical to the str() of the value: for
    instance, a “1” key will not match a 1.0 value or vice versa."""

    def __init__(self, *, locale_identifier, **kwargs):
        """The locale identifier must be understood by Locale.parse."""
        self.locale = babel.Locale.parse(locale_identifier)
        super().__init__(locale_identifier=locale_identifier, **kwargs)

    def convert_field(self, value, conversion):
        if conversion == 'p':
            return _Plural(value, self.locale, self.type_of_format_string)
        return super().convert_field(value, conversion)


class _Plural:
    """Wrapper around a numeric value with special formatting.

    This class formats itself as described in PluralFormatter."""

    def __init__(self, value, locale, type_of_format_spec):
        self.value = value
        self.locale = locale
        self.type_of_format_spec = type_of_format_spec

    def __format__(self, format_spec):
        format_spec = self.type_of_format_spec(format_spec)
        plurals = format_spec.split(':')
        value_eq = str(self.value) + '='
        for plural in plurals:
            if plural.startswith(value_eq):
                return plural[len(value_eq):]
        tag = self.locale.plural_form(self.value)
        tag_eq = tag + '='
        for plural in plurals:
            if plural.startswith(tag_eq):
                return plural[len(tag_eq):]
        # fall back to "other"
        for plural in plurals:
            if plural.startswith('other='):
                return plural[len('other='):]
        raise KeyError('No plurals for tag "{}" or "other" found in format spec "{}"!'.format(tag, format_spec))


class CommaSeparatedListFormatter(BaseI18nFormatter):
    """A string formatter supporting a !l list conversion.

    Format string example:

        "We went to {cities!l}."

    For iterable values converted with !l, the format spec is applied
    to each list element. Afterwards, the list elements are joined
    into a standard list using the locale specified in the
    constructor. (For English, this means separating most items with
    an ASCII comma plus a space, and the final two with an extra
    “and”; Chinese and Japanese, for instance, use a fullwidth comma
    instead.) Attempting to convert non-iterable values with !l is an
    error."""

    def __init__(self, *, locale_identifier, **kwargs):
        """The locale identifier must be understood by Locale.parse."""
        self.locale = babel.Locale.parse(locale_identifier)
        # convert Babel’s list patterns to Markup
        for style in self.locale.list_patterns:
            for key, pattern in self.locale.list_patterns[style].items():
                self.locale.list_patterns[style][key] = markup_type(pattern)
        super().__init__(locale_identifier=locale_identifier, **kwargs)

    def convert_field(self, value, conversion):
        if conversion == 'l':
            return _CommaSeparatedList(value, self.locale, self.type_of_format_string, self.format_field)
        return super().convert_field(value, conversion)


class _CommaSeparatedList:
    """Wrapper around a list with special formatting.

    This class formats itself as described in CommaSeparatedListFormatter."""

    def __init__(self, value, locale, type_of_format_spec, format_function):
        self.value = value
        self.locale = locale
        self.type_of_format_spec = type_of_format_spec
        self.format_function = format_function

    def __format__(self, format_spec):
        format_spec = self.type_of_format_spec(format_spec)
        formatted_values = [markup_type(self.format_function(item, format_spec)) for item in self.value]
        return babel.lists.format_list(formatted_values, locale=self.locale)


class GenderFormatter(BaseI18nFormatter):
    """A string formatter supporting a !g grammatical gender conversion.

    Format string examples:

        "Leave a message on {user!g:m=his:f=her:n=their} talk page."
        "Ci dispiace, ma non sei {user!g:m=autorizzato:f=autorizzata:n=autorizzato/a} a usare il caricamento di massa."

    The formatted value, which can be anything as far as this
    formatter is concerned, is passed into a function specified in the
    constructor, which should return one of the values "m", "f", or
    "n", to select the grammatically masculine, feminine, or neutral
    replacement, respectively. The format spec specifies these three
    replacements separated by colons. Gender values not specified in
    the format spec fall back to "m"."""

    def __init__(self, *, get_gender, **kwargs):
        self.get_gender = get_gender
        super().__init__(get_gender=get_gender, **kwargs)

    def convert_field(self, value, conversion):
        if conversion == 'g':
            return _Gender(value, self.get_gender, self.type_of_format_string)
        return super().convert_field(value, conversion)


class _Gender:
    """Wrapper around a value with special formatting.

    This class formats itself as described in GenderFormatter."""

    def __init__(self, value, get_gender, type_of_format_spec):
        self.value = value
        self.get_gender = get_gender
        self.type_of_format_spec = type_of_format_spec

    def __format__(self, format_spec):
        format_spec = self.type_of_format_spec(format_spec)
        replacements = format_spec.split(':')
        gender = self.get_gender(self.value)
        gender_eq = gender + '='
        for replacement in replacements:
            if replacement.startswith(gender_eq):
                return replacement[len(gender_eq):]
        # fall back to "m"
        for replacement in replacements:
            if replacement.startswith('m='):
                return replacement[len('m='):]
        raise KeyError('No replacement for gender "{}" or "m" found in format spec "{}"!'.format(gender, format_spec))


class HyperlinkFormatter(BaseI18nFormatter):
    """A string formatter supporting an !h hyperlink conversion.

    Format string example:

        "You need to {url!h:log in} before you can edit."

    The formatted value is interpreted as the href attribute of an
    HTML <a> element, whose inner HTML is given by the format spec."""

    def convert_field(self, value, conversion):
        if conversion == 'h':
            return _Hyperlink(value, self.type_of_format_string, self.escape)
        return super().convert_field(value, conversion)


class _Hyperlink:
    """Wrapper around a URL with special formatting.

    This class formats itself as described in HyperlinkFormatter."""

    def __init__(self, value, type_of_format_spec, escape):
        self.value = value
        self.type_of_format_spec = type_of_format_spec
        self.escape = escape

    def __format__(self, format_spec):
        format_spec = self.type_of_format_spec(format_spec)
        # turn the value into the type of the format spec,
        # so that if format spec is str and value is Markup,
        # the value doesn’t escape everything around it –
        # but first escape the value, in case it’s str
        # and the format spec is Markup
        value = self.type_of_format_spec(self.escape(self.value))
        return (self.type_of_format_spec(r'<a href="') +
                value +
                self.type_of_format_spec(r'">') +
                format_spec +
                self.type_of_format_spec(r'</a>'))


class I18nFormatter(PluralFormatter, CommaSeparatedListFormatter, GenderFormatter, HyperlinkFormatter):

    """A string formatter supporting !p (plural), !l (list),
    !g (gender) and !h (hyperlink) conversions.

    See PluralFormatter, CommaSeparatedListFormatter,
    HyperlinkFormatter and GenderFormatter for details."""
