# omicverse.utils.biocontext.search_clinical_trials #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.search_clinical_trials`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.search_clinical_trials.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Search ClinicalTrials.gov by condition.

## Signature

```text
omicverse.utils.biocontext. search_clinical_trials ( condition , status = None , page_size = 10 )
```

## Parameters

- `condition`: ( str ) – Medical condition (e.g. 'breast cancer' ).
- `status`: ( str , optional ) – Trial status filter (e.g. 'RECRUITING' ).
- `page_size`: ( int ) – Number of results.

## Full Documentation

# omicverse.utils.biocontext.search_clinical_trials #

omicverse.utils.biocontext. search_clinical_trials ( condition , status = None , page_size = 10 ) [source] #

Search ClinicalTrials.gov by condition.

Parameters :

-
condition ( str ) – Medical condition (e.g. `'breast cancer' `).

-
status ( str , optional ) – Trial status filter (e.g. `'RECRUITING' `).

-
page_size ( int ) – Number of results.

Returns :

Clinical trial summaries.

Return type :

dict
