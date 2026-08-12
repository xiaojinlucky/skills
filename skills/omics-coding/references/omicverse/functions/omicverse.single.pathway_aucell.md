# omicverse.single.pathway_aucell #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.pathway_aucell`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.pathway_aucell.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Calculate the area under the curve (AUC) for a set of pathways in an AnnData object.

## Signature

```text
omicverse.single. pathway_aucell ( adata , pathway_names , pathways_dict , AUC_threshold = 0.01 , seed = 42 )
```

## Parameters

- `adata`: ( anndata.AnnData ) – AnnData containing expression matrix.
- `pathway_names`: ( list ) – Ordered pathway names to score.
- `pathways_dict`: ( dict ) – Mapping from pathway name to list of genes.
- `AUC_threshold`: ( float ) – AUCell rank threshold percentile.
- `seed`: ( int ) – Random seed for ranking backend.

## Full Documentation

# omicverse.single.pathway_aucell #

omicverse.single. pathway_aucell ( adata , pathway_names , pathways_dict , AUC_threshold = 0.01 , seed = 42 ) [source] #

Calculate the area under the curve (AUC) for a set of pathways in an AnnData object.

Parameters :

-
adata ( anndata.AnnData ) – AnnData containing expression matrix.

-
pathway_names ( list ) – Ordered pathway names to score.

-
pathways_dict ( dict ) – Mapping from pathway name to list of genes.

-
AUC_threshold ( float ) – AUCell rank threshold percentile.

-
seed ( int ) – Random seed for ranking backend.

Returns :

Writes per-pathway AUCell scores to `adata.obs `.

Return type :

None
