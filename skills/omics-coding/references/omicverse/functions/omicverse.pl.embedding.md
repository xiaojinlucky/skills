# omicverse.pl.embedding #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.embedding`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.embedding.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Scatter plot for user specified embedding basis (e.g. umap, pca, etc).

## Signature

```text
omicverse.pl. embedding ( adata , basis , * , color = None , gene_symbols = None , use_raw = None , sort_order = True , edges = False , edges_width = 0.1 , edges_color = 'grey' , neighbors_key = None , arrows = False , arrows_kwds = None , groups = None , components = None , dimensions = None , layer = None , projection = '2d' , scale_factor = None , color_map = None , cmap = None , palette = None , na_color = 'lightgray' , na_in_legend = True , size = None , frameon = 'small' , legend_fontsize = None , legend_fontweight = 'bold' , legend_loc = 'right margin' , legend_fontoutline = None , colorbar_loc = 'right' , vmax = None , vmin = None , vcenter = None , norm = None , add_outline = False , outline_width = (0.3, 0.05) , outline_color = ('black', 'white') , ncols = 4 , hspace = 0.25 , wspace = None , title = None , show = None , save = None , ax = None , return_fig = None , marker = '.' , ** kwargs )
```

## Parameters

- `adata`: ( AnnData ) – Annotated data matrix.
- `basis`: ( str ) – Name of the obsm basis to use.
- `color`: ( Union [ str , Sequence [ str ], None ] (default: None )) – Keys for annotations of observations/cells or variables/genes. (None)
- `gene_symbols`: ( Optional [ str ] (default: None )) – Key for field in .var that stores gene symbols. (None)
- `use_raw`: ( Optional [ bool ] (default: None )) – Use .raw attribute of adata if present. (None)
- `sort_order`: ( bool (default: True )) – For continuous annotations used as color parameter, plot data points with higher values on top of others. (True)
- `edges`: ( bool (default: False )) – Show edges between cells. (False)
- `edges_width`: ( float (default: 0.1 )) – Width of edges. (0.1)
- `edges_color`: ( Union [ str , Sequence [ float ], Sequence [ str ]] (default: 'grey' )) – Color of edges. (‘grey’)
- `neighbors_key`: ( Optional [ str ] (default: None )) – Key to use for neighbors. (None)
- `arrows`: ( bool (default: False )) – Show arrows for velocity. (False)
- `arrows_kwds`: ( Optional [ Mapping [ str , Any ]] (default: None )) – Keyword arguments for arrow plots. (None)
- `groups`: ( Optional [ str ] (default: None )) – Groups to highlight. (None)
- `components`: ( Union [ str , Sequence [ str ], None ] (default: None )) – Components to plot. (None)
- `dimensions`: ( Union [ Tuple [ int , int ], Sequence [ Tuple [ int , int ]], None ] (default: None )) – Dimensions to plot. (None)
- `layer`: ( Optional [ str ] (default: None )) – Name of the layer to use for coloring. (None)
- `projection`: ( Literal [ '2d' , '3d' ] (default: '2d' )) – Type of projection (‘2d’ or ‘3d’). (‘2d’)
- `scale_factor`: ( Optional [ float ] (default: None )) – Scaling factor for sizes. (None)
- `color_map`: ( Union [ Colormap , str , None ] (default: None )) – Colormap to use for continuous variables. (None)
- `cmap`: ( Union [ Colormap , str , None ] (default: None )) – Colormap to use for continuous variables. (None)
- `palette`: ( Union [ str , Sequence [ str ], Cycler , None ] (default: None )) – Colors to use for categorical variables. (None)
- `na_color`: ( Any (default: 'lightgray' )) – Color to use for NaN values. (‘lightgray’)
- `na_in_legend`: ( bool (default: True )) – Include NaN values in legend. (True)
- `size`: ( Union [ float , Sequence [ float ], None ] (default: None )) – Size of the dots. (None)
- `frameon`: ( Optional [ bool ] (default: 'small' )) – Draw a frame around the plot. (‘small’)
- `legend_fontsize`: ( Union [ int , float , Literal [ 'xx-small' , 'x-small' , 'small' , 'medium' , 'large' , 'x-large' , 'xx-large' ], None ] (default: None )) – Font size for legend. (None)
- `legend_fontweight`: ( Union [ int , Literal [ 'light' , 'normal' , 'medium' , 'semibold' , 'bold' , 'heavy' , 'black' ]] (default: 'bold' )) – Font weight for legend. (‘bold’)
- `legend_loc`: ( str (default: 'right margin' )) – Location of legend. (‘right margin’)
- `legend_fontoutline`: ( Optional [ int ] (default: None )) – Outline width for legend text. (None)
- `colorbar_loc`: ( Optional [ str ] (default: 'right' )) – Location of colorbar. (‘right’)
- `vmax`: ( Union [ Any , Sequence [ Any ], None ] (default: None )) – Maximum value for colorbar. (None)
- `vmin`: ( Union [ Any , Sequence [ Any ], None ] (default: None )) – Minimum value for colorbar. (None)
- `vcenter`: ( Union [ Any , Sequence [ Any ], None ] (default: None )) – Center value for colorbar. (None)
- `norm`: ( Union [ Normalize , Sequence [ Normalize ], None ] (default: None )) – Normalization for colorbar. (None)
- `add_outline`: ( Optional [ bool ] (default: False )) – Add outline to points. (False)
- `outline_width`: ( Tuple [ float , float ] (default: (0.3, 0.05) )) – Width of outline. ((0.3, 0.05))
- `outline_color`: ( Tuple [ str , str ] (default: ('black', 'white') )) – Color of outline. ((‘black’, ‘white’))
- `ncols`: ( int (default: 4 )) – Number of columns for subplots. (4)
- `hspace`: ( float (default: 0.25 )) – Height spacing between subplots. (0.25)
- `wspace`: ( Optional [ float ] (default: None )) – Width spacing between subplots. (None)
- `title`: ( Union [ str , Sequence [ str ], None ] (default: None )) – Title for the plot. (None)
- `show`: ( Optional [ bool ] (default: None )) – Show the plot. (None)
- `save`: ( Union [ str , bool , None ] (default: None )) – Save the plot. (None)
- `ax`: ( Optional [ Axes ] (default: None )) – Matplotlib axes object. (None)
- `return_fig`: ( Optional [ bool ] (default: None )) – Return figure object. (None)
- `marker`: ( Union [ str , Sequence [ str ]] (default: '.' )) – Marker style. (‘.’)
- `**kwargs`: – Additional keyword arguments.

## Full Documentation

# omicverse.pl.embedding #

omicverse.pl. embedding ( adata , basis , * , color = None , gene_symbols = None , use_raw = None , sort_order = True , edges = False , edges_width = 0.1 , edges_color = 'grey' , neighbors_key = None , arrows = False , arrows_kwds = None , groups = None , components = None , dimensions = None , layer = None , projection = '2d' , scale_factor = None , color_map = None , cmap = None , palette = None , na_color = 'lightgray' , na_in_legend = True , size = None , frameon = 'small' , legend_fontsize = None , legend_fontweight = 'bold' , legend_loc = 'right margin' , legend_fontoutline = None , colorbar_loc = 'right' , vmax = None , vmin = None , vcenter = None , norm = None , add_outline = False , outline_width = (0.3, 0.05) , outline_color = ('black', 'white') , ncols = 4 , hspace = 0.25 , wspace = None , title = None , show = None , save = None , ax = None , return_fig = None , marker = '.' , ** kwargs ) [source] #

Scatter plot for user specified embedding basis (e.g. umap, pca, etc).

Parameters :

-
adata ( `AnnData `) – Annotated data matrix.

-
basis ( `str `) – Name of the obsm basis to use.

-
color ( `Union `[ `str `, `Sequence `[ `str `], `None `] (default: `None `)) – Keys for annotations of observations/cells or variables/genes. (None)

-
gene_symbols ( `Optional `[ `str `] (default: `None `)) – Key for field in .var that stores gene symbols. (None)

-
use_raw ( `Optional `[ `bool `] (default: `None `)) – Use .raw attribute of adata if present. (None)

-
sort_order ( `bool `(default: `True `)) – For continuous annotations used as color parameter, plot data points with higher values on top of others. (True)

-
edges ( `bool `(default: `False `)) – Show edges between cells. (False)

-
edges_width ( `float `(default: `0.1 `)) – Width of edges. (0.1)

-
edges_color ( `Union `[ `str `, `Sequence `[ `float `], `Sequence `[ `str `]] (default: `'grey' `)) – Color of edges. (‘grey’)

-
neighbors_key ( `Optional `[ `str `] (default: `None `)) – Key to use for neighbors. (None)

-
arrows ( `bool `(default: `False `)) – Show arrows for velocity. (False)

-
arrows_kwds ( `Optional `[ `Mapping `[ `str `, `Any `]] (default: `None `)) – Keyword arguments for arrow plots. (None)

-
groups ( `Optional `[ `str `] (default: `None `)) – Groups to highlight. (None)

-
components ( `Union `[ `str `, `Sequence `[ `str `], `None `] (default: `None `)) – Components to plot. (None)

-
dimensions ( `Union `[ `Tuple `[ `int `, `int `], `Sequence `[ `Tuple `[ `int `, `int `]], `None `] (default: `None `)) – Dimensions to plot. (None)

-
layer ( `Optional `[ `str `] (default: `None `)) – Name of the layer to use for coloring. (None)

-
projection ( `Literal `[ `'2d' `, `'3d' `] (default: `'2d' `)) – Type of projection (‘2d’ or ‘3d’). (‘2d’)

-
scale_factor ( `Optional `[ `float `] (default: `None `)) – Scaling factor for sizes. (None)

-
color_map ( `Union `[ `Colormap `, `str `, `None `] (default: `None `)) – Colormap to use for continuous variables. (None)

-
cmap ( `Union `[ `Colormap `, `str `, `None `] (default: `None `)) – Colormap to use for continuous variables. (None)

-
palette ( `Union `[ `str `, `Sequence `[ `str `], `Cycler `, `None `] (default: `None `)) – Colors to use for categorical variables. (None)

-
na_color ( `Any `(default: `'lightgray' `)) – Color to use for NaN values. (‘lightgray’)

-
na_in_legend ( `bool `(default: `True `)) – Include NaN values in legend. (True)

-
size ( `Union `[ `float `, `Sequence `[ `float `], `None `] (default: `None `)) – Size of the dots. (None)

-
frameon ( `Optional `[ `bool `] (default: `'small' `)) – Draw a frame around the plot. (‘small’)

-
legend_fontsize ( `Union `[ `int `, `float `, `Literal `[ `'xx-small' `, `'x-small' `, `'small' `, `'medium' `, `'large' `, `'x-large' `, `'xx-large' `], `None `] (default: `None `)) – Font size for legend. (None)

-
legend_fontweight ( `Union `[ `int `, `Literal `[ `'light' `, `'normal' `, `'medium' `, `'semibold' `, `'bold' `, `'heavy' `, `'black' `]] (default: `'bold' `)) – Font weight for legend. (‘bold’)

-
legend_loc ( `str `(default: `'right margin' `)) – Location of legend. (‘right margin’)

-
legend_fontoutline ( `Optional `[ `int `] (default: `None `)) – Outline width for legend text. (None)

-
colorbar_loc ( `Optional `[ `str `] (default: `'right' `)) – Location of colorbar. (‘right’)

-
vmax ( `Union `[ `Any `, `Sequence `[ `Any `], `None `] (default: `None `)) – Maximum value for colorbar. (None)

-
vmin ( `Union `[ `Any `, `Sequence `[ `Any `], `None `] (default: `None `)) – Minimum value for colorbar. (None)

-
vcenter ( `Union `[ `Any `, `Sequence `[ `Any `], `None `] (default: `None `)) – Center value for colorbar. (None)

-
norm ( `Union `[ `Normalize `, `Sequence `[ `Normalize `], `None `] (default: `None `)) – Normalization for colorbar. (None)

-
add_outline ( `Optional `[ `bool `] (default: `False `)) – Add outline to points. (False)

-
outline_width ( `Tuple `[ `float `, `float `] (default: `(0.3, 0.05) `)) – Width of outline. ((0.3, 0.05))

-
outline_color ( `Tuple `[ `str `, `str `] (default: `('black', 'white') `)) – Color of outline. ((‘black’, ‘white’))

-
ncols ( `int `(default: `4 `)) – Number of columns for subplots. (4)

-
hspace ( `float `(default: `0.25 `)) – Height spacing between subplots. (0.25)

-
wspace ( `Optional `[ `float `] (default: `None `)) – Width spacing between subplots. (None)

-
title ( `Union `[ `str `, `Sequence `[ `str `], `None `] (default: `None `)) – Title for the plot. (None)

-
show ( `Optional `[ `bool `] (default: `None `)) – Show the plot. (None)

-
save ( `Union `[ `str `, `bool `, `None `] (default: `None `)) – Save the plot. (None)

-
ax ( `Optional `[ `Axes `] (default: `None `)) – Matplotlib axes object. (None)

-
return_fig ( `Optional `[ `bool `] (default: `None `)) – Return figure object. (None)

-
marker ( `Union `[ `str `, `Sequence `[ `str `]] (default: `'.' `)) – Marker style. (‘.’)

-
**kwargs – Additional keyword arguments.

Returns :

If show==False a `Axes `or a list of it.

Return type :

ax
