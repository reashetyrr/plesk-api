class ClientStatistics:
    def __init__(self, _traffic: int, _email_redirects: int, _email_postboxes: int, _mailing_lists: int, _email_response_messages: int, _disk_space: int, _active_domains: int, _traffic_prevday: int, _databases: int, _subdomains: int):
        self._databases = _databases
        self._subdomains = _subdomains
        self._active_domains = _active_domains
        self._mailing_lists = _mailing_lists
        self._email_redirects = _email_redirects
        self._traffic = _traffic
        self._email_postboxes = _email_postboxes
        self._traffic_prevday = _traffic_prevday
        self._email_response_messages = _email_response_messages
        self._disk_space = _disk_space

