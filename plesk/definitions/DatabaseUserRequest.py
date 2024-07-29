from .DomainReference import DomainReference


class DatabaseUserRequest:
    def __init__(self, _login: str, _server_id: int, _parent_domain: DomainReference, _database_id: int, _password: str):
        self._login = _login
        self._server_id = _server_id
        self._parent_domain = _parent_domain
        self._database_id = _database_id
        self._password = _password

