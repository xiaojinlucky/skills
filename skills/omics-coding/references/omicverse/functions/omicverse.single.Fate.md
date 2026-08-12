# omicverse.single.Fate #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.Fate`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.Fate.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Adaptive ridge-regression framework for pseudotime-associated gene discovery.

## Signature

```text
class omicverse.single. Fate ( adata , pseudotime )
```

## Parameters

- `adata`: ( anndata.AnnData ) – AnnData object containing pseudotime in obs and gene expression features.
- `pseudotime`: ( str ) – adata.obs key storing pseudotime values.

## Full Documentation

# omicverse.single.Fate #

class omicverse.single. Fate ( adata , pseudotime ) [source] #

Adaptive ridge-regression framework for pseudotime-associated gene discovery.

Parameters :

-
adata ( anndata.AnnData ) – AnnData object containing pseudotime in `obs `and gene expression features.

-
pseudotime ( str ) – `adata.obs `key storing pseudotime values.

Returns :

Initializes Fate model state.

Return type :

None

Examples

```text
>>> # Initialize Fate analysis

```

__init__ ( adata , pseudotime ) [source] #

Initialize TimeFate model.

Parameters :

-
adata ( anndata.AnnData ) – Input AnnData containing expression matrix and pseudotime metadata.

-
pseudotime ( str ) – Column name in `adata.obs `storing pseudotime values.

Methods

`ATR `([test_size, random_state, alpha, stop, ...])

Adaptive Threshold Regression

`__init__ `(adata, pseudotime)

Initialize TimeFate model.

`atac_init `(columns[, gene_name])

Initialize the atac model

`get_coef `([type])

Get the coef of model

`get_mae `([type])

Get the mae of model

`get_mse `([type])

Get the mse of model

`get_r2 `([type])

Get the r2 of model

`get_related_peak `(peak)

Get the related peak of gene

`get_rmse `([type])

Get the rmse of model

`kendalltau_filter `()

Compute Kendall's tau between filtered gene trends and pseudotime.

`lineage_score `(cluster_key[, lineage, ...])

Compute lineage-specific change scores using low-density variability.

`low_density `([n_components, knn, alpha, ...])

Estimate manifold density on diffusion-map coordinates.

`model_fit `([test_size, random_state, alpha, ...])

Fit the model

`model_init `([test_size, random_state, alpha, ...])

Initialize the model

`plot_color_fitting `([type, cluster_key, ...])

Plot the colorful of clusters fitting result

`plot_filtering `([figsize, color, fontsize, alpha])

Plot the filtering result

`plot_fitting `([type, figsize, color, fontsize])

Plot the fitting result
