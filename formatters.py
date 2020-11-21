import babel
import babel.lists
import string


class BaseI18nFormatter(string.Formatter):
    """Empty base class stripping away constructor arguments."""

    def __init__(self, **kwargs):
        super().__init__()


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
            return _Plural(value, self.locale)
        return super().convert_field(value, conversion)


class _Plural:
    """Wrapper around a numeric value with special formatting.

    This class formats itself as described in PluralFormatter."""

    def __init__(self, value, locale):
        self.value = value
        self.locale = locale

    def __format__(self, format_spec):
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
        raise KeyError('No plural for tag {} found in format spec {}!'.format(tag, format_spec))


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
        super().__init__(locale_identifier=locale_identifier, **kwargs)

    def convert_field(self, value, conversion):
        if conversion == 'l':
            return _CommaSeparatedList(value, self.locale)
        return super().convert_field(value, conversion)


class _CommaSeparatedList:
    """Wrapper around a list with special formatting.

    This class formats itself as described in CommaSeparatedListFormatter."""

    def __init__(self, value, locale):
        self.value = value
        self.locale = locale

    def __format__(self, format_spec):
        return babel.lists.format_list([format(item, format_spec) for item in self.value], locale=self.locale)


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
    replacements separated by colons."""

    def __init__(self, *, get_gender, **kwargs):
        self.get_gender = get_gender
        super().__init__(get_gender=get_gender, **kwargs)

    def convert_field(self, value, conversion):
        if conversion == 'g':
            return _Gender(value, self.get_gender)
        return super().convert_field(value, conversion)


class _Gender:
    """Wrapper around a value with special formatting.

    This class formats itself as described in GenderFormatter."""

    def __init__(self, value, get_gender):
        self.value = value
        self.get_gender = get_gender

    def __format__(self, format_spec):
        replacements = format_spec.split(':')
        gender = self.get_gender(self.value)
        gender_eq = gender + '='
        for replacement in replacements:
            if replacement.startswith(gender_eq):
                return replacement[len(gender_eq):]
        raise KeyError('No replacement for gender {} found in format spec {}!'.format(gender, format_spec))


class I18nFormatter(PluralFormatter, CommaSeparatedListFormatter, GenderFormatter):

    """A string formatter supporting !p (plural), !l (list) and !g (gender) conversions.

    See PluralFormatter, CommaSeparatedListFormatter and GenderFormatter for details."""
