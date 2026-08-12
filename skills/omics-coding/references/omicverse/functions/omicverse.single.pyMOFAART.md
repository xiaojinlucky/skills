# omicverse.single.pyMOFAART #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.pyMOFAART`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.pyMOFAART.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Load pretrained MOFA models for downstream factor interpretation.

## Signature

```text
class omicverse.single. pyMOFAART ( model_path )
```

## Parameters

- `model_path`: ( str ) – Path to a trained MOFA model file.

## Full Documentation

# omicverse.single.pyMOFAART #

class omicverse.single. pyMOFAART ( model_path ) [source] #

Load pretrained MOFA models for downstream factor interpretation.

Parameters :

model_path ( str ) – Path to a trained MOFA model file.

Returns :

Initializes MOFA model reader and analysis utilities.

Return type :

None

Examples

```text
>>> pymofa_obj = ov.single.pyMOFAART(model_path="data/sample/MOFA_POS.hdf5")

```

__init__ ( model_path ) [source] #

Load a pretrained MOFA model for downstream interpretation.

Parameters :

model_path ( str ) – Path to a trained MOFA `.hdf5 `model file.

Methods

`__init__ `(model_path)

Load a pretrained MOFA model for downstream interpretation.

`get_cor `(adata, cluster[, factor_list])

Compute factor-group association scores from MOFA factors.

`get_factors `(adata)

Attach MOFA latent factors to `adata.obsm['X_mofa'] `.

`get_r2 `()

Return factor-wise explained variance table.

`get_top_feature `(view[, log2fc_min, pval_cutoff])

Identify top features for each factor using differential marker ranking.

`plot_cor `(adata, cluster[, factor_list, ...])

Visualize factor-group association scores as a heatmap.

`plot_factor `(adata, cluster, title[, ...])

Plot cells in MOFA factor space colored by group annotation.

`plot_r2 `([figsize, cmap, ticks_fontsize, ...])

Plot a heatmap of variance explained by each MOFA factor.

`plot_top_feature_dotplot `(view[, cmap, ...])

Plot top marker features per factor as a Scanpy dotplot.

`plot_top_feature_heatmap `(view[, cmap, ...])

Plot top marker features per factor as a Scanpy matrix heatmap.

`plot_weight_gene_d1 `(view, factor1, factor2)

Plot gene weights for two factors with 1D threshold-based highlighting.

`plot_weight_gene_d2 `(view, factor1, factor2)

Plot gene weights for two factors with quadrant-based labeling.

`plot_weights_gene_factor `(view, factor[, ...])

Plot ranked gene weights for a single MOFA factor.
