class DomainAlias:
    def __init__(self, _ascii_name: str, _web: bool, _dns: bool, _mail: bool, _seo_redirect: bool, _name: str):
        self._seo_redirect = _seo_redirect
        self._dns = _dns
        self._name = _name
        self._mail = _mail
        self._ascii_name = _ascii_name
        self._web = _web

