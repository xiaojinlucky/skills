# omicverse.pp.filter_cells #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.filter_cells`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.filter_cells.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Filter cell outliers based on counts and numbers of genes expressed.

## Signature

```text
omicverse.pp. filter_cells ( adata , min_counts = None , min_genes = None , max_counts = None , max_genes = None , inplace = True )
```

## Parameters

- `adata`: ( AnnData ) – The (annotated) data matrix of shape n_obs × n_vars . Rows correspond to cells and columns to genes.
- `min_counts`: ( Optional [ int ] (default: None )) – Minimum number of counts required for a cell to pass filtering.
- `min_genes`: ( Optional [ int ] (default: None )) – Minimum number of genes expressed required for a cell to pass filtering.
- `max_counts`: ( Optional [ int ] (default: None )) – Maximum number of counts required for a cell to pass filtering.
- `max_genes`: ( Optional [ int ] (default: None )) – Maximum number of genes expressed required for a cell to pass filtering.
- `inplace`: ( bool (default: True )) – Perform computation inplace or return result.

## Full Documentation

# omicverse.pp.filter_cells #

omicverse.pp. filter_cells ( adata , min_counts = None , min_genes = None , max_counts = None , max_genes = None , inplace = True ) [source] #

Filter cell outliers based on counts and numbers of genes expressed.

For instance, only keep cells with at least min_counts counts or min_genes genes expressed. This is to filter measurement outliers, i.e. “unreliable” observations.

Only provide one of the optional parameters min_counts , min_genes , max_counts , max_genes per call.

Parameters :

-
adata ( `AnnData `) – The (annotated) data matrix of shape n_obs × n_vars . Rows correspond to cells and columns to genes.

-
min_counts ( `Optional `[ `int `] (default: `None `)) – Minimum number of counts required for a cell to pass filtering.

-
min_genes ( `Optional `[ `int `] (default: `None `)) – Minimum number of genes expressed required for a cell to pass filtering.

-
max_counts ( `Optional `[ `int `] (default: `None `)) – Maximum number of counts required for a cell to pass filtering.

-
max_genes ( `Optional `[ `int `] (default: `None `)) – Maximum number of genes expressed required for a cell to pass filtering.

-
inplace ( `bool `(default: `True `)) – Perform computation inplace or return result.

Returns :

-
Depending on inplace , returns the following arrays or directly subsets

-
and annotates the data matrix

-
cells_subset – Boolean index mask that does filtering. True means that the cell is kept. False means the cell is removed.

-
number_per_cell – Depending on what was tresholded ( counts or genes ), the array stores n_counts or n_cells per gene.
