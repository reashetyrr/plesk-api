class FtpUser:
    def __init__(self, _permissions: dict, _home: str, _parent_domain: int, _name: str, _id: int, _quota: int):
        self._home = _home
        self._parent_domain = _parent_domain
        self._name = _name
        self._id = _id
        self._quota = _quota
        self._permissions = _permissions

