# omicverse.space.bin2cell #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.bin2cell`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.bin2cell.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Aggregate binned Visium signals into cell-level profiles.

## Signature

```text
omicverse.space. bin2cell ( adata , labels_key = 'labels_joint' , spatial_keys = ['spatial'] , diameter_scale_factor = None , add_geometry = True , geometry_key = 'geometry' , geometry_spatial_key = 'spatial' , geometry_force_polygon = False , rename_obs_to_cellid = True , show_progress = True )
```

## Parameters

- `adata`: ( AnnData ) – Spatial bin-level AnnData.
- `labels_key`: ( str , default='labels_joint' ) – Label key assigning bins to cells.
- `spatial_keys`: ( list , default= [ 'spatial' ] ) – Spatial coordinate keys to aggregate.
- `diameter_scale_factor`: ( float , optional ) – Optional scaling factor for estimated cell diameters.
- `add_geometry`: ( bool , default=False ) – Whether to generate polygon geometry from labeled bins and store WKT strings in obs[geometry_key] of the returned cell-level AnnData.
- `geometry_key`: ( str , default='geometry' ) – Observation column name used to store generated geometry WKT.
- `geometry_spatial_key`: ( str , default='spatial' ) – Coordinate key in adata.obsm used to reconstruct polygons.
- `geometry_force_polygon`: ( bool , default=False ) – If True , convert MultiPolygon geometries to their largest polygon component so each cell gets a single polygon contour.
- `rename_obs_to_cellid`: ( bool , default=True ) – If True , rename output obs_names to cellid_XXXXXXXXX-1 using obs['object_id'] and also write obs['cellid'] .
- `show_progress`: ( bool , default=True ) – Whether to display progress bars during aggregation and (if enabled) geometry reconstruction.

## Full Documentation

# omicverse.space.bin2cell #

omicverse.space. bin2cell ( adata , labels_key = 'labels_joint' , spatial_keys = ['spatial'] , diameter_scale_factor = None , add_geometry = True , geometry_key = 'geometry' , geometry_spatial_key = 'spatial' , geometry_force_polygon = False , rename_obs_to_cellid = True , show_progress = True ) [source] #

Aggregate binned Visium signals into cell-level profiles.

Parameters :

-
adata ( AnnData ) – Spatial bin-level AnnData.

-
labels_key ( str , default='labels_joint' ) – Label key assigning bins to cells.

-
spatial_keys ( list , default= [ 'spatial' ] ) – Spatial coordinate keys to aggregate.

-
diameter_scale_factor ( float , optional ) – Optional scaling factor for estimated cell diameters.

-
add_geometry ( bool , default=False ) – Whether to generate polygon geometry from labeled bins and store WKT strings in `obs[geometry_key] `of the returned cell-level AnnData.

-
geometry_key ( str , default='geometry' ) – Observation column name used to store generated geometry WKT.

-
geometry_spatial_key ( str , default='spatial' ) – Coordinate key in `adata.obsm `used to reconstruct polygons.

-
geometry_force_polygon ( bool , default=False ) – If `True `, convert `MultiPolygon `geometries to their largest polygon component so each cell gets a single polygon contour.

-
rename_obs_to_cellid ( bool , default=True ) – If `True `, rename output `obs_names `to `cellid_XXXXXXXXX-1 `using `obs['object_id'] `and also write `obs['cellid'] `.

-
show_progress ( bool , default=True ) – Whether to display progress bars during aggregation and (if enabled) geometry reconstruction.

Returns :

Cell-level AnnData generated from labeled bins.

Return type :

AnnData
