# Permutation-based proportion test

- Package: scop
- Language: R
- Function: `RunPermutation`
- Source: https://mengxu98.github.io/scop/reference/RunPermutation.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunPermutation.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Method-specific implementation used by RunProportionTest when proportion_method = "permutation". This method is a permutation-based statistical test for compositional shift rather than a dedicated biological model. Bootstrap confidence intervals are reported as uncertainty estimates for observed log2 fold-differences.

## Signature

```text
RunPermutation( srt, group.by, split.by, comparison = NULL, n_permutations = 1000, include_all_cells = FALSE, verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `group.by`: Name of one or more meta.data columns to group (color) cells by.
- `split.by`: Metadata column that identifies the condition groups to compare. For sample-level methods, if split.by is omitted and sample.by is provided, sample.by is treated as the condition column and virtual samples are created within each condition.
- `comparison`: Optional: specify comparisons to perform.
- `n_permutations`: Number of permutations for permutation-based test.
- `include_all_cells`: Whether to include all cell types in the complete grid for permutation mode.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Permutation-based proportion test

## Usage

```text
RunPermutation( srt, group.by, split.by, comparison = NULL, n_permutations = 1000, include_all_cells = FALSE, verbose = TRUE )
```

## Description

Method-specific implementation used by RunProportionTest when proportion_method = "permutation". This method is a permutation-based statistical test for compositional shift rather than a dedicated biological model. Bootstrap confidence intervals are reported as uncertainty estimates for observed log2 fold-differences.

## Value

A method result bundle used internally by RunProportionTest.
