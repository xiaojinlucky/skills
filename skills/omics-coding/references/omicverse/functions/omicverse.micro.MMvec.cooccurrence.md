# omicverse.micro.MMvec.cooccurrence #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.MMvec.cooccurrence`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.MMvec.cooccurrence.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Raw log-odds co-occurrence matrix U · Vᵀ (microbes × metabolites).

## Signature

```text
MMvec. cooccurrence ( )
```

## Parameters

No parameters detected.

## Full Documentation

# omicverse.micro.MMvec.cooccurrence #

MMvec. cooccurrence ( ) [source] #

Raw log-odds co-occurrence matrix `U · Vᵀ `(microbes × metabolites).

Symmetric scoring before per-microbe softmax normalisation: positive entries indicate microbes and metabolites that appear together in the same samples; negative entries the opposite. Useful when you want signed scores and don’t need them to sum to 1 per microbe — for example, downstream co-occurrence heatmaps and `top_pairs(n) `. Use `conditional_probabilities() `instead when you want proper P(metabolite | microbe) probabilities.
