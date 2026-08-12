# omicverse.utils.biocontext.search_interpro #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.search_interpro`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.search_interpro.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Search InterPro entries.

## Signature

```text
omicverse.utils.biocontext. search_interpro ( query , entry_type = None , page_size = 10 )
```

## Parameters

- `query`: ( str ) – Search term (e.g. 'kinase' ).
- `entry_type`: ( str , optional ) – Filter by type ( 'domain' , 'family' , 'homologous_superfamily' ).
- `page_size`: ( int ) – Number of results. Default 10.

## Full Documentation

# omicverse.utils.biocontext.search_interpro #

omicverse.utils.biocontext. search_interpro ( query , entry_type = None , page_size = 10 ) [source] #

Search InterPro entries.

Parameters :

-
query ( str ) – Search term (e.g. `'kinase' `).

-
entry_type ( str , optional ) – Filter by type ( `'domain' `, `'family' `, `'homologous_superfamily' `).

-
page_size ( int ) – Number of results. Default 10.

Returns :

Search results.

Return type :

dict
