# ESTIMATE gene signatures

- Package: scop
- Language: R
- Function: `estimate_signatures`
- Source: https://mengxu98.github.io/scop/reference/estimate_signatures.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/estimate_signatures.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Gene signatures and common-gene universe used by {[=RunESTIMATE]{RunESTIMATE()}} to compute stromal, immune, combined ESTIMATE, and tumor-purity scores without requiring the external estimate package.

## Signature

```text
estimate_signatures
```

## Parameters

No parameters detected.

## Full Documentation

# ESTIMATE gene signatures

## Usage

```text
estimate_signatures
```

## Description

Gene signatures and common-gene universe used by {[=RunESTIMATE]{RunESTIMATE()}} to compute stromal, immune, combined ESTIMATE, and tumor-purity scores without requiring the external estimate package.

## Examples

```r
data(estimate_signatures)
names(estimate_signatures)
lengths(estimate_signatures[c("stromal_signature", "immune_signature", "common_genes")])
```
