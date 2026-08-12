# omicverse.single.SCENIC #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.SCENIC`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.SCENIC.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Initialize a SCENIC workflow.

## Signature

```text
class omicverse.single. SCENIC ( adata , db_glob = None , motif_path = None , n_jobs = 8 , species = None , data_dir = './data/scenic' , download = True , db_names = None )
```

## Parameters

- `adata`: ( anndata.AnnData ) – Input expression object.
- `db_glob`: ( str , sequence of str or None ) – Ranking database feather path pattern or explicit feather file list. If None , species is used to prepare cisTarget resources automatically.
- `motif_path`: ( str or None ) – Motif-to-TF annotation table. If None , species is used to prepare the matching motif annotation table automatically.
- `n_jobs`: ( int ) – Number of workers used by SCENIC steps.
- `species`: ( {'human' , 'mouse' , 'fly'} or None ) – Species used for automatic cisTarget resource preparation. Aliases such as 'hg38' , 'mm10' and 'dm6' are accepted.
- `data_dir`: ( str ) – Directory used to cache downloaded cisTarget resources.
- `download`: ( bool ) – Whether to download missing automatic resources. If False , missing files raise FileNotFoundError with the expected URLs.
- `db_names`: ( str , sequence of str or None ) – Ranking database names to use for automatic resources. Human and mouse support '500bp' and '10kb' ; fly supports 'default' . If None , all available gene-based ranking databases for the species are used.

## Full Documentation

# omicverse.single.SCENIC #

class omicverse.single. SCENIC ( adata , db_glob = None , motif_path = None , n_jobs = 8 , species = None , data_dir = './data/scenic' , download = True , db_names = None ) [source] #

__init__ ( adata , db_glob = None , motif_path = None , n_jobs = 8 , species = None , data_dir = './data/scenic' , download = True , db_names = None ) [source] #

Initialize a SCENIC workflow.

Parameters :

-
adata ( anndata.AnnData ) – Input expression object.

-
db_glob ( str , sequence of str or None ) – Ranking database feather path pattern or explicit feather file list. If `None `, `species `is used to prepare cisTarget resources automatically.

-
motif_path ( str or None ) – Motif-to-TF annotation table. If `None `, `species `is used to prepare the matching motif annotation table automatically.

-
n_jobs ( int ) – Number of workers used by SCENIC steps.

-
species ( {'human' , 'mouse' , 'fly'} or None ) – Species used for automatic cisTarget resource preparation. Aliases such as `'hg38' `, `'mm10' `and `'dm6' `are accepted.

-
data_dir ( str ) – Directory used to cache downloaded cisTarget resources.

-
download ( bool ) – Whether to download missing automatic resources. If `False `, missing files raise `FileNotFoundError `with the expected URLs.

-
db_names ( str , sequence of str or None ) – Ranking database names to use for automatic resources. Human and mouse support `'500bp' `and `'10kb' `; fly supports `'default' `. If `None `, all available gene-based ranking databases for the species are used.

Methods

`__init__ `(adata[, db_glob, motif_path, ...])

Initialize a SCENIC workflow.

`cal_grn `([method, layer, tf_names])

Infer a GRN and store the edge list on the SCENIC object.

`cal_regulons `([rho_mask_dropouts, seed])
