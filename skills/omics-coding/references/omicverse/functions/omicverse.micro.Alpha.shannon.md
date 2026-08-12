# omicverse.micro.Alpha.shannon #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.Alpha.shannon`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.Alpha.shannon.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Per-sample Shannon entropy.

## Signature

```text
Alpha. shannon ( )
```

## Parameters

No parameters detected.

## Full Documentation

# omicverse.micro.Alpha.shannon #

Alpha. shannon ( ) [source] #

Per-sample Shannon entropy.

Convenience wrapper for `self.run('shannon')['shannon'] `. Higher values mean more even community composition (mathematical max is `log(n_taxa) `). Sensitive to rare taxa, so always rarefy first if sequencing depths are unequal — otherwise samples with more reads will appear “more diverse” purely from depth.
