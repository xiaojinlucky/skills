# omicverse.metabol.impute #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.impute`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.impute.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Impute missing values (NaN / 0) in adata.X .

## Signature

```text
omicverse.metabol. impute ( adata , * , method = 'qrilc' , missing_threshold = 0.5 , n_neighbors = 5 , q = 0.01 , seed = 0 )
```

## Parameters

- `method`: ( Literal [ 'knn' , 'half_min' , 'qrilc' , 'zero' ] (default: 'qrilc' )) – "knn" — per-feature kNN on the sample × sample Euclidean distance restricted to non-missing positions
- `missing_threshold`: ( float (default: 0.5 )) – Before imputation, drop features whose missingness exceeds this fraction. Default 0.5 (drop a feature missing in >50% of samples).
- `n_neighbors`: ( int (default: 5 )) – kNN neighborhood size (only used when method='knn' ).
- `q`: ( float (default: 0.01 )) – Quantile defining the “below-detection-limit” band for QRILC.
- `seed`: ( int (default: 0 )) – RNG seed for the QRILC truncated-normal draws. Default 0 — pass a different integer to bootstrap or change the imputation realization across pipeline runs.
- `adata`: ( AnnData )

## Full Documentation

# omicverse.metabol.impute #

omicverse.metabol. impute ( adata , * , method = 'qrilc' , missing_threshold = 0.5 , n_neighbors = 5 , q = 0.01 , seed = 0 ) [source] #

Impute missing values (NaN / 0) in `adata.X `.

Parameters :

-
method ( `Literal `[ `'knn' `, `'half_min' `, `'qrilc' `, `'zero' `] (default: `'qrilc' `)) –
-
`"knn" `— per-feature kNN on the sample × sample Euclidean distance restricted to non-missing positions

-
`"half_min" `— replace missing with half the minimum non-missing value of that feature (classic MNAR-friendly default)

-
`"qrilc" `— Quantile Regression Imputation of Left-Censored: draws from `TruncatedNormal(mean=mu_below_q, sd=sigma) `where mu and sigma are estimated from values below the `q `-quantile

-
`"zero" `— replace missing with 0 (for downstream methods that treat 0 as a valid observation)

-
missing_threshold ( `float `(default: `0.5 `)) – Before imputation, drop features whose missingness exceeds this fraction. Default 0.5 (drop a feature missing in >50% of samples).

-
n_neighbors ( `int `(default: `5 `)) – kNN neighborhood size (only used when `method='knn' `).

-
q ( `float `(default: `0.01 `)) – Quantile defining the “below-detection-limit” band for QRILC.

-
seed ( `int `(default: `0 `)) – RNG seed for the QRILC truncated-normal draws. Default 0 — pass a different integer to bootstrap or change the imputation realization across pipeline runs.

-
adata ( `AnnData `)

Returns :

New object with imputed `.X `and a `var['missing_frac'] `column recording the pre-imputation missingness of each feature.

Return type :

AnnData
