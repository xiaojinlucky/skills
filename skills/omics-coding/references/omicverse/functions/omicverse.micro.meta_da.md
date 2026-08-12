# omicverse.micro.meta_da #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.meta_da`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.meta_da.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Per-study DA + inverse-variance meta-analysis.

## Signature

```text
omicverse.micro. meta_da ( studies , group_key , group_a = None , group_b = None , method = 'deseq2' , rank = 'genus' , min_prevalence = 0.1 , combine = 'random_effects' , study_names = None , ** method_kwargs )
```

## Parameters

- `studies`: ( Sequence [ AnnData ] ) – List of per-study AnnData objects.
- `group_key`: ( str ) – Same semantics as ov.micro.DA.wilcoxon() / DA.deseq2() / DA.ancombc() . If group_a / group_b are omitted, the two sorted unique values of group_key in the first study are used (and re-used for every study).
- `group_a`: ( Optional [ str ] (default: None )) – Same semantics as ov.micro.DA.wilcoxon() / DA.deseq2() / DA.ancombc() . If group_a / group_b are omitted, the two sorted unique values of group_key in the first study are used (and re-used for every study).
- `group_b`: ( Optional [ str ] (default: None )) – Same semantics as ov.micro.DA.wilcoxon() / DA.deseq2() / DA.ancombc() . If group_a / group_b are omitted, the two sorted unique values of group_key in the first study are used (and re-used for every study).
- `method`: ( str (default: 'deseq2' )) – 'wilcoxon' , 'deseq2' , or 'ancombc' . The per-study effect sizes must be on a log-fold-change scale; Wilcoxon is supported but its reported log2FC has no standard-error, so Wilcoxon meta-DA uses the empirical between-study SE to weight (i.e. every study gets unit weight pre-τ² — still useful as a sanity check).
- `rank`: ( Optional [ str ] (default: 'genus' )) – Collapse to this taxonomic rank in every study before DA, so features align across cohorts. None assumes the studies already share the same feature ids.
- `min_prevalence`: ( float (default: 0.1 )) – Passed through to each per-study DA call.
- `combine`: ( str (default: 'random_effects' )) – 'random_effects' (default; DerSimonian-Laird τ²) or 'fixed_effects' .
- `study_names`: ( Optional [ Sequence [ str ]] (default: None )) – Labels for the per-study result columns; defaults to ['study_0', 'study_1', …] .
- `**method_kwargs`: – Extra kwargs forwarded to the underlying DA call (e.g. pseudocount=0.5 for ancombc).

## Full Documentation

# omicverse.micro.meta_da #

omicverse.micro. meta_da ( studies , group_key , group_a = None , group_b = None , method = 'deseq2' , rank = 'genus' , min_prevalence = 0.1 , combine = 'random_effects' , study_names = None , ** method_kwargs ) [source] #

Per-study DA + inverse-variance meta-analysis.

Parameters :

-
studies ( `Sequence `[ `AnnData `] ) – List of per-study AnnData objects.

-
group_key ( `str `) – Same semantics as `ov.micro.DA.wilcoxon() `/ `DA.deseq2() `/ `DA.ancombc() `. If `group_a `/ `group_b `are omitted, the two sorted unique values of `group_key `in the first study are used (and re-used for every study).

-
group_a ( `Optional `[ `str `] (default: `None `)) – Same semantics as `ov.micro.DA.wilcoxon() `/ `DA.deseq2() `/ `DA.ancombc() `. If `group_a `/ `group_b `are omitted, the two sorted unique values of `group_key `in the first study are used (and re-used for every study).

-
group_b ( `Optional `[ `str `] (default: `None `)) – Same semantics as `ov.micro.DA.wilcoxon() `/ `DA.deseq2() `/ `DA.ancombc() `. If `group_a `/ `group_b `are omitted, the two sorted unique values of `group_key `in the first study are used (and re-used for every study).

-
method ( `str `(default: `'deseq2' `)) – `'wilcoxon' `, `'deseq2' `, or `'ancombc' `. The per-study effect sizes must be on a log-fold-change scale; Wilcoxon is supported but its reported log2FC has no standard-error, so Wilcoxon meta-DA uses the empirical between-study SE to weight (i.e. every study gets unit weight pre-τ² — still useful as a sanity check).

-
rank ( `Optional `[ `str `] (default: `'genus' `)) – Collapse to this taxonomic rank in every study before DA, so features align across cohorts. `None `assumes the studies already share the same feature ids.

-
min_prevalence ( `float `(default: `0.1 `)) – Passed through to each per-study DA call.

-
combine ( `str `(default: `'random_effects' `)) – `'random_effects' `(default; DerSimonian-Laird τ²) or `'fixed_effects' `.

-
study_names ( `Optional `[ `Sequence `[ `str `]] (default: `None `)) – Labels for the per-study result columns; defaults to `['study_0', 'study_1', …] `.

-
**method_kwargs – Extra kwargs forwarded to the underlying DA call (e.g. `pseudocount=0.5 `for ancombc).

Returns :

-
DataFrame indexed by feature with columns

-
-
`combined_lfc `— meta-analytic log2 fold-change estimate

-
-
`combined_se `— standard error of the combined estimate

-
-
`z `— Wald z-score ( `combined_lfc / combined_se `)

-
-
`p_value `/ `fdr_bh `— two-sided p + BH-FDR

-
-
`n_studies `— number of cohorts in which the feature was tested

-
-
`Q `— Cochran’s Q statistic of between-study heterogeneity

-
-
`I2 `— I² heterogeneity (0 → homogeneous, > 75% → high)

-
-
`tau2 `— between-study variance (random-effects only)

-
-
per-study columns `lfc_<study> `and `se_<study> `for traceability
