<!-- Start SDK Example Usage [usage] -->
```python
import platform
from platform.models import operations

s = platform.Platform(
    api_key="<YOUR_API_KEY_HERE>",
)

req = operations.DeleteNpaRulesIDRequest(
    id=324988,
)

res = s.delete_npa_rules_id_(req)

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->