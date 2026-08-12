# Reference datasets for cell type annotation in single-cell RNA data

- Package: scop
- Language: R
- Function: `ref_scMCA`
- Source: https://mengxu98.github.io/scop/reference/ref_scMCA.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/ref_scMCA.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Reference datasets for cell type annotation in single-cell RNA data

## Signature

```text
ref_scMCA
```

## Parameters

No parameters detected.

## Full Documentation

# Reference datasets for cell type annotation in single-cell RNA data

## Usage

```text
ref_scMCA
```

## Description

Reference datasets for cell type annotation in single-cell RNA data

## Examples

```r
thisutils::check_r(c("ggjlab/scMCA"))
ref_scMCA <- NormalizeData(get("ref.expr", envir = asNamespace("scMCA")))
Encoding(colnames(ref_scMCA)) <- "latin1"
colnames(ref_scMCA) <- iconv(colnames(ref_scMCA), "latin1", "UTF-8")
# thisutils::get_namespace_fun("usethis", "use_data")(ref_scMCA, compress = "xz")
```
