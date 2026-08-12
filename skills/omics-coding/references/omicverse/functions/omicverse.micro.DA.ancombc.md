# omicverse.micro.DA.ancombc #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.DA.ancombc`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.DA.ancombc.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

ANCOM-BC via skbio.stats.composition.ancombc (skbio ≥ 0.7.1).

## Signature

```text
DA. ancombc ( group_key , rank = None , min_prevalence = 0.1 , pseudocount = 1.0 )
```

## Parameters

- `pseudocount`: ( float (default: 1.0 )) – Added to every cell before the test so the matrix has no zeros — scikit-bio’s ANCOM-BC explicitly rejects tables with zero or negative components. 1.0 (the default) is the classic count pseudocount; set to None / 0 to skip the replacement (e.g. if you’ve already applied skbio.stats.composition.multi_replace yourself).
- `note::`: ( .. ) – The scikit-bio ANCOM-BC API is evolving (the 0.7.1 return type is a named-tuple-like bundle, not a DataFrame). This wrapper expects the 0.7.1 shape with attributes lfc / se / W / p / q / diff_abn indexed by feature and will raise NotImplementedError on other shapes so the caller knows to pin scikit-bio.
- `group_key`: ( str )
- `rank`: ( Optional [ str ] (default: None ))
- `min_prevalence`: ( float (default: 0.1 ))

## Full Documentation

# omicverse.micro.DA.ancombc #

DA. ancombc ( group_key , rank = None , min_prevalence = 0.1 , pseudocount = 1.0 ) [source] #

ANCOM-BC via `skbio.stats.composition.ancombc `(skbio ≥ 0.7.1).

Parameters :

-
pseudocount ( `float `(default: `1.0 `)) – Added to every cell before the test so the matrix has no zeros — scikit-bio’s ANCOM-BC explicitly rejects tables with zero or negative components. `1.0 `(the default) is the classic count pseudocount; set to `None `/ `0 `to skip the replacement (e.g. if you’ve already applied `skbio.stats.composition.multi_replace `yourself).

-
note:: ( .. ) – The scikit-bio ANCOM-BC API is evolving (the 0.7.1 return type is a named-tuple-like bundle, not a DataFrame). This wrapper expects the 0.7.1 shape with attributes `lfc / se / W / p / q / diff_abn `indexed by feature and will raise `NotImplementedError `on other shapes so the caller knows to pin scikit-bio.

-
group_key ( `str `)

-
rank ( `Optional `[ `str `] (default: `None `))

-
min_prevalence ( `float `(default: `0.1 `))
