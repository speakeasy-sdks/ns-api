# Platform SDK


## Overview

npa_policy: NPA policy CRUD operations.

### Available Operations

* [delete_npa_rules_id_](#delete_npa_rules_id_) - Delete a npa policy
* [get_npa_rules](#get_npa_rules) - Get list of npa policies
* [get_npa_rules_id_](#get_npa_rules_id_) - Get a npa policy
* [patch_npa_rules_id_](#patch_npa_rules_id_) - Patch a npa policy
* [post_npa_rules](#post_npa_rules) - Create a npa policy

## delete_npa_rules_id_

Delete a npa policy with rule id

### Example Usage

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

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.DeleteNpaRulesIDRequest](../../models/operations/deletenparulesidrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.DeleteNpaRulesIDResponse](../../models/operations/deletenparulesidresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.NpaPolicyResponse400 | 400                         | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |

## get_npa_rules

Get list of npa policies

### Example Usage

```python
import platform
from platform.models import operations

s = platform.Platform(
    api_key="<YOUR_API_KEY_HERE>",
)

req = operations.GetNpaRulesRequest()

res = s.get_npa_rules(req)

if res.npa_policy_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetNpaRulesRequest](../../models/operations/getnparulesrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetNpaRulesResponse](../../models/operations/getnparulesresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.NpaPolicyResponse400 | 400                         | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |

## get_npa_rules_id_

Get a npa policy based on policy rule id

### Example Usage

```python
import platform
from platform.models import operations

s = platform.Platform(
    api_key="<YOUR_API_KEY_HERE>",
)

req = operations.GetNpaRulesIDRequest(
    id=408556,
)

res = s.get_npa_rules_id_(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetNpaRulesIDRequest](../../models/operations/getnparulesidrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetNpaRulesIDResponse](../../models/operations/getnparulesidresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.NpaPolicyResponse400 | 400                         | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |

## patch_npa_rules_id_

Patch a npa policy based on rule id

### Example Usage

```python
import platform
from platform.models import operations, shared

s = platform.Platform(
    api_key="<YOUR_API_KEY_HERE>",
)

req = operations.PatchNpaRulesIDRequest(
    id=348436,
    npa_policy_request=shared.NpaPolicyRequest(
        description='any',
        enabled='1',
        group_id='1',
        group_name='My policy group',
        rule_name='vantest',
    ),
)

res = s.patch_npa_rules_id_(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchNpaRulesIDRequest](../../models/operations/patchnparulesidrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.PatchNpaRulesIDResponse](../../models/operations/patchnparulesidresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.NpaPolicyResponse400 | 400                         | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |

## post_npa_rules

Create a policy

### Example Usage

```python
import platform
from platform.models import operations, shared

s = platform.Platform(
    api_key="<YOUR_API_KEY_HERE>",
)

req = operations.PostNpaRulesRequest(
    npa_policy_request=shared.NpaPolicyRequest(
        description='any',
        enabled='1',
        group_id='1',
        group_name='My policy group',
        rule_name='vantest',
    ),
)

res = s.post_npa_rules(req)

if res.npa_policy_response_item is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PostNpaRulesRequest](../../models/operations/postnparulesrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.PostNpaRulesResponse](../../models/operations/postnparulesresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.NpaPolicyResponse400 | 400                         | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |
