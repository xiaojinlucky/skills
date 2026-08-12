# omicverse.utils.convert2gene_id #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.convert2gene_id`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.convert2gene_id.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Convert official gene symbols to Ensembl gene IDs using pyensembl.

## Signature

```text
omicverse.utils. convert2gene_id ( input_names , species = None , ensembl_release = None , force_rebuild = False , multi = 'first' )
```

## Parameters

- `input_names`: ( List [ str ] ) – List of official gene symbols (e.g. ['TP53', 'GAPDH', 'BRCA1'] ).
- `species`: ( str or None , optional ) – Target species. Supported values: 'human' , 'mouse' , 'rat' , 'zebrafish' , 'fly' , 'chicken' , 'dog' , 'pig' , 'cow' , 'macaque' . Defaults to 'human' when None .
- `ensembl_release`: ( int or None , optional ) – Ensembl release number. Defaults to 77 when None .
- `force_rebuild`: ( bool , optional ) – Force re-download and re-index the local database. Default is False .
- `multi`: ( {'first' , 'all' , 'join'} , optional ) – Strategy when a symbol maps to multiple Ensembl IDs (e.g. due to gene duplication): 'first' — return only the first ID (default).

## Full Documentation

# omicverse.utils.convert2gene_id #

omicverse.utils. convert2gene_id ( input_names , species = None , ensembl_release = None , force_rebuild = False , multi = 'first' ) [source] #

Convert official gene symbols to Ensembl gene IDs using pyensembl.

Parameters :

-
input_names ( List [ str ] ) – List of official gene symbols (e.g. `['TP53', 'GAPDH', 'BRCA1'] `).

-
species ( str or None , optional ) – Target species. Supported values: `'human' `, `'mouse' `, `'rat' `, `'zebrafish' `, `'fly' `, `'chicken' `, `'dog' `, `'pig' `, `'cow' `, `'macaque' `. Defaults to `'human' `when `None `.

-
ensembl_release ( int or None , optional ) – Ensembl release number. Defaults to `77 `when `None `.

-
force_rebuild ( bool , optional ) – Force re-download and re-index the local database. Default is `False `.

-
multi ( {'first' , 'all' , 'join'} , optional ) –
Strategy when a symbol maps to multiple Ensembl IDs (e.g. due to gene duplication):

-
`'first' `— return only the first ID (default).

-
`'all' `— return a Python list of all IDs.

-
`'join' `— return all IDs concatenated with `'|' `.

Returns :

DataFrame indexed by `'query' `(original symbol) with column:

-
`'gene_id' `— Ensembl gene ID, or the original symbol when no match is found.

Return type :

pandas.DataFrame

Examples

```text
>>> df = ov.utils.convert2gene_id(['TP53', 'GAPDH'])
>>> df = ov.utils.convert2gene_id(
... ['Trp53', 'Gapdh'],
... species='mouse',
... ensembl_release=102,
... )
>>> df = ov.utils.convert2gene_id(['TP53'], multi='join')

```
