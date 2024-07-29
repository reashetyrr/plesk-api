class OwnerClientReference:
    def __init__(self, _login: str, _guid: str, _id: int, _external_id: str):
        self._login = _login
        self._external_id = _external_id
        self._guid = _guid
        self._id = _id

    def to_request_dict(self):
        return {
            'login': self._login,
            'external_id': self._external_id,
            'guid': self._guid,
            'id': self._id
        }
