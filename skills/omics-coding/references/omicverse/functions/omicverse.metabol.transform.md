# omicverse.metabol.transform #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.transform`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.transform.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Apply a feature-level transformation to adata.X .

## Signature

```text
omicverse.metabol. transform ( adata , * , method = 'log' , pseudocount = 1.0 , stash_raw = True )
```

## Parameters

- `method`: ( Literal [ 'log' , 'glog' , 'autoscale' , 'pareto' , 'none' ] (default: 'log' )) – "log" , "glog" , "autoscale" , "pareto" , or "none" .
- `pseudocount`: ( float (default: 1.0 )) – For "log" and "glog" . Default 1.0 (the MetaboAnalyst default for concentration data).
- `stash_raw`: ( bool (default: True )) – If True, stash the pre-transform matrix in layers['raw'] so later steps (e.g. absolute-value plots) can retrieve it.
- `adata`: ( AnnData )

## Full Documentation

# omicverse.metabol.transform #

omicverse.metabol. transform ( adata , * , method = 'log' , pseudocount = 1.0 , stash_raw = True ) [source] #

Apply a feature-level transformation to `adata.X `.

Parameters :

-
method ( `Literal `[ `'log' `, `'glog' `, `'autoscale' `, `'pareto' `, `'none' `] (default: `'log' `)) – `"log" `, `"glog" `, `"autoscale" `, `"pareto" `, or `"none" `.

-
pseudocount ( `float `(default: `1.0 `)) – For `"log" `and `"glog" `. Default 1.0 (the MetaboAnalyst default for concentration data).

-
stash_raw ( `bool `(default: `True `)) – If True, stash the pre-transform matrix in `layers['raw'] `so later steps (e.g. absolute-value plots) can retrieve it.

-
adata ( `AnnData `)
