# omicverse.io.read_nanostring #

- Package: omicverse
- Language: Python
- Function: `omicverse.io.read_nanostring`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.io.read_nanostring.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read Nanostring formatted dataset.

## Signature

```text
omicverse.io. read_nanostring ( path , * , counts_file , meta_file , fov_file = None )
```

## Parameters

- `path`: ( Union [ str , Path ] )
- `counts_file`: ( str )
- `meta_file`: ( str )
- `fov_file`: ( Optional [ str ] (default: None ))

## Full Documentation

# omicverse.io.read_nanostring #

omicverse.io. read_nanostring ( path , * , counts_file , meta_file , fov_file = None ) [source] #

Read Nanostring formatted dataset.

This follows the Squidpy nanostring reader layout:

-
`obsm['spatial'] `: local cell center coordinates.

-
`obsm['spatial_fov'] `: global cell center coordinates.

-
`uns['spatial'][fov]['images'] `: hires and segmentation images from `CellComposite `and `CellLabels `.

-
`uns['spatial'][fov]['metadata'] `: optional FOV-level metadata.

-
If geometry-like columns exist in metadata, writes `obs['geometry'] `as WKT strings to match `read_visium_hd_seg `format for `ov.pl.spatialseg `.

Parameters :

-
path ( `Union `[ `str `, `Path `] )

-
counts_file ( `str `)

-
meta_file ( `str `)

-
fov_file ( `Optional `[ `str `] (default: `None `))
