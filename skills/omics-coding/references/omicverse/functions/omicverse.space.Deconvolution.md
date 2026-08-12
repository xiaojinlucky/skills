# omicverse.space.Deconvolution #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.Deconvolution`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.Deconvolution.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Spatial deconvolution pipeline that aligns scRNA-seq references with spatial transcriptomics.

## Signature

```text
class omicverse.space. Deconvolution ( adata_sp , adata_sc = None )
```

## Parameters

- `adata_sp`: ( AnnData ) – Spatial transcriptomics AnnData object (spots x genes).
- `adata_sc`: ( AnnData or None ) – Single-cell reference AnnData (cells x genes) containing cell-type labels.

## Full Documentation

# omicverse.space.Deconvolution #

class omicverse.space. Deconvolution ( adata_sp , adata_sc = None ) [source] #

Spatial deconvolution pipeline that aligns scRNA-seq references with spatial transcriptomics.

Parameters :

-
adata_sp ( AnnData ) – Spatial transcriptomics AnnData object (spots x genes).

-
adata_sc ( AnnData or None ) – Single-cell reference AnnData (cells x genes) containing cell-type labels.

Returns :

Initializes the deconvolution manager and backend placeholders.

Return type :

None

Examples

```text
>>> decov = ov.space.Deconvolution(adata_sp=adata_sp, adata_sc=adata_sc)
>>> decov.deconvolution(method='Tangram', celltype_key_sc='cell_type')

```

__init__ ( adata_sp , adata_sc = None ) [source] #

Initialize Deconvolution object. :type adata_sp: :param adata_sp: Spatial transcriptomics data. :type adata_sp: AnnData :type adata_sc: default: `None `:param adata_sc: Single-cell RNA-seq reference. If `None `, only spatial object is initialized. :type adata_sc: AnnData or None

Methods

`__init__ `(adata_sp[, adata_sc])

Initialize Deconvolution object.

`cell2location_inference `([sample_kwargs])

Export cell2location posterior and derive normalized cell-type proportions.

`deconvolution `([method, celltype_key_sc, ...])

Infer spot-level cell-type composition from single-cell references.

`impute `([method])

Generate spot-level imputation outputs from a fitted spatial deconvolution model.

`load_cell2location_model `(mod_sp_path)

Load a previously trained cell2location spatial model.

`load_tangram_model `(model_path)

Load a pre-trained Tangram model for downstream projection/inference.

`preprocess_sc `([mode, n_HVGs, target_sum])

Preprocess the scRNA-seq reference before spatial mapping.

`preprocess_sp `([mode, n_svgs, target_sum, ...])

Preprocess spatial transcriptomics data and select spatially variable genes.

`tangram_inference `([sample_kwargs])

Infer spot-level cell-type proportions using a loaded Tangram model.
