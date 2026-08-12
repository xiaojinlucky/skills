# omicverse.pl.umap #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.umap`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.umap.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot UMAP embedding.

## Signature

```text
omicverse.pl. umap ( adata , convert = True , ** kwargs )
```

## Parameters

- `adata`: ( AnnData ) – Annotated data matrix.
- `color`: – Keys for annotations of observations/cells or variables/genes. (None)
- `gene_symbols`: – Key for field in .var that stores gene symbols. (None)
- `use_raw`: – Use .raw attribute of adata if present. (None)
- `sort_order`: – For continuous annotations used as color parameter, plot data points with higher values on top of others. (True)
- `edges`: – Show edges between cells. (False)
- `edges_width`: – Width of edges. (0.1)
- `edges_color`: – Color of edges. (‘grey’)
- `neighbors_key`: – Key to use for neighbors. (None)
- `arrows`: – Show arrows for velocity. (False)
- `arrows_kwds`: – Keyword arguments for arrow plots. (None)
- `groups`: – Groups to highlight. (None)
- `components`: – Components to plot. (None)
- `dimensions`: – Dimensions to plot. (None)
- `layer`: – Name of the layer to use for coloring. (None)
- `projection`: – Type of projection (‘2d’ or ‘3d’). (‘2d’)
- `scale_factor`: – Scaling factor for sizes. (None)
- `color_map`: – Colormap to use for continuous variables. (None)
- `cmap`: – Colormap to use for continuous variables. (None)
- `palette`: – Colors to use for categorical variables. (None)
- `na_color`: – Color to use for NaN values. (‘lightgray’)
- `na_in_legend`: – Include NaN values in legend. (True)
- `size`: – Size of the dots. (None)
- `frameon`: – Draw a frame around the plot. (‘small’)
- `legend_fontsize`: – Font size for legend. (None)
- `legend_fontweight`: – Font weight for legend. (‘bold’)
- `legend_loc`: – Location of legend. (‘right margin’)
- `legend_fontoutline`: – Outline width for legend text. (None)
- `colorbar_loc`: – Location of colorbar. (‘right’)
- `vmax`: – Maximum value for colorbar. (None)
- `vmin`: – Minimum value for colorbar. (None)
- `vcenter`: – Center value for colorbar. (None)
- `norm`: – Normalization for colorbar. (None)
- `add_outline`: – Add outline to points. (False)
- `outline_width`: – Width of outline. ((0.3, 0.05))
- `outline_color`: – Color of outline. ((‘black’, ‘white’))
- `ncols`: – Number of columns for subplots. (4)
- `hspace`: – Height spacing between subplots. (0.25)
- `wspace`: – Width spacing between subplots. (None)
- `title`: – Title for the plot. (None)
- `show`: – Show the plot. (None)
- `save`: – Save the plot. (None)
- `ax`: – Matplotlib axes object. (None)
- `return_fig`: – Return figure object. (None)
- `marker`: – Marker style. (‘.’)
- `**kwargs`: – Additional keyword arguments.
- `convert`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.pl.umap #

omicverse.pl. umap ( adata , convert = True , ** kwargs ) [source] #

Plot UMAP embedding.

Parameters :

-
adata ( `AnnData `) – Annotated data matrix.

-
color – Keys for annotations of observations/cells or variables/genes. (None)

-
gene_symbols – Key for field in .var that stores gene symbols. (None)

-
use_raw – Use .raw attribute of adata if present. (None)

-
sort_order – For continuous annotations used as color parameter, plot data points with higher values on top of others. (True)

-
edges – Show edges between cells. (False)

-
edges_width – Width of edges. (0.1)

-
edges_color – Color of edges. (‘grey’)

-
neighbors_key – Key to use for neighbors. (None)

-
arrows – Show arrows for velocity. (False)

-
arrows_kwds – Keyword arguments for arrow plots. (None)

-
groups – Groups to highlight. (None)

-
components – Components to plot. (None)

-
dimensions – Dimensions to plot. (None)

-
layer – Name of the layer to use for coloring. (None)

-
projection – Type of projection (‘2d’ or ‘3d’). (‘2d’)

-
scale_factor – Scaling factor for sizes. (None)

-
color_map – Colormap to use for continuous variables. (None)

-
cmap – Colormap to use for continuous variables. (None)

-
palette – Colors to use for categorical variables. (None)

-
na_color – Color to use for NaN values. (‘lightgray’)

-
na_in_legend – Include NaN values in legend. (True)

-
size – Size of the dots. (None)

-
frameon – Draw a frame around the plot. (‘small’)

-
legend_fontsize – Font size for legend. (None)

-
legend_fontweight – Font weight for legend. (‘bold’)

-
legend_loc – Location of legend. (‘right margin’)

-
legend_fontoutline – Outline width for legend text. (None)

-
colorbar_loc – Location of colorbar. (‘right’)

-
vmax – Maximum value for colorbar. (None)

-
vmin – Minimum value for colorbar. (None)

-
vcenter – Center value for colorbar. (None)

-
norm – Normalization for colorbar. (None)

-
add_outline – Add outline to points. (False)

-
outline_width – Width of outline. ((0.3, 0.05))

-
outline_color – Color of outline. ((‘black’, ‘white’))

-
ncols – Number of columns for subplots. (4)

-
hspace – Height spacing between subplots. (0.25)

-
wspace – Width spacing between subplots. (None)

-
title – Title for the plot. (None)

-
show – Show the plot. (None)

-
save – Save the plot. (None)

-
ax – Matplotlib axes object. (None)

-
return_fig – Return figure object. (None)

-
marker – Marker style. (‘.’)

-
**kwargs – Additional keyword arguments.

Returns :

figure and axis ax: axis

Return type :

fig
