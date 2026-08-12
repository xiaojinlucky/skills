# omicverse.pp.highly_variable_features #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.highly_variable_features`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.highly_variable_features.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Select highly variable features (HVF/HVG) for downstream modeling.

## Signature

```text
omicverse.pp. highly_variable_features ( data , batch = None , flavor = 'pegasus' , n_top = 2000 , span = 0.02 , min_disp = 0.5 , max_disp = inf , min_mean = 0.0125 , max_mean = 7 , n_jobs = -1 )
```

## Parameters

- `data`: ( anndata.AnnData ) – AnnData matrix with genes in columns.
- `batch`: ( str , optional ) – Column name in data.obs for batch-aware HVF selection.
- `flavor`: ( {"pegasus" , "Seurat"} , default="pegasus" ) – Algorithm used to rank variable genes.
- `n_top`: ( int , default=2000 ) – Number of top genes to keep.
- `span`: ( float , default=0.02 ) – Loess span used by Pegasus flavor.
- `min_disp`: ( float , default=0.5 ) – Lower bound of normalized dispersion for Seurat flavor.
- `max_disp`: ( float , default=np.inf ) – Upper bound of normalized dispersion for Seurat flavor.
- `min_mean`: ( float , default=0.0125 ) – Lower bound of mean expression for Seurat flavor.
- `max_mean`: ( float , default=7 ) – Upper bound of mean expression for Seurat flavor.
- `n_jobs`: ( int , default=-1 ) – Number of worker threads for computations where applicable.

## Full Documentation

# omicverse.pp.highly_variable_features #

omicverse.pp. highly_variable_features ( data , batch = None , flavor = 'pegasus' , n_top = 2000 , span = 0.02 , min_disp = 0.5 , max_disp = inf , min_mean = 0.0125 , max_mean = 7 , n_jobs = -1 ) [source] #

Select highly variable features (HVF/HVG) for downstream modeling.

Parameters :

-
data ( anndata.AnnData ) – AnnData matrix with genes in columns.

-
batch ( str , optional ) – Column name in `data.obs `for batch-aware HVF selection.

-
flavor ( {"pegasus" , "Seurat"} , default="pegasus" ) – Algorithm used to rank variable genes.

-
n_top ( int , default=2000 ) – Number of top genes to keep.

-
span ( float , default=0.02 ) – Loess span used by Pegasus flavor.

-
min_disp ( float , default=0.5 ) – Lower bound of normalized dispersion for Seurat flavor.

-
max_disp ( float , default=np.inf ) – Upper bound of normalized dispersion for Seurat flavor.

-
min_mean ( float , default=0.0125 ) – Lower bound of mean expression for Seurat flavor.

-
max_mean ( float , default=7 ) – Upper bound of mean expression for Seurat flavor.

-
n_jobs ( int , default=-1 ) – Number of worker threads for computations where applicable.

Returns :

Updates `data.var['highly_variable_features'] `and ranking fields.

Return type :

None
