import pytest

import formatters


@pytest.mark.parametrize('count, expected', [
    (1, 'I ate 1 apple.'),
    (2, 'I ate 2 apples.'),
    (0, 'I ate no apples.'),
])
def test_PluralFormatter_en(count, expected):
    plural_formatter = formatters.PluralFormatter(locale_identifier='en')
    assert plural_formatter.format(
        'I ate {count!p:0=no apples:one={count} apple:other={count} apples}.',
        count=count
    ) == expected

@pytest.mark.parametrize('size, expected', [
    (1, '1 (0x0001) bajt'),
    (2, '2 (0x0002) bajtaj'),
    (3, '3 (0x0003) bajty'),
    (4, '4 (0x0004) bajty'),
    (5, '5 (0x0005) bajtow'),
])
def test_PluralFormatter_hsb(size, expected):
    plural_formatter = formatters.PluralFormatter(locale_identifier='hsb')
    assert plural_formatter.format(
        '{size} (0x{size:04X}) {size!p:one=bajt:two=bajtaj:few=bajty:other=bajtow}',
        size=size
    ) == expected

@pytest.mark.parametrize('num, expected', [
    (0, 'zero'),
    (1, 'one'),
    (2, 'two'),
    (3, 'other'),
    (0.0, 'other'),
])
def test_PluralFormatter_explicit(num, expected):
    plural_formatter = formatters.PluralFormatter(locale_identifier='en')
    assert plural_formatter.format(
        '{num!p:0=zero:1=one:2=two:other=other}',
        num=num
    ) == expected

def test_PluralFormatter_explicit_takes_precedence():
    plural_formatter = formatters.PluralFormatter(locale_identifier='en')
    assert plural_formatter.format(
        '{num!p:other=other:0=zero}',
        num=0
    ) == 'zero'

@pytest.mark.parametrize('format_spec, type', [
    ('{!p}', KeyError),
    ('{!p:}', KeyError),
    ('{!p:en:other=missing plural for one}', KeyError),
])
def test_PluralFormatter_invalid_format_spec(format_spec, type):
    plural_formatter = formatters.PluralFormatter(locale_identifier='en')
    with pytest.raises(type):
        plural_formatter.format(format_spec, 1)


@pytest.mark.parametrize('list, expected', [
    (['FLAC'], 'FLAC.'),
    (['FLAC', 'OGG'], 'FLAC and OGG.'),
    (['FLAC', 'OGG', 'OPUS'], 'FLAC, OGG, and OPUS.'),
])
def test_CommaSeparatedListFormatter_en(list, expected):
    comma_separated_list_formatter = formatters.CommaSeparatedListFormatter(locale_identifier='en')
    assert comma_separated_list_formatter.format(
        '{list!l}.',
        list=list
    ) == expected


@pytest.mark.parametrize('list, expected', [
    (['FLAC'], 'FLAC.'),
    (['FLAC', 'OGG'], 'FLAC和OGG.'),
    (['FLAC', 'OGG', 'OPUS'], 'FLAC、OGG和OPUS.'),
])
def test_CommaSeparatedListFormatter_zh(list, expected):
    comma_separated_list_formatter = formatters.CommaSeparatedListFormatter(locale_identifier='zh')
    assert comma_separated_list_formatter.format(
        '{list!l}.',
        list=list
    ) == expected


def test_CommaSeparatedListFormatter_formats_list_items_with_format_spec():
    comma_separated_list_formatter = formatters.CommaSeparatedListFormatter(locale_identifier='en')
    assert comma_separated_list_formatter.format(
        'The binaries are {sizes!l:04d} bytes large.',
        sizes=[64, 128, 256, 1024, 4096]
    ) == 'The binaries are 0064, 0128, 0256, 1024, and 4096 bytes large.'


@pytest.mark.parametrize('gender, expected', [
    ('m', 'Thank him?'),
    ('f', 'Thank her?'),
    ('n', 'Thank them?'),
])
def test_GenderFormatter(gender, expected):
    user = 'opaque value'
    def get_gender(value):
        assert value == user
        return gender
    gender_formatter = formatters.GenderFormatter(get_gender=get_gender)
    assert gender_formatter.format(
        'Thank {user!g:m=him:f=her:n=them}?',
        user=user
    ) == expected


@pytest.mark.parametrize('formats, user, expected', [
    (['FLAC'], 'Keith', 'His preferred format is FLAC.'),
    (['FLAC', 'OGG'], 'Keira', 'Her preferred formats are FLAC and OGG.'),
    (['FLAC', 'OGG', 'OPUS'], 'Kim', 'Their preferred formats are FLAC, OGG, and OPUS.'),
])
def test_I18nFormatter_en(formats, user, expected):
    genders = {
        'Keith': 'm',
        'Keira': 'f',
        'Kim': 'n',
    }
    i18n_formatter = formatters.I18nFormatter(locale_identifier='en',
                                              get_gender = lambda value: genders[value])
    assert i18n_formatter.format(
        '{user!g:m=His:f=Her:n=Their} preferred {count!p:one=format is:other=formats are} {formats!l}.',
        user=user,
        count=len(formats),
        formats=formats
    ) == expected
