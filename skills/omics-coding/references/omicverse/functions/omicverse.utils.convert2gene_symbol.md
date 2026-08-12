# omicverse.utils.convert2gene_symbol #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.convert2gene_symbol`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.convert2gene_symbol.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Convert Ensembl gene IDs to official gene symbols using pyensembl.

## Signature

```text
omicverse.utils. convert2gene_symbol ( input_names , scopes = 'ensembl.gene' , ensembl_release = None , species = None , force_rebuild = False )
```

## Parameters

- `input_names`: ( List [ str ] ) – List of Ensembl gene IDs, optionally including version suffixes (e.g. 'ENSG00000141510.12' is handled correctly).
- `scopes`: ( list of str or None , optional ) – Kept for API compatibility with older code. Not used internally. Default is 'ensembl.gene' .
- `ensembl_release`: ( int or None , optional ) – Ensembl release number (e.g. 109 ). If None , defaults to release 77 , which is broadly compatible with most datasets.
- `species`: ( str or None , optional ) – Target species. Supported values: 'human' , 'mouse' , 'rat' , 'zebrafish' , 'fly' , 'chicken' , 'dog' , 'pig' , 'cow' , 'macaque' . If None , species is inferred automatically from the Ensembl ID prefix.
- `force_rebuild`: ( bool , optional ) – If True , force re-download and re-index the local database even if it already exists. Useful after a failed index or suspected corruption. Default is False .

## Full Documentation

# omicverse.utils.convert2gene_symbol #

omicverse.utils. convert2gene_symbol ( input_names , scopes = 'ensembl.gene' , ensembl_release = None , species = None , force_rebuild = False ) [source] #

Convert Ensembl gene IDs to official gene symbols using pyensembl.

Parameters :

-
input_names ( List [ str ] ) – List of Ensembl gene IDs, optionally including version suffixes (e.g. `'ENSG00000141510.12' `is handled correctly).

-
scopes ( list of str or None , optional ) – Kept for API compatibility with older code. Not used internally. Default is `'ensembl.gene' `.

-
ensembl_release ( int or None , optional ) – Ensembl release number (e.g. `109 `). If `None `, defaults to release `77 `, which is broadly compatible with most datasets.

-
species ( str or None , optional ) – Target species. Supported values: `'human' `, `'mouse' `, `'rat' `, `'zebrafish' `, `'fly' `, `'chicken' `, `'dog' `, `'pig' `, `'cow' `, `'macaque' `. If `None `, species is inferred automatically from the Ensembl ID prefix.

-
force_rebuild ( bool , optional ) – If `True `, force re-download and re-index the local database even if it already exists. Useful after a failed index or suspected corruption. Default is `False `.

Returns :

DataFrame indexed by `'query' `(original Ensembl ID) with columns:

-
`'symbol' `— official gene symbol, or the original ID when no match is found.

-
`'_score' `— always `1.0 `, kept for downstream compatibility.

Return type :

pandas.DataFrame

Examples

```text
>>> df = ov.utils.convert2gene_symbol(list(adata.var_names))
>>> df = ov.utils.convert2gene_symbol(
... list(adata.var_names),
... species='mouse',
... ensembl_release=102,
... )

```
