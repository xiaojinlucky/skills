# omicverse.micro.combine_studies #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.combine_studies`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.combine_studies.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Stitch a list of per-study AnnDatas into a single cross-cohort table.

## Signature

```text
omicverse.micro. combine_studies ( studies , study_names = None , rank = 'genus' , study_key = 'study' , min_prevalence = 0.0 )
```

## Parameters

- `studies`: ( Sequence [ AnnData ] ) – List of per-study AnnData objects (samples × ASVs or pre-collapsed genera). Each must already carry taxonomy columns in var if a rank other than None is requested.
- `study_names`: ( Optional [ Sequence [ str ]] (default: None )) – Optional list aligned with studies to label each cohort. Default: ['study_0', 'study_1', …] .
- `rank`: ( Optional [ str ] (default: 'genus' )) – Collapse each study to this taxonomic rank before concatenating (so feature labels align across studies). Pass None to skip collapsing — only sensible when all studies already share the same ASV ids.
- `study_key`: ( str (default: 'study' )) – Column name to write the per-sample study label into.
- `min_prevalence`: ( float (default: 0.0 )) – Optional per-study prevalence filter applied before union. A taxon has to appear in >= this fraction of samples in at least one study to survive.

## Full Documentation

# omicverse.micro.combine_studies #

omicverse.micro. combine_studies ( studies , study_names = None , rank = 'genus' , study_key = 'study' , min_prevalence = 0.0 ) [source] #

Stitch a list of per-study AnnDatas into a single cross-cohort table.

Parameters :

-
studies ( `Sequence `[ `AnnData `] ) – List of per-study AnnData objects (samples × ASVs or pre-collapsed genera). Each must already carry taxonomy columns in `var `if a `rank `other than None is requested.

-
study_names ( `Optional `[ `Sequence `[ `str `]] (default: `None `)) – Optional list aligned with `studies `to label each cohort. Default: `['study_0', 'study_1', …] `.

-
rank ( `Optional `[ `str `] (default: `'genus' `)) – Collapse each study to this taxonomic rank before concatenating (so feature labels align across studies). Pass `None `to skip collapsing — only sensible when all studies already share the same ASV ids.

-
study_key ( `str `(default: `'study' `)) – Column name to write the per-sample study label into.

-
min_prevalence ( `float `(default: `0.0 `)) – Optional per-study prevalence filter applied before union. A taxon has to appear in >= this fraction of samples in at least one study to survive.

Returns :

Shape `(Σn_samples, n_union_features) `. The `obs `carries the original per-study metadata (inner join on columns shared by all studies) plus `obs[study_key] `. `var `carries the union of feature names (no taxonomy column — the rank collapse already flattened that). `X `is a sparse CSR of `int64 `counts; features absent from a given study are zero.

Return type :

AnnData
