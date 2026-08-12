# omicverse.space.GASTON #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.GASTON`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.GASTON.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

GASTON spatial depth estimation and clustering.

## Signature

```text
class omicverse.space. GASTON ( adata )
```

## Parameters

- `adata`: ( AnnData ) – Spatial AnnData containing expression matrix and coordinates in adata.obsm['spatial'] .

## Full Documentation

# omicverse.space.GASTON #

class omicverse.space. GASTON ( adata ) [source] #

GASTON spatial depth estimation and clustering.

GASTON (Geometry And Spatial Transcriptomics-based OrganizatioN) is a method for analyzing spatial transcriptomics data by learning continuous spatial depth functions that capture tissue organization. It uses neural networks to model spatial patterns and identify distinct domains.

The method combines gene expression data with spatial information to: 1. Learn continuous spatial depth functions 2. Identify tissue domains and boundaries 3. Model gene expression patterns along spatial gradients 4. Characterize tissue organization and architecture

Parameters :

-
adata ( AnnData ) – Spatial AnnData containing expression matrix and coordinates in `adata.obsm['spatial'] `.

-
Attributes –

adata: AnnData

Input annotated data matrix containing: - Spatial coordinates in adata.obsm[‘spatial’] - Gene expression data in adata.X - Optional histology image in adata.uns[‘spatial’]

model: GASTON model

Trained neural network model after calling train()

gaston_isodepth: array

Computed isodepth values after calling cal_iso_depth()

gaston_labels: array

Domain labels after calling cal_iso_depth()

-
Examples –

```text
>>> import scanpy as sc
>>> import omicverse as ov
>>> # Load spatial data
>>> adata = sc.read_visium(...)
>>> # Initialize GASTON
>>> gaston = ov.space.GASTON(adata)
>>> # Prepare input data
>>> counts, coords, genes = gaston.get_gaston_input()
>>> # Get features
>>> features = gaston.get_top_pearson_residuals(num_dims=10)
>>> # Train model
>>> gaston.load_rescale(features)
>>> gaston.train(num_epochs=5000)
>>> # Get best model
>>> model, features, coords = gaston.get_best_model()
>>> # Calculate domains
>>> isodepth, labels = gaston.cal_iso_depth(num_domains=5)

```

__init__ ( adata ) [source] #

Initialize GASTON spatial clustering object.

Parameters :

adata ( AnnData ) – Input spatial AnnData.

Methods

`__init__ `(adata)

Initialize GASTON spatial clustering object.

`bin_data `([cell_type_df, num_bins, ...])

Bin data along spatial depth gradient.

`cal_iso_depth `([num_domains])

Calculate isodepth values and domain labels.

`filter_genes `([umi_thresh, exclude_prefix])

Filter genes based on expression and name patterns.

`get_best_model `([out_dir, max_domain_num, ...])

Select best GASTON model and determine optimal domain number.

`get_gaston_input `([get_rgb, spot_umi_threshold])

Prepare input data for GASTON analysis.

`get_restricted_adata `([offset])

Create AnnData object from restricted data.

`get_top_pearson_residuals `([num_dims, clip, ...])

Get top Pearson residual features for GASTON analysis.

`load_rescale `(A)

Load and rescale input data for neural network training.

`plot_clusters `(domain_colors[, figsize, s, ...])

Plot spatial domains with cluster colors.

`plot_clusters_restrict `(domain_colors[, ...])

Plot spatial domains with restricted isodepth range.

`plot_gene_gastonrex `(gene_name[, ...])

Plot gene expression with GASTON-specific visualization.

`plot_gene_pwlinear `(gene, domain_colors[, ...])

Plot piecewise linear fit of gene expression.

`plot_gene_raw `(gene_name[, rotate_angle, ...])

Plot raw gene expression in spatial coordinates.

`plot_isodepth `([show_streamlines, ...])

Plot isodepth contours and streamlines.

`pw_linear_fit `([cell_type_df, ct_list, ...])

Perform piecewise linear fitting of gene expression.

`restrict_spot `([isodepth_min, isodepth_max, ...])

Restrict analysis to spots within specific isodepth range.

`train `([isodepth_arch, expression_fn_arch, ...])

Train GASTON neural network models.
