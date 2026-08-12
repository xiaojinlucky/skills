# omicverse.pp.qc #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.qc`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.qc.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Perform quality control on a dictionary of AnnData objects.

## Signature

```text
omicverse.pp. qc ( adata , * , mode = 'seurat' , min_cells = 3 , min_genes = 200 , nmads = 5 , max_cells_ratio = 1 , max_genes_ratio = 1 , batch_key = None , doublets = True , doublets_method = 'scdblfinder' , filter_doublets = True , path_viz = None , tresh = None , mt_startswith = 'auto' , mt_genes = None , ribo_startswith = ('RPS', 'RPL') , ribo_genes = None , hb_startswith = '^HB[^(P)]' , hb_genes = None , use_gpu = True , batch_wise_mad = None , ** kwargs )
```

## Parameters

- `adata`: – AnnData object
- `mode`: ( str (default: 'seurat' )) – The filtering method to use. Valid options are ‘seurat’
- `'seurat'.`: ( and 'mads'. Default is )
- `min_cells`: ( int (default: 3 )) – The minimum number of cells for a sample to pass QC. Default is 3.
- `min_genes`: ( int (default: 200 )) – The minimum number of genes for a cell to pass QC. Default is 200.
- `max_cells_ratio`: ( float (default: 1 )) – The maximum number of cells ratio for a sample to pass QC. Default is 1.
- `max_genes_ratio`: ( float (default: 1 )) – The maximum number of genes ratio for a cell to pass QC. Default is 1.
- `nmads`: ( int (default: 5 )) – The number of MADs to use for MADs filtering. Default is 5.
- `doublets`: ( bool (default: True )) – Whether to perform doublet detection. Default is True.
- `doublets_method`: ( str (default: 'scdblfinder' )) – The doublet detection method to use. Options are ‘scrublet’, ‘sccomposite’, ‘doubletfinder’, or ‘scdblfinder’. Default is ‘scdblfinder’ (Python port of R scDblFinder; xgboost on kNN+cxds features) for cpu and cpu-gpu-mixed modes, falling back to ‘scrublet’ if pyscdblfinder is not installed. The RAPIDS gpu mode keeps ‘scrublet’ as default for backwards compatibility.
- `filter_doublets`: ( bool (default: True )) – Whether to filter out doublets (True) or just flag them (False). Default is True.
- `path_viz`: (default: None ) – The path to save the QC plots. Default is None.
- `tresh`: (default: None ) – A dictionary of QC thresholds. The keys should be ‘mito_perc’,
- `'nUMIs'`: – Only used if mode is ‘seurat’. Default is None.
- `'detected_genes'.`: ( and ) – Only used if mode is ‘seurat’. Default is None.
- `mt_startswith`: ( str (default: 'auto' )) – The prefix of mitochondrial genes. Default is ‘auto’, which automatically detects the prefix (e.g. ‘MT-’ for human, ‘mt-’ for mouse). Set explicitly (e.g. ‘MT-’) to override.
- `mt_genes`: (default: None ) – The list of mitochondrial genes. Default is None.
- `None`: ( if mt_genes is not )
- `ignored.`: ( mt_startswith will be )
- `batch_key`: Detected from function signature; no parameter description detected.
- `ribo_startswith`: Detected from function signature; no parameter description detected.
- `ribo_genes`: Detected from function signature; no parameter description detected.
- `hb_startswith`: Detected from function signature; no parameter description detected.
- `hb_genes`: Detected from function signature; no parameter description detected.
- `use_gpu`: Detected from function signature; no parameter description detected.
- `batch_wise_mad`: Detected from function signature; no parameter description detected.
- `**kwargs`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.pp.qc #

omicverse.pp. qc ( adata , * , mode = 'seurat' , min_cells = 3 , min_genes = 200 , nmads = 5 , max_cells_ratio = 1 , max_genes_ratio = 1 , batch_key = None , doublets = True , doublets_method = 'scdblfinder' , filter_doublets = True , path_viz = None , tresh = None , mt_startswith = 'auto' , mt_genes = None , ribo_startswith = ('RPS', 'RPL') , ribo_genes = None , hb_startswith = '^HB[^(P)]' , hb_genes = None , use_gpu = True , batch_wise_mad = None , ** kwargs ) [source] #

Perform quality control on a dictionary of AnnData objects.

Parameters :

-
adata – AnnData object

-
mode ( `str `(default: `'seurat' `)) – The filtering method to use. Valid options are ‘seurat’

-
'seurat'. ( and 'mads'. Default is )

-
min_cells ( `int `(default: `3 `)) – The minimum number of cells for a sample to pass QC. Default is 3.

-
min_genes ( `int `(default: `200 `)) – The minimum number of genes for a cell to pass QC. Default is 200.

-
max_cells_ratio ( `float `(default: `1 `)) – The maximum number of cells ratio for a sample to pass QC. Default is 1.

-
max_genes_ratio ( `float `(default: `1 `)) – The maximum number of genes ratio for a cell to pass QC. Default is 1.

-
nmads ( `int `(default: `5 `)) – The number of MADs to use for MADs filtering. Default is 5.

-
doublets ( `bool `(default: `True `)) – Whether to perform doublet detection. Default is True.

-
doublets_method ( `str `(default: `'scdblfinder' `)) – The doublet detection method to use. Options are ‘scrublet’, ‘sccomposite’, ‘doubletfinder’, or ‘scdblfinder’. Default is ‘scdblfinder’ (Python port of R scDblFinder; xgboost on kNN+cxds features) for cpu and cpu-gpu-mixed modes, falling back to ‘scrublet’ if pyscdblfinder is not installed. The RAPIDS gpu mode keeps ‘scrublet’ as default for backwards compatibility.

-
filter_doublets ( `bool `(default: `True `)) – Whether to filter out doublets (True) or just flag them (False). Default is True.

-
path_viz (default: `None `) – The path to save the QC plots. Default is None.

-
tresh (default: `None `) – A dictionary of QC thresholds. The keys should be ‘mito_perc’,

-
'nUMIs' – Only used if mode is ‘seurat’. Default is None.

-
'detected_genes'. ( and ) – Only used if mode is ‘seurat’. Default is None.

-
mt_startswith ( `str `(default: `'auto' `)) – The prefix of mitochondrial genes. Default is ‘auto’, which automatically detects the prefix (e.g. ‘MT-’ for human, ‘mt-’ for mouse). Set explicitly (e.g. ‘MT-’) to override.

-
mt_genes (default: `None `) – The list of mitochondrial genes. Default is None.

-
None ( if mt_genes is not )

-
ignored. ( mt_startswith will be )

Returns :

An AnnData object containing cells that passed QC filters.

Return type :

adata

Examples

```text
>>> import omicverse as ov
>>> adata = ov.pp.qc(adata, tresh={'mito_perc': 0.2, 'nUMIs': 500, 'detected_genes': 250})
>>> adata = ov.pp.qc(adata, mode='mads', nmads=5, doublets=True)
>>> # Auto-detects 'mt-' for mouse data
>>> adata = ov.pp.qc(adata)
>>> # Explicit prefix
>>> adata = ov.pp.qc(adata, mt_startswith='mt-')

```

Parameters :

use_gpu ( `bool `(default: `True `))
