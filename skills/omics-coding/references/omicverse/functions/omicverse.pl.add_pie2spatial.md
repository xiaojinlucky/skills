# omicverse.pl.add_pie2spatial #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.add_pie2spatial`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.add_pie2spatial.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Overlay per-spot pie charts of cell-type composition on a spatial map.

## Signature

```text
omicverse.pl. add_pie2spatial ( adata , cell_type_columns , ax , pie_radius = 15 , img_key = 'hires' , spatial_coords = None , pie_radius_px = None , min_proportion = 0.01 , colors = None , alpha = 0.9 , remainder = 'gap' , remainder_color = 'lightgray' , remainder_alpha = 0.5 , renormalize_if_sum_gt1 = True , zorder = 80 , legend_loc = (1.05, 1.0) , ncols = 3 )
```

## Parameters

- `adata`: ( AnnData ) – Spatial AnnData object. Requires adata.obsm['spatial'] .
- `cell_type_columns`: ( list of str ) – Columns in adata.obs (or genes in adata.var_names ) used as pie components.
- `ax`: ( matplotlib.axes.Axes ) – Target axes.
- `pie_radius`: ( float , optional ) – Pie radius in data coordinates when pie_radius_px is not provided.
- `img_key`: ( str , optional ) – Spatial image key used to rescale coordinates (for example 'hires' ).
- `spatial_coords`: ( array-like , optional ) – External coordinates overriding adata.obsm['spatial'] .
- `pie_radius_px`: ( float or None , optional ) – Pie radius in pixels; converted to data units automatically.
- `min_proportion`: ( float , optional ) – Minimum slice proportion to draw.
- `colors`: ( dict or sequence , optional ) – Color mapping for cell types.
- `alpha`: ( float , optional ) – Pie transparency.
- `remainder`: ( {'gap' , 'gray' , 'outline'} , optional ) – How to render unassigned mass when proportions do not sum to 1.
- `remainder_color`: ( str , optional ) – Color for remainder slice when remainder='gray' .
- `remainder_alpha`: ( float , optional ) – Alpha for remainder slice.
- `renormalize_if_sum_gt1`: ( bool , optional ) – If True , renormalize rows whose sum exceeds 1.
- `zorder`: ( int , optional ) – Drawing order for pie artists.
- `legend_loc`: ( tuple , optional ) – Legend anchor location.
- `ncols`: ( int , optional ) – Number of legend columns.

## Full Documentation

# omicverse.pl.add_pie2spatial #

omicverse.pl. add_pie2spatial ( adata , cell_type_columns , ax , pie_radius = 15 , img_key = 'hires' , spatial_coords = None , pie_radius_px = None , min_proportion = 0.01 , colors = None , alpha = 0.9 , remainder = 'gap' , remainder_color = 'lightgray' , remainder_alpha = 0.5 , renormalize_if_sum_gt1 = True , zorder = 80 , legend_loc = (1.05, 1.0) , ncols = 3 ) [source] #

Overlay per-spot pie charts of cell-type composition on a spatial map.

Parameters :

-
adata ( AnnData ) – Spatial AnnData object. Requires `adata.obsm['spatial'] `.

-
cell_type_columns ( list of str ) – Columns in `adata.obs `(or genes in `adata.var_names `) used as pie components.

-
ax ( matplotlib.axes.Axes ) – Target axes.

-
pie_radius ( float , optional ) – Pie radius in data coordinates when `pie_radius_px `is not provided.

-
img_key ( str , optional ) – Spatial image key used to rescale coordinates (for example `'hires' `).

-
spatial_coords ( array-like , optional ) – External coordinates overriding `adata.obsm['spatial'] `.

-
pie_radius_px ( float or None , optional ) – Pie radius in pixels; converted to data units automatically.

-
min_proportion ( float , optional ) – Minimum slice proportion to draw.

-
colors ( dict or sequence , optional ) – Color mapping for cell types.

-
alpha ( float , optional ) – Pie transparency.

-
remainder ( {'gap' , 'gray' , 'outline'} , optional ) – How to render unassigned mass when proportions do not sum to 1.

-
remainder_color ( str , optional ) – Color for remainder slice when `remainder='gray' `.

-
remainder_alpha ( float , optional ) – Alpha for remainder slice.

-
renormalize_if_sum_gt1 ( bool , optional ) – If `True `, renormalize rows whose sum exceeds 1.

-
zorder ( int , optional ) – Drawing order for pie artists.

-
legend_loc ( tuple , optional ) – Legend anchor location.

-
ncols ( int , optional ) – Number of legend columns.

Returns :

Axes with pie overlays.

Return type :

matplotlib.axes.Axes

Examples

```text
>>> ax = ov.pl.plot_spatial(adata)
>>> ov.pl.add_pie2spatial(adata, cell_type_columns=['T', 'B', 'Myeloid'], ax=ax)

```
