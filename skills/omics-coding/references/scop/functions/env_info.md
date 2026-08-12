# Print environment information

- Package: scop
- Language: R
- Function: `env_info`
- Source: https://mengxu98.github.io/scop/reference/env_info.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/env_info.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Print environment information

## Signature

```text
env_info(conda, envname, verbose = TRUE)
```

## Parameters

- `conda`: The path or command name of a conda-compatible executable (conda, mamba, or micromamba). Use "auto" to allow automatically finding an appropriate environment manager. If "micromamba" is requested and micromamba is not available on PATH, a package-managed micromamba is downloaded automatically.
- `envname`: The name of the conda-compatible Python environment. If NULL, the environment name will be set to "scop_env". Default is NULL.
- `verbose`: Whether to print environment information.

## Full Documentation

# Print environment information

## Usage

```text
env_info(conda, envname, verbose = TRUE)
```

## Description

Print environment information
