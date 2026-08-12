# Deprecated workflow entry points

- Package: scop
- Language: R
- Function: `deprecated-workflows`
- Source: https://mengxu98.github.io/scop/reference/deprecated-workflows.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/deprecated-workflows.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

`standard_scop()` and `integration_scop()` were renamed to [RunStandardWorkflow()] and [RunIntegration()]. The compatibility entry points remain available with a warning in releases before 1.0.0 and will be removed in version 1.0.0.

## Signature

```text
standard_scop(...) integration_scop(...)
```

## Parameters

- `...`: Arguments forwarded unchanged to the replacement function.

## Full Documentation

# Deprecated workflow entry points

## Usage

```text
standard_scop(...) integration_scop(...)
```

## Description

`standard_scop()` and `integration_scop()` were renamed to [RunStandardWorkflow()] and [RunIntegration()]. The compatibility entry points remain available with a warning in releases before 1.0.0 and will be removed in version 1.0.0.

## Value

The value returned by the replacement function.
