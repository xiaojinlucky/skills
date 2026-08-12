# omicverse.single.pathway_aucell_enrichment #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.pathway_aucell_enrichment`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.pathway_aucell_enrichment.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Enrich cell annotations with pathway activity scores using the AUC-ell method.

## Signature

```text
omicverse.single. pathway_aucell_enrichment ( adata , pathways_dict , AUC_threshold = 0.01 , seed = 42 , num_workers = 1 , gene_overlap_threshold = 0.8 )
```

## Parameters

- `adata`: ( anndata.AnnData ) – AnnData containing expression matrix.
- `pathways_dict`: ( dict ) – Mapping from pathway name to list of genes.
- `AUC_threshold`: ( float ) – AUCell rank threshold percentile.
- `seed`: ( int ) – Random seed for AUCell backend.
- `num_workers`: ( int ) – Number of workers used in AUCell computation.
- `gene_overlap_threshold`: ( float ) – Minimum fraction of pathway genes present in adata.var_names .

## Full Documentation

# omicverse.single.pathway_aucell_enrichment #

omicverse.single. pathway_aucell_enrichment ( adata , pathways_dict , AUC_threshold = 0.01 , seed = 42 , num_workers = 1 , gene_overlap_threshold = 0.8 ) [source] #

Enrich cell annotations with pathway activity scores using the AUC-ell method.

Parameters :

-
adata ( anndata.AnnData ) – AnnData containing expression matrix.

-
pathways_dict ( dict ) – Mapping from pathway name to list of genes.

-
AUC_threshold ( float ) – AUCell rank threshold percentile.

-
seed ( int ) – Random seed for AUCell backend.

-
num_workers ( int ) – Number of workers used in AUCell computation.

-
gene_overlap_threshold ( float ) – Minimum fraction of pathway genes present in `adata.var_names `.

Returns :

AnnData whose `X `stores pathway AUCell activity matrix.

Return type :

anndata.AnnData
