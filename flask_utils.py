import flask
import flask.json
import flask.json.tag
import werkzeug.datastructures

class OrderedRequest(flask.Request):
    """Request subclass to use ordered parameter storage"""
    parameter_storage_class = werkzeug.datastructures.ImmutableOrderedMultiDict
class OrderedFlask(flask.Flask):
    """Flask subclass to use ordered parameter storage for requests"""
    request_class = OrderedRequest

    # specific type needed to have access to .serializer
    session_interface: flask.sessions.SecureCookieSessionInterface

class TagOrderedMultiDict(flask.json.tag.JSONTag):
    __slots__ = ('serializer',)
    key = ' omd'

    def check(self, value):
        return isinstance(value, werkzeug.datastructures.OrderedMultiDict)

    def to_json(self, value):
        return [(k, self.serializer.tag(v)) for k, v in value.items(multi=True)]

    def to_python(self, value):
        return werkzeug.datastructures.OrderedMultiDict(value)

class TagImmutableOrderedMultiDict(TagOrderedMultiDict):
    key = ' iomd'

    def check(self, value):
        return isinstance(value, werkzeug.datastructures.ImmutableOrderedMultiDict)

    def to_python(self, value):
        return werkzeug.datastructures.ImmutableOrderedMultiDict(value)

class SetJSONProvider(flask.json.provider.DefaultJSONProvider):
    @staticmethod
    def default(o):
        if isinstance(o, set):
            return list(o)
        return super().default(o)
