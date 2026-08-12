# omicverse.single.scanpy_cellanno_from_dict #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.scanpy_cellanno_from_dict`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.scanpy_cellanno_from_dict.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Add cell type annotation from dict to anndata object.

## Signature

```text
omicverse.single. scanpy_cellanno_from_dict ( adata , anno_dict , anno_name = 'major' , clustertype = 'leiden' )
```

## Parameters

- `adata`: ( anndata.AnnData ) – AnnData object to which annotation labels are added.
- `anno_dict`: ( dict ) – Mapping from cluster label to cell-type name.
- `anno_name`: ( str ) – Prefix used to create output obs column {anno_name}_celltype .
- `clustertype`: ( str ) – Cluster column in adata.obs used as mapping key.

## Full Documentation

# omicverse.single.scanpy_cellanno_from_dict #

omicverse.single. scanpy_cellanno_from_dict ( adata , anno_dict , anno_name = 'major' , clustertype = 'leiden' ) [source] #

Add cell type annotation from dict to anndata object.

Parameters :

-
adata ( anndata.AnnData ) – AnnData object to which annotation labels are added.

-
anno_dict ( dict ) – Mapping from cluster label to cell-type name.

-
anno_name ( str ) – Prefix used to create output `obs `column `{anno_name}_celltype `.

-
clustertype ( str ) – Cluster column in `adata.obs `used as mapping key.

Return type :

None
