# omicverse.io.read #

- Package: omicverse
- Language: Python
- Function: `omicverse.io.read`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.io.read.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read common omics file formats into AnnData or pandas DataFrame.

## Signature

```text
omicverse.io. read ( path , backend = 'python' , ** kwargs )
```

## Parameters

- `path`: ( str or pathlib.Path ) – Input file path.
- `backend`: ( {'python' , 'rust'} , default='python' ) – Backend used for .h5ad reading. 'rust' loads out-of-memory via anndataoom / anndata-rs . When the file’s sparse X has unsorted minor indices the call is aborted with a clear ValueError (rather than an anndata-rs panic) pointing at ov.utils.convert_adata_for_rust() for recovery.
- `**kwargs`: – Additional keyword arguments forwarded to backend readers.

## Full Documentation

# omicverse.io.read #

omicverse.io. read ( path , backend = 'python' , ** kwargs ) [source] #

Read common omics file formats into AnnData or pandas DataFrame.

Parameters :

-
path ( str or pathlib.Path ) – Input file path.

-
backend ( {'python' , 'rust'} , default='python' ) – Backend used for `.h5ad `reading. `'rust' `loads out-of-memory via `anndataoom `/ `anndata-rs `. When the file’s sparse X has unsorted minor indices the call is aborted with a clear `ValueError `(rather than an anndata-rs panic) pointing at `ov.utils.convert_adata_for_rust() `for recovery.

-
**kwargs – Additional keyword arguments forwarded to backend readers.

Returns :

Loaded AnnData object (for `.h5ad `) or DataFrame (for table files).

Return type :

anndata.AnnData or pandas.DataFrame

Raises :

-
ImportError – If `backend='rust' `is requested but `anndataoom `is not installed.

-
ValueError – If `backend `is invalid for `.h5ad `reading, the file suffix is unsupported, or the `.h5ad `has an unsorted sparse `X `.
