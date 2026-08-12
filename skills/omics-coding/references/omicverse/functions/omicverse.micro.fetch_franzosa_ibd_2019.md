# omicverse.micro.fetch_franzosa_ibd_2019 #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.fetch_franzosa_ibd_2019`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.fetch_franzosa_ibd_2019.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Download + parse the Franzosa et al. 2019 paired IBD dataset.

## Signature

```text
omicverse.micro. fetch_franzosa_ibd_2019 ( data_dir , overwrite = False , microbe_count_scale = 1000000.0 )
```

## Parameters

- `data_dir`: ( str ) – Absolute path the three TSVs are cached under. No $HOME fallback — you pick where it goes (recommended: a scratch directory).
- `overwrite`: ( bool (default: False )) – Re-download even if the files already exist.
- `microbe_count_scale`: ( float (default: 1000000.0 )) – The Borenstein TSV delivers per-sample relative abundances . To make the tables look like familiar 16S count matrices (integer counts, range 1 to ~100,000) we multiply by this scale and round — a pseudo-count-per-million by default. Pass 1.0 to keep proportions (most useful if you plan to CLR-transform immediately and don’t need integer counts). All downstream ov.micro APIs ( filter_by_prevalence , paired_spearman , paired_cca , MMvec ) work on either, but min_count filters expect counts >= 1.

## Full Documentation

# omicverse.micro.fetch_franzosa_ibd_2019 #

omicverse.micro. fetch_franzosa_ibd_2019 ( data_dir , overwrite = False , microbe_count_scale = 1000000.0 ) [source] #

Download + parse the Franzosa et al. 2019 paired IBD dataset.

Files are fetched from the Borenstein lab’s curated `microbiome-metabolome-curated-data `GitHub repository — three TSVs (genera.tsv, mtb.tsv, metadata.tsv) totalling about 30 MB. Once the files exist in `data_dir `the function is offline.

Parameters :

-
data_dir ( `str `) – Absolute path the three TSVs are cached under. No `$HOME `fallback — you pick where it goes (recommended: a scratch directory).

-
overwrite ( `bool `(default: `False `)) – Re-download even if the files already exist.

-
microbe_count_scale ( `float `(default: `1000000.0 `)) – The Borenstein TSV delivers per-sample relative abundances . To make the tables look like familiar 16S count matrices (integer counts, range 1 to ~100,000) we multiply by this scale and round — a pseudo-count-per-million by default. Pass `1.0 `to keep proportions (most useful if you plan to CLR-transform immediately and don’t need integer counts). All downstream `ov.micro `APIs ( `filter_by_prevalence `, `paired_spearman `, `paired_cca `, `MMvec `) work on either, but `min_count `filters expect counts >= 1.

Returns :

-
`(adata_microbe, adata_metabolite) `— two AnnDatas sharing

-
`obs_names `(same 220 samples, same order). The microbe `var `

-
carries parsed GTDB 7-rank taxonomy ( `` domain / phylum / class /

-
order / family / genus / species`` + the raw GTDB string as

-
`taxonomy `). The metabolite `var `carries the cluster ID and,

-
where annotated, the HMDB name ( `name `column; `NaN `for

-
unannotated clusters). Both `obs `frames carry the same cohort

-
metadata from metadata.tsv ( `Study.Group `= CD / UC / Control,

-
`Subject `, `Age `, `Fecal.Calprotectin `, drug covariates).
