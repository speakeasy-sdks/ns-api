"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import npa_policy_rule_data as shared_npa_policy_rule_data
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from platform import utils
from typing import Optional

class NpaPolicyRequestRuleOrderOrder(str, Enum):
    TOP = 'top'
    BOTTOM = 'bottom'
    BEFORE = 'before'
    AFTER = 'after'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NpaPolicyRequestRuleOrder:
    order: Optional[NpaPolicyRequestRuleOrderOrder] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order'), 'exclude': lambda f: f is None }})
    position: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('position'), 'exclude': lambda f: f is None }})
    rule_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rule_id'), 'exclude': lambda f: f is None }})
    rule_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rule_name'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NpaPolicyRequest:
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    enabled: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    group_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group_id'), 'exclude': lambda f: f is None }})
    group_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group_name'), 'exclude': lambda f: f is None }})
    rule_data: Optional[shared_npa_policy_rule_data.NpaPolicyRuleData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rule_data'), 'exclude': lambda f: f is None }})
    rule_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rule_name'), 'exclude': lambda f: f is None }})
    rule_order: Optional[NpaPolicyRequestRuleOrder] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rule_order'), 'exclude': lambda f: f is None }})
    
