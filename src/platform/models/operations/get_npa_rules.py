"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import npa_policy_response_item as shared_npa_policy_response_item
from typing import List, Optional


@dataclasses.dataclass
class GetNpaRulesRequest:
    fields: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'fields', 'style': 'form', 'explode': True }})
    r"""Return values only from specified fields"""
    filter: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter', 'style': 'form', 'explode': True }})
    r"""Query string based on query operaters"""
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Max number of policies to retrieve. Default will be all policies."""
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""The offset of the first policy in the list to retrieve."""
    sortby: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortby', 'style': 'form', 'explode': True }})
    r"""Sort retrieved policies by specified field. Default is policy id"""
    sortorder: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortorder', 'style': 'form', 'explode': True }})
    r"""Sort in either asc or desc order. The default is asc order"""
    



@dataclasses.dataclass
class GetNpaRulesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    npa_policy_response: Optional[List[shared_npa_policy_response_item.NpaPolicyResponseItem]] = dataclasses.field(default=None)
    r"""successful operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

