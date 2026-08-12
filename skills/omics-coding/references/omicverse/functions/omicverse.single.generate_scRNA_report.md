# omicverse.single.generate_scRNA_report #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.generate_scRNA_report`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.generate_scRNA_report.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Generate a MultiQC-style HTML report for single-cell RNA-seq analysis.

## Signature

```text
omicverse.single. generate_scRNA_report ( adata , output_path = 'scRNA_analysis_report.html' , species = 'human' , sample_key = None , template_dir = None , enable_analytics = True , analytics_id = 'OV-001' )
```

## Parameters

- `adata`: ( AnnData object ) – Analyzed single-cell AnnData, typically produced by ov.single.lazy .
- `output_path`: ( str ) – Output path of generated HTML report.
- `species`: ( str ) – Species label shown in report metadata.
- `sample_key`: ( str or None ) – Column in adata.obs used as sample/batch grouping.
- `template_dir`: ( str or None ) – Directory containing HTML templates. If None , built-in templates are used.
- `enable_analytics`: ( bool ) – Whether analytics snippet is injected into final HTML.
- `analytics_id`: ( str ) – Analytics identifier used when tracking is enabled.

## Full Documentation

# omicverse.single.generate_scRNA_report #

omicverse.single. generate_scRNA_report ( adata , output_path = 'scRNA_analysis_report.html' , species = 'human' , sample_key = None , template_dir = None , enable_analytics = True , analytics_id = 'OV-001' ) [source] #

Generate a MultiQC-style HTML report for single-cell RNA-seq analysis.

Parameters :

-
adata ( AnnData object ) – Analyzed single-cell AnnData, typically produced by `ov.single.lazy `.

-
output_path ( str ) – Output path of generated HTML report.

-
species ( str ) – Species label shown in report metadata.

-
sample_key ( str or None ) – Column in `adata.obs `used as sample/batch grouping.

-
template_dir ( str or None ) – Directory containing HTML templates. If `None `, built-in templates are used.

-
enable_analytics ( bool ) – Whether analytics snippet is injected into final HTML.

-
analytics_id ( str ) – Analytics identifier used when tracking is enabled.

Returns :

Path to saved report file.

Return type :

str
