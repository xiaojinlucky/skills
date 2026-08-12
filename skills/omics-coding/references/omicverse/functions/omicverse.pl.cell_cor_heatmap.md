# omicverse.pl.cell_cor_heatmap #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.cell_cor_heatmap`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.cell_cor_heatmap.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Compute pairwise correlation/similarity between cell groups and plot as heatmap.

## Signature

```text
omicverse.pl. cell_cor_heatmap ( adata , group_by , * , ref_adata = None , ref_group_by = None , features = None , n_features = 2000 , method = 'pearson' , layer = None , use_raw = False , standard_scale = 'var' , cmap = 'RdBu_r' , figsize = (6, 6) , show_values = True , value_fmt = '.2f' , value_cutoff = 0.0 , row_cluster = True , col_cluster = True , vmin = None , vmax = None , legend = True , legend_style = 'tight' , border = False , save = False , save_pathway = '' , show = False )
```

## Parameters

- `adata`: ( AnnData ) – Annotated data matrix.
- `group_by`: ( str ) – Key in adata.obs for grouping cells (e.g. 'cell_type' ).
- `ref_adata`: ( Optional [ AnnData ] (default: None )) – Optional second AnnData for cross-dataset comparison. If None , the query adata is used as both query and reference.
- `ref_group_by`: ( Optional [ str ] (default: None )) – Grouping key in ref_adata . Defaults to group_by .
- `features`: (default: None ) – Specific features to use. If None , highly-variable genes are used.
- `n_features`: ( int (default: 2000 )) – Number of top variable features to select when features is None .
- `method`: ( str (default: 'pearson' )) – Similarity metric: 'pearson' , 'spearman' , or 'cosine' .
- `layer`: ( Optional [ str ] (default: None )) – Which expression slot to read.
- `use_raw`: ( bool (default: False )) – Which expression slot to read.
- `standard_scale`: ( str (default: 'var' )) – 'var' (per-gene) or 'obs' (per-cell) z-scoring.
- `cmap`: ( str (default: 'RdBu_r' )) – Colour map for the heatmap.
- `figsize`: ( tuple (default: (6, 6) )) – Figure size (width, height) in inches.
- `show_values`: ( bool (default: True )) – Whether to print correlation values inside cells.
- `value_fmt`: ( str (default: '.2f' )) – Format string for printed values (e.g. '.2f' ).
- `value_cutoff`: ( float (default: 0.0 )) – Only display text labels for cells with absolute similarity greater than or equal to this threshold.
- `row_cluster`: ( bool (default: True )) – Whether to hierarchically cluster rows / columns.
- `col_cluster`: ( bool (default: True )) – Whether to hierarchically cluster rows / columns.
- `vmin`: ( Optional [ float ] (default: None )) – Colour limits.
- `vmax`: ( Optional [ float ] (default: None )) – Colour limits.
- `legend`: ( bool (default: True )) – Show colour bar.
- `save`: ( bool | str (default: False )) – Output controls. save may be True / False or a concrete path.
- `save_pathway`: ( str (default: '' )) – Output controls. save may be True / False or a concrete path.
- `show`: ( bool (default: False )) – Output controls. save may be True / False or a concrete path.
- `legend_style`: ( str (default: 'tight' ))
- `border`: ( bool (default: False ))

## Full Documentation

# omicverse.pl.cell_cor_heatmap #

omicverse.pl. cell_cor_heatmap ( adata , group_by , * , ref_adata = None , ref_group_by = None , features = None , n_features = 2000 , method = 'pearson' , layer = None , use_raw = False , standard_scale = 'var' , cmap = 'RdBu_r' , figsize = (6, 6) , show_values = True , value_fmt = '.2f' , value_cutoff = 0.0 , row_cluster = True , col_cluster = True , vmin = None , vmax = None , legend = True , legend_style = 'tight' , border = False , save = False , save_pathway = '' , show = False ) [source] #

Compute pairwise correlation/similarity between cell groups and plot as heatmap.

Computes group-level mean expression and plots the resulting similarity matrix.

Parameters :

-
adata ( `AnnData `) – Annotated data matrix.

-
group_by ( `str `) – Key in `adata.obs `for grouping cells (e.g. `'cell_type' `).

-
ref_adata ( `Optional `[ `AnnData `] (default: `None `)) – Optional second AnnData for cross-dataset comparison. If None , the query `adata `is used as both query and reference.

-
ref_group_by ( `Optional `[ `str `] (default: `None `)) – Grouping key in `ref_adata `. Defaults to `group_by `.

-
features (default: `None `) – Specific features to use. If None , highly-variable genes are used.

-
n_features ( `int `(default: `2000 `)) – Number of top variable features to select when `features `is None .

-
method ( `str `(default: `'pearson' `)) – Similarity metric: `'pearson' `, `'spearman' `, or `'cosine' `.

-
layer ( `Optional `[ `str `] (default: `None `)) – Which expression slot to read.

-
use_raw ( `bool `(default: `False `)) – Which expression slot to read.

-
standard_scale ( `str `(default: `'var' `)) – `'var' `(per-gene) or `'obs' `(per-cell) z-scoring.

-
cmap ( `str `(default: `'RdBu_r' `)) – Colour map for the heatmap.

-
figsize ( `tuple `(default: `(6, 6) `)) – Figure size `(width, height) `in inches.

-
show_values ( `bool `(default: `True `)) – Whether to print correlation values inside cells.

-
value_fmt ( `str `(default: `'.2f' `)) – Format string for printed values (e.g. `'.2f' `).

-
value_cutoff ( `float `(default: `0.0 `)) – Only display text labels for cells with absolute similarity greater than or equal to this threshold.

-
row_cluster ( `bool `(default: `True `)) – Whether to hierarchically cluster rows / columns.

-
col_cluster ( `bool `(default: `True `)) – Whether to hierarchically cluster rows / columns.

-
vmin ( `Optional `[ `float `] (default: `None `)) – Colour limits.

-
vmax ( `Optional `[ `float `] (default: `None `)) – Colour limits.

-
legend ( `bool `(default: `True `)) – Show colour bar.

-
save ( `bool `| `str `(default: `False `)) – Output controls. `save `may be `True `/ `False `or a concrete path.

-
save_pathway ( `str `(default: `'' `)) – Output controls. `save `may be `True `/ `False `or a concrete path.

-
show ( `bool `(default: `False `)) – Output controls. `save `may be `True `/ `False `or a concrete path.

-
legend_style ( `str `(default: `'tight' `))

-
border ( `bool `(default: `False `))

Returns :

Returns the Marsilea plotter by default, or the rendered figure when rendering is triggered for saving/showing/tight legends.

Return type :

marsilea.Heatmap or matplotlib.figure.Figure
