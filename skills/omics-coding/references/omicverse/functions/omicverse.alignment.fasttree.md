# omicverse.alignment.fasttree #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.fasttree`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.fasttree.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run FastTree to infer a phylogenetic tree.

## Signature

```text
omicverse.alignment. fasttree ( aligned_fasta , output_dir , output_name = 'tree.nwk' , model = 'gtr' , gamma = True , nt = True , threads = None , extra_args = None , fasttree_path = None , auto_install = True , overwrite = False )
```

## Parameters

- `aligned_fasta`: ( str )
- `output_dir`: ( str )
- `output_name`: ( str (default: 'tree.nwk' ))
- `model`: ( str (default: 'gtr' ))
- `gamma`: ( bool (default: True ))
- `nt`: ( bool (default: True ))
- `threads`: ( Optional [ int ] (default: None ))
- `extra_args`: ( Optional [ Sequence [ str ]] (default: None ))
- `fasttree_path`: ( Optional [ str ] (default: None ))
- `auto_install`: ( bool (default: True ))
- `overwrite`: ( bool (default: False ))

## Full Documentation

# omicverse.alignment.fasttree #

omicverse.alignment. fasttree ( aligned_fasta , output_dir , output_name = 'tree.nwk' , model = 'gtr' , gamma = True , nt = True , threads = None , extra_args = None , fasttree_path = None , auto_install = True , overwrite = False ) [source] #

Run FastTree to infer a phylogenetic tree.

Parameters :

-
aligned_fasta ( `str `)

-
output_dir ( `str `)

-
output_name ( `str `(default: `'tree.nwk' `))

-
model ( `str `(default: `'gtr' `))

-
gamma ( `bool `(default: `True `))

-
nt ( `bool `(default: `True `))

-
threads ( `Optional `[ `int `] (default: `None `))

-
extra_args ( `Optional `[ `Sequence `[ `str `]] (default: `None `))

-
fasttree_path ( `Optional `[ `str `] (default: `None `))

-
auto_install ( `bool `(default: `True `))

-
overwrite ( `bool `(default: `False `))
