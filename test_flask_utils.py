import flask
import flask.json.tag
import pytest

import flask_utils


@pytest.mark.parametrize('value', [
    {'a': 1, 'b': 2},
])
def test_serializer(value):
    serializer = flask.json.tag.TaggedJSONSerializer()

    json = serializer.dumps(value)
    value_ = serializer.loads(json)

    assert value == value_
    assert type(value) is type(value_)


def test_ordered_request():
    app = flask.Flask(__name__)
    with app.test_request_context('/?a=1&a=2&c=4&b=3'):
        assert flask.request.args.getlist('a') == ['1', '2']
        assert flask.request.args.getlist('c') == ['4']
        assert flask.request.args.getlist('b') == ['3']
        # prior to Werkzeug 3.1.0, we used OrderedMultiDict to also assert
        # list(….items(multi=True)) == [('a', '1'), ('a', '2'), ('c', '4'), ('b', '3')]
        # but in fact we don’t care about the order of a/b/c in the args:
        # we only need a=1&a=2 to stay in order
        # (which the ordinary MultiDict guarantees and we test above)


def test_set_json_support():
    app = flask.Flask(__name__)
    app.json = flask_utils.SetJSONProvider(app)
    with app.test_request_context('/'):
        expected = flask.jsonify(['x'])
        actual = flask.jsonify(set(['x']))
    assert expected.get_data(as_text=True) == actual.get_data(as_text=True)


def test_set_json_support_sorted_ints():
    app = flask.Flask(__name__)
    app.json = flask_utils.SetJSONProvider(app)
    with app.test_request_context('/'):
        expected = flask.jsonify([1, 2, 3, 5, 8])
        actual = flask.jsonify(set([8, 1, 5, 1, 3, 2]))
    assert expected.get_data(as_text=True) == actual.get_data(as_text=True)


def test_set_json_support_sorted_strs():
    app = flask.Flask(__name__)
    app.json = flask_utils.SetJSONProvider(app)
    with app.test_request_context('/'):
        expected = flask.jsonify(['a', 'bc', 'def'])
        actual = flask.jsonify(set(['def', 'a', 'bc']))
    assert expected.get_data(as_text=True) == actual.get_data(as_text=True)
