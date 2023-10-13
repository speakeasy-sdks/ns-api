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

<!-- Start SDK Available Operations -->
## Available Resources and Operations

### [Platform SDK](docs/sdks/platform/README.md)

* [delete_npa_rules_id_](docs/sdks/platform/README.md#delete_npa_rules_id_) - Delete a npa policy
* [get_npa_rules](docs/sdks/platform/README.md#get_npa_rules) - Get list of npa policies
* [get_npa_rules_id_](docs/sdks/platform/README.md#get_npa_rules_id_) - Get a npa policy
* [patch_npa_rules_id_](docs/sdks/platform/README.md#patch_npa_rules_id_) - Patch a npa policy
* [post_npa_rules](docs/sdks/platform/README.md#post_npa_rules) - Create a npa policy
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
