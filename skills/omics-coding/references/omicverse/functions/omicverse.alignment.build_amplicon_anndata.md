# omicverse.alignment.build_amplicon_anndata #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.build_amplicon_anndata`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.build_amplicon_anndata.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Compose anndata.AnnData from vsearch stepwise outputs.

## Signature

```text
omicverse.alignment. build_amplicon_anndata ( otutab_tsv , asv_fasta , sintax_tsv = None , sample_metadata = None , sample_order = None )
```

## Parameters

- `otutab_tsv`: ( str ) – Path to the --otutabout TSV from vsearch.usearch_global() . First column = ASV id, remaining columns = sample ids.
- `asv_fasta`: ( str ) – Path to the ASV centroid FASTA (output of vsearch.unoise3() or the non-chimera FASTA from vsearch.uchime3_denovo() ).
- `sintax_tsv`: ( Optional [ str ] (default: None )) – Optional path to the vsearch --sintax --tabbedout TSV. When supplied, 7-rank taxonomy columns ( domain / phylum / class / order / family / genus / species ), the ; -joined taxonomy string and sintax_confidence are written into var .
- `sample_metadata`: ( Optional [ DataFrame ] (default: None )) – Optional DataFrame indexed by sample id; merged into obs .
- `sample_order`: ( Optional [ Sequence [ str ]] (default: None )) – Optional list of sample ids to enforce row order in obs / X . Defaults to the column order of the otutab TSV.

## Full Documentation

# omicverse.alignment.build_amplicon_anndata #

omicverse.alignment. build_amplicon_anndata ( otutab_tsv , asv_fasta , sintax_tsv = None , sample_metadata = None , sample_order = None ) [source] #

Compose `anndata.AnnData `from vsearch stepwise outputs.

Parameters :

-
otutab_tsv ( `str `) – Path to the `--otutabout `TSV from `vsearch.usearch_global() `. First column = ASV id, remaining columns = sample ids.

-
asv_fasta ( `str `) – Path to the ASV centroid FASTA (output of `vsearch.unoise3() `or the non-chimera FASTA from `vsearch.uchime3_denovo() `).

-
sintax_tsv ( `Optional `[ `str `] (default: `None `)) – Optional path to the vsearch `--sintax --tabbedout `TSV. When supplied, 7-rank taxonomy columns ( `domain `/ `phylum `/ `class `/ `order `/ `family `/ `genus `/ `species `), the `; `-joined `taxonomy `string and `sintax_confidence `are written into `var `.

-
sample_metadata ( `Optional `[ `DataFrame `] (default: `None `)) – Optional DataFrame indexed by sample id; merged into `obs `.

-
sample_order ( `Optional `[ `Sequence `[ `str `]] (default: `None `)) – Optional list of sample ids to enforce row order in `obs `/ `X `. Defaults to the column order of the otutab TSV.

Returns :

`X `is a `scipy.sparse.csr_matrix `of int32 counts (samples × ASVs). Same schema as `amplicon_16s_pipeline() `.

Return type :

anndata.AnnData
