# omicverse.space.visium_10x_hd_cellpose_gex #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.visium_10x_hd_cellpose_gex`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.visium_10x_hd_cellpose_gex.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run expression-image segmentation and map labels back to spatial bins.

## Signature

```text
omicverse.space. visium_10x_hd_cellpose_gex ( adata , obs_key = 'n_counts_adjusted' , log1p = False , mpp = 0.3 , sigma = 5 , gex_save_path = 'stardist/gex_colon.tiff' , prob_thresh = 0.01 , nms_thresh = 0.1 , gpu = True , buffer = 150 , ** kwargs )
```

## Parameters

- `adata`: ( AnnData ) – Visium HD AnnData.
- `obs_key`: ( str , default='n_counts_adjusted' ) – Observation value used to generate gene-expression image.
- `log1p`: ( bool , default=False ) – Whether to log-transform values when generating image.
- `mpp`: ( float , default=0.3 ) – Microns-per-pixel scale.
- `sigma`: ( int , default=5 ) – Gaussian smoothing parameter for grid image generation.
- `gex_save_path`: ( str , default='stardist/gex_colon.tiff' ) – Output path of generated expression image.
- `prob_thresh`: ( float , default=0.01 ) – StarDist probability threshold.
- `nms_thresh`: ( float , default=0.1 ) – StarDist non-max-suppression threshold.
- `gpu`: ( bool , default=True ) – Whether to use GPU in StarDist inference.
- `buffer`: ( int , default=150 ) – Crop buffer used for spatial coordinate key.
- `**kwargs`: – Additional StarDist arguments.

## Full Documentation

# omicverse.space.visium_10x_hd_cellpose_gex #

omicverse.space. visium_10x_hd_cellpose_gex ( adata , obs_key = 'n_counts_adjusted' , log1p = False , mpp = 0.3 , sigma = 5 , gex_save_path = 'stardist/gex_colon.tiff' , prob_thresh = 0.01 , nms_thresh = 0.1 , gpu = True , buffer = 150 , ** kwargs ) [source] #

Run expression-image segmentation and map labels back to spatial bins.

Parameters :

-
adata ( AnnData ) – Visium HD AnnData.

-
obs_key ( str , default='n_counts_adjusted' ) – Observation value used to generate gene-expression image.

-
log1p ( bool , default=False ) – Whether to log-transform values when generating image.

-
mpp ( float , default=0.3 ) – Microns-per-pixel scale.

-
sigma ( int , default=5 ) – Gaussian smoothing parameter for grid image generation.

-
gex_save_path ( str , default='stardist/gex_colon.tiff' ) – Output path of generated expression image.

-
prob_thresh ( float , default=0.01 ) – StarDist probability threshold.

-
nms_thresh ( float , default=0.1 ) – StarDist non-max-suppression threshold.

-
gpu ( bool , default=True ) – Whether to use GPU in StarDist inference.

-
buffer ( int , default=150 ) – Crop buffer used for spatial coordinate key.

-
**kwargs – Additional StarDist arguments.

Returns :

Writes `labels_gex `back into `adata `.

Return type :

None
