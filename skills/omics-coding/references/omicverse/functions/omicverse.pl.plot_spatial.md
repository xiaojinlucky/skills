# omicverse.pl.plot_spatial #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.plot_spatial`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.plot_spatial.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Create spatial plot from Visium data with color gradient and interpolation.

## Signature

```text
omicverse.pl. plot_spatial ( adata , color , img_key = 'hires' , show_img = True , ** kwargs )
```

## Parameters

- `adata`: ( AnnData ) – Spatial AnnData containing coordinates and optional image metadata.
- `color`: ( list ) – Feature names from adata.obs or genes from adata.var_names .
- `img_key`: ( str ) – Spatial image resolution key (for example 'hires' or 'lowres' ).
- `show_img`: ( bool ) – Whether to draw tissue image as background.
- `**kwargs`: – Additional arguments forwarded to plot_spatial_general .

## Full Documentation

# omicverse.pl.plot_spatial #

omicverse.pl. plot_spatial ( adata , color , img_key = 'hires' , show_img = True , ** kwargs ) [source] #

Create spatial plot from Visium data with color gradient and interpolation.

Supports up to 7 cell types with default colors: yellow, orange, blue, green, purple, grey, white.

Parameters :

-
adata ( AnnData ) – Spatial AnnData containing coordinates and optional image metadata.

-
color ( list ) – Feature names from `adata.obs `or genes from `adata.var_names `.

-
img_key ( str ) – Spatial image resolution key (for example `'hires' `or `'lowres' `).

-
show_img ( bool ) – Whether to draw tissue image as background.

-
**kwargs – Additional arguments forwarded to `plot_spatial_general `.

Returns :

Figure of spatial abundance/expression plot.

Return type :

matplotlib.figure.Figure
