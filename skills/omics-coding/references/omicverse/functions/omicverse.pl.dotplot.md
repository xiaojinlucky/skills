# omicverse.pl.dotplot #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.dotplot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.dotplot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Make a dot plot of the expression values of var_names .

## Signature

```text
omicverse.pl. dotplot ( adata , var_names , groupby , * , use_raw = None , log = False , num_categories = 7 , categories_order = None , expression_cutoff = 0.0 , mean_only_expressed = False , standard_scale = None , title = None , colorbar_title = 'Mean expression\\nin group' , size_title = 'Fraction of cells\\nin group (%)' , figsize = None , dendrogram = False , gene_symbols = None , var_group_positions = None , var_group_labels = None , var_group_rotation = None , layer = None , swap_axes = False , dot_color_df = None , show = None , save = None , ax = None , figure = None , rect = None , legend = True , legend_side = 'right' , legend_pad = 0.0 , return_fig = False , vmin = None , vmax = None , vcenter = None , norm = None , cmap = 'Reds' , dot_max = None , dot_min = None , smallest_dot = 0.0 , fontsize = 12 , preserve_dict_order = False , ** kwds )
```

## Parameters

- `adata`: ( AnnData ) – AnnData Annotated data matrix.
- `var_names`: ( Union[_VarNames, Mapping[str, _VarNames]] ) – str or list of str or dict Variables to plot.
- `groupby`: ( Union[str, Sequence[str]] ) – str or list of str The key of the observation grouping to consider.
- `use_raw`: ( Optional[bool] (default: None )) – bool, optional (default=None) Use raw attribute of adata if present.
- `log`: ( bool (default: False )) – bool, optional (default=False) Whether to log-transform the data.
- `num_categories`: ( int (default: 7 )) – int, optional (default=7) Number of categories to show.
- `categories_order`: ( Optional[Sequence[str]] (default: None )) – list of str, optional (default=None) Order of categories to display.
- `expression_cutoff`: ( float (default: 0.0 )) – float, optional (default=0.0) Expression cutoff for calculating fraction of expressing cells.
- `mean_only_expressed`: ( bool (default: False )) – bool, optional (default=False) Whether to calculate mean only for expressing cells.
- `standard_scale`: ( Optional[Literal[‘var’, ‘group’]] (default: None )) – {‘var’, ‘group’} or None, optional (default=None) Whether to standardize data.
- `title`: ( Optional[str] (default: None )) – str, optional (default=None) Title for the plot.
- `colorbar_title`: ( Optional[str] (default: 'Mean expression\\nin group' )) – str, optional (default=’Mean expressionnin group’) Title for the color bar.
- `size_title`: ( Optional[str] (default: 'Fraction of cells\\nin group (%)' )) – str, optional (default=’Fraction of cellsnin group (%)’) Title for the size legend.
- `figsize`: ( Optional[Tuple[float, float]] (default: None )) – tuple, optional (default=None) Figure size (width, height) in inches. If provided, the plot dimensions will be scaled accordingly.
- `dendrogram`: ( Union[bool, str] (default: False )) – bool or str, optional (default=False) Whether to add dendrogram to the plot.
- `gene_symbols`: ( Optional[str] (default: None )) – str, optional (default=None) Key for gene symbols in adata.var .
- `var_group_positions`: ( Optional[Sequence[Tuple[int, int]]] (default: None )) – list of tuples, optional (default=None) Positions for variable groups.
- `var_group_labels`: ( Optional[Sequence[str]] (default: None )) – list of str, optional (default=None) Labels for variable groups.
- `var_group_rotation`: ( Optional[float] (default: None )) – float, optional (default=None) Rotation angle for variable group labels.
- `layer`: ( Optional[str] (default: None )) – str, optional (default=None) Layer to use for expression data.
- `swap_axes`: ( Optional[bool] (default: False )) – bool, optional (default=False) Whether to swap x and y axes.
- `dot_color_df`: ( Optional[pd.DataFrame] (default: None )) – pandas.DataFrame, optional (default=None) DataFrame for dot colors.
- `show`: ( Optional[bool] (default: None )) – bool, optional (default=None) Whether to show the plot.
- `save`: ( Optional[Union[str, bool]] (default: None )) – str or bool, optional (default=None) Whether to save the plot.
- `ax`: ( Optional[_AxesSubplot] (default: None )) – matplotlib.axes.Axes, optional (default=None) Axes object to plot on.
- `return_fig`: ( Optional[bool] (default: False )) – bool, optional (default=False) Whether to return the figure object.
- `vmin`: ( Optional[float] (default: None )) – float, optional (default=None) Minimum value for color scaling.
- `vmax`: ( Optional[float] (default: None )) – float, optional (default=None) Maximum value for color scaling.
- `vcenter`: ( Optional[float] (default: None )) – float, optional (default=None) Center value for diverging colormap.
- `norm`: ( Optional[Normalize] (default: None )) – matplotlib.colors.Normalize, optional (default=None) Normalization object for colors.
- `cmap`: ( Union[Colormap, str, None] (default: 'Reds' )) – str or matplotlib.colors.Colormap, optional (default=’Reds’) Colormap for the plot.
- `dot_max`: ( Optional[float] (default: None )) – float, optional (default=None) Maximum dot size.
- `dot_min`: ( Optional[float] (default: None )) – float, optional (default=None) Minimum dot size.
- `smallest_dot`: ( float (default: 0.0 )) – float, optional (default=0.0) Size of the smallest dot.
- `fontsize`: ( int (default: 12 )) – int, optional (default=12) Font size for labels and legends. Titles will be one point larger.
- `preserve_dict_order`: ( bool (default: False )) – bool, optional (default=False) When var_names is a dictionary, whether to preserve the original dictionary order. If True, genes will be ordered according to the dictionary’s insertion order. If False (default), genes will be ordered according to cell type categories.
- `legend`: ( bool (default: True ))
- `legend_side`: ( str (default: 'right' ))
- `legend_pad`: ( float (default: 0.0 ))
- `figure`: Detected from function signature; no parameter description detected.
- `rect`: Detected from function signature; no parameter description detected.
- `**kwds`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.pl.dotplot #

omicverse.pl. dotplot ( adata , var_names , groupby , * , use_raw = None , log = False , num_categories = 7 , categories_order = None , expression_cutoff = 0.0 , mean_only_expressed = False , standard_scale = None , title = None , colorbar_title = 'Mean expression\\nin group' , size_title = 'Fraction of cells\\nin group (%)' , figsize = None , dendrogram = False , gene_symbols = None , var_group_positions = None , var_group_labels = None , var_group_rotation = None , layer = None , swap_axes = False , dot_color_df = None , show = None , save = None , ax = None , figure = None , rect = None , legend = True , legend_side = 'right' , legend_pad = 0.0 , return_fig = False , vmin = None , vmax = None , vcenter = None , norm = None , cmap = 'Reds' , dot_max = None , dot_min = None , smallest_dot = 0.0 , fontsize = 12 , preserve_dict_order = False , ** kwds ) [source] #

Make a dot plot of the expression values of var_names .

For each var_name and each groupby category a dot is plotted. Each dot represents two values: mean expression within each category (visualized by color) and fraction of cells expressing the var_name in the category (visualized by the size of the dot).

Parameters :

-
adata ( AnnData ) – AnnData Annotated data matrix.

-
var_names ( Union[_VarNames, Mapping[str, _VarNames]] ) – str or list of str or dict Variables to plot.

-
groupby ( Union[str, Sequence[str]] ) – str or list of str The key of the observation grouping to consider.

-
use_raw ( Optional[bool] (default: `None `)) – bool, optional (default=None) Use raw attribute of adata if present.

-
log ( bool (default: `False `)) – bool, optional (default=False) Whether to log-transform the data.

-
num_categories ( int (default: `7 `)) – int, optional (default=7) Number of categories to show.

-
categories_order ( Optional[Sequence[str]] (default: `None `)) – list of str, optional (default=None) Order of categories to display.

-
expression_cutoff ( float (default: `0.0 `)) – float, optional (default=0.0) Expression cutoff for calculating fraction of expressing cells.

-
mean_only_expressed ( bool (default: `False `)) – bool, optional (default=False) Whether to calculate mean only for expressing cells.

-
standard_scale ( Optional[Literal[‘var’, ‘group’]] (default: `None `)) – {‘var’, ‘group’} or None, optional (default=None) Whether to standardize data.

-
title ( Optional[str] (default: `None `)) – str, optional (default=None) Title for the plot.

-
colorbar_title ( Optional[str] (default: `'Mean expression\\nin group' `)) – str, optional (default=’Mean expressionnin group’) Title for the color bar.

-
size_title ( Optional[str] (default: `'Fraction of cells\\nin group (%)' `)) – str, optional (default=’Fraction of cellsnin group (%)’) Title for the size legend.

-
figsize ( Optional[Tuple[float, float]] (default: `None `)) – tuple, optional (default=None) Figure size (width, height) in inches. If provided, the plot dimensions will be scaled accordingly.

-
dendrogram ( Union[bool, str] (default: `False `)) – bool or str, optional (default=False) Whether to add dendrogram to the plot.

-
gene_symbols ( Optional[str] (default: `None `)) – str, optional (default=None) Key for gene symbols in adata.var .

-
var_group_positions ( Optional[Sequence[Tuple[int, int]]] (default: `None `)) – list of tuples, optional (default=None) Positions for variable groups.

-
var_group_labels ( Optional[Sequence[str]] (default: `None `)) – list of str, optional (default=None) Labels for variable groups.

-
var_group_rotation ( Optional[float] (default: `None `)) – float, optional (default=None) Rotation angle for variable group labels.

-
layer ( Optional[str] (default: `None `)) – str, optional (default=None) Layer to use for expression data.

-
swap_axes ( Optional[bool] (default: `False `)) – bool, optional (default=False) Whether to swap x and y axes.

-
dot_color_df ( Optional[pd.DataFrame] (default: `None `)) – pandas.DataFrame, optional (default=None) DataFrame for dot colors.

-
show ( Optional[bool] (default: `None `)) – bool, optional (default=None) Whether to show the plot.

-
save ( Optional[Union[str, bool]] (default: `None `)) – str or bool, optional (default=None) Whether to save the plot.

-
ax ( Optional[_AxesSubplot] (default: `None `)) – matplotlib.axes.Axes, optional (default=None) Axes object to plot on.

-
return_fig ( Optional[bool] (default: `False `)) – bool, optional (default=False) Whether to return the figure object.

-
vmin ( Optional[float] (default: `None `)) – float, optional (default=None) Minimum value for color scaling.

-
vmax ( Optional[float] (default: `None `)) – float, optional (default=None) Maximum value for color scaling.

-
vcenter ( Optional[float] (default: `None `)) – float, optional (default=None) Center value for diverging colormap.

-
norm ( Optional[Normalize] (default: `None `)) – matplotlib.colors.Normalize, optional (default=None) Normalization object for colors.

-
cmap ( Union[Colormap, str, None] (default: `'Reds' `)) – str or matplotlib.colors.Colormap, optional (default=’Reds’) Colormap for the plot.

-
dot_max ( Optional[float] (default: `None `)) – float, optional (default=None) Maximum dot size.

-
dot_min ( Optional[float] (default: `None `)) – float, optional (default=None) Minimum dot size.

-
smallest_dot ( float (default: `0.0 `)) – float, optional (default=0.0) Size of the smallest dot.

-
fontsize ( int (default: `12 `)) – int, optional (default=12) Font size for labels and legends. Titles will be one point larger.

-
preserve_dict_order ( bool (default: `False `)) – bool, optional (default=False) When var_names is a dictionary, whether to preserve the original dictionary order. If True, genes will be ordered according to the dictionary’s insertion order. If False (default), genes will be ordered according to cell type categories.

-
legend ( bool (default: `True `))

-
legend_side ( str (default: `'right' `))

-
legend_pad ( float (default: `0.0 `))

Returns :

If return_fig is True, returns the figure object. If show is False, returns the rendered Marsilea board.
