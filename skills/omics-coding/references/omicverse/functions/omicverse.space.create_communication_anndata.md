# omicverse.space.create_communication_anndata #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.create_communication_anndata`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.create_communication_anndata.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Build a CellChat-style communication AnnData from commot outputs.

## Signature

```text
omicverse.space. create_communication_anndata ( adata , clustering_column , n_permutations = 100 )
```

## Parameters

- `adata`: ( anndata.AnnData ) – Input spatial AnnData containing commot communication matrices in adata.obsp and optional commot database metadata in adata.uns .
- `clustering_column`: ( str ) – Column name for cell type clustering
- `n_permutations`: ( int ) – Number of permutations for p-value calculation

## Full Documentation

# omicverse.space.create_communication_anndata #

omicverse.space. create_communication_anndata ( adata , clustering_column , n_permutations = 100 ) [source] #

Build a CellChat-style communication AnnData from commot outputs.

Parameters :

-
adata ( anndata.AnnData ) – Input spatial AnnData containing commot communication matrices in `adata.obsp `and optional commot database metadata in `adata.uns `.

-
clustering_column ( str ) – Column name for cell type clustering

-
n_permutations ( int ) – Number of permutations for p-value calculation

Returns :

comm_adata – Communication results with structure: - obs: cell type pairs (‘celltype1|celltype2’) - var: ligand-receptor pairs with metadata - layers: ‘pvalues’ and ‘means’

Return type :

anndata.AnnData
