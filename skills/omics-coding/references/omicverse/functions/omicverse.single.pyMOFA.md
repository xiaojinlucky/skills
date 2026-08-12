# omicverse.single.pyMOFA #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.pyMOFA`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.pyMOFA.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Train MOFA models for latent factor discovery across multiple omics layers.

## Signature

```text
class omicverse.single. pyMOFA ( omics , omics_name )
```

## Parameters

- `omics`: ( list ) – List of omics data matrices (for example RNA/ATAC/proteomics).
- `omics_name`: ( list ) – Names corresponding to each entry in omics .

## Full Documentation

# omicverse.single.pyMOFA #

class omicverse.single. pyMOFA ( omics , omics_name ) [source] #

Train MOFA models for latent factor discovery across multiple omics layers.

Parameters :

-
omics ( list ) – List of omics data matrices (for example RNA/ATAC/proteomics).

-
omics_name ( list ) – Names corresponding to each entry in `omics `.

Returns :

Initializes MOFA training inputs and metadata.

Return type :

None

Examples

```text
>>> test_mofa = ov.single.pyMOFA(omics=[rna, atac], omics_name=["rna","atac"])

```

__init__ ( omics , omics_name ) [source] #

Initialize a multi-view MOFA training container.

Parameters :

-
omics ( list ) – List of input omics objects, typically `AnnData `matrices for each modality (for example RNA, ATAC, protein).

-
omics_name ( list ) – View names aligned with `omics `order. These names are used in the exported MOFA model and downstream interpretation.

Methods

`__init__ `(omics, omics_name)

Initialize a multi-view MOFA training container.

`mofa_preprocess `()

Convert input omics objects into MOFA-ready dense matrices.

`mofa_run `([outfile, factors, iter, ...])

Train and save a MOFA model using current multi-omics inputs.
