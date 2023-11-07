# PatchNpaRulesIDRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *int*                                                              | :heavy_check_mark:                                                 | policy rule id                                                     |
| `npa_policy_request`                                               | [shared.NpaPolicyRequest](../../models/shared/npapolicyrequest.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `silent`                                                           | [Optional[operations.Silent]](../../models/operations/silent.md)   | :heavy_minus_sign:                                                 | flag to skip output except status code                             |