class ClientUpdateRequest:
    def __init__(self, _owner_login: str, _login: str, _email: str, _description: str, _locale: str, _status: int, _company: str, _name: str, _external_id: str, _password: str = None, **kwargs):
        self._status = _status
        self._login = _login
        self._email = _email
        self._owner_login = _owner_login
        self._description = _description
        self._locale = _locale
        self._name = _name
        self._external_id = _external_id
        self._password = _password
        self._company = _company

    def to_request_dict(self):
        return {key[1:]: value for key, value in self.__dict__.items()}
