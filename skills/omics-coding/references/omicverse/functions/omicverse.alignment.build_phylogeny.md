# omicverse.alignment.build_phylogeny #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.build_phylogeny`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.build_phylogeny.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Build a phylogenetic tree end-to-end.

## Signature

```text
omicverse.alignment. build_phylogeny ( asvs_fasta , workdir = None , * , mafft_mode = 'auto' , fasttree_model = 'gtr' , gamma = True , mafft_threads = 4 , fasttree_threads = None , overwrite = False )
```

## Parameters

- `asvs_fasta`: ( str )
- `workdir`: ( Optional [ str ] (default: None ))
- `mafft_mode`: ( str (default: 'auto' ))
- `fasttree_model`: ( str (default: 'gtr' ))
- `gamma`: ( bool (default: True ))
- `mafft_threads`: ( int (default: 4 ))
- `fasttree_threads`: ( Optional [ int ] (default: None ))
- `overwrite`: ( bool (default: False ))

## Full Documentation

# omicverse.alignment.build_phylogeny #

omicverse.alignment. build_phylogeny ( asvs_fasta , workdir = None , * , mafft_mode = 'auto' , fasttree_model = 'gtr' , gamma = True , mafft_threads = 4 , fasttree_threads = None , overwrite = False ) [source] #

Build a phylogenetic tree end-to-end.

Returns `{"aligned": ..., "tree": ..., "newick": "<tree-text>", ...} `. The newick string has had vsearch’s `;size=N `annotations stripped so that ete3 / unifrac can parse tip labels directly.

Parameters :

-
asvs_fasta ( `str `)

-
workdir ( `Optional `[ `str `] (default: `None `))

-
mafft_mode ( `str `(default: `'auto' `))

-
fasttree_model ( `str `(default: `'gtr' `))

-
gamma ( `bool `(default: `True `))

-
mafft_threads ( `int `(default: `4 `))

-
fasttree_threads ( `Optional `[ `int `] (default: `None `))

-
overwrite ( `bool `(default: `False `))
