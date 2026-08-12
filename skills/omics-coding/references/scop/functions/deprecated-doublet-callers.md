# Deprecated doublet-calling entry points

- Package: scop
- Language: R
- Function: `deprecated-doublet-callers`
- Source: https://mengxu98.github.io/scop/reference/deprecated-doublet-callers.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/deprecated-doublet-callers.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

`db_scDblFinder()`, `db_scds()`, `db_Scrublet()`, and `db_DoubletDetection()` were renamed to [RunscDblFinder()], [Runscds()], [RunScrublet()], and [RunDoubletDetection()]. The compatibility entry points remain available with a warning and will be removed in version 1.0.0.

## Signature

```text
db_scDblFinder(...) db_scds(...) db_Scrublet(...) db_DoubletDetection(...)
```

## Parameters

- `...`: Arguments forwarded unchanged to the replacement function.

## Full Documentation

# Deprecated doublet-calling entry points

## Usage

```text
db_scDblFinder(...) db_scds(...) db_Scrublet(...) db_DoubletDetection(...)
```

## Description

`db_scDblFinder()`, `db_scds()`, `db_Scrublet()`, and `db_DoubletDetection()` were renamed to [RunscDblFinder()], [Runscds()], [RunScrublet()], and [RunDoubletDetection()]. The compatibility entry points remain available with a warning and will be removed in version 1.0.0.

## Value

The value returned by the replacement function.
