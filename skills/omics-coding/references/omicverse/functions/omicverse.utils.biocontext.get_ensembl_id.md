# omicverse.utils.biocontext.get_ensembl_id #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.get_ensembl_id`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.get_ensembl_id.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Convert gene symbol to Ensembl ID.

## Signature

```text
omicverse.utils.biocontext. get_ensembl_id ( gene_symbol , species = 'homo_sapiens' )
```

## Parameters

- `gene_symbol`: ( str ) – Gene symbol (e.g. 'TP53' ).
- `species`: ( str ) – Species name. Default 'homo_sapiens' .

## Full Documentation

# omicverse.utils.biocontext.get_ensembl_id #

omicverse.utils.biocontext. get_ensembl_id ( gene_symbol , species = 'homo_sapiens' ) [source] #

Convert gene symbol to Ensembl ID.

Parameters :

-
gene_symbol ( str ) – Gene symbol (e.g. `'TP53' `).

-
species ( str ) – Species name. Default `'homo_sapiens' `.

Returns :

Ensembl gene ID.

Return type :

str or dict
