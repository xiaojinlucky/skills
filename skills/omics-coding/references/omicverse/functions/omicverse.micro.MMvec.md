# omicverse.micro.MMvec #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.MMvec`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.MMvec.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

MMvec (Morton et al. 2019) in ~80 lines of PyTorch.

## Signature

```text
class omicverse.micro. MMvec ( n_latent = 3 , lr = 0.05 , epochs = 1000 , val_frac = 0.1 , patience = 100 , l2 = 0.001 , seed = 0 , device = None )
```

## Parameters

- `n_latent`: ( int (default: 3 )) – Embedding dimensionality K .
- `lr`: ( float (default: 0.05 )) – Adam learning rate.
- `epochs`: ( int (default: 1000 )) – Maximum training epochs.
- `val_frac`: ( float (default: 0.1 )) – Fraction of samples held out for the validation loss curve / early stopping. Set to 0 to skip validation.
- `patience`: ( int (default: 100 )) – Early-stopping patience on validation loss (epochs without improvement before training halts).
- `l2`: ( float (default: 0.001 )) – Weight-decay on U / V / beta .
- `seed`: ( int (default: 0 )) – Torch RNG seed.
- `device`: ( Optional [ str ] (default: None )) – 'cpu' / 'cuda' / None (auto-pick based on availability).

## Full Documentation

# omicverse.micro.MMvec #

class omicverse.micro. MMvec ( n_latent = 3 , lr = 0.05 , epochs = 1000 , val_frac = 0.1 , patience = 100 , l2 = 0.001 , seed = 0 , device = None ) [source] #

MMvec (Morton et al. 2019) in ~80 lines of PyTorch.

The objective is the exact expected multinomial log-likelihood

\[\ell \;=\; \sum_{i,j} W_{ij} \,\log \mathrm{softmax}(u_i \cdot V^\top + \beta)_j\]
where \(W_{ij} = \sum_s c_{s,i} \cdot m_{s,j} / M_s\) is the co-occurrence weight matrix (total microbe-i count × expected metabolite-j fraction over the cohort). For the tutorial-scale data we use the full softmax; the upstream `mmvec `package uses negative sampling to scale to thousands of features.

Parameters :

-
n_latent ( `int `(default: `3 `)) – Embedding dimensionality `K `.

-
lr ( `float `(default: `0.05 `)) – Adam learning rate.

-
epochs ( `int `(default: `1000 `)) – Maximum training epochs.

-
val_frac ( `float `(default: `0.1 `)) – Fraction of samples held out for the validation loss curve / early stopping. Set to 0 to skip validation.

-
patience ( `int `(default: `100 `)) – Early-stopping patience on validation loss (epochs without improvement before training halts).

-
l2 ( `float `(default: `0.001 `)) – Weight-decay on `U `/ `V `/ `beta `.

-
seed ( `int `(default: `0 `)) – Torch RNG seed.

-
device ( `Optional `[ `str `] (default: `None `)) – `'cpu' `/ `'cuda' `/ `None `(auto-pick based on availability).

__init__ ( n_latent = 3 , lr = 0.05 , epochs = 1000 , val_frac = 0.1 , patience = 100 , l2 = 0.001 , seed = 0 , device = None ) [source] #

Parameters :

-
n_latent ( `int `(default: `3 `))

-
lr ( `float `(default: `0.05 `))

-
epochs ( `int `(default: `1000 `))

-
val_frac ( `float `(default: `0.1 `))

-
patience ( `int `(default: `100 `))

-
l2 ( `float `(default: `0.001 `))

-
seed ( `int `(default: `0 `))

-
device ( `Optional `[ `str `] (default: `None `))

Methods

`__init__ `([n_latent, lr, epochs, val_frac, ...])

`conditional_probabilities `()

Per-microbe P(metabolite | microbe) — softmax of `U @ V.T + β `.

`cooccurrence `()

Raw log-odds co-occurrence matrix `U · Vᵀ `(microbes × metabolites).

`fit `(adata_microbe, adata_metabolite[, verbose])

Fit MMvec on paired microbe / metabolite count tables and return `self `.

`top_pairs `([n])

Top- `n `(microbe, metabolite) pairs ranked by `|log-odds| `.

Attributes

`metabolite_embeddings_ `

`microbe_embeddings_ `
