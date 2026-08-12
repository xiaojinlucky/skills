# omicverse.bulk.readWGCNA #

- Package: omicverse
- Language: Python
- Function: `omicverse.bulk.readWGCNA`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.bulk.readWGCNA.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Load a previously saved WGCNA object from disk.

## Signature

```text
omicverse.bulk. readWGCNA ( file )
```

## Parameters

- `file`: ( str ) – Path to the pickled object produced by pyWGCNA.saveWGCNA(...) .

## Full Documentation

# omicverse.bulk.readWGCNA #

omicverse.bulk. readWGCNA ( file ) [source] #

Load a previously saved WGCNA object from disk.

Lazy wrapper around `omicverse.external.PyWGCNA.utils.readWGCNA() `.

Parameters :

file ( str ) – Path to the pickled object produced by `pyWGCNA.saveWGCNA(...) `.

Returns :

Restored analysis object with all attributes ( `datExpr `, `MEs `, `moduleTraitCor `…) populated.

Return type :

pyWGCNA
