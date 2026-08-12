# omicverse.utils.biocontext.search_preprints #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.search_preprints`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.search_preprints.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Search bioRxiv or medRxiv preprints.

## Signature

```text
omicverse.utils.biocontext. search_preprints ( server = 'biorxiv' , start_date = None , end_date = None , days = None , recent_count = None , category = None , max_results = 100 )
```

## Parameters

- `server`: ( str ) – 'biorxiv' or 'medrxiv' .
- `start_date`: ( str , optional ) – Date range in 'YYYY-MM-DD' format.
- `end_date`: ( str , optional ) – Date range in 'YYYY-MM-DD' format.
- `days`: ( int , optional ) – Search last N days (1–365).
- `recent_count`: ( int , optional ) – Most recent N preprints (1–1000).
- `category`: ( str , optional ) – Category filter (e.g. 'bioinformatics' , 'cell biology' , 'genomics' , 'neuroscience' ).
- `max_results`: ( int ) – Maximum results to return (1–500).

## Full Documentation

# omicverse.utils.biocontext.search_preprints #

omicverse.utils.biocontext. search_preprints ( server = 'biorxiv' , start_date = None , end_date = None , days = None , recent_count = None , category = None , max_results = 100 ) [source] #

Search bioRxiv or medRxiv preprints.

Specify one search method: `start_date `/ `end_date `date range, `days `for last N days, or `recent_count `for most recent N.

Parameters :

-
server ( str ) – `'biorxiv' `or `'medrxiv' `.

-
start_date ( str , optional ) – Date range in `'YYYY-MM-DD' `format.

-
end_date ( str , optional ) – Date range in `'YYYY-MM-DD' `format.

-
days ( int , optional ) – Search last N days (1–365).

-
recent_count ( int , optional ) – Most recent N preprints (1–1000).

-
category ( str , optional ) – Category filter (e.g. `'bioinformatics' `, `'cell biology' `, `'genomics' `, `'neuroscience' `).

-
max_results ( int ) – Maximum results to return (1–500).

Returns :

Preprint metadata.

Return type :

dict
