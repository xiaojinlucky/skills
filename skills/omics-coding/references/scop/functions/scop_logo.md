# scop logo

- Package: scop
- Language: R
- Function: `scop_logo`
- Source: https://mengxu98.github.io/scop/reference/scop_logo.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/scop_logo.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

The scop logo, using ASCII or Unicode characters Use [cli:ansi_strip]{cli::ansi_strip} to get rid of the colors.

## Signature

```text
scop_logo(unicode = cli::is_utf8_output()) print{scop_logo}(x, ...)
```

## Parameters

- `unicode`: Whether to use Unicode symbols on UTF-8 platforms. Default is [cli:is_utf8_output]{cli::is_utf8_output}.
- `x`: Input infromation.
- `...`: Other parameters.

## Full Documentation

# scop logo

## Usage

```text
scop_logo(unicode = cli::is_utf8_output()) print{scop_logo}(x, ...)
```

## Description

The scop logo, using ASCII or Unicode characters Use [cli:ansi_strip]{cli::ansi_strip} to get rid of the colors.

## Examples

```r
scop_logo()
```
