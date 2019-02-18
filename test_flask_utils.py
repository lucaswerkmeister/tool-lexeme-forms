import flask.json.tag
import pytest
import werkzeug.datastructures

import flask_utils


@pytest.mark.parametrize('value', [
    {'a': 1, 'b': 2},
    werkzeug.datastructures.OrderedMultiDict([('a', 1), ('a', 2), ('c', 4), ('b', 3)]),
    werkzeug.datastructures.ImmutableOrderedMultiDict([('a', 1), ('a', 2), ('c', 4), ('b', 3)]),
])
def test_serializer(value):
    serializer = flask.json.tag.TaggedJSONSerializer()
    serializer.register(flask_utils.TagOrderedMultiDict, index=0)
    serializer.register(flask_utils.TagImmutableOrderedMultiDict, index=0)

    json = serializer.dumps(value)
    value_ = serializer.loads(json)

    assert value == value_
    assert type(value) == type(value_)
