# Python environment requirements

- Package: scop
- Language: R
- Function: `env_requirements`
- Source: https://mengxu98.github.io/scop/reference/env_requirements.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/env_requirements.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

The function returns a list of requirements including the required Python version, package versions, and package name aliases for platform-specific packages. All packages will be installed using uv as the primary tool.

## Signature

```text
env_requirements( version = "3.10-1", include_optional = FALSE, modules = NULL, verbose = TRUE )
```

## Parameters

- `version`: The Python version of the environment. Default is "3.10-1". Python "3.9-1" is reserved for the standalone "cell2fate" module.
- `include_optional`: Whether to include optional Python dependencies.
- `modules`: Optional requirement modules to include. Supported values are "scanpy", "scvi", "scanorama", "bbknn", "celltypist", "cellphonedb", "cell2location", "cell2fate", "magic", "scrublet", "doubletdetection", "sccoda", "doublet", "palantir", "scvelo", "cellrank", "wot", "phate", "pacmap", "trimap", "multimap", "scomm", "scenic", "seacells", "tage", "scmalignantfinder", "secact", "scpagwas", "choir", and "external_wrappers". If NULL, the default environment is returned. The default excludes "cell2location", "cell2fate", "sccoda", "scomm", and "scenic" because these workflows require dependency stacks that should be prepared explicitly. The "scenic" module is standalone and always uses Python "3.10-1".
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Python environment requirements

## Usage

```text
env_requirements( version = "3.10-1", include_optional = FALSE, modules = NULL, verbose = TRUE )
```

## Description

The function returns a list of requirements including the required Python version, package versions, and package name aliases for platform-specific packages. All packages will be installed using uv as the primary tool.

## Value

A list containing: { python{Python version string} packages{Named vector of package version specifications} package_aliases{Named list mapping logical package names to actual installed names} }

## Examples

```r
env_requirements("3.10-1")
```
