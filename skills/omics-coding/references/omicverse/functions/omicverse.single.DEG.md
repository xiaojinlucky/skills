# omicverse.single.DEG #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.DEG`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.DEG.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Differential gene-expression testing wrapper for single-cell datasets.

## Signature

```text
class omicverse.single. DEG ( adata , condition , ctrl_group , test_group , method = 'wilcoxon' , use_raw = None )
```

## Parameters

- `adata`: ( AnnData ) – Input single-cell AnnData.
- `condition`: ( str ) – Condition column in adata.obs .
- `ctrl_group`: ( str ) – Control-group label.
- `test_group`: ( str ) – Test-group label.
- `method`: ( str , default='wilcoxon' ) – DEG method name.
- `use_raw`: ( bool or None , default=None ) – Whether to use adata.raw as expression matrix.

## Full Documentation

# omicverse.single.DEG #

class omicverse.single. DEG ( adata , condition , ctrl_group , test_group , method = 'wilcoxon' , use_raw = None ) [source] #

Differential gene-expression testing wrapper for single-cell datasets.

Parameters :

-
adata ( AnnData ) – Input single-cell AnnData.

-
condition ( str ) – Condition column in `adata.obs `.

-
ctrl_group ( str ) – Control-group label.

-
test_group ( str ) – Test-group label.

-
method ( str , default='wilcoxon' ) – DEG method name.

-
use_raw ( bool or None , default=None ) – Whether to use `adata.raw `as expression matrix.

__init__ ( adata , condition , ctrl_group , test_group , method = 'wilcoxon' , use_raw = None ) [source] #

Initialize differential expression analysis.

Parameters :

-
adata ( AnnData ) – Single-cell AnnData object.

-
condition ( str ) – Obs column containing condition labels.

-
ctrl_group ( str ) – Control condition label.

-
test_group ( str ) – Test condition label.

-
method ( str , default='wilcoxon' ) – DEG method: `'wilcoxon' `, `'t-test' `, or `'memento-de' `.

-
use_raw ( bool or None , default=None ) – Whether to use `adata.raw `as expression matrix. If `None `, auto-detects based on availability.

Return type :

None

Methods

`__init__ `(adata, condition, ctrl_group, ...)

Initialize differential expression analysis.

`get_results `()

Get DEG result table.

`run `(celltype_key[, celltype_group, max_cells])

Run differential expression testing.
