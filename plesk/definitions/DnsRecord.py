class DnsRecord:
    def __init__(self, _host: str, _type: str, _value: str, _ttl: int, _opt: str, _id: int):
        self._type = _type
        self._host = _host
        self._ttl = _ttl
        self._value = _value
        self._opt = _opt
        self._id = _id

