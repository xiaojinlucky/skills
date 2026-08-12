# omicverse.metabol.biomarker_panel #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.biomarker_panel`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.biomarker_panel.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Nested-CV evaluation of a multi-metabolite biomarker panel.

## Signature

```text
omicverse.metabol. biomarker_panel ( adata , * , group_col , features = 10 , classifier = 'rf' , cv_outer = 5 , cv_inner = 3 , pos_group = None , neg_group = None , n_permutations = 0 , layer = None , seed = 0 )
```

## Parameters

- `group_col`: ( str ) – Column in adata.obs with the class labels.
- `features`: ( Union [ list , int ] (default: 10 )) – Either a list of metabolite names to use as-is, or an integer N to pre-screen the top- N metabolites by univariate AUC on the full dataset (note: this leaks test-fold information — see “Caveats” below). Default 10.
- `classifier`: ( str (default: 'rf' )) – "rf" (RandomForest, default), "lr" (L2-logistic regression), or "svm" (RBF SVM).
- `cv_outer`: ( int (default: 5 )) – Stratified K-fold counts. Default 5-outer × 3-inner.
- `cv_inner`: ( int (default: 3 )) – Stratified K-fold counts. Default 5-outer × 3-inner.
- `pos_group`: ( Optional [ str ] (default: None )) – Class labels to contrast. None → first two unique values.
- `neg_group`: ( Optional [ str ] (default: None )) – Class labels to contrast. None → first two unique values.
- `n_permutations`: ( int (default: 0 )) – If > 0, compute a permutation null by shuffling labels and re-running nested CV that many times. Reported as permutation_pvalue . Expensive (each permutation costs cv_outer × cv_inner fits).
- `layer`: ( Optional [ str ] (default: None )) – AnnData layer name (default None → adata.X ).
- `seed`: ( int (default: 0 )) – RNG / fold-assignment seed.
- `adata`: ( AnnData )

## Full Documentation

# omicverse.metabol.biomarker_panel #

omicverse.metabol. biomarker_panel ( adata , * , group_col , features = 10 , classifier = 'rf' , cv_outer = 5 , cv_inner = 3 , pos_group = None , neg_group = None , n_permutations = 0 , layer = None , seed = 0 ) [source] #

Nested-CV evaluation of a multi-metabolite biomarker panel.

Parameters :

-
group_col ( `str `) – Column in `adata.obs `with the class labels.

-
features ( `Union `[ `list `, `int `] (default: `10 `)) – Either a list of metabolite names to use as-is, or an integer `N `to pre-screen the top- `N `metabolites by univariate AUC on the full dataset (note: this leaks test-fold information — see “Caveats” below). Default 10.

-
classifier ( `str `(default: `'rf' `)) – `"rf" `(RandomForest, default), `"lr" `(L2-logistic regression), or `"svm" `(RBF SVM).

-
cv_outer ( `int `(default: `5 `)) – Stratified K-fold counts. Default 5-outer × 3-inner.

-
cv_inner ( `int `(default: `3 `)) – Stratified K-fold counts. Default 5-outer × 3-inner.

-
pos_group ( `Optional `[ `str `] (default: `None `)) – Class labels to contrast. `None `→ first two unique values.

-
neg_group ( `Optional `[ `str `] (default: `None `)) – Class labels to contrast. `None `→ first two unique values.

-
n_permutations ( `int `(default: `0 `)) – If > 0, compute a permutation null by shuffling labels and re-running nested CV that many times. Reported as `permutation_pvalue `. Expensive (each permutation costs `cv_outer × cv_inner `fits).

-
layer ( `Optional `[ `str `] (default: `None `)) – AnnData layer name (default `None `→ `adata.X `).

-
seed ( `int `(default: `0 `)) – RNG / fold-assignment seed.

-
adata ( `AnnData `)

Returns :

-
BiomarkerPanelResult

-
Caveats

-
——-

-
When `features `is an integer the pre-screen uses the full

-
dataset, which overestimates AUC on the same folds. For

-
publication-grade estimates pass an explicit feature list chosen

-
from an independent screening cohort, or pre-screen inside a

-
wrapper that repeats the full pipeline per fold.
