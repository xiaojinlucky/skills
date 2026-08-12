# omicverse.alignment.ref #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.ref`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.ref.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Build kallisto index and transcript-to-gene mapping files via kb ref .

## Signature

```text
omicverse.alignment. ref ( index_path , t2g_path , fasta_paths = None , gtf_paths = None , cdna_path = None , workflow = 'standard' , d = None , k = None , threads = 8 , overwrite = False , temp_dir = 'tmp' , make_unique = False , include = None , exclude = None , dlist = None , dlist_overhang = 1 , aa = False , max_ec_size = None , nucleus = False , f2 = None , c1 = None , c2 = None , flank = None , feature = None , no_mismatches = False , distinguish = False , ** kwargs )
```

## Parameters

- `index_path`: ( str ) – Output path for generated kallisto index file.
- `t2g_path`: ( str ) – Output path for transcript-to-gene mapping table.
- `fasta_paths`: ( str | list [ str ] | None , optional ) – Input transcript/genome FASTA file(s) used to build the reference.
- `gtf_paths`: ( str | list [ str ] | None , optional ) – Input GTF annotation file(s) aligned with fasta_paths .
- `cdna_path`: ( str | None , optional ) – Optional cDNA FASTA output path required by some workflows.
- `workflow`: ( str , optional ) – kb workflow mode (for example standard , nucleus , lamanno , kite ).
- `d`: ( str | None , optional ) – Prebuilt reference bundle shortcut ( kb ref -d ).
- `k`: ( int | None , optional ) – K-mer length for kallisto index construction.
- `threads`: ( int , optional ) – Number of threads for kb execution.
- `overwrite`: ( bool , optional ) – Whether to overwrite existing output files.
- `temp_dir`: ( str , optional ) – Temporary directory root for kb intermediate files.
- `make_unique`: ( bool , optional ) – Make feature IDs unique when duplicate names are detected.
- `include`: ( list [ dict [ str , str ] ] | None , optional ) – Attribute filters to include specific transcript/gene records.
- `exclude`: ( list [ dict [ str , str ] ] | None , optional ) – Attribute filters to exclude records.
- `dlist`: ( str | None , optional ) – Decoy list file for selective-alignment workflows.
- `dlist_overhang`: ( int , optional ) – Overhang length used when generating decoy targets.
- `aa`: ( bool , optional ) – Enable amino-acid mode where supported by kb workflow.
- `max_ec_size`: ( int | None , optional ) – Maximum equivalence-class size for index generation.
- `nucleus`: ( bool , optional ) – Shortcut to switch from standard to nucleus workflow.
- `f2`: ( str | None , optional ) – Secondary FASTA output/input path for nucleus/velocity workflows.
- `c1`: ( str | None , optional ) – Spliced transcript capture output path for velocity workflows.
- `c2`: ( str | None , optional ) – Intronic transcript capture output path for velocity workflows.
- `flank`: ( int | None , optional ) – Flanking sequence length for selected workflows.
- `feature`: ( str | None , optional ) – Feature FASTA path used by kite workflow.
- `no_mismatches`: ( bool , optional ) – Disable mismatches for feature barcoding workflows.
- `distinguish`: ( bool , optional ) – Distinguish overlapping features when supported by kb.
- `**kwargs`: – Additional kb flags passed through (for example kallisto , bustools , opt_off ).

## Full Documentation

# omicverse.alignment.ref #

omicverse.alignment. ref ( index_path , t2g_path , fasta_paths = None , gtf_paths = None , cdna_path = None , workflow = 'standard' , d = None , k = None , threads = 8 , overwrite = False , temp_dir = 'tmp' , make_unique = False , include = None , exclude = None , dlist = None , dlist_overhang = 1 , aa = False , max_ec_size = None , nucleus = False , f2 = None , c1 = None , c2 = None , flank = None , feature = None , no_mismatches = False , distinguish = False , ** kwargs ) [source] #

Build kallisto index and transcript-to-gene mapping files via `kb ref `.

Parameters :

-
index_path ( str ) – Output path for generated kallisto index file.

-
t2g_path ( str ) – Output path for transcript-to-gene mapping table.

-
fasta_paths ( str | list [ str ] | None , optional ) – Input transcript/genome FASTA file(s) used to build the reference.

-
gtf_paths ( str | list [ str ] | None , optional ) – Input GTF annotation file(s) aligned with `fasta_paths `.

-
cdna_path ( str | None , optional ) – Optional cDNA FASTA output path required by some workflows.

-
workflow ( str , optional ) – kb workflow mode (for example `standard `, `nucleus `, `lamanno `, `kite `).

-
d ( str | None , optional ) – Prebuilt reference bundle shortcut ( `kb ref -d `).

-
k ( int | None , optional ) – K-mer length for kallisto index construction.

-
threads ( int , optional ) – Number of threads for `kb `execution.

-
overwrite ( bool , optional ) – Whether to overwrite existing output files.

-
temp_dir ( str , optional ) – Temporary directory root for kb intermediate files.

-
make_unique ( bool , optional ) – Make feature IDs unique when duplicate names are detected.

-
include ( list [ dict [ str , str ] ] | None , optional ) – Attribute filters to include specific transcript/gene records.

-
exclude ( list [ dict [ str , str ] ] | None , optional ) – Attribute filters to exclude records.

-
dlist ( str | None , optional ) – Decoy list file for selective-alignment workflows.

-
dlist_overhang ( int , optional ) – Overhang length used when generating decoy targets.

-
aa ( bool , optional ) – Enable amino-acid mode where supported by kb workflow.

-
max_ec_size ( int | None , optional ) – Maximum equivalence-class size for index generation.

-
nucleus ( bool , optional ) – Shortcut to switch from `standard `to `nucleus `workflow.

-
f2 ( str | None , optional ) – Secondary FASTA output/input path for nucleus/velocity workflows.

-
c1 ( str | None , optional ) – Spliced transcript capture output path for velocity workflows.

-
c2 ( str | None , optional ) – Intronic transcript capture output path for velocity workflows.

-
flank ( int | None , optional ) – Flanking sequence length for selected workflows.

-
feature ( str | None , optional ) – Feature FASTA path used by `kite `workflow.

-
no_mismatches ( bool , optional ) – Disable mismatches for feature barcoding workflows.

-
distinguish ( bool , optional ) – Distinguish overlapping features when supported by kb.

-
**kwargs – Additional kb flags passed through (for example `kallisto `, `bustools `, `opt_off `).

Returns :

Metadata dictionary with workflow info and generated output paths.

Return type :

dict [ str , str ]
