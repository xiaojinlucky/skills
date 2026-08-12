# omicverse.pl.embedding_atlas #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.embedding_atlas`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.embedding_atlas.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Render large-scale embeddings with Datashader.

## Signature

```text
omicverse.pl. embedding_atlas ( adata , basis , color = None , * , gene_symbols = None , use_raw = None , layer = None , groups = None , title = None , figsize = (4, 4) , ax = None , cmap = 'RdBu_r' , palette = None , na_color = 'lightgray' , na_in_legend = True , legend_loc = 'right margin' , legend_fontsize = None , legend_fontweight = 'bold' , legend_fontoutline = None , frameon = 'small' , colorbar_loc = 'right' , vmax = None , vmin = None , vcenter = None , norm = None , plot_width = 800 , plot_height = 800 , spread_px = 0 , how = 'eq_hist' , show = None , save = None , return_fig = None , ncols = 4 , wspace = None , hspace = 0.25 , ** kwargs )
```

## Parameters

- `adata`: ( AnnData ) – Annotated data object containing embedding coordinates in obsm .
- `basis`: ( str ) – Embedding key in adata.obsm (for example 'X_umap' ).
- `color`: ( str or Sequence [ str ] or None , default=None ) – Feature(s) used for coloring. Accepts obs columns or gene names.
- `gene_symbols`: ( str or None , default=None ) – Column in adata.var used for resolving gene symbols.
- `use_raw`: ( bool or None , default=None ) – Whether to draw expression values from adata.raw .
- `layer`: ( str or None , default=None ) – Layer name for expression-based coloring.
- `groups`: ( str or None , default=None ) – Optional subset of categorical groups to display.
- `title`: ( str or Sequence [ str ] or None , default=None ) – Plot title(s).
- `figsize`: ( tuple [ float , float ] , default= ( 4 , 4 ) ) – Single-panel figure size.
- `ax`: ( matplotlib.axes.Axes or None , default=None ) – Existing axis for single-panel plotting.
- `cmap`: ( str or Colormap , default='RdBu_r' ) – Colormap for continuous variables.
- `palette`: ( str or sequence or Cycler or None , default=None ) – Palette for categorical variables.
- `na_color`: ( ColorLike , default='lightgray' ) – Color for missing values.
- `na_in_legend`: ( bool , default=True ) – Whether to include missing values in categorical legends.
- `legend_loc`: ( str , default='right margin' ) – Legend location mode.
- `legend_fontsize`: ( int or float or None , default=None ) – Legend font size.
- `legend_fontweight`: ( int or str , default='bold' ) – Legend font weight.
- `legend_fontoutline`: ( int or None , default=None ) – Outline width for legend text.
- `frameon`: ( bool or str or None , default='small' ) – Frame style.
- `colorbar_loc`: ( str or None , default='right' ) – Colorbar placement.
- `vmax`: ( Union [ Any , Sequence [ Any ], None ] (default: None )) – Color normalization controls for continuous features.
- `vmin`: ( Union [ Any , Sequence [ Any ], None ] (default: None )) – Color normalization controls for continuous features.
- `vcenter`: ( Union [ Any , Sequence [ Any ], None ] (default: None )) – Color normalization controls for continuous features.
- `norm`: ( Union [ Normalize , Sequence [ Normalize ], None ] (default: None )) – Color normalization controls for continuous features.
- `plot_width`: ( int , default=800 ) – Datashader canvas width in pixels.
- `plot_height`: ( int , default=800 ) – Datashader canvas height in pixels.
- `spread_px`: ( int , default=0 ) – Pixel spreading radius to improve sparse visibility.
- `how`: ( str , default='eq_hist' ) – Datashader shading strategy.
- `show`: ( bool or None , default=None ) – Whether to display the figure immediately.
- `save`: ( bool or str or None , default=None ) – Save option forwarded to Scanpy-style behavior.
- `return_fig`: ( bool or None , default=None ) – Whether to return the figure object for multi-panel output.
- `ncols`: ( int , default=4 ) – Number of columns in multi-panel mode.
- `wspace`: ( float or None , default=None ) – Horizontal spacing between panels.
- `hspace`: ( float , default=0.25 ) – Vertical spacing between panels.
- `**kwargs`: – Additional arguments passed to lower-level plotting helpers.

## Full Documentation

# omicverse.pl.embedding_atlas #

omicverse.pl. embedding_atlas ( adata , basis , color = None , * , gene_symbols = None , use_raw = None , layer = None , groups = None , title = None , figsize = (4, 4) , ax = None , cmap = 'RdBu_r' , palette = None , na_color = 'lightgray' , na_in_legend = True , legend_loc = 'right margin' , legend_fontsize = None , legend_fontweight = 'bold' , legend_fontoutline = None , frameon = 'small' , colorbar_loc = 'right' , vmax = None , vmin = None , vcenter = None , norm = None , plot_width = 800 , plot_height = 800 , spread_px = 0 , how = 'eq_hist' , show = None , save = None , return_fig = None , ncols = 4 , wspace = None , hspace = 0.25 , ** kwargs ) [source] #

Render large-scale embeddings with Datashader.

Parameters :

-
adata ( AnnData ) – Annotated data object containing embedding coordinates in `obsm `.

-
basis ( str ) – Embedding key in `adata.obsm `(for example `'X_umap' `).

-
color ( str or Sequence [ str ] or None , default=None ) – Feature(s) used for coloring. Accepts obs columns or gene names.

-
gene_symbols ( str or None , default=None ) – Column in `adata.var `used for resolving gene symbols.

-
use_raw ( bool or None , default=None ) – Whether to draw expression values from `adata.raw `.

-
layer ( str or None , default=None ) – Layer name for expression-based coloring.

-
groups ( str or None , default=None ) – Optional subset of categorical groups to display.

-
title ( str or Sequence [ str ] or None , default=None ) – Plot title(s).

-
figsize ( tuple [ float , float ] , default= ( 4 , 4 ) ) – Single-panel figure size.

-
ax ( matplotlib.axes.Axes or None , default=None ) – Existing axis for single-panel plotting.

-
cmap ( str or Colormap , default='RdBu_r' ) – Colormap for continuous variables.

-
palette ( str or sequence or Cycler or None , default=None ) – Palette for categorical variables.

-
na_color ( ColorLike , default='lightgray' ) – Color for missing values.

-
na_in_legend ( bool , default=True ) – Whether to include missing values in categorical legends.

-
legend_loc ( str , default='right margin' ) – Legend location mode.

-
legend_fontsize ( int or float or None , default=None ) – Legend font size.

-
legend_fontweight ( int or str , default='bold' ) – Legend font weight.

-
legend_fontoutline ( int or None , default=None ) – Outline width for legend text.

-
frameon ( bool or str or None , default='small' ) – Frame style.

-
colorbar_loc ( str or None , default='right' ) – Colorbar placement.

-
vmax ( `Union `[ `Any `, `Sequence `[ `Any `], `None `] (default: `None `)) – Color normalization controls for continuous features.

-
vmin ( `Union `[ `Any `, `Sequence `[ `Any `], `None `] (default: `None `)) – Color normalization controls for continuous features.

-
vcenter ( `Union `[ `Any `, `Sequence `[ `Any `], `None `] (default: `None `)) – Color normalization controls for continuous features.

-
norm ( `Union `[ `Normalize `, `Sequence `[ `Normalize `], `None `] (default: `None `)) – Color normalization controls for continuous features.

-
plot_width ( int , default=800 ) – Datashader canvas width in pixels.

-
plot_height ( int , default=800 ) – Datashader canvas height in pixels.

-
spread_px ( int , default=0 ) – Pixel spreading radius to improve sparse visibility.

-
how ( str , default='eq_hist' ) – Datashader shading strategy.

-
show ( bool or None , default=None ) – Whether to display the figure immediately.

-
save ( bool or str or None , default=None ) – Save option forwarded to Scanpy-style behavior.

-
return_fig ( bool or None , default=None ) – Whether to return the figure object for multi-panel output.

-
ncols ( int , default=4 ) – Number of columns in multi-panel mode.

-
wspace ( float or None , default=None ) – Horizontal spacing between panels.

-
hspace ( float , default=0.25 ) – Vertical spacing between panels.

-
**kwargs – Additional arguments passed to lower-level plotting helpers.

Returns :

Plot object when `show=False `or `return_fig=True `; otherwise `None `.

Return type :

Figure or Axes or None
