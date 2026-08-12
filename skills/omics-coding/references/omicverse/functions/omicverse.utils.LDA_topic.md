# omicverse.utils.LDA_topic #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.LDA_topic`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.LDA_topic.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Latent Dirichlet Allocation (LDA) topic modeling for single-cell data using MIRA.

## Signature

```text
class omicverse.utils. LDA_topic ( adata , feature_type = 'expression' , highly_variable_key = 'highly_variable_features' , layers = 'counts' , batch_key = None , learning_rate = 0.001 , ondisk = False )
```

## Parameters

- `adata`: ( anndata.AnnData ) – Single-cell data object.
- `feature_type`: ( str ) – Feature modality passed to MIRA topic model.
- `highly_variable_key`: ( str ) – Var column indicating highly variable features.
- `layers`: ( str ) – Layer key containing count matrix.
- `batch_key`: ( str or None ) – Optional obs covariate for batch-aware modeling.
- `learning_rate`: ( float ) – Learning rate for model optimization.
- `ondisk`: ( bool ) – Whether to use on-disk dataset mode for large datasets.

## Full Documentation

# omicverse.utils.LDA_topic #

class omicverse.utils. LDA_topic ( adata , feature_type = 'expression' , highly_variable_key = 'highly_variable_features' , layers = 'counts' , batch_key = None , learning_rate = 0.001 , ondisk = False ) [source] #

Latent Dirichlet Allocation (LDA) topic modeling for single-cell data using MIRA.

Parameters :

-
adata ( anndata.AnnData ) – Single-cell data object.

-
feature_type ( str ) – Feature modality passed to MIRA topic model.

-
highly_variable_key ( str ) – Var column indicating highly variable features.

-
layers ( str ) – Layer key containing count matrix.

-
batch_key ( str or None ) – Optional obs covariate for batch-aware modeling.

-
learning_rate ( float ) – Learning rate for model optimization.

-
ondisk ( bool ) – Whether to use on-disk dataset mode for large datasets.

Returns :

-
LDA_topic – Topic-model wrapper object.

-
Examples – >>> import omicverse as ov >>> # Basic LDA topic modeling >>> LDA_obj = ov.utils.LDA_topic(adata, feature_type=’expression’, … layers=’counts’) >>> # Determine optimal number of topics >>> LDA_obj.plot_topic_contributions(6) >>> # Fit model and predict topics >>> LDA_obj.predicted(13) >>> # Advanced classification with Random Forest >>> LDA_obj.get_results_rfc(adata, use_rep=’X_pca’, LDA_threshold=0.4)

__init__ ( adata , feature_type = 'expression' , highly_variable_key = 'highly_variable_features' , layers = 'counts' , batch_key = None , learning_rate = 0.001 , ondisk = False ) [source] #

Methods

`__init__ `(adata[, feature_type, ...])

`get_results_rfc `(adata[, use_rep, ...])

`plot_topic_contributions `([num_topics])

`predicted `([num_topics])
