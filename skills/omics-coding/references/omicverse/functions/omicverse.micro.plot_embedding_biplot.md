# omicverse.micro.plot_embedding_biplot #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.plot_embedding_biplot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.plot_embedding_biplot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Biplot of microbe + metabolite embeddings in the MMvec latent space.

## Signature

```text
omicverse.micro. plot_embedding_biplot ( mmvec , components = (0, 1) , label_top = 5 , ax = None )
```

## Parameters

- `mmvec`: ( MMvec ) – Fitted model.
- `components`: ( ( int , int ) , default ( 0 , 1 ) ) – Zero-indexed latent factors to plot.
- `label_top`: ( int , default 5 ) – Number of microbes / metabolites to annotate in each cloud.
- `ax`: ( matplotlib axes , optional )

## Full Documentation

# omicverse.micro.plot_embedding_biplot #

omicverse.micro. plot_embedding_biplot ( mmvec , components = (0, 1) , label_top = 5 , ax = None ) [source] #

Biplot of microbe + metabolite embeddings in the MMvec latent space.

Draws two scatter point clouds in the same panel: microbes (rows of `mmvec.U_ `) and metabolites (rows of `mmvec.V_ `) projected onto the chosen `components `(default the first two latent factors). Annotates the `label_top `items farthest from the origin in each cloud — these are the entities most strongly associated with that pair of latent factors.

Parameters :

-
mmvec ( MMvec ) – Fitted model.

-
components ( ( int , int ) , default ( 0 , 1 ) ) – Zero-indexed latent factors to plot.

-
label_top ( int , default 5 ) – Number of microbes / metabolites to annotate in each cloud.

-
ax ( matplotlib axes , optional )

Return type :

matplotlib axes.
