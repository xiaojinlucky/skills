# omicverse.single.cytotrace2 #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.cytotrace2`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.cytotrace2.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Predict developmental potency with CytoTRACE2.

## Signature

```text
omicverse.single. cytotrace2 ( adata , use_model_dir , species = 'mouse' , batch_size = 10000 , smooth_batch_size = 1000 , disable_parallelization = False , max_cores = None , max_pcs = 200 , seed = 14 , output_dir = 'cytotrace2_results' )
```

## Parameters

- `adata`: ( anndata.AnnData ) – Single-cell expression object. Uses adata.X as the expression matrix.
- `use_model_dir`: ( str ) – Directory containing CytoTRACE2 pretrained model weights.
- `species`: ( str , default='mouse' ) – Species label used by gene preprocessing. Supported values are typically 'mouse' and 'human' .
- `batch_size`: ( int , default=10000 ) – Number of cells per prediction batch.
- `smooth_batch_size`: ( int , default=1000 ) – Number of cells per smoothing batch in diffusion/KNN post-processing.
- `disable_parallelization`: ( bool , default=False ) – Whether to disable multiprocessing.
- `max_cores`: ( int or None , default=None ) – Maximum cores used when parallelization is enabled. None lets the function infer an available value.
- `max_pcs`: ( int , default=200 ) – Number of principal components used in KNN smoothing.
- `seed`: ( int , default=14 ) – Random seed used for chunking and stochastic operations.
- `output_dir`: ( str , default='cytotrace2_results' ) – Directory for intermediate files and final result table.

## Full Documentation

# omicverse.single.cytotrace2 #

omicverse.single. cytotrace2 ( adata , use_model_dir , species = 'mouse' , batch_size = 10000 , smooth_batch_size = 1000 , disable_parallelization = False , max_cores = None , max_pcs = 200 , seed = 14 , output_dir = 'cytotrace2_results' ) [source] #

Predict developmental potency with CytoTRACE2.

Parameters :

-
adata ( anndata.AnnData ) – Single-cell expression object. Uses `adata.X `as the expression matrix.

-
use_model_dir ( str ) – Directory containing CytoTRACE2 pretrained model weights.

-
species ( str , default='mouse' ) – Species label used by gene preprocessing. Supported values are typically `'mouse' `and `'human' `.

-
batch_size ( int , default=10000 ) – Number of cells per prediction batch.

-
smooth_batch_size ( int , default=1000 ) – Number of cells per smoothing batch in diffusion/KNN post-processing.

-
disable_parallelization ( bool , default=False ) – Whether to disable multiprocessing.

-
max_cores ( int or None , default=None ) – Maximum cores used when parallelization is enabled. `None `lets the function infer an available value.

-
max_pcs ( int , default=200 ) – Number of principal components used in KNN smoothing.

-
seed ( int , default=14 ) – Random seed used for chunking and stochastic operations.

-
output_dir ( str , default='cytotrace2_results' ) – Directory for intermediate files and final result table.

Returns :

CytoTRACE2 result table indexed by cell ID, including `CytoTRACE2_Score `, potency category, and relative rank score.

Return type :

pandas.DataFrame

Notes

This function also writes prediction columns into `adata.obs `.
