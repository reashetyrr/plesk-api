class ServerIp:
    def __init__(self, _type: str, _interface: str, _ipv4: str, _netmask: str, _ipv6: str):
        self._type = _type
        self._netmask = _netmask
        self._interface = _interface
        self._ipv4 = _ipv4
        self._ipv6 = _ipv6

