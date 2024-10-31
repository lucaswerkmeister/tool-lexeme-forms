import flask.json

class SetJSONProvider(flask.json.provider.DefaultJSONProvider):
    @staticmethod
    def default(o):
        if isinstance(o, set):
            return sorted(o)
        return super().default(o)
