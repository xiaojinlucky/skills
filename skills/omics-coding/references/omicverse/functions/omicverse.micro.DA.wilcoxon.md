# omicverse.micro.DA.wilcoxon #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.DA.wilcoxon`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.DA.wilcoxon.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Two-group Mann-Whitney U test per feature.

## Signature

```text
DA. wilcoxon ( group_key , group_a = None , group_b = None , rank = None , relative = True , min_prevalence = 0.1 )
```

## Parameters

- `group_key`: ( str ) – Column in adata.obs holding group labels.
- `group_a`: ( Optional [ str ] (default: None )) – Labels of the two groups to compare. If omitted, the first two unique values (sorted) are used.
- `group_b`: ( Optional [ str ] (default: None )) – Labels of the two groups to compare. If omitted, the first two unique values (sorted) are used.
- `rank`: ( Optional [ str ] (default: None )) – If given, collapse to this taxonomic rank first.
- `relative`: ( bool (default: True )) – Test relative abundances (proportions per sample) rather than raw counts. Mann-Whitney is scale-invariant so this mostly affects the reported fold-change.
- `min_prevalence`: ( float (default: 0.1 )) – Skip features present (>0) in fewer than this fraction of samples.

## Full Documentation

# omicverse.micro.DA.wilcoxon #

DA. wilcoxon ( group_key , group_a = None , group_b = None , rank = None , relative = True , min_prevalence = 0.1 ) [source] #

Two-group Mann-Whitney U test per feature.

Parameters :

-
group_key ( `str `) – Column in `adata.obs `holding group labels.

-
group_a ( `Optional `[ `str `] (default: `None `)) – Labels of the two groups to compare. If omitted, the first two unique values (sorted) are used.

-
group_b ( `Optional `[ `str `] (default: `None `)) – Labels of the two groups to compare. If omitted, the first two unique values (sorted) are used.

-
rank ( `Optional `[ `str `] (default: `None `)) – If given, collapse to this taxonomic rank first.

-
relative ( `bool `(default: `True `)) – Test relative abundances (proportions per sample) rather than raw counts. Mann-Whitney is scale-invariant so this mostly affects the reported fold-change.

-
min_prevalence ( `float `(default: `0.1 `)) – Skip features present (>0) in fewer than this fraction of samples.
