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

res = s.npa.create_a_npa_policy(req)

if res.create_a_npa_policy_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->