# Prepare the python environment

- Package: scop
- Language: R
- Function: `PrepareEnv`
- Source: https://mengxu98.github.io/scop/reference/PrepareEnv.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/PrepareEnv.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Prepare the python environment by installing the required dependencies and setting up the environment.

## Signature

```text
PrepareEnv( envname = NULL, conda = "auto", miniconda_repo = "https://repo.anaconda.com/miniconda", version = if (is_windows()) "3.11-1" else "3.10-1", force = FALSE, modules = NULL, pip_options = character(), components = "python", cores = NULL, verbose = TRUE, ... )
```

## Parameters

- `envname`: The name of the conda-compatible Python environment. If NULL, the environment name will be set to "scop_env". Default is NULL.
- `conda`: The path or command name of a conda-compatible executable (conda, mamba, or micromamba). Use "auto" to allow automatically finding an appropriate environment manager. If "micromamba" is requested and micromamba is not available on PATH, a package-managed micromamba is downloaded automatically.
- `miniconda_repo`: Repository URL for miniconda. Default is https://repo.anaconda.com/miniconda.
- `version`: The Python version. Default is "3.10-1" on macOS and Unix and "3.11-1" on Windows.
- `force`: Whether to force recreation of the environment. If TRUE, the existing environment will be removed and recreated. Default is FALSE.
- `modules`: Optional Python dependency modules to install in addition to the default scientific stack. If NULL or omitted in {[=PrepareEnv]{PrepareEnv()}}, the default environment is installed. The default excludes "cell2location", "cell2fate", "sccoda", and "scomm" because these workflows use long-running or incompatible dependency stacks. Cell2fate is prepared in a standalone "cell2fate_env" with Python 3.9. "scenic" is also excluded from the default environment and is prepared in "scenic_env" by default because SCENIC requires an older Python/numpy stack. On Windows, the default also excludes "scvi", "glue", and "multimap" because those upstream stacks are more reliable when requested explicitly for method-specific workflows.
- `pip_options`: Additional command line arguments to be passed to uv/pip when installing pip packages.
- `components`: Components to prepare. Supported values are "python", "r", and "all"; "all" expands to both Python and R. The default, "python", preserves the existing Python-only behavior. The R component collects packages declared through check_r() and checks/installs them, including optional workflow dependencies not listed in DESCRIPTION. CHOIR is R-only, so PrepareEnv(modules = "choir") prepares its pinned optional R backend without creating a Python environment.
- `cores`: Number of workers for R-package installation. Use NULL (the default) to let pak select its worker count automatically.
- `verbose`: Whether to print the message. Default is TRUE.
- `...`: Additional arguments passed to package installation functions.

## Full Documentation

# Prepare the python environment

## Usage

```text
PrepareEnv( envname = NULL, conda = "auto", miniconda_repo = "https://repo.anaconda.com/miniconda", version = if (is_windows()) "3.11-1" else "3.10-1", force = FALSE, modules = NULL, pip_options = character(), components = "python", cores = NULL, verbose = TRUE, ... )
```

## Description

Prepare the python environment by installing the required dependencies and setting up the environment.
