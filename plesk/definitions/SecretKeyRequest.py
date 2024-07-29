class SecretKeyRequest:
    def __init__(self, _login: str, _ip: str, _description: str, _ips: list[str]):
        self._ip = _ip
        self._login = _login
        self._ips = _ips
        self._description = _description

