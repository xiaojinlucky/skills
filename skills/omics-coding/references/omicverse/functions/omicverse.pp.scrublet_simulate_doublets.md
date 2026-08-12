# omicverse.pp.scrublet_simulate_doublets #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.scrublet_simulate_doublets`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.scrublet_simulate_doublets.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Simulate synthetic doublets from random cell pairs.

## Signature

```text
omicverse.pp. scrublet_simulate_doublets ( adata , * , layer = None , sim_doublet_ratio = 2.0 , synthetic_doublet_umi_subsampling = 1.0 , random_seed = 0 )
```

## Parameters

- `adata`: ( AnnData ) – Input AnnData with observed cell transcriptomes.
- `layer`: ( str , optional ) – Layer key to use as input matrix. Uses adata.X when None .
- `sim_doublet_ratio`: ( float , default=2.0 ) – Number of simulated doublets relative to observed cells.
- `synthetic_doublet_umi_subsampling`: ( float , default=1.0 ) – UMI subsampling fraction used when creating synthetic doublets.
- `random_seed`: ( int or RandomState , default=0 ) – Random state controlling pair sampling reproducibility.

## Full Documentation

# omicverse.pp.scrublet_simulate_doublets #

omicverse.pp. scrublet_simulate_doublets ( adata , * , layer = None , sim_doublet_ratio = 2.0 , synthetic_doublet_umi_subsampling = 1.0 , random_seed = 0 ) [source] #

Simulate synthetic doublets from random cell pairs.

Parameters :

-
adata ( AnnData ) – Input AnnData with observed cell transcriptomes.

-
layer ( str , optional ) – Layer key to use as input matrix. Uses `adata.X `when `None `.

-
sim_doublet_ratio ( float , default=2.0 ) – Number of simulated doublets relative to observed cells.

-
synthetic_doublet_umi_subsampling ( float , default=1.0 ) – UMI subsampling fraction used when creating synthetic doublets.

-
random_seed ( int or RandomState , default=0 ) – Random state controlling pair sampling reproducibility.

Returns :

Synthetic-doublet AnnData containing simulated matrix and metadata.

Return type :

AnnData
