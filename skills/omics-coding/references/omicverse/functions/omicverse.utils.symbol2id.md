# omicverse.utils.symbol2id #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.symbol2id`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.symbol2id.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Convert gene symbols in adata.var_names to Ensembl gene IDs.

## Signature

```text
omicverse.utils. symbol2id ( adata , species = None , ensembl_release = None , force_rebuild = False , multi = 'first' , subset = False )
```

## Parameters

- `adata`: ( AnnData ) – Input AnnData object whose var_names are official gene symbols.
- `species`: ( str or None , optional ) – Target species. Supported values: 'human' , 'mouse' , 'rat' , 'zebrafish' , 'fly' , 'chicken' , 'dog' , 'pig' , 'cow' , 'macaque' . Defaults to 'human' .
- `ensembl_release`: ( int or None , optional ) – Ensembl release number. Defaults to 77 when None .
- `force_rebuild`: ( bool , optional ) – Force re-download and re-index the local database. Default is False .
- `multi`: ( {'first' , 'all' , 'join'} , optional ) – Strategy when a symbol maps to multiple Ensembl IDs: 'first' — use only the first ID (default).
- `subset`: ( bool , optional ) – If True , drop genes that could not be converted. If False (default), unconverted genes keep their original symbol as the index.

## Full Documentation

# omicverse.utils.symbol2id #

omicverse.utils. symbol2id ( adata , species = None , ensembl_release = None , force_rebuild = False , multi = 'first' , subset = False ) [source] #

Convert gene symbols in `adata.var_names `to Ensembl gene IDs.

Parameters :

-
adata ( AnnData ) – Input AnnData object whose `var_names `are official gene symbols.

-
species ( str or None , optional ) – Target species. Supported values: `'human' `, `'mouse' `, `'rat' `, `'zebrafish' `, `'fly' `, `'chicken' `, `'dog' `, `'pig' `, `'cow' `, `'macaque' `. Defaults to `'human' `.

-
ensembl_release ( int or None , optional ) – Ensembl release number. Defaults to `77 `when `None `.

-
force_rebuild ( bool , optional ) – Force re-download and re-index the local database. Default is `False `.

-
multi ( {'first' , 'all' , 'join'} , optional ) –
Strategy when a symbol maps to multiple Ensembl IDs:

-
`'first' `— use only the first ID (default).

-
`'all' `— store a list of all IDs in `adata.var['gene_id'] `.

-
`'join' `— store all IDs joined by `'|' `.

-
subset ( bool , optional ) – If `True `, drop genes that could not be converted. If `False `(default), unconverted genes keep their original symbol as the index.

Returns :

Updated AnnData with `var_names `replaced by Ensembl gene IDs. Original symbols are preserved in `adata.var['symbol'] `.

Return type :

AnnData

Examples

```text
>>> adata = ov.utils.symbol2id(adata, species='human')
>>> adata = ov.utils.symbol2id(adata, species='mouse', subset=True)

```
