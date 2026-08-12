# Plot stored Statial Kontextual results

- Package: scop
- Language: R
- Function: `StatialKontextualPlot`
- Source: https://mengxu98.github.io/scop/reference/StatialKontextualPlot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/StatialKontextualPlot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot contextual relationship scores across radii from a result produced by [RunStatialKontextual()] without rerunning Statial.

## Signature

```text
StatialKontextualPlot(object = NULL, res = NULL, tests = NULL, images = NULL)
```

## Parameters

- `object`: Optional `Seurat` object containing the result.
- `res`: Optional result list, usually `object@tools$StatialKontextual`.
- `tests`: Optional relationship names to retain.
- `images`: Optional image identifiers to retain.

## Full Documentation

# Plot stored Statial Kontextual results

## Usage

```text
StatialKontextualPlot(object = NULL, res = NULL, tests = NULL, images = NULL)
```

## Description

Plot contextual relationship scores across radii from a result produced by [RunStatialKontextual()] without rerunning Statial.

## Value

A `ggplot` object.
