# omicverse.metabol.lion_enrichment #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.lion_enrichment`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.lion_enrichment.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

LION-style over-representation for lipid classes / properties.

## Signature

```text
omicverse.metabol. lion_enrichment ( hits , background , * , ontology = None , min_size = 3 )
```

## Parameters

- `hits`: ( Iterable [ str ] ) – Lipid names in LIPID MAPS shorthand (e.g. ['PC 34:1', 'TAG 54:3', ...] ).
- `background`: ( Iterable [ str ] ) – All tested lipid names.
- `ontology`: ( Optional [ dict [ str , dict ]] (default: None )) – Dict of {term_name: {"members": [lipid_class, ...], "category": ...}} . If None , the local LION subset is used.
- `min_size`: ( int (default: 3 ))

## Full Documentation

# omicverse.metabol.lion_enrichment #

omicverse.metabol. lion_enrichment ( hits , background , * , ontology = None , min_size = 3 ) [source] #

LION-style over-representation for lipid classes / properties.

Parameters :

-
hits ( `Iterable `[ `str `] ) – Lipid names in LIPID MAPS shorthand (e.g. `['PC 34:1', 'TAG 54:3', ...] `).

-
background ( `Iterable `[ `str `] ) – All tested lipid names.

-
ontology ( `Optional `[ `dict `[ `str `, `dict `]] (default: `None `)) – Dict of `{term_name: {"members": [lipid_class, ...], "category": ...}} `. If `None `, the local LION subset is used.

-
min_size ( `int `(default: `3 `))
