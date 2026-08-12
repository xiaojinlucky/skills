# Get available CellTypist models

- Package: scop
- Language: R
- Function: `CellTypistModels`
- Source: https://mengxu98.github.io/scop/reference/CellTypistModels.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/CellTypistModels.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Unified CellTypist model management interface. Use it to list available models, download models, inspect model metadata, extract model markers, subset models, convert models, or delete local models.

## Signature

```text
CellTypistModels( action = c("list", "download", "info", "markers", "subset", "convert", "delete"), on_the_fly = FALSE, model = NULL, force_update = FALSE, cell_type = NULL, top_n = 10, only_positive = TRUE, keep_cell_types = NULL, exclude_cell_types = NULL, output_model_path = NULL, map_file = NULL, sep = ",", convert_from = NULL, convert_to = NULL, unique_only = TRUE, collapse = c("average", "random"), random_state = 0, verbose = TRUE )
```

## Parameters

- `action`: Action to perform. One of "list", "download", "info", "markers", "subset", "convert", or "delete".
- `on_the_fly`: If TRUE, only show downloaded models. If FALSE, show all available models (fetch list from server). Used when action = "list". Default is FALSE.
- `model`: Model name(s) used for actions other than "list".
- `force_update`: Whether to refresh the model index before downloading. Used when action = "download".
- `cell_type`: Cell type used when action = "markers".
- `top_n`: Number of markers to extract when action = "markers".
- `only_positive`: Whether to return only positive markers.
- `keep_cell_types`: Cell types retained when action = "subset".
- `exclude_cell_types`: Cell types removed when action = "subset".
- `output_model_path`: Optional output path used by "subset" or "convert". If NULL, the original model file will be overwritten.
- `map_file`: Optional two-column gene mapping file used by action = "convert".
- `sep`: Delimiter used by map_file.
- `convert_from, convert_to`: Column indices used by map_file.
- `unique_only`: Whether to use only one-to-one mappings in action = "convert".
- `collapse`: How to collapse one-to-many mappings in action = "convert".
- `random_state`: Random seed used when collapse = "random".
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Get available CellTypist models

## Usage

```text
CellTypistModels( action = c("list", "download", "info", "markers", "subset", "convert", "delete"), on_the_fly = FALSE, model = NULL, force_update = FALSE, cell_type = NULL, top_n = 10, only_positive = TRUE, keep_cell_types = NULL, exclude_cell_types = NULL, output_model_path = NULL, map_file = NULL, sep = ",", convert_from = NULL, convert_to = NULL, unique_only = TRUE, collapse = c("average", "random"), random_state = 0, verbose = TRUE )
```

## Description

Unified CellTypist model management interface. Use it to list available models, download models, inspect model metadata, extract model markers, subset models, convert models, or delete local models.

## Value

Depends on action: a data frame, a summary list, or a character vector.

## Examples

```r
\dontrun{
# Get available models
models <- CellTypistModels()
print(models)

# Show downloaded models only
local_models <- CellTypistModels(on_the_fly = TRUE)

# Download a model
CellTypistModels(
  action = "download",
  model = "Immune_All_Low.pkl"
)

# Inspect a model
CellTypistModels(
  action = "info",
  model = "Immune_All_Low.pkl"
)

# Extract top markers for a cell type
CellTypistModels(
  action = "markers",
  model = "Immune_All_Low.pkl",
  cell_type = "B cells",
  top_n = 20
)
}
```
