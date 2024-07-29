import json

from plesk.PleskPanel import PleskPanel
import requests

from plesk.definitions.DomainResponse import DomainResponse
from plesk.definitions.ClientRequest import ClientRequest
from plesk.definitions.OwnerClientReference import OwnerClientReference
from plesk.utils import ensure_panel_set


class Client:
    _panel: PleskPanel = None

    def __init__(self, _guid: str, _type: str, _login: str, _email: str, _description: str, _created: str, _locale: str, _status: int, _company: str, _name: str, _id: int, _owner_login: str = None,  _external_id: str = ''):
        self._id = _id
        self._guid = _guid
        self._name = _name
        self._type = _type
        self._login = _login
        self._email = _email
        self._status = _status
        self._locale = _locale
        self._company = _company
        self._created = _created
        self._description = _description
        self._owner_login = _owner_login
        self._external_id = _external_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        self._login = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, value):
        self._guid = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, value):
        self._locale = value

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, value):
        self._created = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def owner_login(self):
        return self._owner_login

    @owner_login.setter
    def owner_login(self, value):
        self._owner_login = value

    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value

    @classmethod
    def fetch_all(cls, existing_panel: PleskPanel) -> list['Client']:
        response: requests.Response = requests.get(f'{existing_panel.url.geturl()}/api/v2/clients', headers={'Authorization': existing_panel.auth_header}, verify=False)
        if not response.ok:
            raise RuntimeError('Received an error during the api call: %r', response.text)

        response_json: list[dict] = response.json()
        user: dict
        return [cls(**{f'_{key}': value for key, value in user.items()}) for user in response_json]

    @classmethod
    def fetch(cls, customer_id: int, existing_panel: PleskPanel) -> 'Client':
        response: requests.Response = requests.get(f'{existing_panel.url.geturl()}/api/v2/clients/{customer_id}', headers={'Authorization': existing_panel.auth_header}, verify=False)
        if not response.ok:
            raise RuntimeError('Received an error during the api call: %r', response.text)

        response_json: dict = response.json()
        return cls(**{f'_{key}': value for key, value in response_json.items()})

    @ensure_panel_set
    def suspend(self):
        response: requests.Response = requests.post(f'{self._panel.url.geturl()}/api/v2/clients/{self._id}/suspend', headers={'Authorization': self._panel.auth_header}, verify=False)
        if not response.ok:
            raise RuntimeError('Received an error during the api call: %r', response.text)

        return True

    @ensure_panel_set
    def activate(self):
        response: requests.Response = requests.post(f'{self._panel.url.geturl()}/api/v2/clients/{self._id}/activate', headers={'Authorization': self._panel.auth_header}, verify=False)
        if not response.ok:
            raise RuntimeError('Received an error during the api call: %r', response.text)

        return True

    @classmethod
    def create(cls, client_request: ClientRequest, existing_panel: PleskPanel) -> 'Client':
        response: requests.Response = requests.post(f'{existing_panel.url.geturl()}/api/v2/clients', headers={'Authorization': existing_panel.auth_header, 'Content-Type': 'application/json'}, data=json.dumps(client_request.to_request_body()), verify=False)
        if not response.ok:
            raise RuntimeError('Received an error during the api call: %r', response.text)

        response_json: dict = response.json()
        return cls.fetch(customer_id=response_json.get('id'), existing_panel=existing_panel)

    @ensure_panel_set
    def fetch_domains(self) -> list['DomainResponse']:
        return DomainResponse.fetch_domains_for_client(client_id=self._id)

    def to_owner_reference(self):
        return OwnerClientReference(
            _login=self._login,
            _guid=self._guid,
            _id=self._id,
            _external_id=self._external_id
        )
