# List conda-compatible Python environments

- Package: scop
- Language: R
- Function: `ListEnv`
- Source: https://mengxu98.github.io/scop/reference/ListEnv.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/ListEnv.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

List conda-compatible Python environments

## Signature

```text
ListEnv(conda = "auto")
```

## Parameters

- `conda`: The path or command name of a conda-compatible executable (conda, mamba, or micromamba). Use "auto" to allow automatically finding an appropriate environment manager. If "micromamba" is requested and micromamba is not available on PATH, a package-managed micromamba is downloaded automatically.

## Full Documentation

# List conda-compatible Python environments

## Usage

```text
ListEnv(conda = "auto")
```

## Description

List conda-compatible Python environments

## Value

A data frame of conda-compatible Python environments.
