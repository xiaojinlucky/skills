# omicverse.micro.attach_tree #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.attach_tree`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.attach_tree.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Attach a phylogenetic tree to adata.uns[store_key] .

## Signature

```text
omicverse.micro. attach_tree ( adata , newick = None , tree_path = None , prune = True , store_key = 'tree' , strict = False )
```

## Parameters

- `adata`: ( AnnData ) – The AnnData to annotate ( var_names = ASV / OTU ids).
- `newick`: ( Optional [ str ] (default: None )) – The tree as a newick string. Mutually exclusive with tree_path .
- `tree_path`: ( Union [ str , Path , None ] (default: None )) – Path to a newick file. Mutually exclusive with newick .
- `prune`: ( bool (default: True )) – When True (default), the tree is restricted to tips that appear in adata.var_names . Tips absent from var_names are dropped.
- `store_key`: ( str (default: 'tree' )) – Key under adata.uns where the newick string is written.
- `strict`: ( bool (default: False )) – If True, raise when any ASV in var_names has no matching tree tip. Default False only warns.

## Full Documentation

# omicverse.micro.attach_tree #

omicverse.micro. attach_tree ( adata , newick = None , tree_path = None , prune = True , store_key = 'tree' , strict = False ) [source] #

Attach a phylogenetic tree to `adata.uns[store_key] `.

Parameters :

-
adata ( `AnnData `) – The AnnData to annotate ( `var_names `= ASV / OTU ids).

-
newick ( `Optional `[ `str `] (default: `None `)) – The tree as a newick string. Mutually exclusive with `tree_path `.

-
tree_path ( `Union `[ `str `, `Path `, `None `] (default: `None `)) – Path to a newick file. Mutually exclusive with `newick `.

-
prune ( `bool `(default: `True `)) – When True (default), the tree is restricted to tips that appear in `adata.var_names `. Tips absent from var_names are dropped.

-
store_key ( `str `(default: `'tree' `)) – Key under `adata.uns `where the newick string is written.

-
strict ( `bool `(default: `False `)) – If True, raise when any ASV in `var_names `has no matching tree tip. Default False only warns.
