# Platform

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/speakeasy-sdks/ns-api.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/ns-api/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/ns-api.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
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
                '<string>',
            ],
            external_dlp='<boolean>',
            json_version='<integer>',
            match_criteria_action=operations.CreateANpaPolicyRequestBodyRuleDataMatchCriteriaAction(
                action_name='allow',
            ),
            net_location_obj=[
                '<string>',
                '<string>',
            ],
            policy_type='private-app',
            private_app_ids=[
                '<string>',
                '<string>',
            ],
            private_app_tag_ids=[
                '<string>',
                '<string>',
            ],
            private_app_tags=[
                '<string>',
                '<string>',
            ],
            private_apps=[
                '<string>',
                '<string>',
            ],
            private_apps_with_activities=[
                operations.CreateANpaPolicyRequestBodyRuleDataPrivateAppsWithActivities(
                    activities=[
                        operations.CreateANpaPolicyRequestBodyRuleDataPrivateAppsWithActivitiesActivities(
                            activity='any',
                            list_of_constraints=[
                                '<string>',
                                '<string>',
                            ],
                        ),
                        operations.CreateANpaPolicyRequestBodyRuleDataPrivateAppsWithActivitiesActivities(
                            activity='any',
                            list_of_constraints=[
                                '<string>',
                                '<string>',
                            ],
                        ),
                    ],
                    app_name='<string>',
                ),
                operations.CreateANpaPolicyRequestBodyRuleDataPrivateAppsWithActivities(
                    activities=[
                        operations.CreateANpaPolicyRequestBodyRuleDataPrivateAppsWithActivitiesActivities(
                            activity='any',
                            list_of_constraints=[
                                '<string>',
                                '<string>',
                            ],
                        ),
                        operations.CreateANpaPolicyRequestBodyRuleDataPrivateAppsWithActivitiesActivities(
                            activity='any',
                            list_of_constraints=[
                                '<string>',
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
                '<string>',
            ],
            user_type='user',
            users=[
                '<string>',
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

res = s.npa.create_a_npa_policy(req)

if res.create_a_npa_policy_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [npa](docs/sdks/npa/README.md)

* [create_a_npa_policy](docs/sdks/npa/README.md#create_a_npa_policy) - Create a npa policy
* [create_a_npa_policy_group](docs/sdks/npa/README.md#create_a_npa_policy_group) - Create a npa policy group
* [delete_a_npa_policy](docs/sdks/npa/README.md#delete_a_npa_policy) - Delete a npa policy
* [get_a_npa_policy](docs/sdks/npa/README.md#get_a_npa_policy) - Get a npa policy
* [get_list_of_npa_policies](docs/sdks/npa/README.md#get_list_of_npa_policies) - Get list of npa policies
* [get_list_of_npa_policy_groups](docs/sdks/npa/README.md#get_list_of_npa_policy_groups) - Get list of npa policy groups
* [patch_a_npa_policy](docs/sdks/npa/README.md#patch_a_npa_policy) - Patch a npa policy

### [policy](docs/sdks/policy/README.md)

* [create_a_npa_policy](docs/sdks/policy/README.md#create_a_npa_policy) - Create a npa policy
* [create_a_npa_policy_group](docs/sdks/policy/README.md#create_a_npa_policy_group) - Create a npa policy group
* [delete_a_npa_policy](docs/sdks/policy/README.md#delete_a_npa_policy) - Delete a npa policy
* [get_a_npa_policy](docs/sdks/policy/README.md#get_a_npa_policy) - Get a npa policy
* [get_list_of_npa_policies](docs/sdks/policy/README.md#get_list_of_npa_policies) - Get list of npa policies
* [get_list_of_npa_policy_groups](docs/sdks/policy/README.md#get_list_of_npa_policy_groups) - Get list of npa policy groups
* [patch_a_npa_policy](docs/sdks/policy/README.md#patch_a_npa_policy) - Patch a npa policy
<!-- End SDK Available Operations -->

<!-- Start Dev Containers -->

<!-- End Dev Containers -->

<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
