# omicverse.utils.biocontext.query_efo #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.query_efo`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.query_efo.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Query EFO for disease ontology terms.

## Signature

```text
omicverse.utils.biocontext. query_efo ( disease_name , size = 10 , exact_match = False )
```

## Parameters

- `disease_name`: ( str ) – Disease name to search.
- `size`: ( int ) – Maximum results.
- `exact_match`: ( bool ) – Require exact match.

## Full Documentation

# omicverse.utils.biocontext.query_efo #

omicverse.utils.biocontext. query_efo ( disease_name , size = 10 , exact_match = False ) [source] #

Query EFO for disease ontology terms.

Parameters :

-
disease_name ( str ) – Disease name to search.

-
size ( int ) – Maximum results.

-
exact_match ( bool ) – Require exact match.

Returns :

EFO terms with IDs and descriptions.

Return type :

dict
