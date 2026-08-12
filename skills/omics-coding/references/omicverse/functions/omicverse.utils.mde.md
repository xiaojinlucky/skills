# omicverse.utils.mde #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.mde`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.mde.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Util to run pymde.preserve_neighbors() for visualization of scvi-tools embeddings.

## Signature

```text
omicverse.utils. mde ( data , device = None , ** kwargs )
```

## Parameters

- `data`: ( Union [ ndarray , DataFrame , spmatrix , Tensor ] ) – The data of shape (n_obs, k), where k is typically defined by one of the models in scvi-tools that produces an embedding (e.g., SCVI .)
- `device`: ( Optional [ Literal [ 'cpu' , 'cuda' ]] (default: None )) – Whether to run on cpu or gpu (“cuda”). If None, tries to run on gpu if available.
- `kwargs`: – Keyword args to pymde.preserve_neighbors()
- `**kwargs`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.utils.mde #

omicverse.utils. mde ( data , device = None , ** kwargs ) [source] #

Util to run `pymde.preserve_neighbors() `for visualization of scvi-tools embeddings.

Parameters :

-
data ( `Union `[ `ndarray `, `DataFrame `, `spmatrix `, `Tensor `] ) – The data of shape (n_obs, k), where k is typically defined by one of the models in scvi-tools that produces an embedding (e.g., `SCVI `.)

-
device ( `Optional `[ `Literal `[ `'cpu' `, `'cuda' `]] (default: `None `)) – Whether to run on cpu or gpu (“cuda”). If None, tries to run on gpu if available.

-
kwargs – Keyword args to `pymde.preserve_neighbors() `

Return type :

The pymde embedding, defaults to two dimensions.

Notes

This function is included in scvi-tools to provide an alternative to UMAP/TSNE that is GPU- accelerated. The appropriateness of use of visualization of high-dimensional spaces in single- cell omics remains an open research questions. See:

Chari, Tara, Joeyta Banerjee, and Lior Pachter. “The specious art of single-cell genomics.” bioRxiv (2021).

If you use this function in your research please cite:

Agrawal, Akshay, Alnur Ali, and Stephen Boyd. “Minimum-distortion embedding.” arXiv preprint arXiv:2103.02559 (2021).

Examples

```text
>>> adata = anndata.read_h5ad(path_to_anndata)
>>> scvi.model.SCVI.setup_anndata(adata, batch_key="batch")
>>> vae = scvi.model.SCVI(adata)
>>> vae.train()
>>> adata.obsm["X_scVI"] = vae.get_latent_representation()
>>> adata.obsm["X_mde"] = scvi.model.utils.mde(adata.obsm["X_scVI"])

```
