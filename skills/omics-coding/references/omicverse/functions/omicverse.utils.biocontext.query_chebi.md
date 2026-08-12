# omicverse.utils.biocontext.query_chebi #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.query_chebi`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.query_chebi.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Query ChEBI for chemical entities.

## Signature

```text
omicverse.utils.biocontext. query_chebi ( chemical_name , size = 10 , exact_match = False )
```

## Parameters

- `chemical_name`: ( str ) – Chemical compound name.
- `size`: ( int ) – Maximum results.
- `exact_match`: ( bool ) – Require exact match.

## Full Documentation

# omicverse.utils.biocontext.query_chebi #

omicverse.utils.biocontext. query_chebi ( chemical_name , size = 10 , exact_match = False ) [source] #

Query ChEBI for chemical entities.

Parameters :

-
chemical_name ( str ) – Chemical compound name.

-
size ( int ) – Maximum results.

-
exact_match ( bool ) – Require exact match.

Returns :

ChEBI terms.

Return type :

dict
