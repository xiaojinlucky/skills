# omicverse.single.factor_exact #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.factor_exact`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.factor_exact.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Add MOFA latent factors from model file into adata.obs .

## Signature

```text
omicverse.single. factor_exact ( adata , hdf5_path )
```

## Parameters

- `adata`: ( anndata.AnnData ) – AnnData object to annotate.
- `hdf5_path`: ( str ) – Path to MOFA .hdf5 model file.

## Full Documentation

# omicverse.single.factor_exact #

omicverse.single. factor_exact ( adata , hdf5_path ) [source] #

Add MOFA latent factors from model file into `adata.obs `.

Parameters :

-
adata ( anndata.AnnData ) – AnnData object to annotate.

-
hdf5_path ( str ) – Path to MOFA `.hdf5 `model file.

Returns :

Input AnnData with added columns `factor1 `, `factor2 `, … in `adata.obs `.

Return type :

anndata.AnnData
