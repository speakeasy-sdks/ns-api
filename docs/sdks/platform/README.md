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

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.DeleteNpaRulesIDRequest](../../models/operations/deletenparulesidrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.DeleteNpaRulesIDResponse](../../models/operations/deletenparulesidresponse.md)**


## get_npa_rules

Get list of npa policies

### Example Usage

```python
import platform
from platform.models import operations, shared

s = platform.Platform(
    api_key="",
)

req = operations.GetNpaRulesRequest()

res = s.platform.get_npa_rules(req)

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


## get_npa_rules_id_

Get a npa policy based on policy rule id

### Example Usage

```python
import platform
from platform.models import operations, shared

s = platform.Platform(
    api_key="",
)

req = operations.GetNpaRulesIDRequest(
    id=408556,
)

res = s.platform.get_npa_rules_id_(req)

if res.get_npa_rules_id_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetNpaRulesIDRequest](../../models/operations/getnparulesidrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetNpaRulesIDResponse](../../models/operations/getnparulesidresponse.md)**


## patch_npa_rules_id_

Patch a npa policy based on rule id

### Example Usage

```python
import platform
from platform.models import operations, shared

s = platform.Platform(
    api_key="",
)

req = operations.PatchNpaRulesIDRequest(
    id=348436,
    npa_policy_request=shared.NpaPolicyRequest(
        description='any',
        enabled='1',
        group_id='1',
        group_name='My policy group',
        rule_data=shared.NpaPolicyRuleData(
            dlp_actions=[
                shared.NpaPolicyRuleDlp(
                    actions=[
                        shared.NpaPolicyRuleDlpActions.ALLOW,
                    ],
                    dlp_profile='Payment Card',
                ),
            ],
            json_version=3,
            match_criteria_action=shared.NpaPolicyRuleDataMatchCriteriaAction(),
            net_location_obj=[
                '190.123.150.10',
                '190.218.0.0/16',
            ],
            organization_units=[
                'engineering/qa',
            ],
            private_app_ids=[
                '100',
                '201',
            ],
            private_app_tag_ids=[
                '1',
                '2',
            ],
            private_app_tags=[
                'tag1',
                'tag2',
            ],
            private_apps=[
                'app1',
                'app2',
            ],
            private_apps_with_activities=[
                shared.NpaPolicyRuleDataPrivateAppsWithActivities(
                    activities=[
                        shared.NpaPolicyRuleDataPrivateAppsWithActivitiesActivities(
                            list_of_constraints=[
                                'Chevrolet',
                            ],
                        ),
                    ],
                    app_name='[172.31.12.135]',
                ),
            ],
            src_countries=[
                'US',
                'AF',
                'CN',
            ],
            user_groups=[
                'usergroup/group1',
            ],
            users=[
                'vphan@netskope.com',
            ],
            version=1,
        ),
        rule_name='vantest',
        rule_order=shared.NpaPolicyRequestRuleOrder(
            position=5,
            rule_id=1,
            rule_name='api-policy-managed',
        ),
    ),
)

res = s.platform.patch_npa_rules_id_(req)

if res.patch_npa_rules_id_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchNpaRulesIDRequest](../../models/operations/patchnparulesidrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.PatchNpaRulesIDResponse](../../models/operations/patchnparulesidresponse.md)**


## post_npa_rules

Create a policy

### Example Usage

```python
import platform
from platform.models import operations, shared

s = platform.Platform(
    api_key="",
)

req = operations.PostNpaRulesRequest(
    npa_policy_request=shared.NpaPolicyRequest(
        description='any',
        enabled='1',
        group_id='1',
        group_name='My policy group',
        rule_data=shared.NpaPolicyRuleData(
            dlp_actions=[
                shared.NpaPolicyRuleDlp(
                    actions=[
                        shared.NpaPolicyRuleDlpActions.ALLOW,
                    ],
                    dlp_profile='Payment Card',
                ),
            ],
            json_version=3,
            match_criteria_action=shared.NpaPolicyRuleDataMatchCriteriaAction(),
            net_location_obj=[
                '190.123.150.10',
                '190.218.0.0/16',
            ],
            organization_units=[
                'engineering/qa',
            ],
            private_app_ids=[
                '100',
                '201',
            ],
            private_app_tag_ids=[
                '1',
                '2',
            ],
            private_app_tags=[
                'tag1',
                'tag2',
            ],
            private_apps=[
                'app1',
                'app2',
            ],
            private_apps_with_activities=[
                shared.NpaPolicyRuleDataPrivateAppsWithActivities(
                    activities=[
                        shared.NpaPolicyRuleDataPrivateAppsWithActivitiesActivities(
                            list_of_constraints=[
                                'woman',
                            ],
                        ),
                    ],
                    app_name='[172.31.12.135]',
                ),
            ],
            src_countries=[
                'US',
                'AF',
                'CN',
            ],
            user_groups=[
                'usergroup/group1',
            ],
            users=[
                'vphan@netskope.com',
            ],
            version=1,
        ),
        rule_name='vantest',
        rule_order=shared.NpaPolicyRequestRuleOrder(
            position=5,
            rule_id=1,
            rule_name='api-policy-managed',
        ),
    ),
)

res = s.platform.post_npa_rules(req)

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

