# example usage:
```python
import plesk
from plesk.definitions.Client import Client
from plesk.definitions.DomainResponse import DomainResponse
from plesk.definitions.DomainRequest import DomainRequest
from plesk.definitions.PlanReference import PlanReference
from plesk.utils import generate_password, generate_guid

panel = plesk.PleskPanel.get_singleton(username='<plesk admin/root username>', password='<plesk password>', fqdn='https://<plesk hostname or ip address>:8443', debug=True)
users: list[Client] = panel.user.fetch_all()
admin_user: Client = panel.user.fetch(customer_id=1)
admin_domains: list[DomainResponse] = admin_user.fetch_domains()
admin_first_domain: DomainResponse = admin_domains[0]
new_domain = DomainRequest(
    _name='example.com',
    _hosting_type='virtual',
    _base_domain=None,
    _parent_domain=None,
    _owner_client=admin_user.to_owner_reference(),
    _description='This is an example subscription made through the api',
    _hosting_settings={
        'ftp_login': 'example_ftp022',
        'ftp_password': generate_password(),
    },
    _ip_addresses=['<ipv4 address to use>'],
    _ipv4=['<ipv4 address to use>'],
    _ipv6=[],
    _plan=PlanReference(_name='Unlimited'),
)
admin_first_domain.add_domain(domain=new_domain)

new_domain_in_subscription = DomainRequest(
    _name='example1.com',
    _hosting_type='virtual',
    _base_domain=admin_first_domain.to_domain_reference(),
    _parent_domain=admin_first_domain.to_domain_reference(),
    _owner_client=admin_user.to_owner_reference(),
    _description='This is an example domain added to a subscription through the api',
    _hosting_settings={
        'ftp_login': 'example_ftp212',
        'ftp_password': generate_password(),
    },
    _ip_addresses=['<ipv4 address to use>'],
    _ipv4=['<ipv4 address to use>'],
    _ipv6=[],
    _plan=PlanReference(_name='Unlimited'),
)
admin_first_domain.add_domain(domain=new_domain_in_subscription)
# new_client = ClientRequest(
#     _name='John Smith',
#     _company='Plesk',
#     _login='john-unit-test',
#     _status=0,
#     _email='john_smith@example.com',
#     _locale='en-US',
#     _owner_login=admin_user.login,
#     _external_id=generate_guid(),
#     _description='Nice guy',
#     _password=generate_password(),
#     _type='customer'
# )
# new_user = panel.user.create(client_request=new_client)
```