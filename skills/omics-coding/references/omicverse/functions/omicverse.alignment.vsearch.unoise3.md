# omicverse.alignment.vsearch.unoise3 #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.vsearch.unoise3`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.vsearch.unoise3.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run UNOISE3 denoising to build ASVs (amplicon sequence variants).

## Signature

```text
omicverse.alignment.vsearch. unoise3 ( uniques_fasta , output_dir , alpha = 2.0 , minsize = 2 , threads = 4 , extra_args = None , vsearch_path = None , auto_install = True , overwrite = False )
```

## Parameters

- `uniques_fasta`: Detected from function signature; no parameter description detected.
- `output_dir`: Detected from function signature; no parameter description detected.
- `alpha`: Detected from function signature; no parameter description detected.
- `minsize`: Detected from function signature; no parameter description detected.
- `threads`: Detected from function signature; no parameter description detected.
- `extra_args`: Detected from function signature; no parameter description detected.
- `vsearch_path`: Detected from function signature; no parameter description detected.
- `auto_install`: Detected from function signature; no parameter description detected.
- `overwrite`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.alignment.vsearch.unoise3 #

omicverse.alignment.vsearch. unoise3 ( uniques_fasta , output_dir , alpha = 2.0 , minsize = 2 , threads = 4 , extra_args = None , vsearch_path = None , auto_install = True , overwrite = False ) [source] #

Run UNOISE3 denoising to build ASVs (amplicon sequence variants).

Equivalent biological resolution to DADA2 ASVs per multiple benchmarks (Vestergaard 2024 ISME Comms); uses VSEARCH’s C implementation of the UNOISE3 algorithm ( `--cluster_unoise `).

## Output #

`asvs_pre.fasta `— raw ASV centroids (pre-chimera removal).

param uniques_fasta :

type uniques_fasta :

`str `

param output_dir :

type output_dir :

`str `

param alpha :

type alpha :

`float `(default: `2.0 `)

param minsize :

type minsize :

`int `(default: `2 `)

param threads :

type threads :

`int `(default: `4 `)

param extra_args :

type extra_args :

`Optional `[ `Sequence `[ `str `]] (default: `None `)

param vsearch_path :

type vsearch_path :

`Optional `[ `str `] (default: `None `)

param auto_install :

type auto_install :

`bool `(default: `True `)

param overwrite :

type overwrite :

`bool `(default: `False `)
