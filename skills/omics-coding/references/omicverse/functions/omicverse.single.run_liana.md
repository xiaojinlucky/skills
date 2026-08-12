# omicverse.single.run_liana #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.run_liana`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.run_liana.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run LIANA ligand-receptor inference on an AnnData object.

## Signature

```text
omicverse.single. run_liana ( adata , * , groupby , method = 'rank_aggregate' , key_added = 'liana_res' , inplace = True , ** kwargs )
```

## Parameters

- `adata`: – AnnData object used by LIANA.
- `groupby`: ( str ) – Observation column with cell-type labels.
- `method`: ( str (default: 'rank_aggregate' )) – LIANA method name under liana.mt . Defaults to 'rank_aggregate' .
- `key_added`: ( str (default: 'liana_res' )) – Key used to store LIANA results in adata.uns when inplace=True .
- `inplace`: ( bool (default: True )) – Whether to write results back to adata.uns .
- `**kwargs`: – Forwarded to the selected LIANA method.

## Full Documentation

# omicverse.single.run_liana #

omicverse.single. run_liana ( adata , * , groupby , method = 'rank_aggregate' , key_added = 'liana_res' , inplace = True , ** kwargs ) [source] #

Run LIANA ligand-receptor inference on an AnnData object.

Parameters :

-
adata – AnnData object used by LIANA.

-
groupby ( `str `) – Observation column with cell-type labels.

-
method ( `str `(default: `'rank_aggregate' `)) – LIANA method name under `liana.mt `. Defaults to `'rank_aggregate' `.

-
key_added ( `str `(default: `'liana_res' `)) – Key used to store LIANA results in `adata.uns `when `inplace=True `.

-
inplace ( `bool `(default: `True `)) – Whether to write results back to `adata.uns `.

-
**kwargs – Forwarded to the selected LIANA method.

Returns :

LIANA result table when `inplace=False `; otherwise returns `adata `.

Return type :

pandas.DataFrame or AnnData
