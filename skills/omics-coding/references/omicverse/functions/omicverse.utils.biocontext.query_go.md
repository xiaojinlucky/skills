# omicverse.utils.biocontext.query_go #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.query_go`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.query_go.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Query Gene Ontology terms for a gene.

## Signature

```text
omicverse.utils.biocontext. query_go ( gene_name , size = 20 )
```

## Parameters

- `gene_name`: ( str ) – Gene symbol (e.g. 'BRCA1' ).
- `size`: ( int ) – Maximum number of GO terms to return.

## Full Documentation

# omicverse.utils.biocontext.query_go #

omicverse.utils.biocontext. query_go ( gene_name , size = 20 ) [source] #

Query Gene Ontology terms for a gene.

Parameters :

-
gene_name ( str ) – Gene symbol (e.g. `'BRCA1' `).

-
size ( int ) – Maximum number of GO terms to return.

Returns :

GO terms (biological process, molecular function, cellular component).

Return type :

dict
