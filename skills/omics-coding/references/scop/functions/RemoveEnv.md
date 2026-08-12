# Remove a conda-compatible Python environment

- Package: scop
- Language: R
- Function: `RemoveEnv`
- Source: https://mengxu98.github.io/scop/reference/RemoveEnv.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RemoveEnv.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Remove a conda-compatible Python environment

## Signature

```text
RemoveEnv(envname = NULL, conda = "auto", force = FALSE, verbose = TRUE)
```

## Parameters

- `envname`: The name of the conda-compatible Python environment. If NULL, the environment name will be set to "scop_env". Default is NULL.
- `conda`: The path or command name of a conda-compatible executable (conda, mamba, or micromamba). Use "auto" to allow automatically finding an appropriate environment manager. If "micromamba" is requested and micromamba is not available on PATH, a package-managed micromamba is downloaded automatically.
- `force`: Whether to force removal without confirmation. Default is FALSE.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Remove a conda-compatible Python environment

## Usage

```text
RemoveEnv(envname = NULL, conda = "auto", force = FALSE, verbose = TRUE)
```

## Description

Remove a conda-compatible Python environment

## Value

Invisibly returns TRUE if successful, FALSE otherwise.

## Examples

```r
\dontrun{
# Remove default environment
RemoveEnv()

# Remove a specific environment
RemoveEnv("my_old_env")

# Removal without confirmation
RemoveEnv("my_old_env", force = TRUE)
}
```
