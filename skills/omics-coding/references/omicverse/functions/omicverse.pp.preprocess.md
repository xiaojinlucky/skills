# omicverse.pp.preprocess #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.preprocess`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.preprocess.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Preprocesses the AnnData object adata using either a scanpy or a pearson residuals workflow for size normalization and highly variable genes (HVGs) selection, and calculates signature scores if necessary.

## Signature

```text
omicverse.pp. preprocess ( adata , mode = 'shiftlog|pearson' , target_sum = 500000.0 , n_HVGs = 2000 , organism = 'human' , no_cc = False , batch_key = None , identify_robust = True , exclude_highly_expressed = None )
```

## Parameters

- `adata`: – The data matrix.
- `mode`: (default: 'shiftlog|pearson' ) – The mode for size normalization and HVGs selection.
- `'scanpy'`: ( It can be either 'scanpy' or 'pearson'. If )
- `target_sum`: Detected from function signature; no parameter description detected.
- `n_HVGs`: Detected from function signature; no parameter description detected.
- `organism`: Detected from function signature; no parameter description detected.
- `no_cc`: Detected from function signature; no parameter description detected.
- `batch_key`: Detected from function signature; no parameter description detected.
- `identify_robust`: Detected from function signature; no parameter description detected.
- `exclude_highly_expressed`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.pp.preprocess #

omicverse.pp. preprocess ( adata , mode = 'shiftlog|pearson' , target_sum = 500000.0 , n_HVGs = 2000 , organism = 'human' , no_cc = False , batch_key = None , identify_robust = True , exclude_highly_expressed = None ) [source] #

Preprocesses the AnnData object adata using either a scanpy or a pearson residuals workflow for size normalization and highly variable genes (HVGs) selection, and calculates signature scores if necessary.

Parameters :

-
adata – The data matrix.

-
mode (default: `'shiftlog|pearson' `) – The mode for size normalization and HVGs selection.

-
'scanpy' ( It can be either 'scanpy' or 'pearson'. If )

:param : :param performs size normalization using scanpy’s normalize_total() function and selects HVGs: :param using pegasus’ highly_variable_features() function with batch correction.: :param If ‘pearson’: :param selects HVGs sing scanpy’s experimental.pp.highly_variable_genes() function: :param with pearson residuals method and performs: :param size normalization using scanpy’s experimental.pp.normalize_pearson_residuals() function.: :type target_sum: default: `500000.0 `:param target_sum: The target total count after normalization. :type n_HVGs: default: `2000 `:param n_HVGs: the number of HVGs to select. :type organism: default: `'human' `:param organism: The organism of the data. It can be either ‘human’ or ‘mouse’. :type no_cc: default: `False `:param no_cc: Whether to remove cc-correlated genes from HVGs. :type identify_robust: default: `True `:param identify_robust: Whether to filter to robust genes before normalization. :type exclude_highly_expressed: default: `None `:param exclude_highly_expressed: Whether to exclude highly expressed genes

when computing the size factor in shiftlog normalization. If `None `, preserves the existing backend defaults.

Returns :

The preprocessed data matrix.

Return type :

adata
