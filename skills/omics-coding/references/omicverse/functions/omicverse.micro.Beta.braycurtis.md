# omicverse.micro.Beta.braycurtis #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.Beta.braycurtis`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.Beta.braycurtis.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Bray-Curtis dissimilarity matrix (samples × samples).

## Signature

```text
Beta. braycurtis ( rarefy = True )
```

## Parameters

- `rarefy`: ( bool (default: True ))

## Full Documentation

# omicverse.micro.Beta.braycurtis #

Beta. braycurtis ( rarefy = True ) [source] #

Bray-Curtis dissimilarity matrix (samples × samples).

Convenience wrapper for `self.run('braycurtis', rarefy=...) `. Bray-Curtis is the de-facto default beta metric for 16S — it weights species by abundance and ranges 0 (identical) to 1 (no shared taxa). When `rarefy=True `(the default), the underlying count matrix is rarefied to a common depth before the calculation; when `False `, raw counts are used (sensible only after CLR or proportion transforms).

Parameters :

rarefy ( `bool `(default: `True `))
