class Admin:
    def __init__(self, _country: str, _email: str, _phone: str, _post_code: str, _state: str, _locale: str, _multiple_sessions: bool, _city: str, _company: str, _fax: str, _name: str, _address: str, _send_announce: bool):
        self._email = _email
        self._city = _city
        self._post_code = _post_code
        self._multiple_sessions = _multiple_sessions
        self._state = _state
        self._send_announce = _send_announce
        self._locale = _locale
        self._name = _name
        self._fax = _fax
        self._phone = _phone
        self._country = _country
        self._address = _address
        self._company = _company

