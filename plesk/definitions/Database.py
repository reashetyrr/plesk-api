class Database:
    def __init__(self, _type: str, _server_id: int, _parent_domain: int, _name: str, _default_user_id: int, _id: int):
        self._type = _type
        self._server_id = _server_id
        self._parent_domain = _parent_domain
        self._default_user_id = _default_user_id
        self._name = _name
        self._id = _id

