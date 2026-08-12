# omicverse.datasets.blobs #

- Package: omicverse
- Language: Python
- Function: `omicverse.datasets.blobs`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.datasets.blobs.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Gaussian Blobs dataset.

## Signature

```text
omicverse.datasets. blobs ( n_variables = 11 , n_centers = 5 , cluster_std = 1.0 , n_observations = 640 , random_state = 0 )
```

## Parameters

- `n_variables`: ( int ) – Feature dimension of generated data.
- `n_centers`: ( int ) – Number of Gaussian cluster centers.
- `cluster_std`: ( float ) – Standard deviation of each Gaussian cluster.
- `n_observations`: ( int ) – Number of synthetic observations (cells).
- `random_state`: ( int ) – Random seed passed to sklearn data generation.

## Full Documentation

# omicverse.datasets.blobs #

omicverse.datasets. blobs ( n_variables = 11 , n_centers = 5 , cluster_std = 1.0 , n_observations = 640 , random_state = 0 ) [source] #

Gaussian Blobs dataset.

Parameters :

-
n_variables ( int ) – Feature dimension of generated data.

-
n_centers ( int ) – Number of Gaussian cluster centers.

-
cluster_std ( float ) – Standard deviation of each Gaussian cluster.

-
n_observations ( int ) – Number of synthetic observations (cells).

-
random_state ( int ) – Random seed passed to sklearn data generation.

Returns :

Synthetic AnnData with `obs['blobs'] `storing cluster labels.

Return type :

AnnData
