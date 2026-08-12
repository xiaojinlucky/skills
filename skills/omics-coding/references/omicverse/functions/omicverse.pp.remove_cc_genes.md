# omicverse.pp.remove_cc_genes #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.remove_cc_genes`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.remove_cc_genes.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Remove cell-cycle-correlated genes from highly_variable_features .

## Signature

```text
omicverse.pp. remove_cc_genes ( adata , organism = 'human' , corr_threshold = 0.1 )
```

## Parameters

- `adata`: ( anndata.AnnData ) – AnnData object containing HVG annotations.
- `organism`: ( {"human" , "mouse"} , default="human" ) – Species used to load canonical cell-cycle signatures.
- `corr_threshold`: ( float , default=0.1 ) – Absolute correlation cutoff. HVGs with maximal correlation to cell-cycle genes above this threshold are removed.

## Full Documentation

# omicverse.pp.remove_cc_genes #

omicverse.pp. remove_cc_genes ( adata , organism = 'human' , corr_threshold = 0.1 ) [source] #

Remove cell-cycle-correlated genes from `highly_variable_features `.

Parameters :

-
adata ( anndata.AnnData ) – AnnData object containing HVG annotations.

-
organism ( {"human" , "mouse"} , default="human" ) – Species used to load canonical cell-cycle signatures.

-
corr_threshold ( float , default=0.1 ) – Absolute correlation cutoff. HVGs with maximal correlation to cell-cycle genes above this threshold are removed.

Returns :

Rewrites `adata.var['highly_variable_features'] `after filtering.

Return type :

None
