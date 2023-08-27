from markupsafe import Markup
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
    ('{!p:0=missing plural for other}', KeyError),
])
def test_PluralFormatter_invalid_format_spec(format_spec, type):
    plural_formatter = formatters.PluralFormatter(locale_identifier='en')
    with pytest.raises(type):
        plural_formatter.format(format_spec, 1)


def test_PluralFormatter_fallback():
    plural_formatter = formatters.PluralFormatter(locale_identifier='en')
    formatted = plural_formatter.format('prefix {val!p:0=zero:other="{val}"} suffix', val=1)
    assert formatted == 'prefix "1" suffix'


@pytest.mark.parametrize('format_type, adjective_type, expected_str', [
    (str, str, 'A single "<strong>cool</strong>" item.'),
    (Markup, Markup, 'A single "<strong>cool</strong>" item.'),
    (str, Markup, 'A single "<strong>cool</strong>" item.'),
    (Markup, str, 'A single "&lt;strong&gt;cool&lt;/strong&gt;" item.'),
])
def test_PluralFormatter_MarkupSafe(format_type, adjective_type, expected_str):
    plural_formatter = formatters.PluralFormatter(locale_identifier='en')
    formatted = plural_formatter.format(
        format_type('{count!p:one=A single "{adjective}" item.:other=Several "{adjective}" items.}'),
        count=1,
        adjective=adjective_type('<strong>cool</strong>'),
    )
    assert formatted == expected_str
    assert type(formatted) is format_type


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


@pytest.mark.parametrize('format_type, item_type, expected_str', [
    (str, str, 'I like <i>Python</i>.'),
    (Markup, Markup, 'I like <i>Python</i>.'),
    (str, Markup, 'I like <i>Python</i>.'),
    (Markup, str, 'I like &lt;i&gt;Python&lt;/i&gt;.'),
])
def test_CommaSeparatedListFormatter_MarkupSafe_one_item(format_type, item_type, expected_str):
    comma_separated_list_formatter = formatters.CommaSeparatedListFormatter(locale_identifier='en')
    formatted = comma_separated_list_formatter.format(
        format_type('I like {list!l}.'),
        list=[
            item_type('<i>Python</i>'),
        ],
    )
    assert formatted == expected_str
    assert type(formatted) is format_type


@pytest.mark.parametrize('format_type, item_one_type, item_two_type, expected_str', [
    (str, str, str, 'I like <i>Python</i> and <i>Wikidata</i>.'),
    (Markup, Markup, Markup, 'I like <i>Python</i> and <i>Wikidata</i>.'),
    (str, Markup, Markup, 'I like <i>Python</i> and <i>Wikidata</i>.'),
    (Markup, str, str, 'I like &lt;i&gt;Python&lt;/i&gt; and &lt;i&gt;Wikidata&lt;/i&gt;.'),
    (Markup, Markup, str, 'I like <i>Python</i> and &lt;i&gt;Wikidata&lt;/i&gt;.'),
    (Markup, str, Markup, 'I like &lt;i&gt;Python&lt;/i&gt; and <i>Wikidata</i>.'),
])
def test_CommaSeparatedListFormatter_MarkupSafe_two_items(format_type, item_one_type, item_two_type, expected_str):
    comma_separated_list_formatter = formatters.CommaSeparatedListFormatter(locale_identifier='en')
    formatted = comma_separated_list_formatter.format(
        format_type('I like {list!l}.'),
        list=[
            item_one_type('<i>Python</i>'),
            item_two_type('<i>Wikidata</i>'),
        ],
    )
    assert formatted == expected_str
    assert type(formatted) is format_type


@pytest.mark.parametrize('format_type, item_one_type, item_two_type, item_three_type, expected_str', [
    (str, str, str, str, 'I like <i>Python</i>, <i>Wikidata</i>, and <i>Music</i>.'),
    (Markup, Markup, Markup, Markup, 'I like <i>Python</i>, <i>Wikidata</i>, and <i>Music</i>.'),
    (Markup, str, Markup, str, 'I like &lt;i&gt;Python&lt;/i&gt;, <i>Wikidata</i>, and &lt;i&gt;Music&lt;/i&gt;.'),
])
def test_CommaSeparatedListFormatter_MarkupSafe_three_items(format_type, item_one_type, item_two_type, item_three_type, expected_str):
    comma_separated_list_formatter = formatters.CommaSeparatedListFormatter(locale_identifier='en')
    formatted = comma_separated_list_formatter.format(
        format_type('I like {list!l}.'),
        list=[
            item_one_type('<i>Python</i>'),
            item_two_type('<i>Wikidata</i>'),
            item_three_type('<i>Music</i>'),
        ],
    )
    assert formatted == expected_str
    assert type(formatted) is format_type


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


@pytest.mark.parametrize('gender', [
    ('m'),
    ('f'),
    ('n'),
])
def test_GenderFormatter_fallback(gender):
    user = 'opaque value'

    def get_gender(value):
        assert value == user
        return gender

    gender_formatter = formatters.GenderFormatter(get_gender=get_gender)
    assert gender_formatter.format(
        'Thank {user!g:m=you:o=unused}!',  # o(ther) only included in format spec to make this test different from _unused below
        user=user
    ) == 'Thank you!'


def test_GenderFormatter_unused():
    user = 'opaque value'

    def get_gender(value):
        # pointless to call get_gender() when format spec only has one replacement
        raise AssertionError('Should not be called at all!')

    gender_formatter = formatters.GenderFormatter(get_gender=get_gender)
    assert gender_formatter.format(
        'Thank {user!g:m=you}!',
        user=user
    ) == 'Thank you!'


@pytest.mark.parametrize('format_type, adjective_type, expected_str', [
    (str, str, 'Please respect <em>their</em> <strong>correct</strong> pronouns.'),
    (Markup, Markup, 'Please respect <em>their</em> <strong>correct</strong> pronouns.'),
    (str, Markup, 'Please respect <em>their</em> <strong>correct</strong> pronouns.'),
    (Markup, str, 'Please respect <em>their</em> &lt;strong&gt;correct&lt;/strong&gt; pronouns.'),
])
def test_GenderFormatter_MarkupSafe(format_type, adjective_type, expected_str):
    gender_formatter = formatters.GenderFormatter(get_gender=lambda _: 'n')
    formatted = gender_formatter.format(
        format_type('Please respect {user!g:m=<em>his</em> {adjective}:f=<em>her</em> {adjective}:n=<em>their</em> {adjective}} pronouns.'),
        user='user',
        adjective=adjective_type('<strong>correct</strong>'),
    )
    assert formatted == expected_str
    assert type(formatted) is format_type


def test_HyperlinkFormatter():
    hyperlink_formatter = formatters.HyperlinkFormatter()
    assert hyperlink_formatter.format(
        'You need to {url!h:log in} before you can edit.',
        url='/login',
    ) == 'You need to <a href="/login">log in</a> before you can edit.'


@pytest.mark.parametrize('format_type, url_type, expected_str', [
    (str, str, 'You need to <a href="/login"">log <em>in</em></a> before you can edit.'),
    (Markup, Markup, 'You need to <a href="/login"">log <em>in</em></a> before you can edit.'),
    (str, Markup, 'You need to <a href="/login"">log <em>in</em></a> before you can edit.'),
    (Markup, str, 'You need to <a href="/login&#34;">log <em>in</em></a> before you can edit.'),
])
def test_HyperlinkFormatter_MarkupSafe(format_type, url_type, expected_str):
    hyperlink_formatter = formatters.HyperlinkFormatter()
    formatted = hyperlink_formatter.format(
        format_type('You need to {url!h:log <em>in</em>} before you can edit.'),
        url=url_type('/login"'),
    )
    assert formatted == expected_str
    assert type(formatted) is format_type


flac = '<abbr title="Free Lossless Audio Codec">FLAC</abbr>'

@pytest.mark.parametrize('formats, user, expected', [
    ([Markup(flac)], 'Keith', f'His preferred <a href="/wiki/Format">format</a> is {flac}.'),
    ([Markup(flac), '"OGG"'], 'Keira', f'Her preferred <a href="/wiki/Format">formats</a> are {flac} and &#34;OGG&#34;.'),
    ([Markup(flac), '"OGG"', 'OPUS'], 'Kim', f'Their preferred <a href="/wiki/Format">formats</a> are {flac}, &#34;OGG&#34;, and OPUS.'),
])
def test_I18nFormatter_en(formats, user, expected):
    genders = {
        'Keith': 'm',
        'Keira': 'f',
        'Kim': 'n',
    }
    i18n_formatter = formatters.I18nFormatter(locale_identifier='en',
                                              get_gender=lambda value: genders[value])
    formatted = i18n_formatter.format(
        Markup('{user!g:m=His:f=Her:n=Their} preferred {count!p:one={url!h:format} is:other={url!h:formats} are} {formats!l}.'),
        user=user,
        count=len(formats),
        formats=formats,
        url='/wiki/Format',
    )
    assert formatted == expected
    assert isinstance(formatted, Markup)
