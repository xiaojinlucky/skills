# omicverse.pp.score_genes_cell_cycle #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.score_genes_cell_cycle`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.score_genes_cell_cycle.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Score cell cycle phases using predefined or custom gene sets.

## Signature

```text
omicverse.pp. score_genes_cell_cycle ( adata , species = 'human' , s_genes = None , g2m_genes = None )
```

## Parameters

- `adata`: – Annotated data matrix with rows for cells and columns for genes.
- `species`: (default: 'human' ) – The species of the data (‘human’ or ‘mouse’). Default: ‘human’.
- `s_genes`: (default: None ) – Custom list of S phase genes. Default: None (uses predefined).
- `g2m_genes`: (default: None ) – Custom list of G2M phase genes. Default: None (uses predefined).

## Full Documentation

# omicverse.pp.score_genes_cell_cycle #

omicverse.pp. score_genes_cell_cycle ( adata , species = 'human' , s_genes = None , g2m_genes = None ) [source] #

Score cell cycle phases using predefined or custom gene sets.

Parameters :

-
adata – Annotated data matrix with rows for cells and columns for genes.

-
species (default: `'human' `) – The species of the data (‘human’ or ‘mouse’). Default: ‘human’.

-
s_genes (default: `None `) – Custom list of S phase genes. Default: None (uses predefined).

-
g2m_genes (default: `None `) – Custom list of G2M phase genes. Default: None (uses predefined).

Returns :

Updates adata.obs with ‘S_score’, ‘G2M_score’, and ‘phase’ columns.

Return type :

None

Examples

```text
>>> import omicverse as ov
>>> # Score cell cycle for human data
>>> ov.pp.score_genes_cell_cycle(adata, species='human')
>>> # Check results
>>> print(adata.obs[['S_score', 'G2M_score', 'phase']].head())

```
