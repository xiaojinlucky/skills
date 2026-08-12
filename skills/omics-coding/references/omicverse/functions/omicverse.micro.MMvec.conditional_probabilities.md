# omicverse.micro.MMvec.conditional_probabilities #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.MMvec.conditional_probabilities`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.MMvec.conditional_probabilities.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Per-microbe P(metabolite | microbe) — softmax of U @ V.T + β .

## Signature

```text
MMvec. conditional_probabilities ( )
```

## Parameters

No parameters detected.

## Full Documentation

# omicverse.micro.MMvec.conditional_probabilities #

MMvec. conditional_probabilities ( ) [source] #

Per-microbe P(metabolite | microbe) — softmax of `U @ V.T + β `.

For each microbe (row), the values across metabolites (columns) sum to 1 — this is what MMvec’s loss directly optimises. Use these when the question is “given that microbe X is present, which metabolite is most likely?” rather than the symmetric co-occurrence question. Numerically stable: subtracts the per-row max before exponentiating.
