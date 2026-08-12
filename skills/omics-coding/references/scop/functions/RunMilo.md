# Milo differential abundance wrapper

- Package: scop
- Language: R
- Function: `RunMilo`
- Source: https://mengxu98.github.io/scop/reference/RunMilo.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunMilo.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Method-specific implementation used by RunProportionTest when proportion_method = "milo". The function always returns a group-level summary and additionally stores a neighborhood-level result list under neighborhood_results.

## Signature

```text
RunMilo( srt, group.by, split.by, sample.by, comparison = NULL, milo_k = 20L, milo_d = 30L, reduction = NULL, backend = c("r", "cpp"), n_bootstrap = 500, seed = 11, verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `group.by`: Name of one or more meta.data columns to group (color) cells by.
- `split.by`: Metadata column that identifies the condition groups to compare. For sample-level methods, if split.by is omitted and sample.by is provided, sample.by is treated as the condition column and virtual samples are created within each condition.
- `sample.by`: Metadata column that identifies biological samples. For "milo", "sccoda", and "propeller", when sample.by is omitted or identical to split.by, virtual samples are created within each split.by group for convenience.
- `comparison`: Optional: specify comparisons to perform.
- `milo_k`: Number of nearest neighbors used for Milo graph building.
- `milo_d`: Number of dimensions used by Milo.
- `reduction`: Dimensional reduction used for Milo graph construction. If NULL, the default PCA-like reduction is used.
- `backend`: Backend used to compute Milo neighborhoods and tests. "r" calls the upstream miloR implementation. "cpp" uses native scop graph/neighborhood/counting kernels and keeps edgeR for the neighborhood-level quasi-likelihood test.
- `n_bootstrap`: Number of bootstrap iterations used by the group-level summary.
- `seed`: Random seed.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Milo differential abundance wrapper

## Usage

```text
RunMilo( srt, group.by, split.by, sample.by, comparison = NULL, milo_k = 20L, milo_d = 30L, reduction = NULL, backend = c("r", "cpp"), n_bootstrap = 500, seed = 11, verbose = TRUE )
```

## Description

Method-specific implementation used by RunProportionTest when proportion_method = "milo". The function always returns a group-level summary and additionally stores a neighborhood-level result list under neighborhood_results.

## Value

A method result bundle used internally by RunProportionTest.
