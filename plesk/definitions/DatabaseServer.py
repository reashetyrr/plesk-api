class DatabaseServer:
    def __init__(self, _is_local: bool, _host: str, _type: str, _is_default: bool, _status: str, _id: int, _port: int, _db_count: int):
        self._type = _type
        self._status = _status
        self._is_default = _is_default
        self._host = _host
        self._port = _port
        self._is_local = _is_local
        self._id = _id
        self._db_count = _db_count

