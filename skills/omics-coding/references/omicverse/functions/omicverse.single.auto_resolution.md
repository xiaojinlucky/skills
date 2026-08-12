# omicverse.single.auto_resolution #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.auto_resolution`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.auto_resolution.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Pick the most reproducible Leiden resolution via null-adjusted bootstrap-ARI (Lange, Roth, Braun & Buhmann, Neural Computation 2004).

## Signature

```text
omicverse.single. auto_resolution ( adata , resolutions = None , * , method = 'bootstrap-ari' , n_subsamples = 5 , subsample_frac = 0.8 , use_null_correction = True , n_null_subsamples = 3 , null_seed = 42 , null_layer = None , gamma_min = 0.05 , gamma_max = 3.0 , n_partitions = 30 , min_clusters = 3 , key_added = 'leiden' , random_state = 0 , verbose = True )
```

## Parameters

- `adata`: Detected from function signature; no parameter description detected.
- `resolutions`: Detected from function signature; no parameter description detected.
- `method`: Detected from function signature; no parameter description detected.
- `n_subsamples`: Detected from function signature; no parameter description detected.
- `subsample_frac`: Detected from function signature; no parameter description detected.
- `use_null_correction`: Detected from function signature; no parameter description detected.
- `n_null_subsamples`: Detected from function signature; no parameter description detected.
- `null_seed`: Detected from function signature; no parameter description detected.
- `null_layer`: Detected from function signature; no parameter description detected.
- `gamma_min`: Detected from function signature; no parameter description detected.
- `gamma_max`: Detected from function signature; no parameter description detected.
- `n_partitions`: Detected from function signature; no parameter description detected.
- `min_clusters`: Detected from function signature; no parameter description detected.
- `key_added`: Detected from function signature; no parameter description detected.
- `random_state`: Detected from function signature; no parameter description detected.
- `verbose`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.single.auto_resolution #

omicverse.single. auto_resolution ( adata , resolutions = None , * , method = 'bootstrap-ari' , n_subsamples = 5 , subsample_frac = 0.8 , use_null_correction = True , n_null_subsamples = 3 , null_seed = 42 , null_layer = None , gamma_min = 0.05 , gamma_max = 3.0 , n_partitions = 30 , min_clusters = 3 , key_added = 'leiden' , random_state = 0 , verbose = True ) [source] #

Pick the most reproducible Leiden resolution via null-adjusted bootstrap-ARI (Lange, Roth, Braun & Buhmann, Neural Computation 2004).

## Algorithm #

For each candidate resolution \(r\) :

-
Run Leiden on the full AnnData → reference labels at `r `.

-
Take `n_subsamples `independent without-replacement subsamples of size `subsample_frac × n_obs `.

-
For each subsample run Leiden on the induced subgraph and compute Adjusted Rand Index against the reference restricted to the subsample.

-
\(s_\mathrm{real}(r) = \mathrm{mean\,ARI}\) across the `n_subsamples `bootstraps — the observed reproducibility.

Bootstrap stability alone is biased toward fine resolutions: small tight clusters are mechanically reproducible under any subsampling procedure regardless of whether they reflect biological structure. The Lange–Buhmann fix is to subtract a procedurally-matched null :

-
Build a null AnnData by independently permuting each gene’s expression across cells. This preserves per-gene marginal distributions but destroys all cell-cell co-expression — there is no cluster structure left.

-
Run the same PCA → kNN-graph → bootstrap-stability pipeline on the null with `n_null_subsamples `subsamples. \(s_\mathrm{null}(r)\) is the chance-level reproducibility of leiden at this resolution given the data’s marginal-only statistical structure.

-
The excess stability is

\[\Delta(r) = s_\mathrm{real}(r) - s_\mathrm{null}(r)\]
and the chosen resolution is \(\arg\max_r \Delta(r)\) subject to producing at least `min_clusters `clusters on the full data.

Setting `use_null_correction ` `=False `falls back to plain bootstrap-ARI; it’s exposed mostly for diagnostics. The default is the null-adjusted variant.

type adata :

`AnnData `

param adata :

AnnData with a precomputed neighbor graph ( `adata.obsp['connectivities'] `).

type resolutions :

`Optional `[ `Sequence `[ `float `]] (default: `None `)

param resolutions :

Candidate resolutions to test. Defaults to `np.round(np.arange(0.2, 1.6, 0.1), 2) `.

type n_subsamples :

`int `(default: `5 `)

param n_subsamples :

Bootstrap subsamples per resolution on the real data.

type subsample_frac :

`float `(default: `0.8 `)

param subsample_frac :

Fraction of cells in each subsample. Default 0.8.

type use_null_correction :

`bool `(default: `True `)

param use_null_correction :

If `True `(default), subtract null-pipeline stability per Lange et al. 2004. `False `returns plain bootstrap stability.

type n_null_subsamples :

`int `(default: `3 `)

param n_null_subsamples :

Bootstrap subsamples per resolution on the null data — can be smaller than `n_subsamples `because the null is low-variance.

type null_seed :

`int `(default: `42 `)

param null_seed :

Seed for the per-gene permutation generating the null. Held separate from `random_state `so the null is reproducible independently of the real-data search.

type null_layer :

`Optional `[ `str `] (default: `None `)

param null_layer :

`adata.layers `key to permute. Defaults to `adata.X `.

type min_clusters :

`int `(default: `3 `)

param min_clusters :

Lower bound on the number of clusters the chosen resolution must produce on the full data; degenerate resolutions are excluded from the argmax.

type key_added :

`str `(default: `'leiden' `)

param key_added :

`adata.obs `column to write the chosen resolution’s labels to.

type random_state :

`int `(default: `0 `)

param random_state :

Seed for subsample selection and Leiden on the real data.

type verbose :

`bool `(default: `True `)

param verbose :

Stream per-resolution scores during the search.

returns :

`(adata, best_resolution, scores_df) `. `scores_df `is indexed by resolution with columns `stability_real `, `stability_null `, `excess_stability `, `std_real `, `n_clusters `. Also writes `adata.obs[key_added] `and `adata.uns['autoResolution'] `.

rtype :

Tuple[anndata.AnnData, float, pandas.DataFrame]

References

Lange, Roth, Braun, Buhmann. “Stability-based validation of clustering solutions.” Neural Computation 16(6):1299–1323, 2004.

Weir, Emmons, Wakefield, Hopkins, Mucha. “Post-processing partitions to identify domains of modularity optimization.” Algorithms 10(3):93, 2017 (used when `method='champ' `).

param method :

type method :

`str `(default: `'bootstrap-ari' `)

param gamma_min :

type gamma_min :

`float `(default: `0.05 `)

param gamma_max :

type gamma_max :

`float `(default: `3.0 `)

param n_partitions :

type n_partitions :

`int `(default: `30 `)
