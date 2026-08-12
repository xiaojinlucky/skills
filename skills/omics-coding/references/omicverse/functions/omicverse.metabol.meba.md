# omicverse.metabol.meba #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.meba`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.meba.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Per-feature Hotelling T-squared for two-group time-course comparison.

## Signature

```text
omicverse.metabol. meba ( adata , * , group_col , time_col , subject_col , groups = None , layer = None )
```

## Parameters

- `group_col`: ( str ) – Column in adata.obs with the two-class labels.
- `time_col`: ( str ) – Column in adata.obs giving the time point (any type castable to str; ordering inferred from pd.unique to preserve appearance order).
- `subject_col`: ( str ) – Column in adata.obs identifying each subject. The same subject must appear at every time point in one (and only one) group.
- `groups`: ( Optional [ tuple ] (default: None )) – (group_a, group_b) pair. None → first two unique values.
- `layer`: ( Optional [ str ] (default: None )) – AnnData layer (default None → adata.X ).
- `adata`: ( AnnData )

## Full Documentation

# omicverse.metabol.meba #

omicverse.metabol. meba ( adata , * , group_col , time_col , subject_col , groups = None , layer = None ) [source] #

Per-feature Hotelling T-squared for two-group time-course comparison.

For each feature, build a `(n_subjects, n_timepoints) `matrix per group — each row is one subject’s time course. Hotelling’s two-sample T-squared tests whether the two groups have the same mean time-course vector, returning an F-distributed statistic.

The design must be balanced : every subject observed at every time point. Subjects missing any cell are dropped and listed in `result.attrs['dropped_subjects'] `.

Parameters :

-
group_col ( `str `) – Column in `adata.obs `with the two-class labels.

-
time_col ( `str `) – Column in `adata.obs `giving the time point (any type castable to str; ordering inferred from `pd.unique `to preserve appearance order).

-
subject_col ( `str `) – Column in `adata.obs `identifying each subject. The same subject must appear at every time point in one (and only one) group.

-
groups ( `Optional `[ `tuple `] (default: `None `)) – `(group_a, group_b) `pair. `None `→ first two unique values.

-
layer ( `Optional `[ `str `] (default: `None `)) – AnnData layer (default `None `→ `adata.X `).

-
adata ( `AnnData `)

Returns :

Indexed by metabolite, columns `T2, F, df1, df2, pvalue, padj, n_a, n_b, k `.

Return type :

pd.DataFrame
