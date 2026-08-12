# omicverse.bulk.batch_correction #

- Package: omicverse
- Language: Python
- Function: `omicverse.bulk.batch_correction`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.bulk.batch_correction.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Perform batch effect correction using ComBat algorithm.

## Signature

```text
omicverse.bulk. batch_correction ( adata , batch_key = None , key_added = 'batch_correction' )
```

## Parameters

- `adata`: ( AnnData ) – AnnData object containing expression data.
- `batch_key`: (default: None ) – Key in adata.obs containing batch information.
- `key_added`: ( str (default: 'batch_correction' )) – Name for the corrected data layer. Default: ‘batch_correction’.

## Full Documentation

# omicverse.bulk.batch_correction #

omicverse.bulk. batch_correction ( adata , batch_key = None , key_added = 'batch_correction' ) [source] #

Perform batch effect correction using ComBat algorithm.

Parameters :

-
adata ( `AnnData `) – AnnData object containing expression data.

-
batch_key (default: `None `) – Key in adata.obs containing batch information.

-
key_added ( `str `(default: `'batch_correction' `)) – Name for the corrected data layer. Default: ‘batch_correction’.

Returns :

The function modifies adata.layers[key_added] in place with batch-corrected expression data.

Return type :

None
