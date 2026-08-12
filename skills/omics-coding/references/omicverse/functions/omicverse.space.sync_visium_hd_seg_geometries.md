# omicverse.space.sync_visium_hd_seg_geometries #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.sync_visium_hd_seg_geometries`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.sync_visium_hd_seg_geometries.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Synchronize adata.uns["spatial"][sample]["geometries"] with current adata.obs_names .

## Signature

```text
omicverse.space. sync_visium_hd_seg_geometries ( adata , sample = None )
```

## Parameters

- `adata`: ( sc.AnnData ) – A (possibly subsetted) AnnData object containing spatial segmentation metadata.
- `sample`: ( str , optional ) – Sample key under adata.uns["spatial"] . If None , the first available key is used (with a warning when multiple samples exist).

## Full Documentation

# omicverse.space.sync_visium_hd_seg_geometries #

omicverse.space. sync_visium_hd_seg_geometries ( adata , sample = None ) [source] #

Synchronize `adata.uns["spatial"][sample]["geometries"] `with current `adata.obs_names `.

This utility is intended for AnnData objects loaded by `read_visium_hd_seg `. After subsetting AnnData, `adata.obs `and `adata.obsm `are subset automatically, but the geometry table stored in `adata.uns["spatial"][sample]["geometries"] `may still contain rows for cells that are no longer present. This function filters that GeoDataFrame by current cell IDs and updates it in place.

Parameters :

-
adata ( sc.AnnData ) – A (possibly subsetted) AnnData object containing spatial segmentation metadata.

-
sample ( str , optional ) – Sample key under `adata.uns["spatial"] `. If `None `, the first available key is used (with a warning when multiple samples exist).

Returns :

The same `adata `object, modified in place.

Return type :

sc.AnnData
