<!-- Start SDK Example Usage -->


```python
import platform
from platform.models import operations, shared

s = platform.Platform(
    api_key="",
)

req = operations.DeleteNpaRulesIDRequest(
    id=324988,
)

res = s.platform.delete_npa_rules_id_(req)

if res.delete_npa_rules_id_200_application_json_object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->