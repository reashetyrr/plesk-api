from typing import *
from urllib.parse import urlparse, ParseResult
import requests
import base64
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plesk.classes.User import User


class PleskPanel:
    instance: Optional['PleskPanel'] = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(PleskPanel, cls).__new__(cls)

        return cls.instance

    def __init__(self, username: str, password: str, host: Optional[str] = None, fqdn: Optional[str] = None, port: int = 8443, debug: bool = False):
        if hasattr(self, 'initialized'):
            return

        if not fqdn and not host:
            raise RuntimeError('Missing both fqdn and host, atleast one of the 2 is required')

        if fqdn and '/api' in fqdn:
            raise RuntimeError('Incorrect fqdn format, should be like: https://{hostname or ip}:{8443 or actual port}')

        if host and '/api' in host:
            raise RuntimeError('Incorrect Host format, probably wanted to use fqdn')

        parsed_url: ParseResult = urlparse(fqdn) if fqdn else urlparse(f'{host}:{port}')

        test_results = requests.get(f'{parsed_url.geturl()}/api/v2/swagger.json', verify=False)

        if not test_results.ok:
            raise RuntimeError('Could not connect to the passed plesk instance, aborting.')

        encode_string = f'{username}:{password}'.encode('utf-8')

        self.url = parsed_url
        self.auth_header = f'Basic {base64.b64encode(encode_string).decode('utf-8')}'
        self._user = None

        if debug:
            self.debug_info = test_results.json()

        self.initialized = True

        admin_request = requests.get(f'{parsed_url.geturl()}/api/v2/clients/1', headers={'Authorization': self.auth_header}, verify=False)
        self.admin_login = admin_request.json().get('login')

    @property
    def user(self) -> 'User':
        if self._user is None:
            from plesk.classes.User import User
            self._user = User
        return self._user

    @classmethod
    def get_singleton(cls, username: Optional[str] = None, password: Optional[str] = None, host: Optional[str] = None, fqdn: Optional[str] = None, port: int = 8443, debug: bool = False):
        if not username and not cls.instance:
            raise RuntimeError('Missing requirements in Panel initialization and no panel was already initialized')

        return cls(username=username, password=password, host=host, fqdn=fqdn, port=port, debug=debug)
