# omicverse.alignment.dada2_pipeline #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.dada2_pipeline`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.dada2_pipeline.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run pydada2 end-to-end and return an AnnData.

## Signature

```text
omicverse.alignment. dada2_pipeline ( samples , workdir = None , * , db_fasta = None , trunc_len = (240, 160) , max_ee = (2.0, 2.0) , trunc_q = 2 , min_overlap = 12 , max_mismatch = 0 , chimera_method = 'consensus' , nbases = 100000000 , sintax_cutoff = 0.8 , sintax_strand = 'both' , threads = 4 , sample_metadata = None , overwrite = False )
```

## Parameters

- `samples`: ( Sequence [ Tuple [ str , str , Optional [ str ]]] ) – [(sample, fq1, fq2), ...] . fq2 may be None for single-end.
- `workdir`: ( Optional [ str ] (default: None )) – Required. Absolute path for intermediates. No $HOME fallback.
- `db_fasta`: ( Optional [ str ] (default: None )) – Optional path to a SINTAX-formatted reference FASTA. When supplied, ASV taxonomy is assigned by piping the ASV FASTA through omicverse.alignment.vsearch.sintax() and merging the 7-rank call into adata.var .
- `trunc_len`: ( Union [ int , Tuple [ int , int ]] (default: (240, 160) )) – (fwd, rev) truncation lengths in bp. V4 default (240, 160) .
- `max_ee`: ( Union [ float , Tuple [ float , float ]] (default: (2.0, 2.0) )) – (fwd, rev) expected-error thresholds.
- `chimera_method`: ( str (default: 'consensus' )) – Passed to pydada2.remove_bimera_denovo .
- `threads`: ( int (default: 4 )) – Used only by the vsearch SINTAX pass at the end.
- `trunc_q`: ( int (default: 2 ))
- `min_overlap`: ( int (default: 12 ))
- `max_mismatch`: ( int (default: 0 ))
- `nbases`: ( int (default: 100000000 ))
- `sintax_cutoff`: ( float (default: 0.8 ))
- `sintax_strand`: ( str (default: 'both' ))
- `sample_metadata`: ( Optional [ DataFrame ] (default: None ))
- `overwrite`: ( bool (default: False ))

## Full Documentation

# omicverse.alignment.dada2_pipeline #

omicverse.alignment. dada2_pipeline ( samples , workdir = None , * , db_fasta = None , trunc_len = (240, 160) , max_ee = (2.0, 2.0) , trunc_q = 2 , min_overlap = 12 , max_mismatch = 0 , chimera_method = 'consensus' , nbases = 100000000 , sintax_cutoff = 0.8 , sintax_strand = 'both' , threads = 4 , sample_metadata = None , overwrite = False ) [source] #

Run pydada2 end-to-end and return an AnnData.

Parameters :

-
samples ( `Sequence `[ `Tuple `[ `str `, `str `, `Optional `[ `str `]]] ) – `[(sample, fq1, fq2), ...] `. `fq2 `may be None for single-end.

-
workdir ( `Optional `[ `str `] (default: `None `)) – Required. Absolute path for intermediates. No `$HOME `fallback.

-
db_fasta ( `Optional `[ `str `] (default: `None `)) – Optional path to a SINTAX-formatted reference FASTA. When supplied, ASV taxonomy is assigned by piping the ASV FASTA through `omicverse.alignment.vsearch.sintax() `and merging the 7-rank call into `adata.var `.

-
trunc_len ( `Union `[ `int `, `Tuple `[ `int `, `int `]] (default: `(240, 160) `)) – `(fwd, rev) `truncation lengths in bp. V4 default `(240, 160) `.

-
max_ee ( `Union `[ `float `, `Tuple `[ `float `, `float `]] (default: `(2.0, 2.0) `)) – `(fwd, rev) `expected-error thresholds.

-
chimera_method ( `str `(default: `'consensus' `)) – Passed to `pydada2.remove_bimera_denovo `.

-
threads ( `int `(default: `4 `)) – Used only by the vsearch SINTAX pass at the end.

-
trunc_q ( `int `(default: `2 `))

-
min_overlap ( `int `(default: `12 `))

-
max_mismatch ( `int `(default: `0 `))

-
nbases ( `int `(default: `100000000 `))

-
sintax_cutoff ( `float `(default: `0.8 `))

-
sintax_strand ( `str `(default: `'both' `))

-
sample_metadata ( `Optional `[ `DataFrame `] (default: `None `))

-
overwrite ( `bool `(default: `False `))
