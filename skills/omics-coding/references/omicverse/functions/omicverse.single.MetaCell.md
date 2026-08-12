# omicverse.single.MetaCell #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.MetaCell`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.MetaCell.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Unified metacell wrapper with dispatchable backends.

## Signature

```text
class omicverse.single. MetaCell ( adata , method = 'seacells' , use_rep = 'X_pca' , n_metacells = None , layer = None , device = 'cpu' , random_state = 0 , ** kwargs )
```

## Parameters

- `adata`: – Input single-cell AnnData.
- `method`: ( str (default: 'seacells' )) – Backend key. One of 'seacells' (default, backward-compatible), 'metaq' , 'mc2' , 'supercell' , 'kmeans' , 'random' , 'geosketch' .
- `use_rep`: ( str (default: 'X_pca' )) – Embedding key in adata.obsm . Used by graph-based backends ( seacells / supercell / kmeans / geosketch ). MetaQ and MC2 derive their own representations and ignore this.
- `n_metacells`: ( Optional [ int ] (default: None )) – Target number of metacells. Default adata.n_obs // 75 .
- `layer`: ( Optional [ str ] (default: None )) – Counts layer for backends that need raw counts (MetaQ, MC2).
- `device`: ( str (default: 'cpu' )) – 'cpu' , 'cuda' , or 'mps' for GPU-capable backends.
- `random_state`: ( int (default: 0 )) – Seed forwarded to all backends.
- `**kwargs`: – Forwarded to the backend constructor. See each backend’s docstring for valid kwargs.

## Full Documentation

# omicverse.single.MetaCell #

class omicverse.single. MetaCell ( adata , method = 'seacells' , use_rep = 'X_pca' , n_metacells = None , layer = None , device = 'cpu' , random_state = 0 , ** kwargs ) [source] #

Unified metacell wrapper with dispatchable backends.

Parameters :

-
adata – Input single-cell AnnData.

-
method ( `str `(default: `'seacells' `)) – Backend key. One of `'seacells' `(default, backward-compatible), `'metaq' `, `'mc2' `, `'supercell' `, `'kmeans' `, `'random' `, `'geosketch' `.

-
use_rep ( `str `(default: `'X_pca' `)) – Embedding key in `adata.obsm `. Used by graph-based backends ( `seacells `/ `supercell `/ `kmeans `/ `geosketch `). MetaQ and MC2 derive their own representations and ignore this.

-
n_metacells ( `Optional `[ `int `] (default: `None `)) – Target number of metacells. Default `adata.n_obs // 75 `.

-
layer ( `Optional `[ `str `] (default: `None `)) – Counts layer for backends that need raw counts (MetaQ, MC2).

-
device ( `str `(default: `'cpu' `)) – `'cpu' `, `'cuda' `, or `'mps' `for GPU-capable backends.

-
random_state ( `int `(default: `0 `)) – Seed forwarded to all backends.

-
**kwargs – Forwarded to the backend constructor. See each backend’s docstring for valid kwargs.

__init__ ( adata , method = 'seacells' , use_rep = 'X_pca' , n_metacells = None , layer = None , device = 'cpu' , random_state = 0 , ** kwargs ) [source] #

Parameters :

-
method ( `str `(default: `'seacells' `))

-
use_rep ( `str `(default: `'X_pca' `))

-
n_metacells ( `Optional `[ `int `] (default: `None `))

-
layer ( `Optional `[ `str `] (default: `None `))

-
device ( `str `(default: `'cpu' `))

-
random_state ( `int `(default: `0 `))

Methods

`__init__ `(adata[, method, use_rep, ...])

`assign_new_cells `(adata_query)

`capability_matrix `()

`check_rigor `([layer_lognorm, feature_use, ...])

Score the rigor of the current partition (mcRigor port).

`codebook `()

`compactness `([use_rep])

Legacy alias → `compute_compactness `.

`compute_celltype_purity `([celltype_label])

Legacy alias → `compute_purity `.

`compute_compactness `([use_rep])

Per-metacell mean pairwise distance in `use_rep `(lower = more compact).

`compute_purity `([label_key])

Per-metacell majority-label purity.

`compute_separation `([use_rep, label_key])

Mean intra/inter-metacell distance ratio per metacell (lower = more separated).

`fit `(**kwargs)

Train the chosen backend; write unified schema into `adata `.

`fit_multi_gamma `(gammas)

`initialize_archetypes `(**kwargs)

Legacy SEACells shim.

`latent `()

`load `(path)

`predicted `([method, layer, summary, ...])

Aggregate single cells into a metacell-level AnnData.

`save `(path)

`separation `([use_rep, nth_nbr])

Legacy alias → `compute_separation `.

`soft_membership `()

`step `([n_steps])

Legacy SEACells shim — only meaningful for the seacells backend.

`train `([min_iter, max_iter])

Legacy SEACells shim → `.fit() `.

Attributes

`capabilities `
