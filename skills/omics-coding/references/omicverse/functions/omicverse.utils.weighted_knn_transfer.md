# omicverse.utils.weighted_knn_transfer #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.weighted_knn_transfer`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.weighted_knn_transfer.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Annotates query_adata cells with an input trained weighted KNN classifier.

## Signature

```text
omicverse.utils. weighted_knn_transfer ( query_adata , query_adata_emb , ref_adata_obs , label_keys , knn_model , threshold = 1 , pred_unknown = False , mode = 'package' )
```

## Parameters

- `query_adata`: ( AnnData )
- `query_adata_emb`: ( str )
- `ref_adata_obs`: ( DataFrame )
- `label_keys`: ( str )
- `knn_model`: ( KNeighborsTransformer )
- `threshold`: ( int (default: 1 ))
- `pred_unknown`: ( bool (default: False ))
- `mode`: ( str (default: 'package' ))

## Full Documentation

# omicverse.utils.weighted_knn_transfer #

omicverse.utils. weighted_knn_transfer ( query_adata , query_adata_emb , ref_adata_obs , label_keys , knn_model , threshold = 1 , pred_unknown = False , mode = 'package' ) [source] #

Annotates `query_adata `cells with an input trained weighted KNN classifier.

Arguments

query_adata: Annotated dataset to be used to queryate KNN classifier. Embedding to be used query_adata_emb: Name of the obsm layer to be used for label transfer. If set to “X”, query_adata.X will be used ref_adata_obs: obs of ref Anndata label_keys: Names of the columns to be used as target variables (e.g. cell_type) in `query_adata `. knn_model: knn model trained on reference adata with weighted_knn_trainer function threshold: Threshold of uncertainty used to annotating cells as “Unknown”. cells with uncertainties higher than this value will be annotated as “Unknown”. Set to 1 to keep all predictions. This enables one to later on play with thresholds. pred_unknown: `False `by default. Whether to annotate any cell as “unknown” or not. If False , `threshold `will not be used and each cell will be annotated with the label which is the most common in its `n_neighbors `nearest cells. mode: Has to be one of “paper” or “package”. If mode is set to “package”, uncertainties will be 1 - P(pred_label), otherwise it will be 1 - P(true_label).

Returns

pred_labels: Dataframe with predicted labels for each cell in `query_adata `. uncertainties: Dataframe with uncertainties for each cell in `query_adata `.

Parameters :

-
query_adata ( `AnnData `)

-
query_adata_emb ( `str `)

-
ref_adata_obs ( `DataFrame `)

-
label_keys ( `str `)

-
knn_model ( `KNeighborsTransformer `)

-
threshold ( `int `(default: `1 `))

-
pred_unknown ( `bool `(default: `False `))

-
mode ( `str `(default: `'package' `))
