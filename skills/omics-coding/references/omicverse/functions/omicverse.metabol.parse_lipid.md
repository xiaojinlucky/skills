# omicverse.metabol.parse_lipid #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.parse_lipid`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.parse_lipid.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Parse a lipid name into a LipidIdentity .

## Signature

```text
omicverse.metabol. parse_lipid ( name )
```

## Parameters

- `name`: ( str )

## Full Documentation

# omicverse.metabol.parse_lipid #

omicverse.metabol. parse_lipid ( name ) [source] #

Parse a lipid name into a `LipidIdentity `.

Tries the Goslin reference parser ( `pygoslin `) first — it handles the LIPID MAPS shorthand and the common vendor dialects and gives class, category and per-chain detail. Falls back to the built-in regex when `pygoslin `is unavailable or the name is unrecognised. Returns `None `if neither parser recognises the name.

Parameters :

name ( `str `)
