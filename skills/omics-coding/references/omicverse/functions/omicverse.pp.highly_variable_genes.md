# omicverse.pp.highly_variable_genes #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.highly_variable_genes`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.highly_variable_genes.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Annotate highly variable genes (Satija 2015 / Zheng 2017 / Stuart 2019).

## Signature

```text
omicverse.pp. highly_variable_genes ( adata , * , layer = None , n_top_genes = None , min_disp = 0.5 , max_disp = None , min_mean = 0.0125 , max_mean = 3 , span = 0.3 , n_bins = 20 , flavor = 'seurat' , subset = False , inplace = True , batch_key = None , filter_unexpressed_genes = None , check_values = True , ** kwargs )
```

## Parameters

- `adata`: ( anndata.AnnData ) – Expression matrix. Expects log-normalised data except for flavor='seurat_v3' / 'seurat_v3_paper' which expect counts.
- `layer`: ( Optional [ str ] (default: None )) – Layer to use. None uses adata.X .
- `n_top_genes`: ( Optional [ int ] (default: None )) – Number of HVGs to keep. Required for flavor='seurat_v3' .
- `min_disp`: ( float (default: 0.5 )) – Dispersion / mean cutoffs for flavor='seurat' and flavor='cell_ranger' .
- `max_disp`: (default: None ) – Dispersion / mean cutoffs for flavor='seurat' and flavor='cell_ranger' .
- `min_mean`: ( float (default: 0.0125 )) – Dispersion / mean cutoffs for flavor='seurat' and flavor='cell_ranger' .
- `max_mean`: ( float (default: 3 )) – Dispersion / mean cutoffs for flavor='seurat' and flavor='cell_ranger' .
- `span`: ( float (default: 0.3 )) – Loess smoothing span for flavor='seurat_v3' .
- `n_bins`: ( int (default: 20 )) – Dispersion normalisation bins.
- `flavor`: ( str (default: 'seurat' )) – 'seurat' (default), 'cell_ranger' , 'seurat_v3' , or 'seurat_v3_paper' .
- `subset`: ( bool (default: False )) – If True, subset the AnnData to the HVGs in place.
- `inplace`: ( bool (default: True )) – Write statistics into adata.var rather than returning a DataFrame.
- `batch_key`: ( Optional [ str ] (default: None )) – If set, HVG detection is done per batch.
- `filter_unexpressed_genes`: ( Optional [ bool ] (default: None )) – Drop genes with zero total expression before selection.
- `check_values`: ( bool (default: True )) – Input validation (log-normalised vs counts).
- `**kwargs`: – Extra options forwarded to omicverse.pp._highly_variable_genes.highly_variable_genes .

## Full Documentation

# omicverse.pp.highly_variable_genes #

omicverse.pp. highly_variable_genes ( adata , * , layer = None , n_top_genes = None , min_disp = 0.5 , max_disp = None , min_mean = 0.0125 , max_mean = 3 , span = 0.3 , n_bins = 20 , flavor = 'seurat' , subset = False , inplace = True , batch_key = None , filter_unexpressed_genes = None , check_values = True , ** kwargs ) [source] #

Annotate highly variable genes (Satija 2015 / Zheng 2017 / Stuart 2019).

Parameters :

-
adata ( anndata.AnnData ) – Expression matrix. Expects log-normalised data except for `flavor='seurat_v3' `/ `'seurat_v3_paper' `which expect counts.

-
layer ( `Optional `[ `str `] (default: `None `)) – Layer to use. `None `uses `adata.X `.

-
n_top_genes ( `Optional `[ `int `] (default: `None `)) – Number of HVGs to keep. Required for `flavor='seurat_v3' `.

-
min_disp ( `float `(default: `0.5 `)) – Dispersion / mean cutoffs for `flavor='seurat' `and `flavor='cell_ranger' `.

-
max_disp (default: `None `) – Dispersion / mean cutoffs for `flavor='seurat' `and `flavor='cell_ranger' `.

-
min_mean ( `float `(default: `0.0125 `)) – Dispersion / mean cutoffs for `flavor='seurat' `and `flavor='cell_ranger' `.

-
max_mean ( `float `(default: `3 `)) – Dispersion / mean cutoffs for `flavor='seurat' `and `flavor='cell_ranger' `.

-
span ( `float `(default: `0.3 `)) – Loess smoothing span for `flavor='seurat_v3' `.

-
n_bins ( `int `(default: `20 `)) – Dispersion normalisation bins.

-
flavor ( `str `(default: `'seurat' `)) – `'seurat' `(default), `'cell_ranger' `, `'seurat_v3' `, or `'seurat_v3_paper' `.

-
subset ( `bool `(default: `False `)) – If True, subset the AnnData to the HVGs in place.

-
inplace ( `bool `(default: `True `)) – Write statistics into `adata.var `rather than returning a DataFrame.

-
batch_key ( `Optional `[ `str `] (default: `None `)) – If set, HVG detection is done per batch.

-
filter_unexpressed_genes ( `Optional `[ `bool `] (default: `None `)) – Drop genes with zero total expression before selection.

-
check_values ( `bool `(default: `True `)) – Input validation (log-normalised vs counts).

-
**kwargs – Extra options forwarded to `omicverse.pp._highly_variable_genes.highly_variable_genes `.

Returns :

Mutates `adata.var `; also returns the stats DataFrame unless `inplace=True `.

Return type :

pandas.DataFrame | None
