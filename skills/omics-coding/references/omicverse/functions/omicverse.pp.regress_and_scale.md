# omicverse.pp.regress_and_scale #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.regress_and_scale`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.regress_and_scale.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Scale the regressed layer and store it as a new analysis layer.

## Signature

```text
omicverse.pp. regress_and_scale ( adata )
```

## Parameters

- `adata`: ( anndata.AnnData ) – AnnData object containing adata.layers['regressed'] .

## Full Documentation

# omicverse.pp.regress_and_scale #

omicverse.pp. regress_and_scale ( adata ) [source] #

Scale the regressed layer and store it as a new analysis layer.

Parameters :

adata ( anndata.AnnData ) – AnnData object containing `adata.layers['regressed'] `.

Returns :

The same object with `adata.layers['regressed_and_scaled'] `added.

Return type :

anndata.AnnData
