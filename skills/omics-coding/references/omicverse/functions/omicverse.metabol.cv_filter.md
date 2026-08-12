# omicverse.metabol.cv_filter #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.cv_filter`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.cv_filter.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Drop features with coefficient-of-variation above cv_threshold .

## Signature

```text
omicverse.metabol. cv_filter ( adata , * , qc_mask = None , cv_threshold = 0.3 , across = 'qc' )
```

## Parameters

- `qc_mask`: ( Union [ str , ndarray , None ] (default: None )) – Either the name of a boolean column in adata.obs (True = QC pool sample), or a boolean array of length adata.n_obs . Required when across='qc' (the default). Ignored when across='all' .
- `cv_threshold`: ( float (default: 0.3 )) – Features with std/mean > cv_threshold are dropped. Default 0.30 is the community standard for untargeted LC-MS with QC pools; for across='all' on biological samples a much higher threshold (1–2) is typical because biology itself adds variance.
- `across`: ( str (default: 'qc' )) – "qc" (default) — compute CV across QC-pool samples only (the MetaboAnalyst convention for LC-MS); requires qc_mask .
- `adata`: ( AnnData )

## Full Documentation

# omicverse.metabol.cv_filter #

omicverse.metabol. cv_filter ( adata , * , qc_mask = None , cv_threshold = 0.3 , across = 'qc' ) [source] #

Drop features with coefficient-of-variation above `cv_threshold `.

Parameters :

-
qc_mask ( `Union `[ `str `, `ndarray `, `None `] (default: `None `)) – Either the name of a boolean column in `adata.obs `(True = QC pool sample), or a boolean array of length `adata.n_obs `. Required when `across='qc' `(the default). Ignored when `across='all' `.

-
cv_threshold ( `float `(default: `0.3 `)) – Features with `std/mean > cv_threshold `are dropped. Default 0.30 is the community standard for untargeted LC-MS with QC pools; for `across='all' `on biological samples a much higher threshold (1–2) is typical because biology itself adds variance.

-
across ( `str `(default: `'qc' `)) –
-
`"qc" `(default) — compute CV across QC-pool samples only (the MetaboAnalyst convention for LC-MS); requires `qc_mask `.

-
`"all" `— compute CV across every sample. Use for NMR datasets or any workflow without pooled QC injections. MTBLS1-style studies fall in this bucket.

-
adata ( `AnnData `)

Returns :

Subset to features that passed. `adata.var['qc_cv'] `carries the CV values on the kept features.

Return type :

AnnData
