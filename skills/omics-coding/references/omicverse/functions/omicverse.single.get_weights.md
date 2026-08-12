# omicverse.single.get_weights #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.get_weights`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.get_weights.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Extract feature loadings for one factor from a MOFA model.

## Signature

```text
omicverse.single. get_weights ( hdf5_path , view , factor , scale = True )
```

## Parameters

- `hdf5_path`: ( str ) – Path to MOFA .hdf5 model file.
- `view`: ( str ) – View/modality name to query.
- `factor`: ( int ) – 1-based factor index.
- `scale`: ( bool ) – If True , rescale weights by maximum absolute value.

## Full Documentation

# omicverse.single.get_weights #

omicverse.single. get_weights ( hdf5_path , view , factor , scale = True ) [source] #

Extract feature loadings for one factor from a MOFA model.

Parameters :

-
hdf5_path ( str ) – Path to MOFA `.hdf5 `model file.

-
view ( str ) – View/modality name to query.

-
factor ( int ) – 1-based factor index.

-
scale ( bool ) – If `True `, rescale weights by maximum absolute value.

Returns :

Feature table containing raw/absolute weights and sign label.

Return type :

pd.DataFrame
