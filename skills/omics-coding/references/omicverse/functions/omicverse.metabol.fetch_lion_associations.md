# omicverse.metabol.fetch_lion_associations #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.fetch_lion_associations`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.fetch_lion_associations.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Fetch the full LION lipid↔ontology associations.

## Signature

```text
omicverse.metabol. fetch_lion_associations ( * , cache = True , refresh = False )
```

## Parameters

- `cache`: ( bool (default: True ))
- `refresh`: ( bool (default: False ))

## Full Documentation

# omicverse.metabol.fetch_lion_associations #

omicverse.metabol. fetch_lion_associations ( * , cache = True , refresh = False ) [source] #

Fetch the full LION lipid↔ontology associations.

Returns :

`{term_name: {"category": str, "members": [lipid_class, ...]}} `— same shape as the shipped `lion_subset.json `so `lion_enrichment() `consumes it directly. LION terms that attach to many thousands of species are aggregated to the class level (first token of the LIPID MAPS shorthand) to match how the lipidomics module does enrichment.

Return type :

dict [ str , dict ]

Parameters :

-
cache ( `bool `(default: `True `))

-
refresh ( `bool `(default: `False `))
