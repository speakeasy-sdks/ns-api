# Policy
(*policy*)

### Available Operations

* [create_a_npa_policy](#create_a_npa_policy) - Create a npa policy
* [create_a_npa_policy_group](#create_a_npa_policy_group) - Create a npa policy group
* [delete_a_npa_policy](#delete_a_npa_policy) - Delete a npa policy
* [get_a_npa_policy](#get_a_npa_policy) - Get a npa policy
* [get_list_of_npa_policies](#get_list_of_npa_policies) - Get list of npa policies
* [get_list_of_npa_policy_groups](#get_list_of_npa_policy_groups) - Get list of npa policy groups
* [patch_a_npa_policy](#patch_a_npa_policy) - Patch a npa policy

## create_a_npa_policy

Create a policy

### Example Usage

```python
import platform
from platform.models import operations

s = platform.Platform()

req = operations.CreateANpaPolicyRequest(
    request_body=operations.CreateANpaPolicyRequestBody(
        description='<string>',
        group_id='<string>',
        rule_data=operations.CreateANpaPolicyRequestBodyRuleData(
            access_method='Clientless',
            b_negate_net_location='<boolean>',
            b_negate_src_countries='<boolean>',
            classification='<string>',
            excluded_users=[
                '<string>',
            ],
            external_dlp='<boolean>',
            json_version='<integer>',
            match_criteria_action=operations.CreateANpaPolicyRequestBodyRuleDataMatchCriteriaAction(
                action_name='allow',
            ),
            net_location_obj=[
                '<string>',
            ],
            policy_type='private-app',
            private_app_ids=[
                '<string>',
            ],
            private_app_tag_ids=[
                '<string>',
            ],
            private_app_tags=[
                '<string>',
            ],
            private_apps=[
                '<string>',
            ],
            private_apps_with_activities=[
                operations.CreateANpaPolicyRequestBodyRuleDataPrivateAppsWithActivities(
                    activities=[
                        operations.CreateANpaPolicyRequestBodyRuleDataPrivateAppsWithActivitiesActivities(
                            activity='any',
                            list_of_constraints=[
                                '<string>',
                            ],
                        ),
                    ],
                    app_name='<string>',
                ),
            ],
            show_dlp_profile_action_table='<boolean>',
            src_countries=[
                '<string>',
            ],
            user_type='user',
            users=[
                '<string>',
            ],
            version='<integer>',
        ),
        rule_name='<string>',
        rule_order=operations.CreateANpaPolicyRequestBodyRuleOrder(
            order='top',
            position='<integer>',
        ),
    ),
    silent='0',
)

res = s.policy.create_a_npa_policy(req)

if res.create_a_npa_policy_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateANpaPolicyRequest](../../models/operations/createanpapolicyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateANpaPolicyResponse](../../models/operations/createanpapolicyresponse.md)**


## create_a_npa_policy_group

Create a npa policy group

### Example Usage

```python
import platform
from platform.models import operations

s = platform.Platform()

req = operations.CreateANpaPolicyGroupRequest(
    request_body=operations.CreateANpaPolicyGroupRequestBody(
        group_name='<string>',
        group_pinned_id='<string>',
        group_prod_id='<string>',
        group_type='<integer>',
        modify_by='<string>',
        modify_type='<string>',
    ),
    silent='0',
)

res = s.policy.create_a_npa_policy_group(req)

if res.create_a_npa_policy_group_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateANpaPolicyGroupRequest](../../models/operations/createanpapolicygrouprequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.CreateANpaPolicyGroupResponse](../../models/operations/createanpapolicygroupresponse.md)**


## delete_a_npa_policy

Delete a npa policy with rule id

### Example Usage

```python
import platform
from platform.models import operations

s = platform.Platform()

req = operations.DeleteANpaPolicyRequest(
    id='<integer>',
)

res = s.policy.delete_a_npa_policy(req)

if res.delete_a_npa_policy_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.DeleteANpaPolicyRequest](../../models/operations/deleteanpapolicyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.DeleteANpaPolicyResponse](../../models/operations/deleteanpapolicyresponse.md)**


## get_a_npa_policy

Get a npa policy based on policy rule id

### Example Usage

```python
import platform
from platform.models import operations

s = platform.Platform()

req = operations.GetANpaPolicyRequest(
    fields_='<string>',
    id='<integer>',
)

res = s.policy.get_a_npa_policy(req)

if res.get_a_npa_policy_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetANpaPolicyRequest](../../models/operations/getanpapolicyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetANpaPolicyResponse](../../models/operations/getanpapolicyresponse.md)**


## get_list_of_npa_policies

Get list of npa policies

### Example Usage

```python
import platform
from platform.models import operations

s = platform.Platform()

req = operations.GetListOfNpaPoliciesRequest(
    fields_='<string>',
    filter='<string>',
    limit='<integer>',
    offset='<integer>',
    sortby='<string>',
    sortorder='<string>',
)

res = s.policy.get_list_of_npa_policies(req)

if res.get_list_of_npa_policies_200_application_json_objects is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetListOfNpaPoliciesRequest](../../models/operations/getlistofnpapoliciesrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetListOfNpaPoliciesResponse](../../models/operations/getlistofnpapoliciesresponse.md)**


## get_list_of_npa_policy_groups

Get list of npa policy groups

### Example Usage

```python
import platform
from platform.models import operations

s = platform.Platform()

req = operations.GetListOfNpaPolicyGroupsRequest(
    fields_='<string>',
    filter='<string>',
    limit='<integer>',
    offset='<integer>',
    sortby='<string>',
    sortorder='<string>',
)

res = s.policy.get_list_of_npa_policy_groups(req)

if res.get_list_of_npa_policy_groups_200_application_json_objects is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetListOfNpaPolicyGroupsRequest](../../models/operations/getlistofnpapolicygroupsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetListOfNpaPolicyGroupsResponse](../../models/operations/getlistofnpapolicygroupsresponse.md)**


## patch_a_npa_policy

Patch a npa policy based on rule id

### Example Usage

```python
import platform
from platform.models import operations

s = platform.Platform()

req = operations.PatchANpaPolicyRequest(
    request_body=operations.PatchANpaPolicyRequestBody(
        description='<string>',
        group_id='<string>',
        rule_data=operations.PatchANpaPolicyRequestBodyRuleData(
            access_method='Clientless',
            b_negate_net_location='<boolean>',
            b_negate_src_countries='<boolean>',
            classification='<string>',
            excluded_users=[
                '<string>',
            ],
            external_dlp='<boolean>',
            json_version='<integer>',
            match_criteria_action=operations.PatchANpaPolicyRequestBodyRuleDataMatchCriteriaAction(
                action_name='allow',
            ),
            net_location_obj=[
                '<string>',
            ],
            policy_type='private-app',
            private_app_ids=[
                '<string>',
            ],
            private_app_tag_ids=[
                '<string>',
            ],
            private_app_tags=[
                '<string>',
            ],
            private_apps=[
                '<string>',
            ],
            private_apps_with_activities=[
                operations.PatchANpaPolicyRequestBodyRuleDataPrivateAppsWithActivities(
                    activities=[
                        operations.PatchANpaPolicyRequestBodyRuleDataPrivateAppsWithActivitiesActivities(
                            activity='any',
                            list_of_constraints=[
                                '<string>',
                            ],
                        ),
                    ],
                    app_name='<string>',
                ),
            ],
            show_dlp_profile_action_table='<boolean>',
            src_countries=[
                '<string>',
            ],
            user_type='user',
            users=[
                '<string>',
            ],
            version='<integer>',
        ),
        rule_name='<string>',
        rule_order=operations.PatchANpaPolicyRequestBodyRuleOrder(
            order='top',
            position='<integer>',
        ),
    ),
    id='<integer>',
    silent='0',
)

res = s.policy.patch_a_npa_policy(req)

if res.patch_a_npa_policy_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchANpaPolicyRequest](../../models/operations/patchanpapolicyrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.PatchANpaPolicyResponse](../../models/operations/patchanpapolicyresponse.md)**

