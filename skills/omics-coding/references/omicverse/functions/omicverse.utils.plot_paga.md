# omicverse.utils.plot_paga #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.plot_paga`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.plot_paga.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot PAGA graph and optional embedding-level annotations.

## Signature

```text
omicverse.utils. plot_paga ( adata , basis = None , vkey = 'velocity' , color = None , layer = None , title = None , threshold = None , layout = None , layout_kwds = None , init_pos = None , root = 0 , labels = None , single_component = False , dashed_edges = 'connectivities' , solid_edges = 'transitions_confidence' , transitions = 'transitions_confidence' , node_size_scale = 1 , node_size_power = 0.5 , edge_width_scale = 0.4 , min_edge_width = None , max_edge_width = 2 , arrowsize = 15 , random_state = 0 , pos = None , node_colors = None , normalize_to_color = False , cmap = None , cax = None , cb_kwds = None , add_pos = True , export_to_gexf = False , plot = True , use_raw = None , size = None , groups = None , components = None , figsize = None , dpi = None , show = None , save = None , ax = None , ncols = None , scatter_flag = None , ** kwargs )
```

## Parameters

- `adata`: ( AnnData ) – AnnData with PAGA graph stored in adata.uns['paga'] .
- `basis`: ( str or None , optional ) – Embedding basis used for overlay (for example 'umap' ). Set None to draw graph layout only.
- `vkey`: ( str , optional ) – Velocity key used by scVelo when velocity-aware plotting is enabled.
- `color`: ( str or sequence of str , optional ) – Cell-level annotation(s) used for coloring.
- `layer`: ( str or None , optional ) – Layer used for expression coloring.
- `title`: ( str or None , optional ) – Plot title.
- `threshold`: ( float or None , optional ) – Minimum edge threshold.
- `layout`: ( str or None , optional ) – Graph layout algorithm name.
- `layout_kwds`: ( dict or None , optional ) – Additional layout options.
- `init_pos`: ( str or None , optional ) – Initialization for graph layout.
- `root`: ( int or None , optional ) – Root index used by tree-like layouts.
- `labels`: ( str or None , optional ) – Node labels to display.
- `single_component`: ( bool , optional ) – Keep only the largest connected component.
- `dashed_edges`: ( str or None , optional ) – Key for dashed edges.
- `solid_edges`: ( str or None , optional ) – Key for solid edges.
- `transitions`: ( str or None , optional ) – Transition-confidence edge key.
- `node_size_scale`: ( float , optional ) – Scale factor for node sizes.
- `node_size_power`: ( float , optional ) – Exponent for node-size scaling.
- `edge_width_scale`: ( float , optional ) – Scale factor for edge widths.
- `min_edge_width`: ( float or None , optional ) – Lower bound for edge widths.
- `max_edge_width`: ( float , optional ) – Upper bound for edge widths.
- `arrowsize`: ( float , optional ) – Arrow size for directed edges.
- `random_state`: ( int , optional ) – Random seed used by layout routines.
- `pos`: ( dict or None , optional ) – Precomputed node positions.
- `node_colors`: ( dict or sequence , optional ) – Custom node colors.
- `normalize_to_color`: ( bool , optional ) – Whether to normalize values before color mapping.
- `cmap`: ( str or matplotlib colormap , optional ) – Colormap.
- `cax`: ( matplotlib.axes.Axes or None , optional ) – Colorbar axis.
- `cb_kwds`: ( dict or None , optional ) – Colorbar keyword arguments.
- `add_pos`: ( bool , optional ) – Whether to save computed positions back to adata.uns .
- `export_to_gexf`: ( bool , optional ) – Whether to export graph to GEXF.
- `plot`: ( bool , optional ) – If False , only compute/return graph data.
- `use_raw`: ( bool or None , optional ) – Whether to use adata.raw .
- `size`: ( float or None , optional ) – Point size for scatter overlay.
- `groups`: ( str or sequence or None , optional ) – Category subset.
- `components`: ( str or sequence or None , optional ) – Embedding components to plot.
- `figsize`: ( tuple or None , optional ) – Figure size.
- `dpi`: ( int or None , optional ) – Figure dpi.
- `show`: ( bool or None , optional ) – Whether to immediately show the figure.
- `save`: ( str or bool or None , optional ) – Save path or Scanpy-style save flag.
- `ax`: ( matplotlib.axes.Axes or None , optional ) – Existing axis.
- `ncols`: ( int or None , optional ) – Number of columns when plotting multiple panels.
- `scatter_flag`: ( bool or None , optional ) – Whether to add embedding scatter underlay.
- `**kwargs`: – Additional arguments forwarded to scvelo.pl.paga .

## Full Documentation

# omicverse.utils.plot_paga #

omicverse.utils. plot_paga ( adata , basis = None , vkey = 'velocity' , color = None , layer = None , title = None , threshold = None , layout = None , layout_kwds = None , init_pos = None , root = 0 , labels = None , single_component = False , dashed_edges = 'connectivities' , solid_edges = 'transitions_confidence' , transitions = 'transitions_confidence' , node_size_scale = 1 , node_size_power = 0.5 , edge_width_scale = 0.4 , min_edge_width = None , max_edge_width = 2 , arrowsize = 15 , random_state = 0 , pos = None , node_colors = None , normalize_to_color = False , cmap = None , cax = None , cb_kwds = None , add_pos = True , export_to_gexf = False , plot = True , use_raw = None , size = None , groups = None , components = None , figsize = None , dpi = None , show = None , save = None , ax = None , ncols = None , scatter_flag = None , ** kwargs ) [source] #

Plot PAGA graph and optional embedding-level annotations.

Parameters :

-
adata ( AnnData ) – AnnData with PAGA graph stored in `adata.uns['paga'] `.

-
basis ( str or None , optional ) – Embedding basis used for overlay (for example `'umap' `). Set `None `to draw graph layout only.

-
vkey ( str , optional ) – Velocity key used by scVelo when velocity-aware plotting is enabled.

-
color ( str or sequence of str , optional ) – Cell-level annotation(s) used for coloring.

-
layer ( str or None , optional ) – Layer used for expression coloring.

-
title ( str or None , optional ) – Plot title.

-
threshold ( float or None , optional ) – Minimum edge threshold.

-
layout ( str or None , optional ) – Graph layout algorithm name.

-
layout_kwds ( dict or None , optional ) – Additional layout options.

-
init_pos ( str or None , optional ) – Initialization for graph layout.

-
root ( int or None , optional ) – Root index used by tree-like layouts.

-
labels ( str or None , optional ) – Node labels to display.

-
single_component ( bool , optional ) – Keep only the largest connected component.

-
dashed_edges ( str or None , optional ) – Key for dashed edges.

-
solid_edges ( str or None , optional ) – Key for solid edges.

-
transitions ( str or None , optional ) – Transition-confidence edge key.

-
node_size_scale ( float , optional ) – Scale factor for node sizes.

-
node_size_power ( float , optional ) – Exponent for node-size scaling.

-
edge_width_scale ( float , optional ) – Scale factor for edge widths.

-
min_edge_width ( float or None , optional ) – Lower bound for edge widths.

-
max_edge_width ( float , optional ) – Upper bound for edge widths.

-
arrowsize ( float , optional ) – Arrow size for directed edges.

-
random_state ( int , optional ) – Random seed used by layout routines.

-
pos ( dict or None , optional ) – Precomputed node positions.

-
node_colors ( dict or sequence , optional ) – Custom node colors.

-
normalize_to_color ( bool , optional ) – Whether to normalize values before color mapping.

-
cmap ( str or matplotlib colormap , optional ) – Colormap.

-
cax ( matplotlib.axes.Axes or None , optional ) – Colorbar axis.

-
cb_kwds ( dict or None , optional ) – Colorbar keyword arguments.

-
add_pos ( bool , optional ) – Whether to save computed positions back to `adata.uns `.

-
export_to_gexf ( bool , optional ) – Whether to export graph to GEXF.

-
plot ( bool , optional ) – If `False `, only compute/return graph data.

-
use_raw ( bool or None , optional ) – Whether to use `adata.raw `.

-
size ( float or None , optional ) – Point size for scatter overlay.

-
groups ( str or sequence or None , optional ) – Category subset.

-
components ( str or sequence or None , optional ) – Embedding components to plot.

-
figsize ( tuple or None , optional ) – Figure size.

-
dpi ( int or None , optional ) – Figure dpi.

-
show ( bool or None , optional ) – Whether to immediately show the figure.

-
save ( str or bool or None , optional ) – Save path or Scanpy-style save flag.

-
ax ( matplotlib.axes.Axes or None , optional ) – Existing axis.

-
ncols ( int or None , optional ) – Number of columns when plotting multiple panels.

-
scatter_flag ( bool or None , optional ) – Whether to add embedding scatter underlay.

-
**kwargs – Additional arguments forwarded to `scvelo.pl.paga `.

Returns :

Return value from `scvelo.pl.paga `.

Return type :

Any

Examples

```text
>>> ov.utils.plot_paga(adata, basis='umap', color='celltype', threshold=0.05)

```
