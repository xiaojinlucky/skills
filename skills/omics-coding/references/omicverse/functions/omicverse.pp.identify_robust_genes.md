# omicverse.pp.identify_robust_genes #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.identify_robust_genes`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.identify_robust_genes.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Identify robust genes for downstream HVG selection.

## Signature

```text
omicverse.pp. identify_robust_genes ( data , percent_cells = 0.05 )
```

## Parameters

- `data`: ( anndata.AnnData ) – AnnData object containing a gene expression matrix in .X . Genes with zero counts across all cells are removed.
- `percent_cells`: ( float , default=0.05 ) – Minimum percentage of cells in which a gene must be detected to be marked as robust .

## Full Documentation

# omicverse.pp.identify_robust_genes #

omicverse.pp. identify_robust_genes ( data , percent_cells = 0.05 ) [source] #

Identify robust genes for downstream HVG selection.

Parameters :

-
data ( anndata.AnnData ) – AnnData object containing a gene expression matrix in `.X `. Genes with zero counts across all cells are removed.

-
percent_cells ( float , default=0.05 ) – Minimum percentage of cells in which a gene must be detected to be marked as `robust `.

Returns :

Updates `data.var `with `n_cells `, `percent_cells `, `robust `, and initializes `highly_variable_features `from `robust `.

Return type :

None
