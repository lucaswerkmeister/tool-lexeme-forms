import mwapi
import sys

class T272319RetryingSession(mwapi.Session):
    """Session subclass that retries requests once on certain errors"""
    def get(self, *args, **kwargs):
        try:
            return super().get(*args, **kwargs)
        except mwapi.errors.APIError as e:
            if e.code == 'mwoauth-invalid-authorization' and 'Nonce already used' in e.info:
                print('Got “Nonce already used” error (T272319), retrying:', file=sys.stderr)
                print(e, file=sys.stderr)
                return super().get(*args, **kwargs)
            else:
                raise e

    def post(self, *args, **kwargs):
        try:
            return super().post(*args, **kwargs)
        except mwapi.errors.APIError as e:
            if e.code == 'mwoauth-invalid-authorization' and 'Nonce already used' in e.info:
                print('Got “Nonce already used” error (T272319), retrying:', file=sys.stderr)
                print(e, file=sys.stderr)
                return super().post(*args, **kwargs)
            else:
                raise e
