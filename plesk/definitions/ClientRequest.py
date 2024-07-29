class ClientRequest:
    def __init__(self, _owner_login: str, _type: str, _login: str, _email: str, _description: str, _locale: str, _status: int, _company: str, _name: str, _external_id: str, _password: str):
        self._type = _type
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

    def to_request_body(self):
        return {
            'owner_login': self._owner_login,
            'type': self._type,
            'login': self._login,
            'email': self._email,
            'description': self._description,
            'locale': self._locale,
            'status': self._status,
            'company': self._company,
            'name': self._name,
            'external_id': self._external_id,
            'password': self._password
        }
