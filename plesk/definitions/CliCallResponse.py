class CliCallResponse:
    def __init__(self, _stdout: str, _code: int, _stderr: str):
        self._stdout = _stdout
        self._code = _code
        self._stderr = _stderr

