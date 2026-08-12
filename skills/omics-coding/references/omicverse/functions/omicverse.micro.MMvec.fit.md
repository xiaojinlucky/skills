# omicverse.micro.MMvec.fit #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.MMvec.fit`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.MMvec.fit.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Fit MMvec on paired microbe / metabolite count tables and return self .

## Signature

```text
MMvec. fit ( adata_microbe , adata_metabolite , verbose = False )
```

## Parameters

- `adata_microbe`: ( AnnData ) – Sample-aligned count tables.
- `adata_metabolite`: ( AnnData ) – Sample-aligned count tables.
- `verbose`: ( bool , default False ) – Print loss every epochs // 10 epochs.

## Full Documentation

# omicverse.micro.MMvec.fit #

MMvec. fit ( adata_microbe , adata_metabolite , verbose = False ) [source] #

Fit MMvec on paired microbe / metabolite count tables and return `self `.

Trains a low-rank latent-space model `logits[i, j] = U[i] · V[j] + β[j] `, where rows of `U `are microbe embeddings, rows of `V `are metabolite embeddings, and the loss is per-microbe negative log-likelihood of the sample-weighted metabolite distribution. The cooccurrence weights `W[i, j] = Σ_s X_mb[s, i] · X_mt[s, j] / Σ_s X_mt[s, :] `capture which microbes covary with which metabolites across samples.

Both AnnDatas must share `obs_names `in the same order ( _check_paired enforces this). Training reports an early-stop validation loss every epoch when `val_frac > 0 `; `patience `epochs without validation improvement stops training and restores the best checkpoint.

Parameters :

-
adata_microbe ( AnnData ) – Sample-aligned count tables.

-
adata_metabolite ( AnnData ) – Sample-aligned count tables.

-
verbose ( bool , default False ) – Print loss every `epochs // 10 `epochs.

Returns :

-
self — fitted; access `microbe_embeddings_ `,

-
`metabolite_embeddings_ `, `cooccurrence() `,

-
`conditional_probabilities() `, `top_pairs(n) `.
