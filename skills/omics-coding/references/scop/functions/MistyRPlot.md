# Plot stored MISTy results

- Package: scop
- Language: R
- Function: `MistyRPlot`
- Source: https://mengxu98.github.io/scop/reference/MistyRPlot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/MistyRPlot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot model improvements or view contributions from a result produced by [RunMistyR()] without rerunning the backend.

## Signature

```text
MistyRPlot( object = NULL, res = NULL, type = c("improvements", "contributions"), top_n = 20, target = NULL )
```

## Parameters

- `object`: Optional `Seurat` object containing `MistyR` results.
- `res`: Optional result list, usually `object@tools$MistyR`.
- `type`: Result table to plot.
- `top_n`: Maximum number of records shown after ranking by absolute value.
- `target`: Optional target feature filter.

## Full Documentation

# Plot stored MISTy results

## Usage

```text
MistyRPlot( object = NULL, res = NULL, type = c("improvements", "contributions"), top_n = 20, target = NULL )
```

## Description

Plot model improvements or view contributions from a result produced by [RunMistyR()] without rerunning the backend.

## Value

A `ggplot` object.
