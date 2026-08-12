# omicverse.utils.biocontext.search_literature #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.search_literature`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.search_literature.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Search Europe PMC for biomedical literature.

## Signature

```text
omicverse.utils.biocontext. search_literature ( query , search_type = 'lite' , sort_by = 'RELEVANCE' , page_size = 10 )
```

## Parameters

- `query`: ( str ) – Search query string.
- `search_type`: ( str ) – 'lite' for basic metadata, 'core' for full records.
- `sort_by`: ( str ) – Sort order: 'RELEVANCE' or 'DATE' .
- `page_size`: ( int ) – Number of results.

## Full Documentation

# omicverse.utils.biocontext.search_literature #

omicverse.utils.biocontext. search_literature ( query , search_type = 'lite' , sort_by = 'RELEVANCE' , page_size = 10 ) [source] #

Search Europe PMC for biomedical literature.

Parameters :

-
query ( str ) – Search query string.

-
search_type ( str ) – `'lite' `for basic metadata, `'core' `for full records.

-
sort_by ( str ) – Sort order: `'RELEVANCE' `or `'DATE' `.

-
page_size ( int ) – Number of results.

Returns :

Search results with article metadata.

Return type :

dict
