# omicverse.pp.filter_genes #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.filter_genes`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.filter_genes.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Filter genes based on number of cells or counts.

## Signature

```text
omicverse.pp. filter_genes ( adata , min_counts = None , min_cells = None , max_counts = None , max_cells = None , inplace = True )
```

## Parameters

- `adata`: ( AnnData ) – An annotated data matrix of shape n_obs × n_vars . Rows correspond to cells and columns to genes.
- `min_counts`: ( Optional [ int ] (default: None )) – Minimum number of counts required for a gene to pass filtering.
- `min_cells`: ( Optional [ int ] (default: None )) – Minimum number of cells expressed required for a gene to pass filtering.
- `max_counts`: ( Optional [ int ] (default: None )) – Maximum number of counts required for a gene to pass filtering.
- `max_cells`: ( Optional [ int ] (default: None )) – Maximum number of cells expressed required for a gene to pass filtering.
- `inplace`: ( bool (default: True )) – Perform computation inplace or return result.

## Full Documentation

# omicverse.pp.filter_genes #

omicverse.pp. filter_genes ( adata , min_counts = None , min_cells = None , max_counts = None , max_cells = None , inplace = True ) [source] #

Filter genes based on number of cells or counts.

Keep genes that have at least min_counts counts or are expressed in at least min_cells cells or have at most max_counts counts or are expressed in at most max_cells cells.

Only provide one of the optional parameters min_counts , min_cells , max_counts , max_cells per call.

Parameters :

-
adata ( `AnnData `) – An annotated data matrix of shape n_obs × n_vars . Rows correspond to cells and columns to genes.

-
min_counts ( `Optional `[ `int `] (default: `None `)) – Minimum number of counts required for a gene to pass filtering.

-
min_cells ( `Optional `[ `int `] (default: `None `)) – Minimum number of cells expressed required for a gene to pass filtering.

-
max_counts ( `Optional `[ `int `] (default: `None `)) – Maximum number of counts required for a gene to pass filtering.

-
max_cells ( `Optional `[ `int `] (default: `None `)) – Maximum number of cells expressed required for a gene to pass filtering.

-
inplace ( `bool `(default: `True `)) – Perform computation inplace or return result.

Returns :

-
Depending on inplace , returns the following arrays or directly subsets

-
and annotates the data matrix

-
gene_subset – Boolean index mask that does filtering. True means that the gene is kept. False means the gene is removed.

-
number_per_gene – Depending on what was tresholded ( counts or cells ), the array stores n_counts or n_cells per gene.
