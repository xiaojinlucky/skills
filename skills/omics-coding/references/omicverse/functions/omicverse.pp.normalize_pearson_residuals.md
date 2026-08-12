# omicverse.pp.normalize_pearson_residuals #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.normalize_pearson_residuals`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.normalize_pearson_residuals.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Normalize a count matrix using analytic Pearson residuals (Lause 2021).

## Signature

```text
omicverse.pp. normalize_pearson_residuals ( adata , * , theta = 100 , clip = None , check_values = True , layer = None , inplace = True , copy = False , ** kwargs )
```

## Parameters

- `adata`: ( anndata.AnnData ) – AnnData object containing counts in adata.X (or layer ).
- `theta`: ( float (default: 100 )) – Negative binomial overdispersion parameter. 100 matches Lause 2021 and is a reasonable default for scRNA.
- `clip`: ( Optional [ float ] (default: None )) – Clip residuals to [-clip, clip] . None uses the scanpy default ( sqrt(n_obs) ).
- `check_values`: ( bool (default: True )) – Validate that the input looks like counts.
- `layer`: ( Optional [ str ] (default: None )) – Layer to normalise. None uses adata.X .
- `inplace`: ( bool (default: True )) – Write back into adata ( True ) or return the matrix ( False ).
- `copy`: ( bool (default: False )) – Return a new AnnData instead of modifying in place (only when inplace=True ).
- `**kwargs`: – Forwarded to scanpy.experimental.pp.normalize_pearson_residuals .

## Full Documentation

# omicverse.pp.normalize_pearson_residuals #

omicverse.pp. normalize_pearson_residuals ( adata , * , theta = 100 , clip = None , check_values = True , layer = None , inplace = True , copy = False , ** kwargs ) [source] #

Normalize a count matrix using analytic Pearson residuals (Lause 2021).

Parameters :

-
adata ( anndata.AnnData ) – AnnData object containing counts in `adata.X `(or `layer `).

-
theta ( `float `(default: `100 `)) – Negative binomial overdispersion parameter. `100 `matches Lause 2021 and is a reasonable default for scRNA.

-
clip ( `Optional `[ `float `] (default: `None `)) – Clip residuals to `[-clip, clip] `. `None `uses the scanpy default ( `sqrt(n_obs) `).

-
check_values ( `bool `(default: `True `)) – Validate that the input looks like counts.

-
layer ( `Optional `[ `str `] (default: `None `)) – Layer to normalise. `None `uses `adata.X `.

-
inplace ( `bool `(default: `True `)) – Write back into `adata `( `True `) or return the matrix ( `False `).

-
copy ( `bool `(default: `False `)) – Return a new AnnData instead of modifying in place (only when `inplace=True `).

-
**kwargs – Forwarded to `scanpy.experimental.pp.normalize_pearson_residuals `.

Returns :

Updates `adata.X `in place with Pearson residuals.

Return type :

None
