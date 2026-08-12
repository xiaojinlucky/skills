# omicverse.space.CAST #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.CAST`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.CAST.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

CAST (Cell Annotation for Spatial Transcriptomics) embedding for multiple spatial samples.

## Signature

```text
omicverse.space. CAST ( adata , sample_key = None , basis = 'spatial' , layer = 'norm_1e4' , output_path = 'output/CAST_Mark' , gpu_t = 0 , device = 'cuda:0' , ** kwargs )
```

## Parameters

- `adata`: ( anndata.AnnData ) – Multi-sample spatial AnnData object.
- `sample_key`: ( str , optional ) – Column in adata.obs identifying sample/batch labels.
- `basis`: ( str , default="spatial" ) – Key in adata.obsm storing spatial coordinates.
- `layer`: ( str , default="norm_1e4" ) – Layer key containing normalized expression used by CAST.
- `output_path`: ( str , default="output/CAST_Mark" ) – Directory for CAST intermediate files and outputs.
- `gpu_t`: ( int , default=0 ) – GPU index used by CAST backend.
- `device`: ( str , default="cuda:0" ) – Torch device string passed to CAST backend.
- `**kwargs`: – Extra keyword arguments forwarded to CAST_MARK .

## Full Documentation

# omicverse.space.CAST #

omicverse.space. CAST ( adata , sample_key = None , basis = 'spatial' , layer = 'norm_1e4' , output_path = 'output/CAST_Mark' , gpu_t = 0 , device = 'cuda:0' , ** kwargs ) [source] #

CAST (Cell Annotation for Spatial Transcriptomics) embedding for multiple spatial samples.

This function implements the CAST algorithm to learn unified embeddings across multiple spatial transcriptomics samples, enabling joint analysis and integration of spatial data from different sources.

Parameters :

-
adata ( anndata.AnnData ) – Multi-sample spatial AnnData object.

-
sample_key ( str , optional ) – Column in `adata.obs `identifying sample/batch labels.

-
basis ( str , default="spatial" ) – Key in `adata.obsm `storing spatial coordinates.

-
layer ( str , default="norm_1e4" ) – Layer key containing normalized expression used by CAST.

-
output_path ( str , default="output/CAST_Mark" ) – Directory for CAST intermediate files and outputs.

-
gpu_t ( int , default=0 ) – GPU index used by CAST backend.

-
device ( str , default="cuda:0" ) – Torch device string passed to CAST backend.

-
**kwargs – Extra keyword arguments forwarded to `CAST_MARK `.

Returns :

-
anndata.AnnData – Updated AnnData with embedding saved in `adata.obsm['X_cast'] `.

-
Notes –

-
Requires normalized expression data in specified layer

-
GPU acceleration is enabled by default

-
Creates output directory if it doesn’t exist

-
Progress is shown with tqdm progress bars

-
Examples – >>> import scanpy as sc >>> import omicverse as ov >>> # Load multiple samples >>> adata = sc.read_h5ad(‘spatial_samples.h5ad’) >>> # Run CAST integration >>> adata = ov.space.CAST( … adata, … sample_key=’sample_id’, … basis=’spatial’, … layer=’normalized_counts’ … ) >>> # Access CAST embeddings >>> cast_embeddings = adata.obsm[‘X_cast’]
