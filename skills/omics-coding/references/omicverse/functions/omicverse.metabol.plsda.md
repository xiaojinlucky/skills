# omicverse.metabol.plsda #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.plsda`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.plsda.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Partial Least Squares Discriminant Analysis (wraps sklearn PLS).

## Signature

```text
omicverse.metabol. plsda ( adata , * , group_col = 'group' , group_a = None , group_b = None , n_components = 2 , scale = False )
```

## Parameters

- `n_components`: ( int (default: 2 )) – Number of latent components. 2 is standard for visualization; use leave-one-out Q² to pick the optimal count for classification.
- `scale`: ( bool (default: False )) – Scale features inside sklearn PLS (z-score). Usually False here because you’ve already Pareto-scaled via transform() .
- `adata`: ( AnnData )
- `group_col`: ( str (default: 'group' ))
- `group_a`: ( Optional [ str ] (default: None ))
- `group_b`: ( Optional [ str ] (default: None ))

## Full Documentation

# omicverse.metabol.plsda #

omicverse.metabol. plsda ( adata , * , group_col = 'group' , group_a = None , group_b = None , n_components = 2 , scale = False ) [source] #

Partial Least Squares Discriminant Analysis (wraps sklearn PLS).

Parameters :

-
n_components ( `int `(default: `2 `)) – Number of latent components. 2 is standard for visualization; use leave-one-out Q² to pick the optimal count for classification.

-
scale ( `bool `(default: `False `)) – Scale features inside sklearn PLS (z-score). Usually False here because you’ve already Pareto-scaled via `transform() `.

-
adata ( `AnnData `)

-
group_col ( `str `(default: `'group' `))

-
group_a ( `Optional `[ `str `] (default: `None `))

-
group_b ( `Optional `[ `str `] (default: `None `))
