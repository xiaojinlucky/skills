# omicverse.pl.dynamic_heatmap #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.dynamic_heatmap`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.dynamic_heatmap.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot dynamic feature trends along pseudotime, optionally by lineage.

## Signature

```text
omicverse.pl. dynamic_heatmap ( adata , pseudotime , var_names = None , * , lineage_key = None , lineages = None , max_lineages = 2 , top_features = None , cell_bins = 100 , use_cell_columns = True , use_fitted = True , aggregate = 'mean' , smooth_window = 15 , score_smooth_window = 21 , fitted_window = 31 , figsize = (8, 6) , layer = None , use_raw = False , gene_symbols = None , standard_scale = 'var' , cmap = 'viridis' , pseudotime_cmap = 'cividis' , order_by = 'peak' , reverse_ht = None , n_split = None , split_method = 'kmeans-peaktime' , cluster_features_by = None , row_cluster = False , col_cluster = False , show_row_names = False , show_column_names = False , pseudotime_label = None , cell_annotation = None , separate_annotation = None , separate_annotation_type = 'auto' , separate_smooth_window = 21 , feature_labels = None , top_label_features = 10 , legend = True , legend_style = 'tight' , border = False , save = False , save_pathway = '' , show = False , verbose = True )
```

## Parameters

- `adata`: ( AnnData ) – Annotated data matrix containing the expression values.
- `var_names`: (default: None ) – Features to plot. Accepts a list of genes, a single gene name, a mapping of group label to gene list, or None to start from all available features. When None , the function prefers adata.var['highly_variable_features'] or adata.var['highly_variable'] as the candidate pool before falling back to all features.
- `pseudotime`: ( str ) – Key in adata.obs containing the continuous ordering variable.
- `lineage_key`: ( Optional [ str ] (default: None )) – Optional key in adata.obs describing lineage membership.
- `lineages`: (default: None ) – Optional lineage subset to include. When provided, the displayed lineage order follows this sequence.
- `max_lineages`: ( int (default: 2 )) – Maximum number of lineages retained after ordering.
- `top_features`: ( Optional [ int ] (default: None )) – Keep only the highest-scoring dynamic features after ranking. Dynamic scores are computed from smoothed pseudotime correlation multiplied by feature amplitude, so this parameter acts as a post-ranking cap rather than the initial feature selection pool. The printed feature count before fitting refers to the candidate pool before this cap is applied.
- `cell_bins`: ( int (default: 100 )) – Number of bins used when aggregating cells along pseudotime.
- `use_cell_columns`: ( bool (default: True )) – Whether to keep columns at cell/bin resolution instead of grouped lineage blocks.
- `use_fitted`: ( bool (default: True )) – Whether to smooth/fitted the matrix before plotting.
- `aggregate`: ( str (default: 'mean' )) – Aggregation function used when binning cells, for example 'mean' .
- `smooth_window`: ( int (default: 15 )) – Window sizes used for display smoothing, dynamic feature scoring, and fitted trend estimation respectively.
- `score_smooth_window`: ( int (default: 21 )) – Window sizes used for display smoothing, dynamic feature scoring, and fitted trend estimation respectively.
- `fitted_window`: ( int (default: 31 )) – Window sizes used for display smoothing, dynamic feature scoring, and fitted trend estimation respectively.
- `figsize`: ( tuple (default: (8, 6) )) – Figure size (width, height) in inches.
- `layer`: ( Optional [ str ] (default: None )) – Expression source selection passed through to obs_df .
- `use_raw`: ( bool (default: False )) – Expression source selection passed through to obs_df .
- `gene_symbols`: ( Optional [ str ] (default: None )) – Expression source selection passed through to obs_df .
- `standard_scale`: ( str (default: 'var' )) – Scaling mode. Supported values include 'var' , 'zscore' , 'group' , 'minmax' , 'obs' , 'raw' , or None .
- `cmap`: ( str (default: 'viridis' )) – Colormaps for the heatmap body and pseudotime annotations.
- `pseudotime_cmap`: ( str (default: 'cividis' )) – Colormaps for the heatmap body and pseudotime annotations.
- `order_by`: ( str (default: 'peak' )) – Feature ordering strategy, e.g. 'peak' or 'valley' .
- `reverse_ht`: (default: None ) – Optional lineage names or positions whose pseudotime direction should be reversed before plotting.
- `n_split`: ( Optional [ int ] (default: None )) – Controls for splitting dynamic features into blocks.
- `split_method`: ( str (default: 'kmeans-peaktime' )) – Controls for splitting dynamic features into blocks.
- `cluster_features_by`: ( Optional [ str ] (default: None )) – Optional metadata-driven feature clustering mode.
- `row_cluster`: ( bool (default: False )) – Whether to add hierarchical dendrograms for rows or columns.
- `col_cluster`: ( bool (default: False )) – Whether to add hierarchical dendrograms for rows or columns.
- `show_row_names`: ( bool (default: False )) – Whether to show row or column labels directly on the plot. When show_row_names=True , gene names are placed directly beside the heatmap without connector lines.
- `show_column_names`: ( bool (default: False )) – Whether to show row or column labels directly on the plot. When show_row_names=True , gene names are placed directly beside the heatmap without connector lines.
- `pseudotime_label`: (default: None ) – Optional custom label for the pseudotime annotation.
- `cell_annotation`: (default: None ) – Optional adata.obs key or keys to annotate cells/bins above the heatmap.
- `separate_annotation`: (default: None ) – Controls for auxiliary smoothed annotation tracks.
- `separate_annotation_type`: ( str (default: 'auto' )) – Controls for auxiliary smoothed annotation tracks.
- `separate_smooth_window`: ( int (default: 21 )) – Controls for auxiliary smoothed annotation tracks.
- `feature_labels`: (default: None ) – Explicit feature labels to force-display. When provided, these labels take priority over top_label_features .
- `top_label_features`: ( int (default: 10 )) – Target number of automatically selected feature labels to display when feature_labels is not provided and show_row_names=False . The function tries to honor this count while still enforcing spacing between labels, so the final number may be slightly smaller in dense layouts.
- `legend`: ( bool (default: True )) – Legend visibility and layout strategy.
- `legend_style`: ( str (default: 'tight' )) – Legend visibility and layout strategy.
- `border`: ( bool (default: False )) – Whether to draw a visible border around heatmap axes after rendering.
- `save`: ( bool | str (default: False )) – Output controls. save may be True / False or a concrete path.
- `save_pathway`: ( str (default: '' )) – Output controls. save may be True / False or a concrete path.
- `show`: ( bool (default: False )) – Output controls. save may be True / False or a concrete path.
- `verbose`: ( bool (default: True )) – Whether to print a short preparation/rendering summary.

## Full Documentation

# omicverse.pl.dynamic_heatmap #

omicverse.pl. dynamic_heatmap ( adata , pseudotime , var_names = None , * , lineage_key = None , lineages = None , max_lineages = 2 , top_features = None , cell_bins = 100 , use_cell_columns = True , use_fitted = True , aggregate = 'mean' , smooth_window = 15 , score_smooth_window = 21 , fitted_window = 31 , figsize = (8, 6) , layer = None , use_raw = False , gene_symbols = None , standard_scale = 'var' , cmap = 'viridis' , pseudotime_cmap = 'cividis' , order_by = 'peak' , reverse_ht = None , n_split = None , split_method = 'kmeans-peaktime' , cluster_features_by = None , row_cluster = False , col_cluster = False , show_row_names = False , show_column_names = False , pseudotime_label = None , cell_annotation = None , separate_annotation = None , separate_annotation_type = 'auto' , separate_smooth_window = 21 , feature_labels = None , top_label_features = 10 , legend = True , legend_style = 'tight' , border = False , save = False , save_pathway = '' , show = False , verbose = True ) [source] #

Plot dynamic feature trends along pseudotime, optionally by lineage.

Parameters :

-
adata ( `AnnData `) – Annotated data matrix containing the expression values.

-
var_names (default: `None `) – Features to plot. Accepts a list of genes, a single gene name, a mapping of group label to gene list, or `None `to start from all available features. When `None `, the function prefers `adata.var['highly_variable_features'] `or `adata.var['highly_variable'] `as the candidate pool before falling back to all features.

-
pseudotime ( `str `) – Key in `adata.obs `containing the continuous ordering variable.

-
lineage_key ( `Optional `[ `str `] (default: `None `)) – Optional key in `adata.obs `describing lineage membership.

-
lineages (default: `None `) – Optional lineage subset to include. When provided, the displayed lineage order follows this sequence.

-
max_lineages ( `int `(default: `2 `)) – Maximum number of lineages retained after ordering.

-
top_features ( `Optional `[ `int `] (default: `None `)) – Keep only the highest-scoring dynamic features after ranking. Dynamic scores are computed from smoothed pseudotime correlation multiplied by feature amplitude, so this parameter acts as a post-ranking cap rather than the initial feature selection pool. The printed feature count before fitting refers to the candidate pool before this cap is applied.

-
cell_bins ( `int `(default: `100 `)) – Number of bins used when aggregating cells along pseudotime.

-
use_cell_columns ( `bool `(default: `True `)) – Whether to keep columns at cell/bin resolution instead of grouped lineage blocks.

-
use_fitted ( `bool `(default: `True `)) – Whether to smooth/fitted the matrix before plotting.

-
aggregate ( `str `(default: `'mean' `)) – Aggregation function used when binning cells, for example `'mean' `.

-
smooth_window ( `int `(default: `15 `)) – Window sizes used for display smoothing, dynamic feature scoring, and fitted trend estimation respectively.

-
score_smooth_window ( `int `(default: `21 `)) – Window sizes used for display smoothing, dynamic feature scoring, and fitted trend estimation respectively.

-
fitted_window ( `int `(default: `31 `)) – Window sizes used for display smoothing, dynamic feature scoring, and fitted trend estimation respectively.

-
figsize ( `tuple `(default: `(8, 6) `)) – Figure size `(width, height) `in inches.

-
layer ( `Optional `[ `str `] (default: `None `)) – Expression source selection passed through to `obs_df `.

-
use_raw ( `bool `(default: `False `)) – Expression source selection passed through to `obs_df `.

-
gene_symbols ( `Optional `[ `str `] (default: `None `)) – Expression source selection passed through to `obs_df `.

-
standard_scale ( `str `(default: `'var' `)) – Scaling mode. Supported values include `'var' `, `'zscore' `, `'group' `, `'minmax' `, `'obs' `, `'raw' `, or `None `.

-
cmap ( `str `(default: `'viridis' `)) – Colormaps for the heatmap body and pseudotime annotations.

-
pseudotime_cmap ( `str `(default: `'cividis' `)) – Colormaps for the heatmap body and pseudotime annotations.

-
order_by ( `str `(default: `'peak' `)) – Feature ordering strategy, e.g. `'peak' `or `'valley' `.

-
reverse_ht (default: `None `) – Optional lineage names or positions whose pseudotime direction should be reversed before plotting.

-
n_split ( `Optional `[ `int `] (default: `None `)) – Controls for splitting dynamic features into blocks.

-
split_method ( `str `(default: `'kmeans-peaktime' `)) – Controls for splitting dynamic features into blocks.

-
cluster_features_by ( `Optional `[ `str `] (default: `None `)) – Optional metadata-driven feature clustering mode.

-
row_cluster ( `bool `(default: `False `)) – Whether to add hierarchical dendrograms for rows or columns.

-
col_cluster ( `bool `(default: `False `)) – Whether to add hierarchical dendrograms for rows or columns.

-
show_row_names ( `bool `(default: `False `)) – Whether to show row or column labels directly on the plot. When `show_row_names=True `, gene names are placed directly beside the heatmap without connector lines.

-
show_column_names ( `bool `(default: `False `)) – Whether to show row or column labels directly on the plot. When `show_row_names=True `, gene names are placed directly beside the heatmap without connector lines.

-
pseudotime_label (default: `None `) – Optional custom label for the pseudotime annotation.

-
cell_annotation (default: `None `) – Optional `adata.obs `key or keys to annotate cells/bins above the heatmap.

-
separate_annotation (default: `None `) – Controls for auxiliary smoothed annotation tracks.

-
separate_annotation_type ( `str `(default: `'auto' `)) – Controls for auxiliary smoothed annotation tracks.

-
separate_smooth_window ( `int `(default: `21 `)) – Controls for auxiliary smoothed annotation tracks.

-
feature_labels (default: `None `) – Explicit feature labels to force-display. When provided, these labels take priority over `top_label_features `.

-
top_label_features ( `int `(default: `10 `)) – Target number of automatically selected feature labels to display when `feature_labels `is not provided and `show_row_names=False `. The function tries to honor this count while still enforcing spacing between labels, so the final number may be slightly smaller in dense layouts.

-
legend ( `bool `(default: `True `)) – Legend visibility and layout strategy.

-
legend_style ( `str `(default: `'tight' `)) – Legend visibility and layout strategy.

-
border ( `bool `(default: `False `)) – Whether to draw a visible border around heatmap axes after rendering.

-
save ( `bool `| `str `(default: `False `)) – Output controls. `save `may be `True `/ `False `or a concrete path.

-
save_pathway ( `str `(default: `'' `)) – Output controls. `save `may be `True `/ `False `or a concrete path.

-
show ( `bool `(default: `False `)) – Output controls. `save `may be `True `/ `False `or a concrete path.

-
verbose ( `bool `(default: `True `)) – Whether to print a short preparation/rendering summary.

Returns :

Returns the assembled Marsilea board by default. When rendering is triggered for saving, showing, or tight-legend export, returns the rendered matplotlib figure instead.

Return type :

marsilea.StackBoard or matplotlib.figure.Figure
