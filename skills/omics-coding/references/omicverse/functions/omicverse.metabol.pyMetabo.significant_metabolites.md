# omicverse.metabol.pyMetabo.significant_metabolites #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.pyMetabo.significant_metabolites`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.pyMetabo.significant_metabolites.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Filter self.deg_table to padj < padj_thresh and |log2fc| ≥ log2fc_thresh .

## Signature

```text
pyMetabo. significant_metabolites ( * , padj_thresh = 0.05 , log2fc_thresh = 1.0 )
```

## Parameters

- `padj_thresh`: ( float (default: 0.05 ))
- `log2fc_thresh`: ( float (default: 1.0 ))

## Full Documentation

# omicverse.metabol.pyMetabo.significant_metabolites #

pyMetabo. significant_metabolites ( * , padj_thresh = 0.05 , log2fc_thresh = 1.0 ) [source] #

Filter `self.deg_table `to padj < `padj_thresh `and |log2fc| ≥ `log2fc_thresh `.

Convenience selector — equivalent to the standard volcano-plot cutoffs. Raises `RuntimeError `if `differential() `hasn’t run. For small-cohort metabolomics studies, consider relaxing `padj_thresh `(e.g. 0.10–0.20) since BH-FDR is conservative.

Parameters :

-
padj_thresh ( `float `(default: `0.05 `))

-
log2fc_thresh ( `float `(default: `1.0 `))
