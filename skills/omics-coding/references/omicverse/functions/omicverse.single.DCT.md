# omicverse.single.DCT #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.DCT`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.DCT.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Differential cell-type abundance testing wrapper.

## Signature

```text
class omicverse.single. DCT ( adata , condition , ctrl_group , test_group , cell_type_key , method = 'sccoda' , sample_key = None , use_rep = None )
```

## Parameters

- `adata`: ( AnnData ) – Input single-cell AnnData.
- `condition`: ( str ) – Condition column in adata.obs .
- `ctrl_group`: ( str ) – Control-group label.
- `test_group`: ( str ) – Test-group label.
- `cell_type_key`: ( str ) – Cell-type annotation column.
- `method`: ( str , default='sccoda' ) – Differential-abundance backend.
- `sample_key`: Detected from function signature; no parameter description detected.
- `use_rep`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.single.DCT #

class omicverse.single. DCT ( adata , condition , ctrl_group , test_group , cell_type_key , method = 'sccoda' , sample_key = None , use_rep = None ) [source] #

Differential cell-type abundance testing wrapper.

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
cell_type_key ( str ) – Cell-type annotation column.

-
method ( str , default='sccoda' ) – Differential-abundance backend.

__init__ ( adata , condition , ctrl_group , test_group , cell_type_key , method = 'sccoda' , sample_key = None , use_rep = None ) [source] #

Initialize differential cell-type abundance analysis.

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
cell_type_key ( str ) – Obs column containing cell-type annotations.

-
method ( str , default='sccoda' ) – Differential abundance method: `'sccoda' `, `'milo' `, or `'milopy' `.

-
sample_key ( str or None , default=None ) – Obs column containing sample IDs (required for Milo methods).

-
use_rep ( str or None , default=None ) – Embedding key in `adata.obsm `used for neighborhood graph in Milo.

Return type :

None

Methods

`__init__ `(adata, condition, ctrl_group, ...)

Initialize differential cell-type abundance analysis.

`get_results `([mix_threshold])

Retrieve differential abundance results.

`run `(**kwargs)

Run differential abundance testing.
