# omicverse.io.read_10x_mtx #

- Package: omicverse
- Language: Python
- Function: `omicverse.io.read_10x_mtx`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.io.read_10x_mtx.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read a 10x Genomics Matrix Market directory.

## Signature

```text
omicverse.io. read_10x_mtx ( path , * , var_names = 'gene_symbols' , make_unique = True , gex_only = True , prefix = None , compressed = True )
```

## Parameters

- `path`: ( str or pathlib.Path ) – Directory containing matrix.mtx and matching feature/barcode files.
- `var_names`: ( {'gene_symbols' , 'gene_ids'} , default='gene_symbols' ) – Which feature column should be used as adata.var_names .
- `make_unique`: ( bool , default=True ) – Whether to enforce unique var_names when using gene symbols.
- `gex_only`: ( bool , default=True ) – If True , keep only features labeled as Gene Expression (v3+ format).
- `prefix`: ( str or None , default=None ) – Optional filename prefix before matrix.mtx , features.tsv , and barcodes.tsv .
- `compressed`: ( bool , default=True ) – Whether v3+ files are expected to be gzip-compressed ( .gz ). Set False for plain-text exports such as some STARsolo outputs.

## Full Documentation

# omicverse.io.read_10x_mtx #

omicverse.io. read_10x_mtx ( path , * , var_names = 'gene_symbols' , make_unique = True , gex_only = True , prefix = None , compressed = True ) [source] #

Read a 10x Genomics Matrix Market directory.

Parameters :

-
path ( str or pathlib.Path ) – Directory containing `matrix.mtx `and matching feature/barcode files.

-
var_names ( {'gene_symbols' , 'gene_ids'} , default='gene_symbols' ) – Which feature column should be used as `adata.var_names `.

-
make_unique ( bool , default=True ) – Whether to enforce unique `var_names `when using gene symbols.

-
gex_only ( bool , default=True ) – If `True `, keep only features labeled as `Gene Expression `(v3+ format).

-
prefix ( str or None , default=None ) – Optional filename prefix before `matrix.mtx `, `features.tsv `, and `barcodes.tsv `.

-
compressed ( bool , default=True ) – Whether v3+ files are expected to be gzip-compressed ( `.gz `). Set `False `for plain-text exports such as some STARsolo outputs.

Returns :

Loaded expression matrix with barcodes and feature annotations.

Return type :

anndata.AnnData
