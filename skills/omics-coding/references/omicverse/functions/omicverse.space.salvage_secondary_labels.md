# omicverse.space.salvage_secondary_labels #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.salvage_secondary_labels`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.salvage_secondary_labels.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Merge primary and secondary segmentation labels.

## Signature

```text
omicverse.space. salvage_secondary_labels ( adata , primary_label = 'labels_he' , secondary_label = 'labels_gex' , labels_key = 'labels_joint' , ** kwargs )
```

## Parameters

- `adata`: ( AnnData ) – Visium HD AnnData with multiple label layers.
- `primary_label`: ( str , default='labels_he' ) – Primary segmentation label key.
- `secondary_label`: ( str , default='labels_gex' ) – Secondary segmentation label key.
- `labels_key`: ( str , default='labels_joint' ) – Output merged-label key.
- `**kwargs`: – Reserved keyword arguments.

## Full Documentation

# omicverse.space.salvage_secondary_labels #

omicverse.space. salvage_secondary_labels ( adata , primary_label = 'labels_he' , secondary_label = 'labels_gex' , labels_key = 'labels_joint' , ** kwargs ) [source] #

Merge primary and secondary segmentation labels.

Parameters :

-
adata ( AnnData ) – Visium HD AnnData with multiple label layers.

-
primary_label ( str , default='labels_he' ) – Primary segmentation label key.

-
secondary_label ( str , default='labels_gex' ) – Secondary segmentation label key.

-
labels_key ( str , default='labels_joint' ) – Output merged-label key.

-
**kwargs – Reserved keyword arguments.

Returns :

Updates merged labels in `adata `.

Return type :

None
