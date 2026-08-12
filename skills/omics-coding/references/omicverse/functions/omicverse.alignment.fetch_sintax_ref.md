# omicverse.alignment.fetch_sintax_ref #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.fetch_sintax_ref`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.fetch_sintax_ref.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Download a SINTAX-formatted 16S reference FASTA.

## Signature

```text
omicverse.alignment. fetch_sintax_ref ( source = 'rdp_16s_v18' , db_dir = None , overwrite = False , timeout = 300 )
```

## Parameters

- `source`: ( str (default: 'rdp_16s_v18' )) – One of 'rdp_16s_v18' (small, 6.8 MB) or 'silva_16s_v123' (comprehensive, ~440 MB; but old — see notes below). Both are pre-formatted for vsearch --sintax .
- `db_dir`: ( Optional [ str ] (default: None )) – Required (or set OMICVERSE_DB_DIR ). Target directory under which the reference is saved. No $HOME fallback.
- `overwrite`: ( bool (default: False )) – Re-download even if the file already exists.
- `timeout`: ( int (default: 300 )) – Per-connection read timeout in seconds (default 300).

## Full Documentation

# omicverse.alignment.fetch_sintax_ref #

omicverse.alignment. fetch_sintax_ref ( source = 'rdp_16s_v18' , db_dir = None , overwrite = False , timeout = 300 ) [source] #

Download a SINTAX-formatted 16S reference FASTA.

Parameters :

-
source ( `str `(default: `'rdp_16s_v18' `)) – One of `'rdp_16s_v18' `(small, 6.8 MB) or `'silva_16s_v123' `(comprehensive, ~440 MB; but old — see notes below). Both are pre-formatted for vsearch `--sintax `.

-
db_dir ( `Optional `[ `str `] (default: `None `)) – Required (or set `OMICVERSE_DB_DIR `). Target directory under which the reference is saved. No `$HOME `fallback.

-
overwrite ( `bool `(default: `False `)) – Re-download even if the file already exists.

-
timeout ( `int `(default: `300 `)) – Per-connection read timeout in seconds (default 300).

Returns :

Absolute path to the downloaded `.fa.gz `.

Return type :

str
