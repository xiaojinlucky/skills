# omicverse.pl.calculate_gene_density #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.calculate_gene_density`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.calculate_gene_density.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Calculate weighted kernel density estimates for gene expression on 2D embeddings.

## Signature

```text
omicverse.pl. calculate_gene_density ( adata , features , basis = 'X_umap' , dims = (0, 1) , adjust = 1 , min_expr = 0.1 , layer = None , use_raw = None )
```

## Parameters

- `adata`: – Annotated data object with embedding coordinates
- `features`: – List of gene names or feature names to process
- `basis`: (default: 'X_umap' ) – Key in adata.obsm containing 2D embedding coordinates (‘X_umap’)
- `dims`: (default: (0, 1) ) – Embedding dimensions to use as (x_dim, y_dim) ((0, 1))
- `adjust`: (default: 1 ) – Bandwidth scaling factor for KDE (1)
- `min_expr`: (default: 0.1 ) – Minimum expression threshold for including cells (0.1)
- `layer`: (default: None ) – Read expression from adata.layers[layer] instead of .X (None)
- `use_raw`: (default: None ) – Force ( True ) or forbid ( False ) reading from adata.raw . None reads .X and falls back to .raw only for names that are absent from .var_names — see ov.pl.get_values (None)

## Full Documentation

# omicverse.pl.calculate_gene_density #

omicverse.pl. calculate_gene_density ( adata , features , basis = 'X_umap' , dims = (0, 1) , adjust = 1 , min_expr = 0.1 , layer = None , use_raw = None ) [source] #

Calculate weighted kernel density estimates for gene expression on 2D embeddings.

Computes KDE for each feature using expression values as weights and stores density values in adata.obs as ‘density_{feature}’ columns.

Parameters :

-
adata – Annotated data object with embedding coordinates

-
features – List of gene names or feature names to process

-
basis (default: `'X_umap' `) – Key in adata.obsm containing 2D embedding coordinates (‘X_umap’)

-
dims (default: `(0, 1) `) – Embedding dimensions to use as (x_dim, y_dim) ((0, 1))

-
adjust (default: `1 `) – Bandwidth scaling factor for KDE (1)

-
min_expr (default: `0.1 `) – Minimum expression threshold for including cells (0.1)

-
layer (default: `None `) – Read expression from adata.layers[layer] instead of .X (None)

-
use_raw (default: `None `) – Force ( True ) or forbid ( False ) reading from adata.raw . None reads .X and falls back to .raw only for names that are absent from .var_names — see ov.pl.get_values (None)

Returns :

Updates adata.obs with density_{feature} columns

Return type :

None
