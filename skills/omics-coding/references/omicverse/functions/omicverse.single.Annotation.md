# omicverse.single.Annotation #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.Annotation`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.Annotation.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Unified single-cell annotation manager for cell-type labeling.

## Signature

```text
class omicverse.single. Annotation ( adata )
```

## Parameters

- `adata`: ( AnnData ) – Query single-cell AnnData to annotate.

## Full Documentation

# omicverse.single.Annotation #

class omicverse.single. Annotation ( adata ) [source] #

Unified single-cell annotation manager for cell-type labeling.

Parameters :

adata ( AnnData ) – Query single-cell AnnData to annotate.

Returns :

Initializes annotation manager state and reference caches.

Return type :

None

__init__ ( adata ) [source] #

Initialize annotation manager with a query AnnData object.

Parameters :

adata ( AnnData ) – Query dataset to annotate.

Methods

`__init__ `(adata)

Initialize annotation manager with a query AnnData object.

`add_reference_pkl `(reference)

Register a CellTypist model file for supervised annotation.

`add_reference_sc `(reference[, celltype_key])

Register a single-cell reference atlas for transfer-based annotation.

`add_reference_scsa_db `(reference)

Register a local SCSA marker database file.

`annotate `([method, cluster_key])

Annotate cells or clusters using the selected annotation backend.

`download_reference_pkl `(reference_name, save_path)

Download a CellTypist model by model name and store it locally.

`download_scmulan_ckpt `([save_path, ...])

Download the pretrained scMulan checkpoint.

`download_scsa_db `([save_path])

Download SCSA database with fallback mirrors.

`query_reference `([source, data_desc, ...])

Use an LLM to identify relevant reference resources based on a description.
