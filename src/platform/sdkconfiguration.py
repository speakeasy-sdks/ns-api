"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""


import requests as requests_http
from ._hooks import SDKHooks
from .utils import utils
from .utils.retries import RetryConfig
from dataclasses import dataclass, field
from platform.models import shared
from typing import Callable, Dict, List, Tuple, Union


SERVERS = [
    'https://{tenant}.goskope.com:/{basePath}',
    # The production API server
]
"""Contains the list of servers available to the SDK"""



@dataclass
class SDKConfiguration:
    client: requests_http.Session
    security: Union[shared.Security,Callable[[], shared.Security]] = None
    server_url: str = ''
    server_idx: int = 0
    server_defaults: List[Dict[str, str]] = field(default_factory=List)
    language: str = 'python'
    openapi_doc_version: str = '1.0.0'
    sdk_version: str = '0.10.1'
    gen_version: str = '2.280.6'
    user_agent: str = 'speakeasy-sdk/python 0.10.1 2.280.6 1.0.0 Platform'
    retry_config: RetryConfig = None
    _hooks: SDKHooks = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], self.server_defaults[self.server_idx]


    def get_hooks(self) -> SDKHooks:
        return self._hooks
