# Excluded words in keyword enrichment analysis and extraction

- Package: scop
- Language: R
- Function: `words_excluded`
- Source: https://mengxu98.github.io/scop/reference/words_excluded.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/words_excluded.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

The variable words_excluded represents the words that are excluded during keyword enrichment analysis or keyword extraction process. These mainly include words that are excessively redundant or of little value.

## Signature

```text
words_excluded
```

## Parameters

No parameters detected.

## Full Documentation

# Excluded words in keyword enrichment analysis and extraction

## Usage

```text
words_excluded
```

## Description

The variable words_excluded represents the words that are excluded during keyword enrichment analysis or keyword extraction process. These mainly include words that are excessively redundant or of little value.

## Examples

```r
words_excluded <- c(
  "the", "is", "and", "or", "a",
  "in", "on", "under", "between", "of",
  "through", "via", "along", "that",
  "for", "with", "within", "without",
  "cell", "cellular", "dna", "rna",
  "protein", "peptide", "amino", "acid",
  "development", "involved", "organization", "system",
  "regulation", "regulated", "positive", "negative",
  "response", "process", "processing", "small", "large", "change"
)
use_data <- thisutils::get_namespace_fun("usethis", "use_data")
use_data(words_excluded, compress = "xz")
```
