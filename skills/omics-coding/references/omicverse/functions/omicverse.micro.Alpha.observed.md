# omicverse.micro.Alpha.observed #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.Alpha.observed`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.Alpha.observed.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Per-sample observed-OTU count.

## Signature

```text
Alpha. observed ( )
```

## Parameters

No parameters detected.

## Full Documentation

# omicverse.micro.Alpha.observed #

Alpha. observed ( ) [source] #

Per-sample observed-OTU count.

Convenience wrapper for `self.run('observed_otus')['observed_otus'] `. Number of distinct ASVs / OTUs with non-zero counts in each sample. Strongly depth-dependent — always rarefy first or pair with a depth-corrected metric ( `chao1 `, `faith_pd `).
