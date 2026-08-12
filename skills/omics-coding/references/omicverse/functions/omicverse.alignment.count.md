# omicverse.alignment.count #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.count`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.count.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Quantify expression matrices from FASTQ files via kb count .

## Signature

```text
omicverse.alignment. count ( index_path , t2g_path , technology , fastq_paths , output_path = '.' , whitelist_path = None , replacement_path = None , threads = 8 , memory = '2G' , workflow = 'standard' , overwrite = False , temp_dir = 'tmp' , tcc = False , mm = False , filter_barcodes = False , filter_threshold = None , loom = False , loom_names = None , h5ad = False , cellranger = False , gene_names = False , report = False , strand = None , parity = None , fragment_l = None , fragment_s = None , bootstraps = None , em = False , aa = False , genomebam = False , inleaved = False , batch_barcodes = False , exact_barcodes = False , numreads = None , store_num = False , long_read = False , threshold = 0.8 , platform = 'ONT' , c1 = None , c2 = None , nucleus = False , ** kwargs )
```

## Parameters

- `index_path`: ( str ) – Path to kallisto index produced by kb ref .
- `t2g_path`: ( str ) – Transcript-to-gene mapping table used for gene-level aggregation.
- `technology`: ( str ) – Sequencing technology preset (for example 10XV3 , BULK ).
- `fastq_paths`: ( str | list [ str ] ) – One or more FASTQ file paths passed to kb count.
- `output_path`: ( str , optional ) – Output directory for count matrices and intermediate files.
- `whitelist_path`: ( str | None , optional ) – Optional custom barcode whitelist.
- `replacement_path`: ( str | None , optional ) – Optional barcode replacement file.
- `threads`: ( int , optional ) – Number of threads used by kb.
- `memory`: ( str , optional ) – Memory request string passed to kb (for example 2G ).
- `workflow`: ( str , optional ) – kb workflow mode ( standard , nucleus , lamanno etc.).
- `overwrite`: ( bool , optional ) – Whether to overwrite existing output directory contents.
- `temp_dir`: ( str , optional ) – Temporary directory root for kb intermediate files.
- `tcc`: ( bool , optional ) – Output transcript compatibility counts instead of gene matrix.
- `mm`: ( bool , optional ) – Use memory-mapped mode when supported.
- `filter_barcodes`: ( bool , optional ) – Enable barcode filtering (not valid for technology='BULK' ).
- `filter_threshold`: ( int | None , optional ) – Barcode filter threshold used by bustools filtering.
- `loom`: ( bool , optional ) – Export loom matrix.
- `loom_names`: ( str | list [ str ] | None , optional ) – Custom loom row/column naming behavior.
- `h5ad`: ( bool , optional ) – Export H5AD matrix output.
- `cellranger`: ( bool , optional ) – Emit Cell Ranger-compatible output structure.
- `gene_names`: ( bool , optional ) – Prefer gene symbols over IDs when possible.
- `report`: ( bool , optional ) – Generate additional kb report files.
- `strand`: ( str | None , optional ) – Strand option for long-read/technology-specific modes.
- `parity`: ( str | None , optional ) – Read parity setting for specific technologies.
- `fragment_l`: ( int | None , optional ) – Mean fragment length for bulk-like protocols.
- `fragment_s`: ( int | None , optional ) – Fragment length standard deviation.
- `bootstraps`: ( int | None , optional ) – Number of kallisto bootstrap rounds.
- `em`: ( bool , optional ) – Enable EM optimization.
- `aa`: ( bool , optional ) – Enable amino-acid mode where supported.
- `genomebam`: ( bool , optional ) – Request genome BAM generation (version-dependent support).
- `inleaved`: ( bool , optional ) – Treat reads as interleaved input.
- `batch_barcodes`: ( bool , optional ) – Enable batched barcode handling.
- `exact_barcodes`: ( bool , optional ) – Require exact barcode matching.
- `numreads`: ( int | None , optional ) – Limit number of reads processed.
- `store_num`: ( bool , optional ) – Store BUS record counts in output metadata.
- `long_read`: ( bool , optional ) – Enable long-read mode.
- `threshold`: ( float , optional ) – Long-read assignment threshold.
- `platform`: ( str , optional ) – Long-read platform label (for example ONT ).
- `c1`: ( str | None , optional ) – Spliced capture file path for velocity workflows.
- `c2`: ( str | None , optional ) – Intronic capture file path for velocity workflows.
- `nucleus`: ( bool , optional ) – Shortcut to switch workflow from standard to nucleus .
- `**kwargs`: – Extra kb flags forwarded verbatim.

## Full Documentation

# omicverse.alignment.count #

omicverse.alignment. count ( index_path , t2g_path , technology , fastq_paths , output_path = '.' , whitelist_path = None , replacement_path = None , threads = 8 , memory = '2G' , workflow = 'standard' , overwrite = False , temp_dir = 'tmp' , tcc = False , mm = False , filter_barcodes = False , filter_threshold = None , loom = False , loom_names = None , h5ad = False , cellranger = False , gene_names = False , report = False , strand = None , parity = None , fragment_l = None , fragment_s = None , bootstraps = None , em = False , aa = False , genomebam = False , inleaved = False , batch_barcodes = False , exact_barcodes = False , numreads = None , store_num = False , long_read = False , threshold = 0.8 , platform = 'ONT' , c1 = None , c2 = None , nucleus = False , ** kwargs ) [source] #

Quantify expression matrices from FASTQ files via `kb count `.

Parameters :

-
index_path ( str ) – Path to kallisto index produced by `kb ref `.

-
t2g_path ( str ) – Transcript-to-gene mapping table used for gene-level aggregation.

-
technology ( str ) – Sequencing technology preset (for example `10XV3 `, `BULK `).

-
fastq_paths ( str | list [ str ] ) – One or more FASTQ file paths passed to kb count.

-
output_path ( str , optional ) – Output directory for count matrices and intermediate files.

-
whitelist_path ( str | None , optional ) – Optional custom barcode whitelist.

-
replacement_path ( str | None , optional ) – Optional barcode replacement file.

-
threads ( int , optional ) – Number of threads used by kb.

-
memory ( str , optional ) – Memory request string passed to kb (for example `2G `).

-
workflow ( str , optional ) – kb workflow mode ( `standard `, `nucleus `, `lamanno `etc.).

-
overwrite ( bool , optional ) – Whether to overwrite existing output directory contents.

-
temp_dir ( str , optional ) – Temporary directory root for kb intermediate files.

-
tcc ( bool , optional ) – Output transcript compatibility counts instead of gene matrix.

-
mm ( bool , optional ) – Use memory-mapped mode when supported.

-
filter_barcodes ( bool , optional ) – Enable barcode filtering (not valid for `technology='BULK' `).

-
filter_threshold ( int | None , optional ) – Barcode filter threshold used by bustools filtering.

-
loom ( bool , optional ) – Export loom matrix.

-
loom_names ( str | list [ str ] | None , optional ) – Custom loom row/column naming behavior.

-
h5ad ( bool , optional ) – Export H5AD matrix output.

-
cellranger ( bool , optional ) – Emit Cell Ranger-compatible output structure.

-
gene_names ( bool , optional ) – Prefer gene symbols over IDs when possible.

-
report ( bool , optional ) – Generate additional kb report files.

-
strand ( str | None , optional ) – Strand option for long-read/technology-specific modes.

-
parity ( str | None , optional ) – Read parity setting for specific technologies.

-
fragment_l ( int | None , optional ) – Mean fragment length for bulk-like protocols.

-
fragment_s ( int | None , optional ) – Fragment length standard deviation.

-
bootstraps ( int | None , optional ) – Number of kallisto bootstrap rounds.

-
em ( bool , optional ) – Enable EM optimization.

-
aa ( bool , optional ) – Enable amino-acid mode where supported.

-
genomebam ( bool , optional ) – Request genome BAM generation (version-dependent support).

-
inleaved ( bool , optional ) – Treat reads as interleaved input.

-
batch_barcodes ( bool , optional ) – Enable batched barcode handling.

-
exact_barcodes ( bool , optional ) – Require exact barcode matching.

-
numreads ( int | None , optional ) – Limit number of reads processed.

-
store_num ( bool , optional ) – Store BUS record counts in output metadata.

-
long_read ( bool , optional ) – Enable long-read mode.

-
threshold ( float , optional ) – Long-read assignment threshold.

-
platform ( str , optional ) – Long-read platform label (for example `ONT `).

-
c1 ( str | None , optional ) – Spliced capture file path for velocity workflows.

-
c2 ( str | None , optional ) – Intronic capture file path for velocity workflows.

-
nucleus ( bool , optional ) – Shortcut to switch workflow from `standard `to `nucleus `.

-
**kwargs – Extra kb flags forwarded verbatim.

Returns :

Metadata dictionary including workflow settings and discovered output files.

Return type :

dict [ str , str ]
