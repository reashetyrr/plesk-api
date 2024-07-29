class DnsRecordRequest:
    def __init__(self, _host: str, _type: str, _value: str, _ttl: int, _opt: str):
        self._type = _type
        self._host = _host
        self._ttl = _ttl
        self._value = _value
        self._opt = _opt

