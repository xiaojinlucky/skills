# List spatial methods

- Package: scop
- Language: R
- Function: `ListSpatialMethods`
- Source: https://mengxu98.github.io/scop/reference/ListSpatialMethods.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/ListSpatialMethods.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

List the public spatial analysis, visualization, framework bridge, and workflow entry points registered by scop. This function does not inspect optional packages unless `available` is `TRUE` or `FALSE`.

## Signature

```text
ListSpatialMethods( task = NULL, kind = NULL, backend = NULL, status = NULL, available = NULL, pattern = NULL )
```

## Parameters

- `task, kind, backend, status`: Optional exact filters.
- `available`: Optional logical availability filter. `NULL` avoids backend inspection.
- `pattern`: Optional case-insensitive pattern matched against method, task, backend, and documentation fields.

## Full Documentation

# List spatial methods

## Usage

```text
ListSpatialMethods( task = NULL, kind = NULL, backend = NULL, status = NULL, available = NULL, pattern = NULL )
```

## Description

List the public spatial analysis, visualization, framework bridge, and workflow entry points registered by scop. This function does not inspect optional packages unless `available` is `TRUE` or `FALSE`.

## Value

A data frame with one row per registered public method.
