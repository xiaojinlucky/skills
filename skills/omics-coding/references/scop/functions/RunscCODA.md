# scCODA differential abundance

- Package: scop
- Language: R
- Function: `RunscCODA`
- Source: https://mengxu98.github.io/scop/reference/RunscCODA.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunscCODA.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

scCODA differential abundance

## Signature

```text
RunscCODA( srt, group.by, split.by, sample.by, comparison = NULL, reference_cell_type = NULL, credible_effect_threshold = 0.95, n_mcmc_samples = 20000L, envname = "sccoda_env", conda = "auto", seed = 11, verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `group.by`: Name of one or more meta.data columns to group (color) cells by.
- `split.by`: Metadata column that identifies the condition groups to compare. For sample-level methods, if split.by is omitted and sample.by is provided, sample.by is treated as the condition column and virtual samples are created within each condition.
- `sample.by`: Metadata column that identifies biological samples. For "milo", "sccoda", and "propeller", when sample.by is omitted or identical to split.by, virtual samples are created within each split.by group for convenience.
- `comparison`: Optional: specify comparisons to perform.
- `reference_cell_type`: Optional reference cell type for scCODA.
- `credible_effect_threshold`: Inclusion probability threshold for credible effects.
- `n_mcmc_samples`: Number of MCMC samples requested in scCODA.
- `envname`: Name of the conda-compatible environment used by scCODA. Defaults to "sccoda_env" to keep the TensorFlow/scCODA stack isolated from the default Python environment.
- `conda`: The path or command name of a conda-compatible executable.
- `seed`: Random seed.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# scCODA differential abundance

## Usage

```text
RunscCODA( srt, group.by, split.by, sample.by, comparison = NULL, reference_cell_type = NULL, credible_effect_threshold = 0.95, n_mcmc_samples = 20000L, envname = "sccoda_env", conda = "auto", seed = 11, verbose = TRUE )
```

## Description

scCODA differential abundance

## Value

A method result bundle used internally by RunProportionTest.
