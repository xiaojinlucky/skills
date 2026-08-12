# omicverse.micro.rarefy #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.rarefy`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.rarefy.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Rarefy counts to a common depth.

## Signature

```text
omicverse.micro. rarefy ( adata , depth = None , seed = 0 , drop_shallow = True , save_original = True , copy = False )
```

## Parameters

- `adata`: ( AnnData ) – Samples × features AnnData with int counts.
- `depth`: ( Optional [ int ] (default: None )) – Target depth. If None , uses the minimum sample library size.
- `seed`: ( int (default: 0 )) – Random seed for reproducibility.
- `drop_shallow`: ( bool (default: True )) – If True, samples with library size < depth are DROPPED. If False, their original counts are kept (no subsampling possible below depth).
- `save_original`: ( bool (default: True )) – If True, a copy of the pre-rarefaction X is saved to adata.layers['counts_raw'] .
- `copy`: ( bool (default: False )) – Return a copy instead of modifying in place.

## Full Documentation

# omicverse.micro.rarefy #

omicverse.micro. rarefy ( adata , depth = None , seed = 0 , drop_shallow = True , save_original = True , copy = False ) [source] #

Rarefy counts to a common depth.

The rarefied matrix overwrites `adata.X `; the original counts are retained in `adata.layers['counts_raw'] `when `save_original=True `.

Parameters :

-
adata ( `AnnData `) – Samples × features AnnData with int counts.

-
depth ( `Optional `[ `int `] (default: `None `)) – Target depth. If `None `, uses the minimum sample library size.

-
seed ( `int `(default: `0 `)) – Random seed for reproducibility.

-
drop_shallow ( `bool `(default: `True `)) – If True, samples with library size < depth are DROPPED. If False, their original counts are kept (no subsampling possible below depth).

-
save_original ( `bool `(default: `True `)) – If True, a copy of the pre-rarefaction `X `is saved to `adata.layers['counts_raw'] `.

-
copy ( `bool `(default: `False `)) – Return a copy instead of modifying in place.
