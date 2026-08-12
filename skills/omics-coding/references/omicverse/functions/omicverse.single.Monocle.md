# omicverse.single.Monocle #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.Monocle`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.Monocle.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Monocle2-style single-cell trajectory analysis.

## Signature

```text
class omicverse.single. Monocle ( adata )
```

## Parameters

- `adata`: ( AnnData ) – Annotated data matrix (cells × genes). Expression matrix in adata.X should be raw/normalized counts (negative binomial model).

## Full Documentation

# omicverse.single.Monocle #

class omicverse.single. Monocle ( adata ) [source] #

Monocle2-style single-cell trajectory analysis.

Wraps a pure-Python implementation of Monocle 2 as a stateful analyzer operating on an AnnData object. All results are stored in the AnnData ( `.obs `, `.var `, `.uns['monocle'] `, `.obsm `) so the usual scanpy workflow continues to work seamlessly.

Parameters :

adata ( AnnData ) – Annotated data matrix (cells × genes). Expression matrix in `adata.X `should be raw/normalized counts (negative binomial model).

adata #

The annotated data matrix with analysis results stored in-place.

Type :

AnnData

Examples

Basic trajectory analysis:

```text
>>> mono = ov.single.Monocle(adata)
>>> mono.preprocess() # size factors + dispersions
>>> mono.select_ordering_genes() # high-variance gene selection
>>> mono.reduce_dimension() # DDRTree
>>> mono.order_cells() # assign pseudotime + State
>>> mono.plot_trajectory(color_by='clusters')
>>> mono.plot_genes_in_pseudotime(['Ins1', 'Gcg'])

```

Differential expression along pseudotime:

```text
>>> de = mono.differential_gene_test()
>>> beam = mono.BEAM(branch_point=1)

```

__init__ ( adata ) [source] #

Initialise the Monocle analyser.

Parameters :

adata ( AnnData ) – Annotated data matrix (cells × genes). The expression matrix in `adata.X `should contain raw or normalised counts — the negative binomial model used by size-factor estimation and BEAM assumes count-like data. All downstream results ( `Pseudotime `, `State `, dispersions, DDRTree reduction) are written back to the same AnnData, so subsequent scanpy-style workflows continue to work.

Notes

The external `monocle2_py `backend is imported lazily inside this constructor (not at module scope) to keep `omicverse.single `free of top-level `..external `imports, per the architecture test.

Methods

`BEAM `([branch_point, branch_states, ...])

Branched Expression Analysis Modelling.

`__init__ `(adata)

Initialise the Monocle analyser.

`cal_ABCs `([branch_point])

Compute the Area Between Curves for branch-specific genes.

`cal_ILRs `([branch_point, return_all])

Compute the Intrinsic Log-Ratio (per-gene lineage bias).

`cluster_cells `([method, k, ...])

Cluster cells on the reduced-dim space and write labels to `adata.obs['Cluster'] `.

`cluster_genes `(expression_matrix, k[, method])

Cluster genes by their expression pattern along pseudotime.

`detect_genes `([min_expr])

Flag genes expressed above a threshold.

`differential_gene_test `([...])

Pseudotime-dependent differential expression via a likelihood-ratio test between a full GLM (gene ~ f(Pseudotime)) and a reduced null model.

`dispersion_table `()

Return the per-gene dispersion table populated by `estimate_dispersions() `, as a `pandas.DataFrame `.

`estimate_dispersions `([min_cells_detected, ...])

Fit per-gene dispersions under the negative-binomial model.

`estimate_size_factors `([method, round_exprs])

Estimate per-cell size factors.

`fit_model `([modelFormulaStr, relative_expr, ...])

Fit a per-gene GLM under the NB model.

`gen_smooth_curves `([new_data, trend_formula, ...])

Predict smoothed expression trajectories from a fitted model.

`order_cells `([root_state, reverse, ...])

Order cells along the learned trajectory, assigning Pseudotime and State.

`plot_cell_clusters `([color_by])

Plot cells colored by cluster in reduced-dim space.

`plot_cell_trajectory `([color_by])

plot_cell_trajectory — main DDRTree trajectory plot.

`plot_complex_cell_trajectory `([color_by])

Dendrogram-style trajectory layout (Pseudotime on Y-axis).

`plot_genes_branched_heatmap `([branch_point])

Heatmap of branch-specific gene expression.

`plot_genes_branched_pseudotime `(genes[, ...])

Gene expression split by branch.

`plot_genes_in_pseudotime `(genes, **kwargs)

Gene expression vs pseudotime with smoothed curves.

`plot_genes_jitter `(genes[, grouping])

Jitter plot of gene expression by group.

`plot_genes_violin `(genes[, grouping])

Violin plot of gene expression by group.

`plot_multiple_branches_heatmap `(branches, ...)

Multi-branch expression heatmap.

`plot_multiple_branches_pseudotime `(genes, ...)

Multi-branch gene expression curves.

`plot_ordering_genes `(**kwargs)

Dispersion vs mean-expression plot, highlighting ordering genes.

`plot_pc_variance_explained `([max_components])

Plot variance explained by principal components.

`plot_pseudotime_heatmap `([genes])

Heatmap of gene expression sorted by pseudotime.

`plot_rho_delta `(**kwargs)

Plot rho vs delta for density-peak clustering.

`plot_trajectory `([color_by])

plot_cell_trajectory — main DDRTree trajectory plot.

`plot_trajectory_overlay `(ax, **kwargs)

Overlay the DDRTree principal-graph skeleton + branch points on an externally-drawn axes (e.g. one produced by `ov.pl.embedding(basis='X_DDRTree') `).

`plot_trajectory_with_embedding `([color, ...])

Convenience combo: render `ov.pl.embedding `then overlay the DDRTree backbone + branch points.

`preprocess `([min_expr, verbose])

Run `detect_genes() `, `estimate_size_factors() `and `estimate_dispersions() `in sequence.

`reduce_dimension `([max_components, ...])

Reduce dimensionality and learn the principal graph.

`relative2abs `([method, ...])

Census normalisation — convert TPM / FPKM-scaled counts into estimated absolute transcript counts per cell.

`select_ordering_genes `([genes, ...])

Select genes used for trajectory inference.

`set_ordering_filter `(genes)

Explicitly set the list of ordering genes.

Attributes

`Y `

Tree-center coordinates (dim × K).

`Z `

Reduced-dim cell coordinates (dim × N).

`branch_points `

Branch-point vertex names in the learned tree.

`pseudotime `

Per-cell pseudotime (after order_cells).

`state `

Per-cell state (after order_cells).
