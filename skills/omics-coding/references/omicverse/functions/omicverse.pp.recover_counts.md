# omicverse.pp.recover_counts #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.recover_counts`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.recover_counts.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Given log-normalized gene expression data, recover the raw read/UMI counts by inferring the unknown size factors.

## Signature

```text
omicverse.pp. recover_counts ( X , mult_value , max_range , log_base = None , chunk_size = 1000 )
```

## Parameters

- `X`: – The log-normalized expression data. This data is assumed to be normalized via X := log(X/S * mult_value + 1) IMPORTANT : This function REQUIRES log-transformed data (e.g., after scanpy.pp.normalize_total() followed by scanpy.pp.log1p() ). It will NOT work correctly on linearly normalized data (e.g., data normalized to CPM/TPM without log transformation). Expected preprocessing workflow: 1. sc.pp.normalize_total(adata, target_sum=mult_value) 2. sc.pp.log1p(adata) 3. ov.pp.recover_counts(adata.X, mult_value, max_range)
- `max_range`: – Maximum size-factor search range to use in binary search.
- `mult_value`: – The multiplicative value used in the normalization. For example, for TPM this value is one million. For logT10K, this value is ten thousand.
- `log_base`: (default: None ) – The base of the logarithm (None for natural log)
- `chunk_size`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.pp.recover_counts #

omicverse.pp. recover_counts ( X , mult_value , max_range , log_base = None , chunk_size = 1000 ) [source] #

Given log-normalized gene expression data, recover the raw read/UMI counts by inferring the unknown size factors.

Parameters :

-
X –
The log-normalized expression data. This data is assumed to be normalized via X := log(X/S * mult_value + 1)

IMPORTANT : This function REQUIRES log-transformed data (e.g., after scanpy.pp.normalize_total() followed by scanpy.pp.log1p() ). It will NOT work correctly on linearly normalized data (e.g., data normalized to CPM/TPM without log transformation).

Expected preprocessing workflow: 1. sc.pp.normalize_total(adata, target_sum=mult_value) 2. sc.pp.log1p(adata) 3. ov.pp.recover_counts(adata.X, mult_value, max_range)

-
max_range – Maximum size-factor search range to use in binary search.

-
mult_value – The multiplicative value used in the normalization. For example, for TPM this value is one million. For logT10K, this value is ten thousand.

-
log_base (default: `None `) – The base of the logarithm (None for natural log)

Returns :

-
counts – The inferred counts matrix

-
size_factors – The array of inferred size-factors (i.e., total counts)

Raises :

ValueError: – If input data appears to be non-log-transformed (contains very large values that would cause numerical overflow)
