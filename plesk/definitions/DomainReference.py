class DomainReference:
    def __init__(self, _guid: str, _id: int, _name: str):
        self._name = _name
        self._guid = _guid
        self._id = _id


    def to_request_dict(self):
        return {
            'name': self._name,
            'guid': self._guid,
            'id': self._id
        }
