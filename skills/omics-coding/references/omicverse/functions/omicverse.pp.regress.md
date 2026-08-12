# omicverse.pp.regress #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.regress`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.regress.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Regress out technical covariates from each gene.

## Signature

```text
omicverse.pp. regress ( adata , * , keys = None , layer = None , n_jobs = 8 , ** kwargs )
```

## Parameters

- `adata`: ( anndata.AnnData ) – AnnData object. The columns specified in keys must exist in adata.obs .
- `keys`: ( list of str , optional ) – Column names in adata.obs to regress out. Defaults to ['mito_perc', 'nUMIs'] , which are computed by ov.pp.qc . Common additions include cell-cycle scores ( S_score , G2M_score ) and ribosomal gene percentage.
- `layer`: (default: None ) – Expression layer to regress. None uses adata.X .
- `n_jobs`: (default: 8 ) – Parallel jobs for the CPU regressor. Default 8 .
- `**kwargs`: – Extra options forwarded to scanpy.pp.regress_out on CPU (e.g. copy ). Ignored when the GPU backend ( rapids_singlecell ) is active.

## Full Documentation

# omicverse.pp.regress #

omicverse.pp. regress ( adata , * , keys = None , layer = None , n_jobs = 8 , ** kwargs ) [source] #

Regress out technical covariates from each gene.

Parameters :

-
adata ( anndata.AnnData ) – AnnData object. The columns specified in `keys `must exist in `adata.obs `.

-
keys ( list of str , optional ) – Column names in `adata.obs `to regress out. Defaults to `['mito_perc', 'nUMIs'] `, which are computed by `ov.pp.qc `. Common additions include cell-cycle scores ( `S_score `, `G2M_score `) and ribosomal gene percentage.

-
layer (default: `None `) – Expression layer to regress. `None `uses `adata.X `.

-
n_jobs (default: `8 `) – Parallel jobs for the CPU regressor. Default `8 `.

-
**kwargs – Extra options forwarded to `scanpy.pp.regress_out `on CPU (e.g. `copy `). Ignored when the GPU backend ( `rapids_singlecell `) is active.

Returns :

Writes the residualised expression to `adata.layers['regressed'] `.

Return type :

None
