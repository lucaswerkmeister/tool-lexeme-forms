import babel
import string


class PluralFormatter(string.Formatter):
    """A string formatter supporting a !p plural conversion.

    Format string examples:

        "I ate {count} {count!p:one=apple:other=apples}."
        "{size} (0x{size:04X}) {size!p:one=bajt:two=bajtaj:few=bajty:other=bajtow}"

    For numeric values converted with !p, the format spec is
    interpreted differently: it consists of a set of tag=text specs,
    separated by colons. The tag should match one of the CLDR plural
    rule tags, currently zero, one, two, few, many, or other (though
    most languages do not use all possible tags). The text for the
    matching tag, according to the plural rules of the locale
    specified in the constructor, is substituted into the message. For
    all other values, the format spec is interpreted as usual."""

    def __init__(self, locale_identifier):
        """The locale identifier must be understood by Locale.parse."""
        self.locale = babel.Locale.parse(locale_identifier)

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
        tag = self.locale.plural_form(self.value)
        tag_eq = tag + '='
        for plural in plurals:
            if plural.startswith(tag_eq):
                return plural[len(tag_eq):]
        raise KeyError('No plural for tag {} found in format spec {}!'.format(tag, format_spec))
