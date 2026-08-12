# omicverse.pl.feature_heatmap #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.feature_heatmap`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.feature_heatmap.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot cell-level feature expression ordered by groups or metadata.

## Signature

```text
omicverse.pl. feature_heatmap ( adata , var_names , * , groupby = None , cell_orderby = None , max_cells = 100 , figsize = (8, 4) , layer = None , use_raw = False , gene_symbols = None , standard_scale = 'var' , cmap = 'RdBu_r' , legend = True , legend_style = 'tight' , border = False , show_row_names = True , show_column_names = False , save = False , save_pathway = '' , show = False )
```

## Parameters

- `adata`: ( AnnData ) – Annotated data matrix containing the expression values.
- `var_names`: – Features to plot. Accepts a list of genes, a single gene name, or a mapping of group label to gene list.
- `groupby`: ( Optional [ str ] (default: None )) – Optional categorical key in adata.obs used to color and group columns by cell identity.
- `cell_orderby`: ( Optional [ str ] (default: None )) – Optional continuous or categorical key in adata.obs used to order cells before plotting.
- `max_cells`: ( int (default: 100 )) – Maximum number of cells retained per group when groupby is set.
- `figsize`: ( tuple (default: (8, 4) )) – Figure size (width, height) in inches.
- `layer`: ( Optional [ str ] (default: None )) – Expression source selection passed through to obs_df .
- `use_raw`: ( bool (default: False )) – Expression source selection passed through to obs_df .
- `gene_symbols`: ( Optional [ str ] (default: None )) – Expression source selection passed through to obs_df .
- `standard_scale`: ( str (default: 'var' )) – Optional scaling mode. Supported values are 'obs' , 'var' , 'group' , or None .
- `cmap`: ( str (default: 'RdBu_r' )) – Colormap used for the heatmap body.
- `legend`: ( bool (default: True )) – Legend visibility and layout strategy.
- `legend_style`: ( str (default: 'tight' )) – Legend visibility and layout strategy.
- `border`: ( bool (default: False )) – Whether to draw a visible border around heatmap axes after rendering.
- `show_row_names`: ( bool (default: True )) – Whether to display feature labels on rows or cell labels on columns.
- `show_column_names`: ( bool (default: False )) – Whether to display feature labels on rows or cell labels on columns.
- `save`: ( bool | str (default: False )) – Output controls. save may be True / False or a concrete path.
- `save_pathway`: ( str (default: '' )) – Output controls. save may be True / False or a concrete path.
- `show`: ( bool (default: False )) – Output controls. save may be True / False or a concrete path.

## Full Documentation

# omicverse.pl.feature_heatmap #

omicverse.pl. feature_heatmap ( adata , var_names , * , groupby = None , cell_orderby = None , max_cells = 100 , figsize = (8, 4) , layer = None , use_raw = False , gene_symbols = None , standard_scale = 'var' , cmap = 'RdBu_r' , legend = True , legend_style = 'tight' , border = False , show_row_names = True , show_column_names = False , save = False , save_pathway = '' , show = False ) [source] #

Plot cell-level feature expression ordered by groups or metadata.

Parameters :

-
adata ( `AnnData `) – Annotated data matrix containing the expression values.

-
var_names – Features to plot. Accepts a list of genes, a single gene name, or a mapping of group label to gene list.

-
groupby ( `Optional `[ `str `] (default: `None `)) – Optional categorical key in `adata.obs `used to color and group columns by cell identity.

-
cell_orderby ( `Optional `[ `str `] (default: `None `)) – Optional continuous or categorical key in `adata.obs `used to order cells before plotting.

-
max_cells ( `int `(default: `100 `)) – Maximum number of cells retained per group when `groupby `is set.

-
figsize ( `tuple `(default: `(8, 4) `)) – Figure size `(width, height) `in inches.

-
layer ( `Optional `[ `str `] (default: `None `)) – Expression source selection passed through to `obs_df `.

-
use_raw ( `bool `(default: `False `)) – Expression source selection passed through to `obs_df `.

-
gene_symbols ( `Optional `[ `str `] (default: `None `)) – Expression source selection passed through to `obs_df `.

-
standard_scale ( `str `(default: `'var' `)) – Optional scaling mode. Supported values are `'obs' `, `'var' `, `'group' `, or `None `.

-
cmap ( `str `(default: `'RdBu_r' `)) – Colormap used for the heatmap body.

-
legend ( `bool `(default: `True `)) – Legend visibility and layout strategy.

-
legend_style ( `str `(default: `'tight' `)) – Legend visibility and layout strategy.

-
border ( `bool `(default: `False `)) – Whether to draw a visible border around heatmap axes after rendering.

-
show_row_names ( `bool `(default: `True `)) – Whether to display feature labels on rows or cell labels on columns.

-
show_column_names ( `bool `(default: `False `)) – Whether to display feature labels on rows or cell labels on columns.

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
