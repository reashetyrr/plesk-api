from .DomainReference import DomainReference


class DatabaseRequest:
    def __init__(self, _parent_domain: DomainReference, _server_id: int, _type: str, _name: str):
        self._type = _type
        self._server_id = _server_id
        self._parent_domain = _parent_domain
        self._name = _name

