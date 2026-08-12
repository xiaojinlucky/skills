# omicverse.metabol.run_mofa #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.run_mofa`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.run_mofa.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Train MOFA+ on sample-aligned metabolomics + other-omics views.

## Signature

```text
omicverse.metabol. run_mofa ( views , * , n_factors = 10 , outfile = 'mofa_model.hdf5' , scale_views = True , center_groups = True , max_iter = 500 , convergence_mode = 'fast' , gpu_mode = False , seed = 0 )
```

## Parameters

- `views`: ( dict ) – Mapping {view_name: AnnData} . Each AnnData must have the same ``obs_names`` in the same order — MOFA+ concatenates samples across views by position. Mismatched indices raise a ValueError with the first few offending sample IDs.
- `n_factors`: ( int (default: 10 )) – Number of latent factors. Default 10 — MOFA+ drops factors with variance explained below dropR2=0.001 automatically.
- `outfile`: ( str | Path (default: 'mofa_model.hdf5' )) – Path to the HDF5 the trainer writes. Kept on disk so the user can reload it with ov.single.pyMOFAART if they want to drive the sc-oriented downstream helpers on their own.
- `scale_views`: ( bool (default: True )) – Scale each view to unit total variance before training. The MOFA+ recommendation when view dimensions / dynamic ranges differ by >10x (metabolomics vs RNA-seq definitely qualifies).
- `center_groups`: ( bool (default: True )) – Mean-centre each (view, sample-group) block before training.
- `max_iter`: ( int (default: 500 )) – Passed to pyMOFA.mofa_run .
- `convergence_mode`: ( str (default: 'fast' )) – Passed to pyMOFA.mofa_run .
- `gpu_mode`: ( bool (default: False )) – Pass through to MOFA’s GPU path. Requires CuPy.
- `seed`: ( int (default: 0 )) – Deterministic seed.

## Full Documentation

# omicverse.metabol.run_mofa #

omicverse.metabol. run_mofa ( views , * , n_factors = 10 , outfile = 'mofa_model.hdf5' , scale_views = True , center_groups = True , max_iter = 500 , convergence_mode = 'fast' , gpu_mode = False , seed = 0 ) [source] #

Train MOFA+ on sample-aligned metabolomics + other-omics views.

Parameters :

-
views ( `dict `) – Mapping `{view_name: AnnData} `. Each AnnData must have the same ``obs_names`` in the same order — MOFA+ concatenates samples across views by position. Mismatched indices raise a `ValueError `with the first few offending sample IDs.

-
n_factors ( `int `(default: `10 `)) – Number of latent factors. Default 10 — MOFA+ drops factors with variance explained below `dropR2=0.001 `automatically.

-
outfile ( `str `| `Path `(default: `'mofa_model.hdf5' `)) – Path to the HDF5 the trainer writes. Kept on disk so the user can reload it with `ov.single.pyMOFAART `if they want to drive the sc-oriented downstream helpers on their own.

-
scale_views ( `bool `(default: `True `)) – Scale each view to unit total variance before training. The MOFA+ recommendation when view dimensions / dynamic ranges differ by >10x (metabolomics vs RNA-seq definitely qualifies).

-
center_groups ( `bool `(default: `True `)) – Mean-centre each (view, sample-group) block before training.

-
max_iter ( `int `(default: `500 `)) – Passed to `pyMOFA.mofa_run `.

-
convergence_mode ( `str `(default: `'fast' `)) – Passed to `pyMOFA.mofa_run `.

-
gpu_mode ( `bool `(default: `False `)) – Pass through to MOFA’s GPU path. Requires CuPy.

-
seed ( `int `(default: `0 `)) – Deterministic seed.

Returns :

`(n_samples, n_factors_retained) `factor matrix indexed by the shared sample IDs, columns `F1, F2, ... `. To plug it into a downstream step:

```text
>>> factors = ov.metabol.run_mofa({'metabol': adata, 'rna': rna})
>>> adata.obsm['X_mofa'] = factors.reindex(adata.obs_names).to_numpy()

```

Return type :

pd.DataFrame
