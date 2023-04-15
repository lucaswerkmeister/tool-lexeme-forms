import flask
import flask.json.tag
import pytest
import werkzeug.datastructures

import flask_utils


@pytest.mark.parametrize('value', [
    {'a': 1, 'b': 2},
    werkzeug.datastructures.OrderedMultiDict([('a', 1), ('a', 2), ('c', 4), ('b', 3)]),  # type: ignore
    werkzeug.datastructures.ImmutableOrderedMultiDict([('a', 1), ('a', 2), ('c', 4), ('b', 3)]),  # type: ignore
])
def test_serializer(value):
    serializer = flask.json.tag.TaggedJSONSerializer()
    serializer.register(flask_utils.TagOrderedMultiDict, index=0)
    serializer.register(flask_utils.TagImmutableOrderedMultiDict, index=0)

    json = serializer.dumps(value)
    value_ = serializer.loads(json)

    assert value == value_
    assert type(value) == type(value_)


def test_ordered_request():
    app = flask_utils.OrderedFlask(__name__)
    with app.test_request_context('/?a=1&a=2&c=4&b=3'):
        assert list(flask.request.args.items(multi=True)) == [('a', '1'), ('a', '2'), ('c', '4'), ('b', '3')]


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
