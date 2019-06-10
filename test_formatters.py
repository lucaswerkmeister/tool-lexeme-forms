import pytest

import formatters


@pytest.mark.parametrize('count, expected', [
    (1, 'I ate 1 apple.'),
    (2, 'I ate 2 apples.'),
    (0, 'I ate no apples.'),
])
def test_PluralFormatter_en(count, expected):
    plural_formatter = formatters.PluralFormatter('en')
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
    plural_formatter = formatters.PluralFormatter('hsb')
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
    plural_formatter = formatters.PluralFormatter('en')
    assert plural_formatter.format(
        '{num!p:0=zero:1=one:2=two:other=other}',
        num=num
    ) == expected

def test_PluralFormatter_explicit_takes_precedence():
    plural_formatter = formatters.PluralFormatter('en')
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
    plural_formatter = formatters.PluralFormatter('en')
    with pytest.raises(type):
        plural_formatter.format(format_spec, 1)
