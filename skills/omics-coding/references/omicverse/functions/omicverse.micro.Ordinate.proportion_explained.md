# omicverse.micro.Ordinate.proportion_explained #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.Ordinate.proportion_explained`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.Ordinate.proportion_explained.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Eigenvalue proportions from the most recent PCoA call.

## Signature

```text
Ordinate. proportion_explained ( )
```

## Parameters

No parameters detected.

## Full Documentation

# omicverse.micro.Ordinate.proportion_explained #

Ordinate. proportion_explained ( ) [source] #

Eigenvalue proportions from the most recent PCoA call.

Returns `None `if PCoA hasn’t run yet (NMDS doesn’t produce eigenvalues — use `adata.uns['micro'][f'{dist_key}_nmds_stress'] `instead). The first two values are the canonical “PC1 / PC2” % variance labels for ordination plots.
