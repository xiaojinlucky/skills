# omicverse.single.Velo #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.Velo`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.Velo.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

RNA velocity analysis wrapper for directional cell-state transition inference.

## Signature

```text
class omicverse.single. Velo ( adata )
```

## Parameters

- `adata`: ( AnnData ) – AnnData containing spliced/unspliced layers (or backend-compatible count layers) and low-dimensional embeddings.

## Full Documentation

# omicverse.single.Velo #

class omicverse.single. Velo ( adata ) [source] #

RNA velocity analysis wrapper for directional cell-state transition inference.

Parameters :

adata ( AnnData ) – AnnData containing spliced/unspliced layers (or backend-compatible count layers) and low-dimensional embeddings.

Returns :

Initializes velocity workflow state.

Return type :

None

Examples

```text
>>> velo_obj = ov.single.Velo(adata)

```

__init__ ( adata ) [source] #

Methods

`__init__ `(adata)

`cal_velocity `([method, batch_key, ...])

Estimate RNA velocity vectors and write them into AnnData.

`cell_fate_perturbation `(perturbed[, ...])

Summarize perturbation effects on terminal cell fates.

`cellrank_fate `([velocity_key, xkey, ...])

Run a CellRank fate-analysis step from OmicVerse velocity output.

`dynamics `([backend])

Fit transcriptional dynamics parameters for velocity inference.

`filter_genes `([min_shared_counts])

Filter genes for velocity modeling using scVelo shared-count criteria.

`graphvelo `([xkey, vkey, n_jobs, basis_keys, ...])

Refine velocity vectors with GraphVelo and project to selected embeddings.

`moments `([backend, n_pcs, n_neighbors])

Compute neighborhood moments required by RNA velocity models.

`perturbation_effect `(perturbed_adata, ...[, ...])

Write single-cell perturbation effects back to `adata.obs `.

`prepare_regvelo `(prior_grn[, regulators, ...])

Prepare AnnData for `cal_velocity(method='regvelo') `.

`preprocess `([recipe, n_neighbors, n_pcs])

Preprocess expression data before velocity estimation.

`regvelo_perturb `(tf[, model, adata, effects, ...])

Run RegVelo's native in-silico TF regulon blockade from a Velo object.

`run `()

Print a quick diagnostic summary for velocity input data.

`velocity_effect `(perturbed_adata[, ...])

Compute per-cell velocity direction change after perturbation.

`velocity_embedding `([basis, vkey])

Project velocity vectors onto a low-dimensional embedding.

`velocity_graph `([basis, vkey])

Build a velocity transition graph from precomputed velocity vectors.

`velocity_streamplot `([basis, velocity_key, ...])

Plot cells and velocity streamlines with OmicVerse plotting helpers.
