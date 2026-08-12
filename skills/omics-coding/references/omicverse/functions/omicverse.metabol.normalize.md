# omicverse.metabol.normalize #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.normalize`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.normalize.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Normalize each sample (row) of adata.X to correct for dilution.

## Signature

```text
omicverse.metabol. normalize ( adata , * , method = 'pqn' , reference = 'median' , missing_threshold = 0.5 )
```

## Parameters

- `method`: ( Literal [ 'pqn' , 'tic' , 'median' , 'mstus' ] (default: 'pqn' )) – "pqn" (Dieterle 2006, recommended), "tic" , "median" , or "mstus" .
- `reference`: ( Literal [ 'median' , 'mean' ] (default: 'median' )) – Only used by "pqn" . The reference sample is the element-wise median (robust) or mean (noisier) of all samples. MetaboAnalyst uses median by default; we match.
- `missing_threshold`: ( float (default: 0.5 )) – Only used by "mstus" . Features missing in a higher fraction of samples are excluded from the denominator sum.
- `adata`: ( AnnData )

## Full Documentation

# omicverse.metabol.normalize #

omicverse.metabol. normalize ( adata , * , method = 'pqn' , reference = 'median' , missing_threshold = 0.5 ) [source] #

Normalize each sample (row) of `adata.X `to correct for dilution.

Parameters :

-
method ( `Literal `[ `'pqn' `, `'tic' `, `'median' `, `'mstus' `] (default: `'pqn' `)) – `"pqn" `(Dieterle 2006, recommended), `"tic" `, `"median" `, or `"mstus" `.

-
reference ( `Literal `[ `'median' `, `'mean' `] (default: `'median' `)) – Only used by `"pqn" `. The reference sample is the element-wise median (robust) or mean (noisier) of all samples. MetaboAnalyst uses median by default; we match.

-
missing_threshold ( `float `(default: `0.5 `)) – Only used by `"mstus" `. Features missing in a higher fraction of samples are excluded from the denominator sum.

-
adata ( `AnnData `)
