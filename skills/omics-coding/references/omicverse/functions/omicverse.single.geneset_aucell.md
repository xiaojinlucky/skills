# omicverse.single.geneset_aucell #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.geneset_aucell`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.geneset_aucell.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Calculate the AUC-ell score for a given gene set.

## Signature

```text
omicverse.single. geneset_aucell ( adata , geneset_name , geneset , AUC_threshold = 0.01 , seed = 42 )
```

## Parameters

- `adata`: ( anndata.AnnData ) – AnnData containing expression matrix.
- `geneset_name`: ( str ) – Name of gene set; used as output column prefix.
- `geneset`: ( list ) – Gene symbols composing the gene set.
- `AUC_threshold`: ( float ) – AUCell rank threshold percentile.
- `seed`: ( int ) – Random seed for ranking backend.

## Full Documentation

# omicverse.single.geneset_aucell #

omicverse.single. geneset_aucell ( adata , geneset_name , geneset , AUC_threshold = 0.01 , seed = 42 ) [source] #

Calculate the AUC-ell score for a given gene set.

Parameters :

-
adata ( anndata.AnnData ) – AnnData containing expression matrix.

-
geneset_name ( str ) – Name of gene set; used as output column prefix.

-
geneset ( list ) – Gene symbols composing the gene set.

-
AUC_threshold ( float ) – AUCell rank threshold percentile.

-
seed ( int ) – Random seed for ranking backend.

Returns :

Writes AUCell score to `adata.obs[f'{geneset_name}_aucell'] `.

Return type :

None
