# omicverse.utils.weighted_knn_trainer #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.weighted_knn_trainer`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.weighted_knn_trainer.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Trains a weighted KNN classifier on train_adata .

## Signature

```text
omicverse.utils. weighted_knn_trainer ( train_adata , train_adata_emb , n_neighbors = 50 )
```

## Parameters

- `train_adata`: ( AnnData )
- `train_adata_emb`: ( str )
- `n_neighbors`: ( int (default: 50 ))

## Full Documentation

# omicverse.utils.weighted_knn_trainer #

omicverse.utils. weighted_knn_trainer ( train_adata , train_adata_emb , n_neighbors = 50 ) [source] #

Trains a weighted KNN classifier on `train_adata `.

Arguments

train_adata: :Annotated dataset to be used to train KNN classifier with `label_key `as the target variable. train_adata_emb: Name of the obsm layer to be used for calculation of neighbors. If set to “X”, anndata.X will be used n_neighbors: Number of nearest neighbors in KNN classifier.

Returns

k_neighbors_transformer: KNeighborsTransformer

Parameters :

-
train_adata ( `AnnData `)

-
train_adata_emb ( `str `)

-
n_neighbors ( `int `(default: `50 `))
