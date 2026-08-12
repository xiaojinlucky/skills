# omicverse.space.visium_10x_hd_cellpose_expand #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.visium_10x_hd_cellpose_expand`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.visium_10x_hd_cellpose_expand.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Expand segmentation labels from nuclei to nearby bins.

## Signature

```text
omicverse.space. visium_10x_hd_cellpose_expand ( adata , max_bin_distance = 4 , labels_key = 'labels_he' , expanded_labels_key = 'labels_he_expanded' , ** kwargs )
```

## Parameters

- `adata`: ( AnnData ) – Visium HD AnnData containing primary segmentation labels.
- `max_bin_distance`: ( int , default=4 ) – Maximum bin distance for expansion.
- `labels_key`: ( str , default='labels_he' ) – Source label column/key.
- `expanded_labels_key`: ( str , default='labels_he_expanded' ) – Output label key for expanded labels.
- `**kwargs`: – Extra arguments forwarded to expand_labels .

## Full Documentation

# omicverse.space.visium_10x_hd_cellpose_expand #

omicverse.space. visium_10x_hd_cellpose_expand ( adata , max_bin_distance = 4 , labels_key = 'labels_he' , expanded_labels_key = 'labels_he_expanded' , ** kwargs ) [source] #

Expand segmentation labels from nuclei to nearby bins.

Parameters :

-
adata ( AnnData ) – Visium HD AnnData containing primary segmentation labels.

-
max_bin_distance ( int , default=4 ) – Maximum bin distance for expansion.

-
labels_key ( str , default='labels_he' ) – Source label column/key.

-
expanded_labels_key ( str , default='labels_he_expanded' ) – Output label key for expanded labels.

-
**kwargs – Extra arguments forwarded to `expand_labels `.

Returns :

Updates labels in `adata `in place.

Return type :

None
