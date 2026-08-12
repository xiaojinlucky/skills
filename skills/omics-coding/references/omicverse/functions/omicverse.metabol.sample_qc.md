# omicverse.metabol.sample_qc #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.sample_qc`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.sample_qc.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Hotelling T-squared + DModX sample-level outlier detection.

## Signature

```text
omicverse.metabol. sample_qc ( adata , * , n_components = 2 , alpha = 0.95 , center = True , scale = True , layer = None )
```

## Parameters

- `n_components`: ( int (default: 2 )) – Number of PCs to retain. Default 2 — enough for a 2-D score plot, too few for detecting outliers in high-dimensional data. Try 3–5 for real studies.
- `alpha`: ( float (default: 0.95 )) – Significance level for flagging. Default 0.95.
- `center`: ( bool (default: True )) – Pre-processing. Default: mean-centre + scale to unit variance (matches SIMCA / MetaboAnalyst convention).
- `scale`: ( bool (default: True )) – Pre-processing. Default: mean-centre + scale to unit variance (matches SIMCA / MetaboAnalyst convention).
- `layer`: ( Optional [ str ] (default: None )) – AnnData layer (default None → adata.X ).
- `adata`: ( AnnData )

## Full Documentation

# omicverse.metabol.sample_qc #

omicverse.metabol. sample_qc ( adata , * , n_components = 2 , alpha = 0.95 , center = True , scale = True , layer = None ) [source] #

Hotelling T-squared + DModX sample-level outlier detection.

Fits PCA on `adata.X `(after mean-centre + unit-variance scale by default) and returns per-sample diagnostics.

-
Hotelling T-squared `= Σ (t_a / s_a)^2 `— quadratic-form distance from the sample to the model origin inside the PC subspace. Critical value at level `alpha `is the `(1-alpha) `-quantile of a scaled F distribution (Hotelling 1947); flagged samples are deep within the model space.

-
DModX `= sqrt(||residual||² / (p - A)) `— standardised distance from the sample to the residual subspace. Flagged samples are outside the model space. DModX critical value is based on an F approximation (Eriksson 2013, Ch. 7).

A sample flagged by either metric should be inspected before downstream stats — T-squared catches unusual profiles that still “look like” the training set; DModX catches novel profiles that don’t fit the PCA subspace at all.

Parameters :

-
n_components ( `int `(default: `2 `)) – Number of PCs to retain. Default 2 — enough for a 2-D score plot, too few for detecting outliers in high-dimensional data. Try 3–5 for real studies.

-
alpha ( `float `(default: `0.95 `)) – Significance level for flagging. Default 0.95.

-
center ( `bool `(default: `True `)) – Pre-processing. Default: mean-centre + scale to unit variance (matches SIMCA / MetaboAnalyst convention).

-
scale ( `bool `(default: `True `)) – Pre-processing. Default: mean-centre + scale to unit variance (matches SIMCA / MetaboAnalyst convention).

-
layer ( `Optional `[ `str `] (default: `None `)) – AnnData layer (default `None `→ `adata.X `).

-
adata ( `AnnData `)

Returns :

Indexed by sample name, columns: `T2 `(Hotelling T-squared), `DModX `, `T2_crit `/ `DModX_crit `(critical values at `alpha `), `T2_flag `/ `DModX_flag `(bools), `is_outlier `(flagged by either).

Also attaches `attrs['variance_explained'] `(array of length `n_components `) and `attrs['n_components'] `.

Return type :

pd.DataFrame
