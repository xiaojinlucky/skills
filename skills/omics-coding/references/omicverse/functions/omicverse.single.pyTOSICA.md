# omicverse.single.pyTOSICA #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.pyTOSICA`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.pyTOSICA.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

TOSICA wrapper for pathway-informed transformer-based cell-type annotation.

## Signature

```text
class omicverse.single. pyTOSICA ( adata , project_path , gmt_path = None , label_name = 'Celltype' , mask_ratio = 0.015 , max_g = 300 , max_gs = 300 , n_unannotated = 1 , embed_dim = 48 , depth = 1 , num_heads = 4 , batch_size = 8 , device = 'cuda:0' , auto_download = True )
```

## Parameters

- `adata`: ( anndata.AnnData ) – Training/reference AnnData with labels.
- `project_path`: ( str ) – Output directory for TOSICA checkpoints and logs.
- `gmt_path`: ( str | None , optional , default=None ) – Pathway GMT file path. If None , default gene-set resources are used.
- `label_name`: ( str , optional , default='Celltype' ) – Label column in adata.obs .
- `mask_ratio`: ( float , optional , default=0.015 ) – Ratio of masked genes/tokens used for training regularization.
- `max_g`: ( int , optional , default=300 ) – Maximum number of genes used per pathway/tokenization unit.
- `max_gs`: ( int , optional , default=300 ) – Maximum number of gene sets used in the model.
- `n_unannotated`: ( int , optional , default=1 ) – Number of unlabeled classes reserved during training.
- `embed_dim`: ( int , optional , default=48 ) – Transformer embedding dimension.
- `depth`: ( int , optional , default=1 ) – Number of transformer encoder layers.
- `num_heads`: ( int , optional , default=4 ) – Number of attention heads.
- `batch_size`: ( int , optional , default=8 ) – Mini-batch size used during training/inference.
- `device`: ( str , optional , default='cuda:0' ) – Device used for model training/inference.
- `auto_download`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.single.pyTOSICA #

class omicverse.single. pyTOSICA ( adata , project_path , gmt_path = None , label_name = 'Celltype' , mask_ratio = 0.015 , max_g = 300 , max_gs = 300 , n_unannotated = 1 , embed_dim = 48 , depth = 1 , num_heads = 4 , batch_size = 8 , device = 'cuda:0' , auto_download = True ) [source] #

TOSICA wrapper for pathway-informed transformer-based cell-type annotation.

Parameters :

-
adata ( anndata.AnnData ) – Training/reference AnnData with labels.

-
project_path ( str ) – Output directory for TOSICA checkpoints and logs.

-
gmt_path ( str | None , optional , default=None ) – Pathway GMT file path. If `None `, default gene-set resources are used.

-
label_name ( str , optional , default='Celltype' ) – Label column in `adata.obs `.

-
mask_ratio ( float , optional , default=0.015 ) – Ratio of masked genes/tokens used for training regularization.

-
max_g ( int , optional , default=300 ) – Maximum number of genes used per pathway/tokenization unit.

-
max_gs ( int , optional , default=300 ) – Maximum number of gene sets used in the model.

-
n_unannotated ( int , optional , default=1 ) – Number of unlabeled classes reserved during training.

-
embed_dim ( int , optional , default=48 ) – Transformer embedding dimension.

-
depth ( int , optional , default=1 ) – Number of transformer encoder layers.

-
num_heads ( int , optional , default=4 ) – Number of attention heads.

-
batch_size ( int , optional , default=8 ) – Mini-batch size used during training/inference.

-
device ( str , optional , default='cuda:0' ) – Device used for model training/inference.

Returns :

Initializes TOSICA model configuration and training resources.

Return type :

None

Examples

```text
>>> tosica_obj = ov.single.pyTOSICA(adata=ref_adata, project_path="./tosica")

```

Parameters :

auto_download ( `bool `(default: `True `))

__init__ ( adata , project_path , gmt_path = None , label_name = 'Celltype' , mask_ratio = 0.015 , max_g = 300 , max_gs = 300 , n_unannotated = 1 , embed_dim = 48 , depth = 1 , num_heads = 4 , batch_size = 8 , device = 'cuda:0' , auto_download = True ) [source] #

Initialize a pyTOSICA object for cell type classification.

Parameters :

-
adata ( anndata.AnnData ) – Training/reference AnnData for TOSICA.

-
project_path ( str ) – Directory used to save masks, labels, checkpoints, and logs.

-
gmt_path ( str or None ) – Pathway GMT identifier/path. If `None `, full-connection mask is used.

-
label_name ( str ) – Label column in `adata.obs `.

-
mask_ratio ( float ) – Random mask ratio used when pathway mask is unavailable.

-
max_g ( int ) – Maximum number of genes per pathway.

-
max_gs ( int ) – Maximum number of pathway tokens used by the model.

-
n_unannotated ( int ) – Number of extra unannotated tokens appended to pathway mask.

-
embed_dim ( int ) – Transformer embedding dimension.

-
depth ( int ) – Number of transformer layers.

-
num_heads ( int ) – Number of attention heads.

-
batch_size ( int ) – Training batch size.

-
device ( str ) – Preferred device string (for example `'cuda:0' `).

-
auto_download ( `bool `(default: `True `))

Methods

`__init__ `(adata, project_path[, gmt_path, ...])

Initialize a pyTOSICA object for cell type classification.

`load `([load_path])

Load a pre-trained TOSICA model.

`predicted `(pre_adata[, laten, n_step, ...])

Predict cell types for new single-cell data.

`save `([save_path])

Save the trained TOSICA model.

`train `([pre_weights, lr, epochs, lrf])

Train the TOSICA model for cell type classification.
