# omicverse.utils.convert2symbol #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.convert2symbol`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.convert2symbol.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Convert Ensembl IDs in adata.var_names to official gene symbols.

## Signature

```text
omicverse.utils. convert2symbol ( adata , scopes = None , subset = True )
```

## Parameters

- `adata`: ( AnnData ) – Input AnnData object whose var_names contain Ensembl gene or transcript IDs (e.g. ENSG* , ENSMUSG* , ENST* ).
- `scopes`: ( str , iterable , or None , optional ) – Identifier type passed to convert2gene_symbol() . Common values are 'ensembl.gene' and 'ensembl.transcript' . If None , the scope is inferred from the first entry of adata.var_names : ENSG* / ENSMUSG* → 'ensembl.gene'
- `subset`: ( bool , optional ) – If True (default), genes that could not be converted are dropped from adata . If False , unconverted genes retain their original Ensembl ID.

## Full Documentation

# omicverse.utils.convert2symbol #

omicverse.utils. convert2symbol ( adata , scopes = None , subset = True ) [source] #

Convert Ensembl IDs in `adata.var_names `to official gene symbols.

Parameters :

-
adata ( AnnData ) – Input AnnData object whose `var_names `contain Ensembl gene or transcript IDs (e.g. `ENSG* `, `ENSMUSG* `, `ENST* `).

-
scopes ( str , iterable , or None , optional ) –
Identifier type passed to `convert2gene_symbol() `. Common values are `'ensembl.gene' `and `'ensembl.transcript' `. If `None `, the scope is inferred from the first entry of `adata.var_names `:

-
`ENSG* `/ `ENSMUSG* `→ `'ensembl.gene' `

-
`ENST* `/ `ENSMUST* `→ `'ensembl.transcript' `

-
subset ( bool , optional ) – If `True `(default), genes that could not be converted are dropped from `adata `. If `False `, unconverted genes retain their original Ensembl ID.

Returns :

Updated AnnData with `var_names `replaced by official gene symbols. The original Ensembl IDs are preserved in `adata.var['query'] `.

Return type :

AnnData

Raises :

Exception – If `scopes `is `None `and the gene IDs cannot be recognised as `ensembl.gene `or `ensembl.transcript `.

Examples

```text
>>> adata = ov.utils.convert2symbol(adata)
>>> adata = ov.utils.convert2symbol(adata, subset=False)

```
