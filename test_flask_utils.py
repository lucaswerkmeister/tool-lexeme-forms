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
