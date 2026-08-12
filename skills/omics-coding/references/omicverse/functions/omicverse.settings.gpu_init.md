# omicverse.settings.gpu_init #

- Package: omicverse
- Language: Python
- Function: `omicverse.settings.gpu_init`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.settings.gpu_init.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Initialize GPU mode with RAPIDS for accelerated single-cell analysis.

## Signature

```text
settings. gpu_init ( managed_memory = True , pool_allocator = True , devices = 0 )
```

## Parameters

- `managed_memory`: ( bool , optional ) – Enable NVIDIA Unified Memory to support oversubscription for large datasets.
- `pool_allocator`: ( bool , optional ) – Enable RMM memory pool allocator for faster repeated GPU allocations.
- `devices`: ( int | list [ int ] , optional ) – CUDA device index (or indices) to register in RMM.

## Full Documentation

# omicverse.settings.gpu_init #

settings. gpu_init ( managed_memory = True , pool_allocator = True , devices = 0 ) [source] #

Initialize GPU mode with RAPIDS for accelerated single-cell analysis.

Parameters :

-
managed_memory ( bool , optional ) – Enable NVIDIA Unified Memory to support oversubscription for large datasets.

-
pool_allocator ( bool , optional ) – Enable RMM memory pool allocator for faster repeated GPU allocations.

-
devices ( int | list [ int ] , optional ) – CUDA device index (or indices) to register in RMM.

Returns :

-
None – Sets `self.mode `to `'gpu' `and configures RAPIDS/CuPy allocators.

-
Examples – >>> import omicverse as ov >>> # Initialize GPU mode with default settings >>> ov.settings.gpu_init() >>> # Custom GPU initialization >>> ov.settings.gpu_init(managed_memory=False, pool_allocator=True)
