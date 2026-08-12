# omicverse.metabol.serrf #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.serrf`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.serrf.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

SERRF — QC-based Random Forest drift correction (Fan 2019).

## Signature

```text
omicverse.metabol. serrf ( adata , * , qc_col , qc_label = 'QC' , batch_col = None , top_k = 10 , n_estimators = 100 , min_qc_samples = 5 , layer = None , seed = 0 )
```

## Parameters

- `qc_col`: ( str ) – Column in adata.obs that tags QC vs real samples.
- `qc_label`: ( str (default: 'QC' )) – Value in qc_col marking QC rows. Default "QC" .
- `batch_col`: ( Optional [ str ] (default: None )) – Optional column in adata.obs for per-batch correction. Without a batch column the full run is treated as one batch.
- `top_k`: ( int (default: 10 )) – Number of co-features to use as RF predictors. Fan 2019 uses 10; larger values add runtime and marginal accuracy.
- `n_estimators`: ( int (default: 100 )) – RF tree count. Default 100 (the Fan R package uses 500 but 100 is within 1% AUC on benchmarks at 5× the speed).
- `min_qc_samples`: ( int (default: 5 )) – If a batch has fewer QC samples than this, correction is skipped for that batch (features left as raw). Default 5.
- `layer`: ( Optional [ str ] (default: None )) – Which adata.layers entry to correct. None → use adata.X .
- `seed`: ( int (default: 0 )) – RandomForest seed.
- `adata`: ( AnnData )

## Full Documentation

# omicverse.metabol.serrf #

omicverse.metabol. serrf ( adata , * , qc_col , qc_label = 'QC' , batch_col = None , top_k = 10 , n_estimators = 100 , min_qc_samples = 5 , layer = None , seed = 0 ) [source] #

SERRF — QC-based Random Forest drift correction (Fan 2019).

For each feature and batch:

-
Rank other features by absolute correlation with the target feature across QC samples only .

-
Fit `RandomForestRegressor `with the target as response and the top- `top_k `correlated features as predictors, trained on QC injections only.

-
Predict the target abundance for every sample in the batch from its co-feature vector.

-
Corrected value = `raw / predicted * mean(QC_raw) `.

The ratio scales each sample onto the QC baseline; features whose QC mean is zero or negative, or whose predictions collapse, are left uncorrected.

Parameters :

-
qc_col ( `str `) – Column in `adata.obs `that tags QC vs real samples.

-
qc_label ( `str `(default: `'QC' `)) – Value in `qc_col `marking QC rows. Default `"QC" `.

-
batch_col ( `Optional `[ `str `] (default: `None `)) – Optional column in `adata.obs `for per-batch correction. Without a batch column the full run is treated as one batch.

-
top_k ( `int `(default: `10 `)) – Number of co-features to use as RF predictors. Fan 2019 uses 10; larger values add runtime and marginal accuracy.

-
n_estimators ( `int `(default: `100 `)) – RF tree count. Default 100 (the Fan R package uses 500 but 100 is within 1% AUC on benchmarks at 5× the speed).

-
min_qc_samples ( `int `(default: `5 `)) – If a batch has fewer QC samples than this, correction is skipped for that batch (features left as raw). Default 5.

-
layer ( `Optional `[ `str `] (default: `None `)) – Which `adata.layers `entry to correct. `None `→ use `adata.X `.

-
seed ( `int `(default: `0 `)) – RandomForest seed.

-
adata ( `AnnData `)

Returns :

New AnnData with corrected `.X `. The original matrix is preserved in `out.layers['raw'] `. Per-feature CV% before / after is stored in `out.var['cv_qc_raw'] `/ `cv_qc_serrf''] `to help users audit improvement.

Return type :

AnnData
