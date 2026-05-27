from collections.abc import Callable
from urllib.parse import urlsplit
from requests_oauthlib import OAuth2Session
from typing import Any, Optional, cast

class MWOAuth2:

    def __init__(
            self,
            host: str,
            client_id: str,
            client_secret: str,
            pop_oauth_state: Callable[[], dict[str, Any]],
            set_oauth_state: Callable[[dict[str, Any]], None],
            get_access_token: Callable[[], Optional[dict[str, Any]]],
            set_access_token: Callable[[dict[str, Any]], None],
            del_access_token: Callable[[], None],
            user_agent: str,
            api_path: str = '/w/api.php',
    ):
        self.host = host
        self.client_id = client_id
        self.client_secret = client_secret
        self.set_oauth_state = set_oauth_state
        self.pop_oauth_state = pop_oauth_state
        self.get_access_token = get_access_token
        self.set_access_token = set_access_token
        self.del_access_token = del_access_token
        self.user_agent = user_agent
        self.api_path = api_path

    def _oauth2session(self, **kwargs: Any) -> OAuth2Session:
        session = OAuth2Session(self.client_id, **kwargs)
        session.headers['User-Agent'] = self.user_agent
        return session

    def _rest_url(self) -> str:
        api_url = self.host + self.api_path
        assert api_url.endswith('api.php')
        return api_url[:-len('api.php')] + 'rest.php'

    def has_access_token(self) -> bool:
        return self.get_access_token() is not None

    def has_well_formed_access_token(self) -> bool:
        # mainly based on oauthlib.oauth2.rfc6749.parameters.parse_token_response
        access_token = self.get_access_token()
        if access_token is None:
            return False
        valid_params = {
            'access_token',
            'token_type',
            'expires_in',
            'expires_at',
            'refresh_token',
            'scope',
        }
        invalid_params = set(access_token.keys()).difference(valid_params)
        if invalid_params:
            return False
        required_params = {'access_token', 'token_type'}
        missing_params = required_params.difference(access_token.keys())
        if missing_params:
            return False
        return True

    def authorization_url(self) -> str:
        redirect, oauth_state = self._oauth2session().authorization_url(f'{self._rest_url()}/oauth2/authorize')
        # store the state as a dict for future extensibility, e.g. PKCE code verifier (requests/requests-oauthlib#550)
        self.set_oauth_state({'state': oauth_state})
        return redirect

    def fetch_token(
            self,
            request_url: str,
    ) -> None:
        split = urlsplit(request_url)
        if split.scheme == 'http' and (
            split.hostname == 'localhost' or
            (split.hostname or '').endswith('.toolforge.org') or
            (split.hostname or '').endswith('.wmcloud.org') or
            (split.hostname or '').endswith('.wmflabs.org')
        ):
            # OAuthLib raises InsecureTransportError for all HTTP URLs;
            # fix localhost (for local development)
            # and WMCS domains (WMCS does TLS termination, tool did not apply `X-Forwarded-Proto: https`)
            # to prevent this
            request_url = split._replace(scheme='https').geturl()
        oauth_state = self.pop_oauth_state()
        access_token = self._oauth2session(state=oauth_state['state']).fetch_token(
            f'{self._rest_url()}/oauth2/access_token',
            client_secret=self.client_secret,
            authorization_response=request_url,
        )
        self.set_access_token(access_token)

    def oauth2_session(
            self,
    ) -> Optional[OAuth2Session]:
        access_token = self.get_access_token()
        if access_token is None:
            return None
        return self._oauth2session(
            token=access_token,
            token_updater=self.set_access_token,
            auto_refresh_url=f'{self._rest_url()}/oauth2/access_token',
            auto_refresh_kwargs={
                'client_id': self.client_id,
                'client_secret': self.client_secret,
            },
        )

try:
    import flask
except ModuleNotFoundError:
    pass
else:
    def _pop_oauth_state_flask_session() -> dict[str, Any]:
        return cast(dict[str, Any], flask.session.pop('oauth_state'))

    def _set_oauth_state_flask_session(oauth_state: dict[str, Any]) -> None:
        flask.session['oauth_state'] = oauth_state

    def _get_access_token_flask_session() -> Optional[dict[str, Any]]:
        return flask.session.get('oauth_access_token')

    def _set_access_token_flask_session(access_token: dict[str, Any]) -> None:
        flask.session['oauth_access_token'] = access_token

    def _del_access_token_flask_session() -> None:
        del flask.session['oauth_access_token']

    class MWOAuth2FlaskUninitializedException(Exception):

        def __init__(self, class_name: str):
            super().__init__(
                f'{class_name} was not initialized correctly. '
                'You must either configure it with a Flask app, '
                'by passing it into the constructor '
                'or calling init_app() later, '
                'or you must pass a client_id and client_secret into the constructor, '
                'before it can be used.'
            )
            self.class_name = class_name

        def __reduce__(self) -> tuple[Callable[[str], MWOAuth2FlaskUninitializedException], tuple[str]]:
            return (MWOAuth2FlaskUninitializedException, (self.class_name,))

    class MWOAuth2Flask(MWOAuth2):

        def __init__(
                self,
                host: str,
                user_agent: str,
                app: Optional[flask.Flask] = None,
                check_access_token_before_request: bool = False,
                client_id: Optional[str] = None,
                client_secret: Optional[str] = None,
                pop_oauth_state: Optional[Callable[[], dict[str, Any]]] = None,
                set_oauth_state: Optional[Callable[[dict[str, Any]], None]] = None,
                get_access_token: Optional[Callable[[], Optional[dict[str, Any]]]] = None,
                set_access_token: Optional[Callable[[dict[str, Any]], None]] = None,
                del_access_token: Optional[Callable[[], None]] = None,
                api_path: str = '/w/api.php',
        ):
            super().__init__(
                host=host,
                client_id=cast(str, client_id),  # may be set to non-None only in init_app() later
                client_secret=cast(str, client_secret),  # may be set to non-None only in init_app() later
                pop_oauth_state=pop_oauth_state or _pop_oauth_state_flask_session,
                set_oauth_state=set_oauth_state or _set_oauth_state_flask_session,
                get_access_token=get_access_token or _get_access_token_flask_session,
                set_access_token=set_access_token or _set_access_token_flask_session,
                del_access_token=del_access_token or _del_access_token_flask_session,
                user_agent=user_agent,
                api_path=api_path,
            )
            self.check_access_token_before_request = check_access_token_before_request

            if app is not None:
                self.init_app(app)

        def init_app(self, app: flask.Flask) -> None:
            if self.client_id is None:
                self.client_id = app.config['OAUTH']['CLIENT_ID']
            if self.client_secret is None:
                self.client_secret = app.config['OAUTH']['CLIENT_SECRET']
            if self.check_access_token_before_request:
                app.before_request(self._check_access_token)

        def _check_access_token(self) -> None:
            if self.has_access_token() and not self.has_well_formed_access_token():
                self.del_access_token()

        def _oauth2session(self, **kwargs: Any) -> OAuth2Session:
            if self.client_id is None or self.client_secret is None:
                raise MWOAuth2FlaskUninitializedException(type(self).__name__)
            return super()._oauth2session(**kwargs)

        def fetch_token(
                self,
                request_url: Optional[str] = None,
        ) -> None:
            super().fetch_token(
                request_url=request_url or flask.request.url,
            )

try:
    import mwapi  # type: ignore
except ModuleNotFoundError:
    pass
else:
    class MWOAuth2MWApi(MWOAuth2):

        def mwapi_session(
                self,
                host: Optional[str] = None,
        ) -> Optional[mwapi.Session]:
            oauth2_session = self.oauth2_session()
            if oauth2_session is None:
                return None
            return mwapi.Session(
                host=host or self.host,
                user_agent=self.user_agent,
                session=oauth2_session,
            )

try:
    class MWOAuth2FlaskMWApi(MWOAuth2Flask, MWOAuth2MWApi):
        pass
except NameError:
    pass
