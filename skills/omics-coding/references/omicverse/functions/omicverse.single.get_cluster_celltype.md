# omicverse.single.get_cluster_celltype #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.get_cluster_celltype`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.get_cluster_celltype.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Resolve one final cell type for each cluster with LLM calls.

## Signature

```text
omicverse.single. get_cluster_celltype ( cluster_celltypes , cluster_markers , species , organization , model , base_url , provider , api_key = None , timeout = 30 , max_retries = 2 , retry_backoff = 1.5 , verbose = True )
```

## Parameters

- `cluster_celltypes`: ( dict ) – Candidate labels per cluster, usually dict[cluster_id -> list[str]] .
- `cluster_markers`: ( dict ) – Marker genes per cluster, usually dict[cluster_id -> list[str]] .
- `species`: ( str ) – Species context used in prompt construction.
- `organization`: ( str ) – Tissue/organ context used in prompt construction.
- `model`: ( str ) – Chat completion model name.
- `base_url`: ( str or None ) – API base URL. If None , inferred from provider .
- `provider`: ( str ) – Provider preset used for base URL fallback.
- `api_key`: ( str or None , default=None ) – Optional API key override. If None , reads AGI_API_KEY .
- `timeout`: ( int , default=30 ) – Request timeout in seconds for each API call.
- `max_retries`: ( int , default=2 ) – Maximum retry count for failed requests.
- `retry_backoff`: ( float , default=1.5 ) – Exponential backoff base for retry waiting time.
- `verbose`: ( bool , default=True ) – Whether to print retry/fallback diagnostics.

## Full Documentation

# omicverse.single.get_cluster_celltype #

omicverse.single. get_cluster_celltype ( cluster_celltypes , cluster_markers , species , organization , model , base_url , provider , api_key = None , timeout = 30 , max_retries = 2 , retry_backoff = 1.5 , verbose = True ) [source] #

Resolve one final cell type for each cluster with LLM calls.

Parameters :

-
cluster_celltypes ( dict ) – Candidate labels per cluster, usually `dict[cluster_id -> list[str]] `.

-
cluster_markers ( dict ) – Marker genes per cluster, usually `dict[cluster_id -> list[str]] `.

-
species ( str ) – Species context used in prompt construction.

-
organization ( str ) – Tissue/organ context used in prompt construction.

-
model ( str ) – Chat completion model name.

-
base_url ( str or None ) – API base URL. If `None `, inferred from `provider `.

-
provider ( str ) – Provider preset used for base URL fallback.

-
api_key ( str or None , default=None ) – Optional API key override. If `None `, reads `AGI_API_KEY `.

-
timeout ( int , default=30 ) – Request timeout in seconds for each API call.

-
max_retries ( int , default=2 ) – Maximum retry count for failed requests.

-
retry_backoff ( float , default=1.5 ) – Exponential backoff base for retry waiting time.

-
verbose ( bool , default=True ) – Whether to print retry/fallback diagnostics.

Returns :

Mapping from cluster ID to predicted (or fallback) cell-type label.

Return type :

dict
