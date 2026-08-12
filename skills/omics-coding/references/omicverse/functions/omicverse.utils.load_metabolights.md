# omicverse.utils.load_metabolights #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.load_metabolights`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.load_metabolights.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Load a Metabolights study into a samples × metabolites AnnData.

## Signature

```text
omicverse.utils. load_metabolights ( study_id , * , group_col = None , cache_dir = 'metabolights_cache' , maf_name = None , sample_name_col = 'Sample Name' , refresh = False )
```

## Parameters

- `study_id`: ( str ) – Metabolights accession, e.g. "MTBLS1" . The study must be under the public mirror at ftp.ebi.ac.uk/pub/databases/ metabolights/studies/public .
- `group_col`: ( Optional [ str ] (default: None )) – Column in the sample sheet to use as the primary phenotype label. When given, the column is renamed to "group" in adata.obs to match the convention the rest of ov.metabol expects ( differential(group_col="group") , roc_feature(group_col="group") , …). Common choices: "Factor Value[<name>]" .
- `cache_dir`: ( str | Path (default: 'metabolights_cache' )) – Directory to cache downloaded files. Default ./metabolights_cache/ . Re-runs reuse cached files unless refresh=True .
- `maf_name`: ( Optional [ str ] (default: None )) – Explicit MAF filename. Default: first alphabetical m_*_maf.tsv in the directory listing. Override when a study ships multiple MAFs (e.g. positive vs. negative mode).
- `sample_name_col`: ( str (default: 'Sample Name' )) – Column in the sample sheet carrying the assay-side sample identifiers. Default "Sample Name" — works for every study that follows the ISA-Tab standard.
- `refresh`: ( bool (default: False )) – Force re-download even if the cached file exists. Use when Metabolights updates a study version in place.

## Full Documentation

# omicverse.utils.load_metabolights #

omicverse.utils. load_metabolights ( study_id , * , group_col = None , cache_dir = 'metabolights_cache' , maf_name = None , sample_name_col = 'Sample Name' , refresh = False ) [source] #

Load a Metabolights study into a samples × metabolites AnnData.

Parameters :

-
study_id ( `str `) – Metabolights accession, e.g. `"MTBLS1" `. The study must be under the public mirror at `ftp.ebi.ac.uk/pub/databases/ metabolights/studies/public `.

-
group_col ( `Optional `[ `str `] (default: `None `)) – Column in the sample sheet to use as the primary phenotype label. When given, the column is renamed to `"group" `in `adata.obs `to match the convention the rest of `ov.metabol `expects ( `differential(group_col="group") `, `roc_feature(group_col="group") `, …). Common choices: `"Factor Value[<name>]" `.

-
cache_dir ( `str `| `Path `(default: `'metabolights_cache' `)) – Directory to cache downloaded files. Default `./metabolights_cache/ `. Re-runs reuse cached files unless `refresh=True `.

-
maf_name ( `Optional `[ `str `] (default: `None `)) – Explicit MAF filename. Default: first alphabetical `m_*_maf.tsv `in the directory listing. Override when a study ships multiple MAFs (e.g. positive vs. negative mode).

-
sample_name_col ( `str `(default: `'Sample Name' `)) – Column in the sample sheet carrying the assay-side sample identifiers. Default `"Sample Name" `— works for every study that follows the ISA-Tab standard.

-
refresh ( `bool `(default: `False `)) – Force re-download even if the cached file exists. Use when Metabolights updates a study version in place.

Returns :

`obs `carries every column of the sample sheet plus a derived `group `column (if `group_col `was supplied). `var `carries `metabolite_identification `(filled with `unknown_shift_<ppm> `for NMR rows that lack a named identification) plus `chemical_formula `and `smiles `when available. `uns['metabolights'] = {'study_id', 'maf_name', 'sample_sheet'} `records provenance.

Return type :

AnnData
