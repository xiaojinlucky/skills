# omicverse.single.GLUE_pair #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.GLUE_pair`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.GLUE_pair.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Pair RNA and ATAC cells using GLUE latent embeddings and neighbor matching.

## Signature

```text
class omicverse.single. GLUE_pair ( rna , atac )
```

## Parameters

- `rna`: ( anndata.AnnData ) – RNA AnnData with obsm['X_glue'] .
- `atac`: ( anndata.AnnData ) – ATAC AnnData with obsm['X_glue'] .

## Full Documentation

# omicverse.single.GLUE_pair #

class omicverse.single. GLUE_pair ( rna , atac ) [source] #

Pair RNA and ATAC cells using GLUE latent embeddings and neighbor matching.

Parameters :

-
rna ( anndata.AnnData ) – RNA AnnData with `obsm['X_glue'] `.

-
atac ( anndata.AnnData ) – ATAC AnnData with `obsm['X_glue'] `.

Returns :

Initializes paired-modality matching workflow.

Return type :

None

Examples

```text
>>> pair_obj = ov.single.GLUE_pair(rna, atac)

```

__init__ ( rna , atac ) [source] #

Pair the cells between RNA and ATAC using result of GLUE.

Parameters :

-
rna ( anndata.AnnData ) – RNA AnnData containing `obsm['X_glue'] `.

-
atac ( anndata.AnnData ) – ATAC AnnData containing `obsm['X_glue'] `.

Return type :

None

Methods

`__init__ `(rna, atac)

Pair the cells between RNA and ATAC using result of GLUE.

`correlation `()

Perform Pearson Correlation analysis in the layer of GLUE.

`find_neighbor_cell `([depth, cor])

Find the neighbor cells between two omics using pearson correlation.

`pair_omic `(omic1, omic2)

Pair the omics using the result of find_neighbor_cell.
