# omicverse.single.cNMF #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.cNMF`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.cNMF.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Consensus NMF workflow wrapper for robust gene-program discovery.

## Signature

```text
class omicverse.single. cNMF ( adata , components , n_iter = 100 , densify = False , tpm_fn = None , seed = None , beta_loss = 'frobenius' , num_highvar_genes = 2000 , genes_file = None , alpha_usage = 0.0 , alpha_spectra = 0.0 , init = 'random' , output_dir = None , name = None , use_gpu = True , gpu_id = 0 )
```

## Parameters

- `adata`: ( AnnData ) – Input single-cell expression AnnData.
- `components`: ( array-like ) – Candidate rank values (number of programs/topics) to evaluate.
- `n_iter`: ( int , default=100 ) – Number of NMF restarts per rank.
- `output_dir`: ( str , optional ) – Directory used to store temporary and result files.
- `name`: ( str , optional ) – Analysis name prefix for output artifacts.
- `use_gpu`: ( bool , default=True ) – Whether to use GPU-accelerated factorization when available.
- `gpu_id`: ( int , default=0 ) – CUDA device index.
- `densify`: Detected from function signature; no parameter description detected.
- `tpm_fn`: Detected from function signature; no parameter description detected.
- `seed`: Detected from function signature; no parameter description detected.
- `beta_loss`: Detected from function signature; no parameter description detected.
- `num_highvar_genes`: Detected from function signature; no parameter description detected.
- `genes_file`: Detected from function signature; no parameter description detected.
- `alpha_usage`: Detected from function signature; no parameter description detected.
- `alpha_spectra`: Detected from function signature; no parameter description detected.
- `init`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.single.cNMF #

class omicverse.single. cNMF ( adata , components , n_iter = 100 , densify = False , tpm_fn = None , seed = None , beta_loss = 'frobenius' , num_highvar_genes = 2000 , genes_file = None , alpha_usage = 0.0 , alpha_spectra = 0.0 , init = 'random' , output_dir = None , name = None , use_gpu = True , gpu_id = 0 ) [source] #

Consensus NMF workflow wrapper for robust gene-program discovery.

Parameters :

-
adata ( AnnData ) – Input single-cell expression AnnData.

-
components ( array-like ) – Candidate rank values (number of programs/topics) to evaluate.

-
n_iter ( int , default=100 ) – Number of NMF restarts per rank.

-
output_dir ( str , optional ) – Directory used to store temporary and result files.

-
name ( str , optional ) – Analysis name prefix for output artifacts.

-
use_gpu ( bool , default=True ) – Whether to use GPU-accelerated factorization when available.

-
gpu_id ( int , default=0 ) – CUDA device index.

__init__ ( adata , components , n_iter = 100 , densify = False , tpm_fn = None , seed = None , beta_loss = 'frobenius' , num_highvar_genes = 2000 , genes_file = None , alpha_usage = 0.0 , alpha_spectra = 0.0 , init = 'random' , output_dir = None , name = None , use_gpu = True , gpu_id = 0 ) [source] #

Parameters :

-
output_dir (default: `None `) – path, optional (default=None). Output directory for analysis files. If None, all analysis is done in memory.

-
name (default: `None `) – string, optional (default=None). A name for this analysis. Will be prefixed to all output files. If set to None, will be automatically generated from date (and random string).

-
use_gpu (default: `True `) – bool, optional (default=True). If True and GPU is available, use GPU acceleration for NMF factorization.

-
gpu_id (default: `0 `) – int, optional (default=0). GPU device ID to use when multiple GPUs are available.

Methods

`__init__ `(adata, components[, n_iter, ...])

`calculate_silhouette_k `(k[, ...])

Calculate silhouette scores for a given k value.

`combine `([components, skip_missing_files])

Combine NMF iterations for the same value of K :type components: default: `None `:param components: Values of K to combine iterations for.

`combine_nmf `(k[, skip_missing_files, ...])

`consensus `(k[, density_threshold, ...])

Obtain consensus estimates of spectra and usages from a cNMF run and output a clustergram of the consensus matrix.

`factorize `([worker_i, total_workers])

Iteratively run NMF with prespecified parameters.

`factorize_multi_process `(total_workers)

multiproces wrapper for nmf.factorize() factorize_multi_process() is direct wrapper around factorize to be able to launch it form mp.

`get_nmf_iter_params `(ks[, n_iter, ...])

Create a DataFrame with parameters for NMF iterations.

`get_norm_counts `(counts, tpm[, ...])

`get_results `(adata, result_dict)

`get_results_rfc `(adata, result_dict[, ...])

Map cNMF results to `adata `and train RFC/decision-tree cluster labels.

`k_selection_plot `([close_fig, ...])

Plot stability, reconstruction error, and optionally silhouette scores for K selection.

`load `(filename)

Load a saved cNMF object from file.

`load_results `(K, density_threshold[, ...])

Loads normalized usages and gene_spectra_scores for a given choice of K and local_density_threshold for the cNMF run.

`plot_silhouette_for_k `(k[, ...])

Plot detailed silhouette plot for a single k value.

`plot_silhouette_survey `([k_range, ...])

Generate a grid of silhouette plots for multiple k values for easy comparison.

`prepare `(adata, components[, n_iter, ...])

Load input counts, reduce to high-variance genes, and variance normalize genes.

`refit_spectra `(X, usage)

Takes an input data matrix and a fixed usage matrix and uses NNLS to find the optimal spectra matrix.

`refit_usage `(X, spectra)

Takes an input data matrix and a fixed spectra and uses NNLS to find the optimal usage matrix.

`save `(filename)

Save the cNMF object to a file for later use.

`save_nmf_iter_params `(replicate_params, ...)

`save_norm_counts `(norm_counts)
