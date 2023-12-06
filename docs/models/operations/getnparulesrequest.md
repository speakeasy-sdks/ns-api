# GetNpaRulesRequest


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `fields`                                                          | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Return values only from specified fields                          |
| `filter_`                                                         | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Query string based on query operaters                             |
| `limit`                                                           | *Optional[int]*                                                   | :heavy_minus_sign:                                                | Max number of policies to retrieve. Default will be all policies. |
| `offset`                                                          | *Optional[int]*                                                   | :heavy_minus_sign:                                                | The offset of the first policy in the list to retrieve.           |
| `sortby`                                                          | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Sort retrieved policies by specified field. Default is policy id  |
| `sortorder`                                                       | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Sort in either asc or desc order. The default is asc order        |