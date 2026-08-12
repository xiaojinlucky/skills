# omicverse.metabol.drift_correct #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.drift_correct`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.drift_correct.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Correct systematic signal drift using LOESS regression on QC samples.

## Signature

```text
omicverse.metabol. drift_correct ( adata , * , injection_order , qc_mask , frac = 0.5 )
```

## Parameters

- `injection_order`: ( str | ndarray ) – Name of a numeric column in adata.obs (or a 1-D array) that gives the run order of each sample.
- `qc_mask`: ( str | ndarray ) – Bool column/array marking QC pool samples.
- `frac`: ( float (default: 0.5 )) – LOESS smoothing fraction ( statsmodels.lowess frac argument). 0.5 is robust for runs of <500 samples; tighten to 0.3 for larger runs.
- `adata`: ( AnnData )

## Full Documentation

# omicverse.metabol.drift_correct #

omicverse.metabol. drift_correct ( adata , * , injection_order , qc_mask , frac = 0.5 ) [source] #

Correct systematic signal drift using LOESS regression on QC samples.

Fits `log1p(intensity) ~ injection_order `per feature on QC samples only, then divides the raw intensities in both QC and real samples by the fitted drift curve.

Parameters :

-
injection_order ( `str `| `ndarray `) – Name of a numeric column in `adata.obs `(or a 1-D array) that gives the run order of each sample.

-
qc_mask ( `str `| `ndarray `) – Bool column/array marking QC pool samples.

-
frac ( `float `(default: `0.5 `)) – LOESS smoothing fraction ( `statsmodels.lowess ` `frac `argument). 0.5 is robust for runs of <500 samples; tighten to 0.3 for larger runs.

-
adata ( `AnnData `)

Returns :

Intensity matrix corrected in place on a copy; `uns['qc_drift'] `records the per-feature LOESS fit for reproducibility.

Return type :

AnnData
