# omicverse.utils.biocontext.search_drugs #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.search_drugs`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.search_drugs.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Search FDA drug database.

## Signature

```text
omicverse.utils.biocontext. search_drugs ( brand_name = None , generic_name = None , active_ingredient = None , limit = 10 )
```

## Parameters

- `brand_name`: ( str , optional ) – Brand name to search.
- `generic_name`: ( str , optional ) – Generic name to search.
- `active_ingredient`: ( str , optional ) – Active ingredient to search.
- `limit`: ( int ) – Maximum results.

## Full Documentation

# omicverse.utils.biocontext.search_drugs #

omicverse.utils.biocontext. search_drugs ( brand_name = None , generic_name = None , active_ingredient = None , limit = 10 ) [source] #

Search FDA drug database.

Parameters :

-
brand_name ( str , optional ) – Brand name to search.

-
generic_name ( str , optional ) – Generic name to search.

-
active_ingredient ( str , optional ) – Active ingredient to search.

-
limit ( int ) – Maximum results.

Returns :

Drug information from OpenFDA.

Return type :

dict
