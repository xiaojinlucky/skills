# omicverse.datasets.get_adata #

- Package: omicverse
- Language: Python
- Function: `omicverse.datasets.get_adata`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.datasets.get_adata.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Download example data to local folder.

## Signature

```text
omicverse.datasets. get_adata ( url , filename = None )
```

## Parameters

- `url`: ( str ) – Download URL of an .h5ad or .loom dataset file.
- `filename`: ( Optional [ str ] ) – Local filename used for caching.

## Full Documentation

# omicverse.datasets.get_adata #

omicverse.datasets. get_adata ( url , filename = None ) [source] #

Download example data to local folder.

Parameters :

-
url ( str ) – Download URL of an `.h5ad `or `.loom `dataset file.

-
filename ( Optional [ str ] ) – Local filename used for caching.

Returns :

Loaded AnnData object; `None `if loading fails.

Return type :

Optional[AnnData]
