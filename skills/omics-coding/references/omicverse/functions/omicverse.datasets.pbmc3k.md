# omicverse.datasets.pbmc3k #

- Package: omicverse
- Language: Python
- Function: `omicverse.datasets.pbmc3k`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.datasets.pbmc3k.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Load PBMC 3k dataset from URL.

## Signature

```text
omicverse.datasets. pbmc3k ( processed = False )
```

## Parameters

- `processed`: ( bool ) – If True , load processed PBMC3k file; otherwise load raw matrix.

## Full Documentation

# omicverse.datasets.pbmc3k #

omicverse.datasets. pbmc3k ( processed = False ) [source] #

Load PBMC 3k dataset from URL.

3k PBMCs from 10x Genomics. Downloads directly from public URLs, falls back to mock data generation if URLs are unavailable.

Parameters :

processed ( bool ) – If `True `, load processed PBMC3k file; otherwise load raw matrix.

Returns :

PBMC3k AnnData, with mock fallback if remote download fails.

Return type :

AnnData
