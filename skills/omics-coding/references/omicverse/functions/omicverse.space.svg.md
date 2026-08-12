# omicverse.space.svg #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.svg`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.svg.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Identify spatially variable genes using multiple methods.

## Signature

```text
omicverse.space. svg ( adata , mode = 'prost' , n_svgs = 3000 , target_sum = 500000.0 , platform = 'visium' , mt_startwith = 'MT-' , ** kwargs )
```

## Parameters

- `adata`: ( AnnData ) – Spatial AnnData containing expression matrix and coordinates in adata.obsm['spatial'] .
- `mode`: ( {'prost' , 'pearsonr' , 'spateo' , 'somde' , 'spatialde'} , default='prost' ) – SVG detection backend.
- `n_svgs`: ( int , default=3000 ) – Number of spatially variable genes to select.
- `target_sum`: ( float , default=50*1e4 ) – Target-sum used during normalization.
- `platform`: ( str , default='visium' ) – Platform identifier used by PROST preprocessing.
- `mt_startwith`: ( str , default='MT-' ) – Mitochondrial gene prefix excluded by default.
- `**kwargs`: – Additional method-specific options. For somde : k , qval_threshold , retrain_epoch . For spatialde : qval_threshold , min_total_count , regress_formula , n_jobs , kernel_space , approx_rank , approx_seed , approx_models , show_progress .

## Full Documentation

# omicverse.space.svg #

omicverse.space. svg ( adata , mode = 'prost' , n_svgs = 3000 , target_sum = 500000.0 , platform = 'visium' , mt_startwith = 'MT-' , ** kwargs ) [source] #

Identify spatially variable genes using multiple methods.

This function identifies genes that show significant spatial variation in their expression patterns across the tissue. It supports multiple methods including PROST (Pattern RecognitiOn of Spatial Transcriptomics), Pearson correlation, and Spateo-based analysis.

Parameters :

-
adata ( AnnData ) – Spatial AnnData containing expression matrix and coordinates in `adata.obsm['spatial'] `.

-
mode ( {'prost' , 'pearsonr' , 'spateo' , 'somde' , 'spatialde'} , default='prost' ) – SVG detection backend.

-
n_svgs ( int , default=3000 ) – Number of spatially variable genes to select.

-
target_sum ( float , default=50*1e4 ) – Target-sum used during normalization.

-
platform ( str , default='visium' ) – Platform identifier used by PROST preprocessing.

-
mt_startwith ( str , default='MT-' ) – Mitochondrial gene prefix excluded by default.

-
**kwargs – Additional method-specific options. For `somde `: `k `, `qval_threshold `, `retrain_epoch `. For `spatialde `: `qval_threshold `, `min_total_count `, `regress_formula `, `n_jobs `, `kernel_space `, `approx_rank `, `approx_seed `, `approx_models `, `show_progress `.

Returns :

-
AnnData – Updated AnnData with SVG flags in `adata.var['space_variable_features'] `and `adata.var['highly_variable'] `.

-
Notes –

-
PROST mode requires opencv-python package

-

Different modes use different statistical approaches:

-
PROST: Pattern recognition and spatial autocorrelation

-
pearsonr: Correlation between gene expression and spatial coordinates

-
spateo: Wasserstein distance-based spatial variation

-
somde: SOM-compressed SpatialDE GP test (fast for large datasets)

-
SOMDE kwargs: `k `(cells/node, default 20), `qval_threshold `(default 0.05), `retrain_epoch `(extra SOM epochs, default 0)

-
SOMDE stores `adata.var['somde_LLR'] `, `somde_pval `, `somde_qval `, `somde_FSV `

-
SOMDE requires `somoclu `and `patsy `

-
spatialde: GP-based test directly on single-cell coordinates (no SOM compression), uses bundled NaiveDE + SpatialDE packages from `omicverse/external/ `

-
SpatialDE kwargs: `qval_threshold `(default 0.05), `min_total_count `(default 3), `regress_formula `(default `'np.log(total_counts)' `), `n_jobs `(default `1 `), `kernel_space `(optional custom covariance search space), `approx_rank `(optional Nyström low-rank approximation rank), `approx_seed `(landmark sampling seed), `approx_models `(kernel list for approximation, default `('SE',) `), `show_progress `(whether to show tqdm progress bars, default `True `)

-
SpatialDE stores `adata.var['spatialde_LLR'] `, `spatialde_pval `, `spatialde_qval `, `spatialde_FSV `, `spatialde_l `

-
SpatialDE requires `patsy `and `tqdm `

-
Mitochondrial genes are excluded by default

-
Results are normalized and log-transformed

-
Examples – >>> import scanpy as sc >>> import omicverse as ov >>> # Load spatial data >>> adata = sc.read_visium(…) >>> # Find SVGs using PROST >>> adata = ov.space.svg( … adata, … mode=’prost’, … n_svgs=2000, … platform=’visium’ … ) >>> # Access SVGs >>> svgs = adata.var_names[adata.var[‘space_variable_features’]]
