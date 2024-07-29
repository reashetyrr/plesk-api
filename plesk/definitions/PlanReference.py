class PlanReference:
    def __init__(self, _name: str):
        self._name = _name

    def to_request_dict(self):
        return {
            'name': self._name
        }
