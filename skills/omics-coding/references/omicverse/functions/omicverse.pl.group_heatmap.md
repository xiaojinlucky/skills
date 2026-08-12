# omicverse.pl.group_heatmap #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.group_heatmap`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.group_heatmap.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot grouped mean expression as a Marsilea heatmap.

## Signature

```text
omicverse.pl. group_heatmap ( adata , var_names , groupby , * , figsize = (6, 10) , layer = None , use_raw = False , gene_symbols = None , standard_scale = None , cmap = 'RdBu_r' , row_cluster = False , col_cluster = False , row_split = None , col_split = None , left_color_bars = None , left_color_labels = None , right_color_bars = None , right_color_labels = None , col_color_bars = None , legend = True , legend_style = 'tight' , border = False , label = 'Mean expression' , show_values = False , value_fmt = '.2f' , value_cutoff = 0.0 , save = False , save_pathway = '' , show = False )
```

## Parameters

- `adata`: ( AnnData ) – Annotated data matrix containing the expression values.
- `var_names`: – Features to plot. Accepts a list of genes, a single gene name, or a mapping of group label to gene list.
- `groupby`: ( str ) – Key in adata.obs used to aggregate cells into groups.
- `figsize`: ( tuple (default: (6, 10) )) – Figure size (width, height) in inches.
- `layer`: ( Optional [ str ] (default: None )) – Expression source selection passed through to obs_df .
- `use_raw`: ( bool (default: False )) – Expression source selection passed through to obs_df .
- `gene_symbols`: ( Optional [ str ] (default: None )) – Expression source selection passed through to obs_df .
- `standard_scale`: ( Optional [ str ] (default: None )) – Optional scaling mode. Supported values are 'obs' , 'var' , or None .
- `cmap`: ( str (default: 'RdBu_r' )) – Colormap used for the heatmap body.
- `row_cluster`: ( bool (default: False )) – Whether to add hierarchical dendrograms for rows or columns.
- `col_cluster`: ( bool (default: False )) – Whether to add hierarchical dendrograms for rows or columns.
- `row_split`: (default: None ) – Optional explicit ordering of row or column groups.
- `col_split`: (default: None ) – Optional explicit ordering of row or column groups.
- `left_color_bars`: ( Optional [ dict ] (default: None )) – Optional annotation palettes or labels for row-side annotations.
- `left_color_labels`: ( Optional [ dict ] (default: None )) – Optional annotation palettes or labels for row-side annotations.
- `right_color_bars`: ( Optional [ dict ] (default: None )) – Optional annotation palettes or labels for row-side annotations.
- `right_color_labels`: ( Optional [ dict ] (default: None )) – Optional annotation palettes or labels for row-side annotations.
- `col_color_bars`: ( Optional [ dict ] (default: None )) – Optional palette for grouped column annotations.
- `legend`: ( bool (default: True )) – Legend visibility and layout strategy.
- `legend_style`: ( str (default: 'tight' )) – Legend visibility and layout strategy.
- `border`: ( bool (default: False )) – Whether to draw a visible border around heatmap axes after rendering.
- `label`: ( str (default: 'Mean expression' )) – Label used for the heatmap value legend.
- `show_values`: ( bool (default: False )) – Whether to print heatmap values inside cells.
- `value_fmt`: ( str (default: '.2f' )) – Format string for printed values (e.g. '.2f' ).
- `value_cutoff`: ( float (default: 0.0 )) – Only display text labels for values greater than or equal to this threshold.
- `save`: ( bool | str (default: False )) – Output controls. save may be True / False or a concrete path.
- `save_pathway`: ( str (default: '' )) – Output controls. save may be True / False or a concrete path.
- `show`: ( bool (default: False )) – Output controls. save may be True / False or a concrete path.

## Full Documentation

# omicverse.pl.group_heatmap #

omicverse.pl. group_heatmap ( adata , var_names , groupby , * , figsize = (6, 10) , layer = None , use_raw = False , gene_symbols = None , standard_scale = None , cmap = 'RdBu_r' , row_cluster = False , col_cluster = False , row_split = None , col_split = None , left_color_bars = None , left_color_labels = None , right_color_bars = None , right_color_labels = None , col_color_bars = None , legend = True , legend_style = 'tight' , border = False , label = 'Mean expression' , show_values = False , value_fmt = '.2f' , value_cutoff = 0.0 , save = False , save_pathway = '' , show = False ) [source] #

Plot grouped mean expression as a Marsilea heatmap.

Parameters :

-
adata ( `AnnData `) – Annotated data matrix containing the expression values.

-
var_names – Features to plot. Accepts a list of genes, a single gene name, or a mapping of group label to gene list.

-
groupby ( `str `) – Key in `adata.obs `used to aggregate cells into groups.

-
figsize ( `tuple `(default: `(6, 10) `)) – Figure size `(width, height) `in inches.

-
layer ( `Optional `[ `str `] (default: `None `)) – Expression source selection passed through to `obs_df `.

-
use_raw ( `bool `(default: `False `)) – Expression source selection passed through to `obs_df `.

-
gene_symbols ( `Optional `[ `str `] (default: `None `)) – Expression source selection passed through to `obs_df `.

-
standard_scale ( `Optional `[ `str `] (default: `None `)) – Optional scaling mode. Supported values are `'obs' `, `'var' `, or `None `.

-
cmap ( `str `(default: `'RdBu_r' `)) – Colormap used for the heatmap body.

-
row_cluster ( `bool `(default: `False `)) – Whether to add hierarchical dendrograms for rows or columns.

-
col_cluster ( `bool `(default: `False `)) – Whether to add hierarchical dendrograms for rows or columns.

-
row_split (default: `None `) – Optional explicit ordering of row or column groups.

-
col_split (default: `None `) – Optional explicit ordering of row or column groups.

-
left_color_bars ( `Optional `[ `dict `] (default: `None `)) – Optional annotation palettes or labels for row-side annotations.

-
left_color_labels ( `Optional `[ `dict `] (default: `None `)) – Optional annotation palettes or labels for row-side annotations.

-
right_color_bars ( `Optional `[ `dict `] (default: `None `)) – Optional annotation palettes or labels for row-side annotations.

-
right_color_labels ( `Optional `[ `dict `] (default: `None `)) – Optional annotation palettes or labels for row-side annotations.

-
col_color_bars ( `Optional `[ `dict `] (default: `None `)) – Optional palette for grouped column annotations.

-
legend ( `bool `(default: `True `)) – Legend visibility and layout strategy.

-
legend_style ( `str `(default: `'tight' `)) – Legend visibility and layout strategy.

-
border ( `bool `(default: `False `)) – Whether to draw a visible border around heatmap axes after rendering.

-
label ( `str `(default: `'Mean expression' `)) – Label used for the heatmap value legend.

-
show_values ( `bool `(default: `False `)) – Whether to print heatmap values inside cells.

-
value_fmt ( `str `(default: `'.2f' `)) – Format string for printed values (e.g. `'.2f' `).

-
value_cutoff ( `float `(default: `0.0 `)) – Only display text labels for values greater than or equal to this threshold.

-
save ( `bool `| `str `(default: `False `)) – Output controls. `save `may be `True `/ `False `or a concrete path.

-
save_pathway ( `str `(default: `'' `)) – Output controls. `save `may be `True `/ `False `or a concrete path.

-
show ( `bool `(default: `False `)) – Output controls. `save `may be `True `/ `False `or a concrete path.

Returns :

Returns the Marsilea plotter by default, or the rendered figure when rendering is triggered for saving/showing/tight legends.

Return type :

marsilea.Heatmap or matplotlib.figure.Figure
