import json

import requests
from urllib.parse import ParseResult

from plesk.definitions.Client import Client
from plesk.definitions.ClientRequest import ClientRequest
from plesk.utils import ensure_panel_set
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from plesk.PleskPanel import PleskPanel


class User:
    _panel: 'PleskPanel' = None

    @classmethod
    @ensure_panel_set
    def fetch_all(cls) -> list['Client']:
        return Client.fetch_all(existing_panel=cls._panel)

    @classmethod
    @ensure_panel_set
    def fetch(cls, customer_id: int) -> 'Client':
        return Client.fetch(customer_id=customer_id, existing_panel=cls._panel)

    @classmethod
    @ensure_panel_set
    def create(cls, client_request: ClientRequest) -> 'Client':
        return Client.create(client_request=client_request, existing_panel=cls._panel)