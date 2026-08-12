# omicverse.pp.champ #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.champ`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.champ.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Pick the modularity-stablest Leiden partition via CHAMP (Weir et al. 2017).

## Signature

```text
omicverse.pp. champ ( adata , resolutions = None , * , n_partitions = 30 , gamma_min = 0.05 , gamma_max = 3.0 , n_seeds = 1 , modularity = 'newman' , width_metric = 'log' , adaptive = False , adaptive_max_iter = 3 , adaptive_n_refine = 3 , key_added = 'champ' , random_state = 0 , verbose = True )
```

## Parameters

- `adata`: Detected from function signature; no parameter description detected.
- `resolutions`: Detected from function signature; no parameter description detected.
- `n_partitions`: Detected from function signature; no parameter description detected.
- `gamma_min`: Detected from function signature; no parameter description detected.
- `gamma_max`: Detected from function signature; no parameter description detected.
- `n_seeds`: Detected from function signature; no parameter description detected.
- `modularity`: Detected from function signature; no parameter description detected.
- `width_metric`: Detected from function signature; no parameter description detected.
- `adaptive`: Detected from function signature; no parameter description detected.
- `adaptive_max_iter`: Detected from function signature; no parameter description detected.
- `adaptive_n_refine`: Detected from function signature; no parameter description detected.
- `key_added`: Detected from function signature; no parameter description detected.
- `random_state`: Detected from function signature; no parameter description detected.
- `verbose`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.pp.champ #

omicverse.pp. champ ( adata , resolutions = None , * , n_partitions = 30 , gamma_min = 0.05 , gamma_max = 3.0 , n_seeds = 1 , modularity = 'newman' , width_metric = 'log' , adaptive = False , adaptive_max_iter = 3 , adaptive_n_refine = 3 , key_added = 'champ' , random_state = 0 , verbose = True ) [source] #

Pick the modularity-stablest Leiden partition via CHAMP (Weir et al. 2017).

## Algorithm #

-
Run Leiden at `n_partitions `candidate γ values evenly spaced over \([\gamma_\min,\,\gamma_\max]\) (or use the explicit grid passed in `resolutions `). Deduplicate partitions that produce identical labels.

-
For each unique partition \(P\) , compute \((a_P, b_P)\) such that

\[Q(\gamma; P) = a_P - \gamma\, b_P.\]

-
Compute the upper convex hull of the points \(\{(b_P, a_P)\}\) . The hull’s vertices are the partitions that are modularity-optimal for some γ; everything else is dominated.

-
For each consecutive pair of hull vertices, compute the γ at which their lines intersect:

\[\gamma_{i,i+1} = \frac{a_{i+1} - a_i}{b_{i+1} - b_i}.\]

-
Each hull partition’s admissible γ-range is the interval between its two adjacent crossover γ’s (capped at \([0,\,\gamma_\max]\) ).

-
Return the hull partition with the widest admissible range .

No Monte Carlo, no null model — purely a geometric statement about the modularity landscape’s convex structure.

type adata :

`AnnData `

param adata :

AnnData with a precomputed neighbor graph ( `adata.obsp['connectivities'] `).

type resolutions :

`Optional `[ `Sequence `[ `float `]] (default: `None `)

param resolutions :

Explicit γ grid; overrides `n_partitions `/ `gamma_min `/ `gamma_max `.

type n_partitions :

`int `(default: `30 `)

param n_partitions :

Number of γ values to scan when `resolutions `is `None `.

type gamma_min :

`float `(default: `0.05 `)

param gamma_min :

Endpoints of the γ scan; `gamma_max `also caps the leftmost hull partition’s “open” admissible range so widths are finite.

type gamma_max :

`float `(default: `3.0 `)

param gamma_max :

Endpoints of the γ scan; `gamma_max `also caps the leftmost hull partition’s “open” admissible range so widths are finite.

type n_seeds :

`int `(default: `1 `)

param n_seeds :

Number of random seeds to try at each γ. Leiden is heuristic and converges to a local modularity maximum; running multiple seeds at the same γ can surface different partitions and gives CHAMP a denser candidate cloud to find the true upper hull on. Default 1; the original Weir et al. 2017 paper recommends 3-5. Cost scales linearly: `n_seeds × n_partitions `leiden calls.

type modularity :

`str `(default: `'newman' `)

param modularity :

`'newman' `(default) — Newman-Girvan modularity. `'cpm' `— Constant Potts Model (Reichardt-Bornholdt 2006), which is resolution-limit-free in the sense of Fortunato & Barthelemy 2007. Both have the same linear-in-γ structure; `'cpm' `writes `b_P = Σ_c |c|² / N² `instead of degree squared, so γ-units differ — narrower γ ranges typically work. For `'cpm' `the candidate generator passes `partition_type=leidenalg.CPMVertexPartition `to leiden so that candidates and scoring share an objective.

type width_metric :

`str `(default: `'log' `)

param width_metric :

How “widest admissible γ-range” is measured when picking the chosen partition. Choices:

-
`'log' `( default , omicverse): multiplicative width \(\log(\gamma_{hi}/\gamma_{lo})\) . Modularity is invariant under \(\gamma \mapsto c\gamma\) (the optimal partition at each γ doesn’t change), so γ has no natural additive scale — the canonical “width” on a scale-free axis is multiplicative. Matters in practice because additive width systematically over-rewards fine partitions: small differences in \(b\) between fine partitions get amplified into large additive γ-ranges by the small denominator in the crossover formula \(\gamma = \Delta a / \Delta b\) . The log metric undoes this geometric bias.

-
`'linear' `(Weir et al. 2017 canonical): additive width \(\gamma_{hi} - \gamma_{lo}\) . Reproduces the original paper’s behaviour. Tends to over-cluster on data with wide high-γ plateaus (typical for scRNA).

-
`'relative' `: \((\gamma_{hi}-\gamma_{lo}) / \overline{\gamma}\) where \(\overline{\gamma}\) is the midpoint. Closely related to log width; included for completeness.

type adaptive :

`bool `(default: `False `)

param adaptive :

If `True `, iteratively refine the γ-grid around the current hull’s crossovers (active-set style): build the hull → for each crossover sample `adaptive_n_refine `extra γ values nearby → re-run leiden → recompute the hull → repeat until no new hull vertex appears or `adaptive_max_iter `iterations are reached. Catches hull partitions that uniform γ-sampling misses around sharp transitions.

type adaptive_max_iter :

`int `(default: `3 `)

param adaptive_max_iter :

Cap on the adaptive-refinement outer loop. Default 3.

type adaptive_n_refine :

`int `(default: `3 `)

param adaptive_n_refine :

Number of extra γ values sampled around each crossover per adaptive iteration. Default 3.

type key_added :

`str `(default: `'champ' `)

param key_added :

`adata.obs `column to write the chosen partition’s labels to.

type random_state :

`int `(default: `0 `)

param random_state :

Seed for Leiden RNG.

type verbose :

`bool `(default: `True `)

param verbose :

Stream per-step progress.

returns :

`(adata, (gamma_lo, gamma_hi), partitions_df) `where `partitions_df `is one row per unique candidate partition with columns `a `, `b `, `n_clusters `, `origin_resolution `, `on_hull `(bool), `gamma_lo `, `gamma_hi `, `gamma_range `. Also writes `adata.obs[key_added] `and `adata.uns['champ'] `.

rtype :

Tuple[anndata.AnnData, Tuple[float, float], pandas.DataFrame]

References

Weir, Emmons, Wakefield, Hopkins, Mucha. “Post-processing partitions to identify domains of modularity optimization.” Algorithms 10(3):93, 2017. https://doi.org/10.3390/a10030093
