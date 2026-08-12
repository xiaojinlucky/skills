# omicverse.single.MetaTiME #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.MetaTiME`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.MetaTiME.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

MetaTiME wrapper for tumor microenvironment cell-state annotation.

## Signature

```text
class omicverse.single. MetaTiME ( adata , mode = 'table' )
```

## Parameters

- `adata`: ( anndata.AnnData ) – AnnData to annotate with MetaTiME meta-components.
- `mode`: ( str , optional , default='table' ) – Output mapping mode for component-to-cell-state interpretation.

## Full Documentation

# omicverse.single.MetaTiME #

class omicverse.single. MetaTiME ( adata , mode = 'table' ) [source] #

MetaTiME wrapper for tumor microenvironment cell-state annotation.

Parameters :

-
adata ( anndata.AnnData ) – AnnData to annotate with MetaTiME meta-components.

-
mode ( str , optional , default='table' ) – Output mapping mode for component-to-cell-state interpretation.

Returns :

Initializes MetaTiME resources and annotation mode.

Return type :

None

Examples

```text
>>> TiME_object = ov.single.MetaTiME(adata, mode="table")

```

__init__ ( adata , mode = 'table' ) [source] #

Initialize MetaTiME model resources and annotation table.

Parameters :

-
adata ( anndata.AnnData ) – AnnData object for MetaTiME annotation.

-
mode ( str ) – Name-mapping mode in `metatime.mecs.load_mecname `. Choose from `'mecnamedict' `, `'table' `or `'meciddict' `.

Methods

`__init__ `(adata[, mode])

Initialize MetaTiME model resources and annotation table.

`overcluster `([resolution, random_state, ...])

Perform high-resolution Leiden clustering for MetaTiME input.

`plot `([basis, cluster_key, fontsize, ...])

Plot MetaTiME annotations with optional label collision adjustment.

`predictTiME `([save_obs_name])

Predict tumor microenvironment cell states for each cell.
