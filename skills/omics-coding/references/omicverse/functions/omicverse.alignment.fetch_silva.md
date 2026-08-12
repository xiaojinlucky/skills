# omicverse.alignment.fetch_silva #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.fetch_silva`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.fetch_silva.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Alias for fetch_sintax_ref('silva_16s_v123', db_dir=...) .

## Signature

```text
omicverse.alignment. fetch_silva ( db_dir = None , overwrite = False )
```

## Parameters

- `db_dir`: ( Optional [ str ] (default: None ))
- `overwrite`: ( bool (default: False ))

## Full Documentation

# omicverse.alignment.fetch_silva #

omicverse.alignment. fetch_silva ( db_dir = None , overwrite = False ) [source] #

Alias for `fetch_sintax_ref('silva_16s_v123', db_dir=...) `.

Warning

`silva_16s_v123 `dates from 2015. The current SILVA release is v138.1+ (2020). For publication-grade work, export a newer SILVA release to SINTAX format yourself and pass it to `omicverse.alignment.vsearch.sintax() `via `db_fasta= `. A DeprecationWarning is emitted each time this alias is called.

Parameters :

-
db_dir ( `Optional `[ `str `] (default: `None `))

-
overwrite ( `bool `(default: `False `))
