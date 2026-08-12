# omicverse.metabol.pyMetabo #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.pyMetabo`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.pyMetabo.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Lifecycle class for a metabolomics analysis.

## Signature

```text
class omicverse.metabol. pyMetabo ( adata , random_state = 0 )
```

## Parameters

- `adata`: ( AnnData )
- `random_state`: ( int (default: 0 ))

## Full Documentation

# omicverse.metabol.pyMetabo #

class omicverse.metabol. pyMetabo ( adata , random_state = 0 ) [source] #

Lifecycle class for a metabolomics analysis.

## Attributes populated as the pipeline runs #

adata : the current state of the AnnData (updated in place on each call) raw : the original AnnData handed in at construction (never mutated) deg_table : DataFrame returned by `differential() `plsda_result : PLSDAResult from `plsda() `/ `opls_da() `

param adata :

type adata :

`AnnData `

param random_state :

type random_state :

`int `(default: `0 `)

__init__ ( adata , random_state = 0 ) #

Parameters :

-
adata ( `AnnData `)

-
random_state ( `int `(default: `0 `))

Methods

`__init__ `(adata[, random_state])

`blank_filter `(*, blank_mask[, ratio])

Drop features whose mean signal isn't `` ratio``× the blank mean.

`cv_filter `(*, qc_mask[, cv_threshold])

Drop features with QC coefficient-of-variation above `cv_threshold `.

`differential `(*[, group_col, group_a, ...])

Two-group univariate test across all metabolites; stores `self.deg_table `.

`drift_correct `(*, injection_order, qc_mask[, ...])

Correct injection-order drift via LOESS regression on QC samples.

`impute `(*[, method, seed])

Impute missing values in `adata.X `and return `self `.

`normalize `(*[, method])

Normalize each sample row to correct dilution and return `self `.

`opls_da `(*[, n_ortho, group_col, group_a, ...])

Fit OPLS-DA (one predictive + `n_ortho `orthogonal components).

`plsda `(*[, n_components, group_col, group_a, ...])

Fit PLS-DA and stash the result on `self.plsda_result `.

`significant_metabolites `(*[, padj_thresh, ...])

Filter `self.deg_table `to padj < `padj_thresh `and |log2fc| ≥ `log2fc_thresh `.

`transform `(*[, method])

Apply a feature-level transformation and return `self `.

`vip_table `()

Return VIP scores per metabolite — requires a prior PLS-DA / OPLS-DA fit.

Attributes

`deg_table `

`plsda_result `

`random_state `

`adata `

`raw `
