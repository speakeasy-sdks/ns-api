"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from platform import utils
from typing import Optional

class NpaPolicyRuleDlpActions(str, Enum):
    ALLOW = 'allow'
    BLOCK = 'block'
    ALERT = 'alert'
    QUANRANTINE = 'quanrantine'
    BYPASS = 'bypass'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class NpaPolicyRuleDlp:
    actions: Optional[list[NpaPolicyRuleDlpActions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actions'), 'exclude': lambda f: f is None }})
    dlp_profile: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dlp_profile'), 'exclude': lambda f: f is None }})
    

