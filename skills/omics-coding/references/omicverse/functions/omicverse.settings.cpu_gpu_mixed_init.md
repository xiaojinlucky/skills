# omicverse.settings.cpu_gpu_mixed_init #

- Package: omicverse
- Language: Python
- Function: `omicverse.settings.cpu_gpu_mixed_init`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.settings.cpu_gpu_mixed_init.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Initialize CPU-GPU mixed mode for accelerated single-cell analysis.

## Signature

```text
settings. cpu_gpu_mixed_init ( devices = None )
```

## Parameters

- `devices`: ( int | str | None , optional ) – CUDA device to pin for the torch-backed mixed-mode kernels. Accepts an index ( 1 ), a string ( "1" or "cuda:1" ), or a single-element list. None (default) keeps the previous behaviour of using torch’s current device. On a shared multi-GPU server this lets you route omicverse to a free GPU (e.g. GPU 1 while another user holds GPU 0) without touching CUDA_VISIBLE_DEVICES . The selected device is pinned via torch.cuda.set_device so downstream kernels that resolve a bare "cuda" (through current_device ) land on it, and is recorded in ov.settings.device .

## Full Documentation

# omicverse.settings.cpu_gpu_mixed_init #

settings. cpu_gpu_mixed_init ( devices = None ) [source] #

Initialize CPU-GPU mixed mode for accelerated single-cell analysis.

Parameters :

devices ( int | str | None , optional ) – CUDA device to pin for the torch-backed mixed-mode kernels. Accepts an index ( `1 `), a string ( `"1" `or `"cuda:1" `), or a single-element list. `None `(default) keeps the previous behaviour of using torch’s current device. On a shared multi-GPU server this lets you route omicverse to a free GPU (e.g. GPU 1 while another user holds GPU 0) without touching `CUDA_VISIBLE_DEVICES `. The selected device is pinned via `torch.cuda.set_device `so downstream kernels that resolve a bare `"cuda" `(through `current_device `) land on it, and is recorded in `ov.settings.device `.

Returns :

-
None – Sets `self.mode `to `'cpu-gpu-mixed' `and reports detected accelerators.

-
Examples – >>> import omicverse as ov >>> # Initialize mixed mode for better performance >>> ov.settings.cpu_gpu_mixed_init() >>> # Pin GPU 1 on a shared multi-GPU server >>> ov.settings.cpu_gpu_mixed_init(devices=1) >>> adata = ov.pp.qc(adata) # Automatically uses mixed mode on GPU 1
