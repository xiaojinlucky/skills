# omicverse.pl.plot1cell #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.plot1cell`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.plot1cell.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Circular UMAP with metadata tracks.

## Signature

```text
omicverse.pl. plot1cell ( adata , clusters , basis = 'X_umap' , tracks = None , * , coord_scale = 0.8 , point_size = 3.0 , point_alpha = 0.3 , contour_levels = (0.2, 0.3) , contour_color = 'ae9c76' , kde_n = 200 , do_label = True , label_fontsize = 9.0 , label_orient = 'radial' , cluster_palette = None , track_palette = None , track_palettes = None , bg_color = None , gap_between_deg = 2.0 , gap_start_deg = 12.0 , cluster_track_width = 0.035 , track_width = 0.025 , track_gap = 0.004 , cluster_label_pad = 0.03 , show_ticks = True , tick_fontsize = 4.5 , tick_length = 0.012 , figsize = (7, 7) , ax = None , show = True , return_data = False )
```

## Parameters

- `adata`: ( AnnData )
- `clusters`: ( str ) – Key in adata.obs giving the cluster label per cell.
- `basis`: ( str ) – Key in adata.obsm ; first two columns are used.
- `tracks`: ( list [ str ] | None ) – Additional adata.obs columns to show as outer rings.
- `coord_scale`: ( float ) – zoom parameter from the R version; the scatter fills [-coord_scale, coord_scale] on each axis.
- `contour_levels`: ( tuple [ float , ... ] | None ) – Level set(s) of the 2-D KDE to overlay. None disables contours.
- `gap_between_deg`: ( float ) – Angular gaps (degrees) between adjacent cluster sectors and at the circle’s starting point.
- `gap_start_deg`: ( float ) – Angular gaps (degrees) between adjacent cluster sectors and at the circle’s starting point.
- `cluster_track_width`: ( float ) – Radial thickness of the cluster ring and each metadata ring, expressed as a fraction of the unit radius.
- `track_width`: ( float ) – Radial thickness of the cluster ring and each metadata ring, expressed as a fraction of the unit radius.
- `ax`: ( matplotlib Axes | None ) – If given, draw into it (must be aspect='equal' ). A new figure is created otherwise.
- `return_data`: ( bool ) – If True, also return the per-cell dataframe used for plotting (useful for reproducing or extending the figure).
- `point_size`: ( float (default: 3.0 ))
- `point_alpha`: ( float (default: 0.3 ))
- `contour_color`: ( str (default: '#ae9c76' ))
- `kde_n`: ( int (default: 200 ))
- `do_label`: ( bool (default: True ))
- `label_fontsize`: ( float (default: 9.0 ))
- `label_orient`: ( str (default: 'radial' ))
- `track_palettes`: ( Optional [ Sequence ] (default: None ))
- `bg_color`: ( Optional [ str ] (default: None ))
- `track_gap`: ( float (default: 0.004 ))
- `cluster_label_pad`: ( float (default: 0.03 ))
- `show_ticks`: ( bool (default: True ))
- `tick_fontsize`: ( float (default: 4.5 ))
- `tick_length`: ( float (default: 0.012 ))
- `show`: ( bool (default: True ))
- `cluster_palette`: Detected from function signature; no parameter description detected.
- `track_palette`: Detected from function signature; no parameter description detected.
- `figsize`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.pl.plot1cell #

omicverse.pl. plot1cell ( adata , clusters , basis = 'X_umap' , tracks = None , * , coord_scale = 0.8 , point_size = 3.0 , point_alpha = 0.3 , contour_levels = (0.2, 0.3) , contour_color = '#ae9c76' , kde_n = 200 , do_label = True , label_fontsize = 9.0 , label_orient = 'radial' , cluster_palette = None , track_palette = None , track_palettes = None , bg_color = None , gap_between_deg = 2.0 , gap_start_deg = 12.0 , cluster_track_width = 0.035 , track_width = 0.025 , track_gap = 0.004 , cluster_label_pad = 0.03 , show_ticks = True , tick_fontsize = 4.5 , tick_length = 0.012 , figsize = (7, 7) , ax = None , show = True , return_data = False ) [source] #

Circular UMAP with metadata tracks.

Mirrors plot1cell::plot_circlize (Wu 2021). Clusters are laid out as arc sectors on the circumference, sector length proportional to `log10(n_cells) `. The scatter is drawn in Cartesian coordinates inside the unit circle, with a Gaussian-KDE contour overlay. Each entry in `tracks `becomes one extra concentric ring coloured by the run-length segments of that metadata column within each cluster sector .

Parameters :

-
adata ( AnnData )

-
clusters ( str ) – Key in `adata.obs `giving the cluster label per cell.

-
basis ( str ) – Key in `adata.obsm `; first two columns are used.

-
tracks ( list [ str ] | None ) – Additional `adata.obs `columns to show as outer rings.

-
coord_scale ( float ) – `zoom `parameter from the R version; the scatter fills `[-coord_scale, coord_scale] `on each axis.

-
contour_levels ( tuple [ float , ... ] | None ) – Level set(s) of the 2-D KDE to overlay. `None `disables contours.

-
gap_between_deg ( float ) – Angular gaps (degrees) between adjacent cluster sectors and at the circle’s starting point.

-
gap_start_deg ( float ) – Angular gaps (degrees) between adjacent cluster sectors and at the circle’s starting point.

-
cluster_track_width ( float ) – Radial thickness of the cluster ring and each metadata ring, expressed as a fraction of the unit radius.

-
track_width ( float ) – Radial thickness of the cluster ring and each metadata ring, expressed as a fraction of the unit radius.

-
ax ( matplotlib Axes | None ) – If given, draw into it (must be `aspect='equal' `). A new figure is created otherwise.

-
return_data ( bool ) – If True, also return the per-cell dataframe used for plotting (useful for reproducing or extending the figure).

-
point_size ( `float `(default: `3.0 `))

-
point_alpha ( `float `(default: `0.3 `))

-
contour_color ( `str `(default: `'#ae9c76' `))

-
kde_n ( `int `(default: `200 `))

-
do_label ( `bool `(default: `True `))

-
label_fontsize ( `float `(default: `9.0 `))

-
label_orient ( `str `(default: `'radial' `))

-
track_palettes ( `Optional `[ `Sequence `] (default: `None `))

-
bg_color ( `Optional `[ `str `] (default: `None `))

-
track_gap ( `float `(default: `0.004 `))

-
cluster_label_pad ( `float `(default: `0.03 `))

-
show_ticks ( `bool `(default: `True `))

-
tick_fontsize ( `float `(default: `4.5 `))

-
tick_length ( `float `(default: `0.012 `))

-
show ( `bool `(default: `True `))

Returns :

-
ax ( matplotlib.axes.Axes )

-
(ax, df) if `return_data=True `.
