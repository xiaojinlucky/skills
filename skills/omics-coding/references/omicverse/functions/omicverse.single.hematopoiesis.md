# omicverse.single.hematopoiesis #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.hematopoiesis`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.hematopoiesis.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Load scRNA-seq hematopoiesis dataset for trajectory inference.

## Signature

```text
omicverse.single. hematopoiesis ( )
```

## Parameters

No parameters detected.

## Full Documentation

# omicverse.single.hematopoiesis #

omicverse.single. hematopoiesis ( ) [source] #

Load scRNA-seq hematopoiesis dataset for trajectory inference.

Returns :

Preprocessed hematopoiesis dataset with embeddings and annotations.

Return type :

AnnData

Examples

```text
>>> import omicverse as ov
>>> adata = ov.single.scRNA_hematopoiesis()
>>> print(adata.shape)

```
