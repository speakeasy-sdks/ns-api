"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import npa_policy_response_item as shared_npa_policy_response_item
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from platform import utils
from typing import Optional



@dataclasses.dataclass
class GetNpaRulesIDRequest:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""npa policy id"""
    fields_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'fields', 'style': 'form', 'explode': True }})
    r"""Return values only from specified fields"""
    


class GetNpaRulesID200ApplicationJSONStatus(str, Enum):
    SUCCESS = 'success'
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetNpaRulesID200ApplicationJSON:
    r"""successful operation"""
    data: Optional[shared_npa_policy_response_item.NpaPolicyResponseItem] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    status: Optional[GetNpaRulesID200ApplicationJSONStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class GetNpaRulesIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_npa_rules_id_200_application_json_object: Optional[GetNpaRulesID200ApplicationJSON] = dataclasses.field(default=None)
    r"""successful operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

