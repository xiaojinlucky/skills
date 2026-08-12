# omicverse.datasets.create_mock_dataset #

- Package: omicverse
- Language: Python
- Function: `omicverse.datasets.create_mock_dataset`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.datasets.create_mock_dataset.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Create a mock single-cell dataset for testing statistical functions.

## Signature

```text
omicverse.datasets. create_mock_dataset ( n_cells = 2000 , n_genes = 1500 , n_cell_types = 6 , with_clustering = False , random_state = 42 )
```

## Parameters

- `n_cells`: ( int ) – Number of cells simulated in mock dataset.
- `n_genes`: ( int ) – Number of genes simulated in mock dataset.
- `n_cell_types`: ( int ) – Number of synthetic cell types.
- `with_clustering`: ( bool ) – Whether to run lightweight preprocessing and clustering-like fields.
- `random_state`: ( int ) – Random seed for deterministic dataset generation.

## Full Documentation

# omicverse.datasets.create_mock_dataset #

omicverse.datasets. create_mock_dataset ( n_cells = 2000 , n_genes = 1500 , n_cell_types = 6 , with_clustering = False , random_state = 42 ) [source] #

Create a mock single-cell dataset for testing statistical functions.

Parameters :

-
n_cells ( int ) – Number of cells simulated in mock dataset.

-
n_genes ( int ) – Number of genes simulated in mock dataset.

-
n_cell_types ( int ) – Number of synthetic cell types.

-
with_clustering ( bool ) – Whether to run lightweight preprocessing and clustering-like fields.

-
random_state ( int ) – Random seed for deterministic dataset generation.

Returns :

Simulated AnnData with expression matrix and basic metadata fields.

Return type :

AnnData
