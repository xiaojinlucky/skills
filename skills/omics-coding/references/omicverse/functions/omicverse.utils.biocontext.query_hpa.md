# omicverse.utils.biocontext.query_hpa #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.query_hpa`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.query_hpa.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Query Human Protein Atlas for tissue-level expression.

## Signature

```text
omicverse.utils.biocontext. query_hpa ( gene_symbol , gene_id = None )
```

## Parameters

- `gene_symbol`: ( str ) – Gene symbol (e.g. 'TP53' ).
- `gene_id`: ( str , optional ) – Ensembl gene ID (e.g. 'ENSG00000141510' ). If not provided, it is resolved automatically via get_ensembl_id .

## Full Documentation

# omicverse.utils.biocontext.query_hpa #

omicverse.utils.biocontext. query_hpa ( gene_symbol , gene_id = None ) [source] #

Query Human Protein Atlas for tissue-level expression.

Parameters :

-
gene_symbol ( str ) – Gene symbol (e.g. `'TP53' `).

-
gene_id ( str , optional ) – Ensembl gene ID (e.g. `'ENSG00000141510' `). If not provided, it is resolved automatically via `get_ensembl_id `.

Returns :

HPA expression data across tissues.

Return type :

dict
