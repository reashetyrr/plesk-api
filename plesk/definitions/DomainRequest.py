from typing import Union

from .PlanReference import PlanReference
from .DomainReference import DomainReference
from .OwnerClientReference import OwnerClientReference


class DomainRequest:
    def __init__(self, _ip_addresses: list[str], _ipv6: list[str], _plan: PlanReference, _base_domain: Union[DomainReference, None], _description: str, _hosting_type: str, _parent_domain: Union[DomainReference, None], _name: str, _hosting_settings: dict, _owner_client: OwnerClientReference, _ipv4: list[str]):
        self._parent_domain = _parent_domain
        self._hosting_settings = _hosting_settings
        self._base_domain = _base_domain
        self._description = _description
        self._hosting_type = _hosting_type
        self._name = _name
        self._ip_addresses = _ip_addresses
        self._ipv4 = _ipv4
        self._owner_client = _owner_client
        self._ipv6 = _ipv6
        self._plan = _plan

    def to_request_dict(self):
        return {
            'parent_domain': self._parent_domain.to_request_dict() if self._parent_domain is not None else None,
            'hosting_settings': self._hosting_settings,
            'base_domain': self._base_domain.to_request_dict() if self._base_domain is not None else None,
            'description': self._description,
            'hosting_type': self._hosting_type,
            'name': self._name,
            'ip_addresses': self._ip_addresses,
            'ipv4': self._ipv4,
            'owner_client': self._owner_client.to_request_dict(),
            'ipv6': self._ipv6,
            'plan': self._plan.to_request_dict()
        }