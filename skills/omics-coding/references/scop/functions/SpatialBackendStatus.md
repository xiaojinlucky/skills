# Inspect spatial backend availability

- Package: scop
- Language: R
- Function: `SpatialBackendStatus`
- Source: https://mengxu98.github.io/scop/reference/SpatialBackendStatus.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/SpatialBackendStatus.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Diagnose optional spatial backend installation and exported API status. The function is read-only: it never installs or updates a package. Actual method calls remain the authoritative runtime check for system libraries, S4 registration, and data-specific requirements.

## Signature

```text
SpatialBackendStatus( backend = NULL, method = NULL, api_check = TRUE, refresh = FALSE, envname = NULL, conda = "auto" )
```

## Parameters

- `backend`: Optional backend identifier filter.
- `method`: Optional registered spatial method filter.
- `api_check`: Whether to inspect required namespace exports.
- `refresh`: Whether to refresh the session-local diagnostic cache.
- `envname`: Existing SCOP Python environment to inspect for Python backends. The diagnostic never creates or modifies the environment.
- `conda`: Existing conda-compatible executable, or `"auto"` to discover one without installing it.

## Full Documentation

# Inspect spatial backend availability

## Usage

```text
SpatialBackendStatus( backend = NULL, method = NULL, api_check = TRUE, refresh = FALSE, envname = NULL, conda = "auto" )
```

## Description

Diagnose optional spatial backend installation and exported API status. The function is read-only: it never installs or updates a package. Actual method calls remain the authoritative runtime check for system libraries, S4 registration, and data-specific requirements.

## Value

A data frame with one row per backend.
