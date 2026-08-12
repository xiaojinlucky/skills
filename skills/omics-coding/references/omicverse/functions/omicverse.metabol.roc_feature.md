# omicverse.metabol.roc_feature #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.roc_feature`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.roc_feature.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Per-feature AUC for a binary class.

## Signature

```text
omicverse.metabol. roc_feature ( adata , * , group_col , pos_group = None , neg_group = None , layer = None , ci = False , n_bootstrap = 1000 , seed = 0 )
```

## Parameters

- `group_col`: ( str ) – Column in adata.obs with the class labels.
- `pos_group`: ( Optional [ str ] (default: None )) – Label strings. If None the first two unique values in group_col are used ( neg_group first, pos_group second — i.e. alphabetical/appearance order).
- `neg_group`: ( Optional [ str ] (default: None )) – Label strings. If None the first two unique values in group_col are used ( neg_group first, pos_group second — i.e. alphabetical/appearance order).
- `layer`: ( Optional [ str ] (default: None )) – AnnData layer name (default None → adata.X ).
- `ci`: ( bool (default: False )) – If True compute bootstrap 95% CI per feature. Costs n_bootstrap × n_features AUC evaluations; default False .
- `n_bootstrap`: ( int (default: 1000 )) – Number of bootstrap resamples per feature. Default 1000.
- `seed`: ( int (default: 0 )) – Bootstrap RNG seed.
- `adata`: ( AnnData )

## Full Documentation

# omicverse.metabol.roc_feature #

omicverse.metabol. roc_feature ( adata , * , group_col , pos_group = None , neg_group = None , layer = None , ci = False , n_bootstrap = 1000 , seed = 0 ) [source] #

Per-feature AUC for a binary class.

Parameters :

-
group_col ( `str `) – Column in `adata.obs `with the class labels.

-
pos_group ( `Optional `[ `str `] (default: `None `)) – Label strings. If `None `the first two unique values in `group_col `are used ( `neg_group `first, `pos_group `second — i.e. alphabetical/appearance order).

-
neg_group ( `Optional `[ `str `] (default: `None `)) – Label strings. If `None `the first two unique values in `group_col `are used ( `neg_group `first, `pos_group `second — i.e. alphabetical/appearance order).

-
layer ( `Optional `[ `str `] (default: `None `)) – AnnData layer name (default `None `→ `adata.X `).

-
ci ( `bool `(default: `False `)) – If True compute bootstrap 95% CI per feature. Costs `n_bootstrap × n_features `AUC evaluations; default `False `.

-
n_bootstrap ( `int `(default: `1000 `)) – Number of bootstrap resamples per feature. Default 1000.

-
seed ( `int `(default: `0 `)) – Bootstrap RNG seed.

-
adata ( `AnnData `)

Returns :

Indexed by feature, sorted by AUC descending, with columns `auc `(and `ci_low `, `ci_high `if `ci=True `).

Return type :

pd.DataFrame
