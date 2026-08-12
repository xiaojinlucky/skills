# omicverse.micro.simulate_paired #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.simulate_paired`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.simulate_paired.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Build a paired microbe + metabolite cohort with planted producer pairs.

## Signature

```text
omicverse.micro. simulate_paired ( n_samples = 30 , n_microbes = 40 , n_metabolites = 20 , n_pairs = 5 , effect_range = (1.0, 2.0) , depth_range = (1000, 10000) , seed = 0 )
```

## Parameters

- `n_samples`: ( int (default: 30 ))
- `n_microbes`: ( int (default: 40 ))
- `n_metabolites`: ( int (default: 20 ))
- `n_pairs`: ( int (default: 5 ))
- `effect_range`: ( Tuple [ float , float ] (default: (1.0, 2.0) ))
- `depth_range`: ( Tuple [ int , int ] (default: (1000, 10000) ))
- `seed`: ( int (default: 0 ))

## Full Documentation

# omicverse.micro.simulate_paired #

omicverse.micro. simulate_paired ( n_samples = 30 , n_microbes = 40 , n_metabolites = 20 , n_pairs = 5 , effect_range = (1.0, 2.0) , depth_range = (1000, 10000) , seed = 0 ) [source] #

Build a paired microbe + metabolite cohort with planted producer pairs.

Returns `(adata_microbe, adata_metabolite, truth) `where `truth `is a DataFrame with columns `microbe / metabolite / effect `listing the planted microbe→metabolite log-linear associations.

Parameters :

-
n_samples ( `int `(default: `30 `))

-
n_microbes ( `int `(default: `40 `))

-
n_metabolites ( `int `(default: `20 `))

-
n_pairs ( `int `(default: `5 `))

-
effect_range ( `Tuple `[ `float `, `float `] (default: `(1.0, 2.0) `))

-
depth_range ( `Tuple `[ `int `, `int `] (default: `(1000, 10000) `))

-
seed ( `int `(default: `0 `))
