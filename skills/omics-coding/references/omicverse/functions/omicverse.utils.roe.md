# omicverse.utils.roe #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.roe`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.roe.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Compute the Ro/e (observed/expected) cell-type enrichment matrix.

## Signature

```text
omicverse.utils. roe ( adata , sample_key , cell_type_key , pval_threshold = 0.05 , expected_value_threshold = 5 , order = None )
```

## Parameters

- `adata`: ( AnnData ) – Object with sample and cell-type annotations in .obs .
- `sample_key`: ( str ) – adata.obs column with the sample / tissue / condition labels (these become the Ro/e columns).
- `cell_type_key`: ( str ) – adata.obs column with the cell-type / cluster labels (these become the Ro/e rows).
- `pval_threshold`: ( float , default=0.05 ) – Significance level for the global χ² test of cluster–sample independence. Recorded as a QC flag; it does not gate the returned matrix.
- `expected_value_threshold`: ( float , default=5 ) – Minimum expected count below which the χ² approximation is considered unreliable. For a 2×2 table the global p-value then falls back to Fisher’s exact test; for larger tables a warning is emitted.
- `order`: ( list of str or None , default=None ) – Explicit column (sample) order. A comma-separated string is also accepted for backwards compatibility. None keeps the natural order. (The legacy sentinel 'F' is still accepted = None .)

## Full Documentation

# omicverse.utils.roe #

omicverse.utils. roe ( adata , sample_key , cell_type_key , pval_threshold = 0.05 , expected_value_threshold = 5 , order = None ) [source] #

Compute the Ro/e (observed/expected) cell-type enrichment matrix.

Parameters :

-
adata ( AnnData ) – Object with sample and cell-type annotations in `.obs `.

-
sample_key ( str ) – `adata.obs `column with the sample / tissue / condition labels (these become the Ro/e columns).

-
cell_type_key ( str ) – `adata.obs `column with the cell-type / cluster labels (these become the Ro/e rows).

-
pval_threshold ( float , default=0.05 ) – Significance level for the global χ² test of cluster–sample independence. Recorded as a QC flag; it does not gate the returned matrix.

-
expected_value_threshold ( float , default=5 ) – Minimum expected count below which the χ² approximation is considered unreliable. For a 2×2 table the global p-value then falls back to Fisher’s exact test; for larger tables a warning is emitted.

-
order ( list of str or None , default=None ) – Explicit column (sample) order. A comma-separated string is also accepted for backwards compatibility. `None `keeps the natural order. (The legacy sentinel `'F' `is still accepted = `None `.)

Returns :

Ro/e matrix, cell types (rows) × samples (columns). Also stored, together with the observed / expected tables and the χ² result, in `adata.uns['roe'] `; `adata.uns['roe_results'] `and `adata.uns['expected_values'] `are kept for backwards compatibility.

Return type :

pandas.DataFrame
