# omicverse.space.update_classification_from_database #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.update_classification_from_database`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.update_classification_from_database.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Update communication interaction annotations from commot database metadata.

## Signature

```text
omicverse.space. update_classification_from_database ( comm_adata , adata_with_db )
```

## Parameters

- `comm_adata`: ( anndata.AnnData ) – Communication AnnData returned by create_communication_anndata .
- `adata_with_db`: ( anndata.AnnData ) – Original spatial AnnData containing commot-*-info entries in uns .

## Full Documentation

# omicverse.space.update_classification_from_database #

omicverse.space. update_classification_from_database ( comm_adata , adata_with_db ) [source] #

Update communication interaction annotations from commot database metadata.

Parameters :

-
comm_adata ( anndata.AnnData ) – Communication AnnData returned by `create_communication_anndata `.

-
adata_with_db ( anndata.AnnData ) – Original spatial AnnData containing `commot-*-info `entries in `uns `.

Returns :

comm_adata – Updated communication AnnData with refined pathway/classification fields.

Return type :

anndata.AnnData
