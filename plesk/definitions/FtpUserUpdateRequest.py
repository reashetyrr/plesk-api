class FtpUserUpdateRequest:
    def __init__(self, _permissions: dict, _home: str, _name: str, _password: str, _quota: int):
        self._home = _home
        self._name = _name
        self._password = _password
        self._quota = _quota
        self._permissions = _permissions

