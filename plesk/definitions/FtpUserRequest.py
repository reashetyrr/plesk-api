from .DomainReference import DomainReference


class FtpUserRequest:
    def __init__(self, _permissions: dict, _home: str, _parent_domain: DomainReference, _name: str, _password: str, _quota: int):
        self._home = _home
        self._parent_domain = _parent_domain
        self._name = _name
        self._password = _password
        self._quota = _quota
        self._permissions = _permissions

