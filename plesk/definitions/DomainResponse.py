import json

import requests

from .DomainAlias import DomainAlias
from .DomainReference import DomainReference
from .DomainRequest import DomainRequest
from plesk.utils import ensure_panel_set
from plesk.PleskPanel import PleskPanel


class DomainResponse:
    _panel: PleskPanel = None

    def __init__(self, _guid: str, _ascii_name: str, _www_root: str, _created: str, _hosting_type: str, _base_domain_id: int, _aliases: list[DomainAlias], _name: str, _id: int):
        self._www_root = _www_root
        self._hosting_type = _hosting_type
        self._name = _name
        self._base_domain_id = _base_domain_id
        self._aliases = _aliases
        self._id = _id
        self._ascii_name = _ascii_name
        self._created = _created
        self._guid = _guid

    @property
    def www_root(self):
        return self._www_root

    @www_root.setter
    def www_root(self, value):
        self._www_root = value

    @property
    def hosting_type(self):
        return self._hosting_type

    @hosting_type.setter
    def hosting_type(self, value):
        self._hosting_type = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def base_domain_id(self):
        return self._base_domain_id

    @base_domain_id.setter
    def base_domain_id(self, value):
        self._base_domain_id = value

    @property
    def aliases(self):
        return self._aliases

    @aliases.setter
    def aliases(self, value):
        self._aliases = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def ascii_name(self):
        return self._ascii_name

    @ascii_name.setter
    def ascii_name(self, value):
        self._ascii_name = value

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, value):
        self._created = value

    @property
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, value):
        self._guid = value

    @classmethod
    @ensure_panel_set
    def fetch_domains_for_client(cls, client_id: int) -> list['DomainResponse']:
        response: requests.Response = requests.get(f'{cls._panel.url.geturl()}/api/v2/clients/{client_id}/domains', headers={'Authorization': cls._panel.auth_header}, verify=False)
        if not response.ok:
            raise RuntimeError('Received an error during the api call: %r', response.text)

        response_json: list[dict] = response.json()
        return [DomainResponse(**{f'_{key}': value for key, value in response_item.items()}) for response_item in response_json]

    @ensure_panel_set
    def add_domain(self, domain: DomainRequest) -> 'DomainResponse':
        response: requests.Response = requests.post(f'{self._panel.url.geturl()}/api/v2/domains', headers={'Authorization': self._panel.auth_header, 'Content-Type': 'application/json'}, data=json.dumps(domain.to_request_dict()), verify=False)
        if not response.ok:
            raise RuntimeError('Received an error during the api call: %r', response.text)

        response_json: dict = response.json()
        return self.fetch_domain(domain_id=response_json.get('id'))

    @classmethod
    @ensure_panel_set
    def fetch_domain(cls, domain_id: int) -> 'DomainResponse':
        response: requests.Response = requests.get(f'{cls._panel.url.geturl()}/api/v2/domains/{domain_id}', headers={'Authorization': cls._panel.auth_header}, verify=False)
        if not response.ok:
            raise RuntimeError('Received an error during the api call: %r', response.text)

        response_json: dict = response.json()
        return DomainResponse(**{f'_{key}': value for key, value in response_json.items()})

    def to_domain_reference(self) -> 'DomainReference':
        return DomainReference(_id=self._id, _name=self._name, _guid=self._guid)
