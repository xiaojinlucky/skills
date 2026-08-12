# omicverse.alignment.vsearch.usearch_global #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.vsearch.usearch_global`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.vsearch.usearch_global.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Build the ASV count matrix.

## Signature

```text
omicverse.alignment.vsearch. usearch_global ( reads_fasta , asvs_fasta , output_dir , identity = 0.97 , threads = 4 , strand = 'plus' , extra_args = None , vsearch_path = None , auto_install = True , overwrite = False )
```

## Parameters

- `reads_fasta`: Detected from function signature; no parameter description detected.
- `asvs_fasta`: Detected from function signature; no parameter description detected.
- `output_dir`: Detected from function signature; no parameter description detected.
- `identity`: Detected from function signature; no parameter description detected.
- `threads`: Detected from function signature; no parameter description detected.
- `strand`: Detected from function signature; no parameter description detected.
- `extra_args`: Detected from function signature; no parameter description detected.
- `vsearch_path`: Detected from function signature; no parameter description detected.
- `auto_install`: Detected from function signature; no parameter description detected.
- `overwrite`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.alignment.vsearch.usearch_global #

omicverse.alignment.vsearch. usearch_global ( reads_fasta , asvs_fasta , output_dir , identity = 0.97 , threads = 4 , strand = 'plus' , extra_args = None , vsearch_path = None , auto_install = True , overwrite = False ) [source] #

Build the ASV count matrix.

`reads_fasta `is typically the concatenated filtered FASTA (with `<sample>.<n> `headers) from `dereplicate() `(output `combined `). Each read is mapped to the closest ASV at `identity `(default 0.97) and tallied per sample.

## Output #

`otutab.tsv `— tab-delimited; first column `#OTU ID `, subsequent columns one per sample, rows = ASVs.

param reads_fasta :

type reads_fasta :

`str `

param asvs_fasta :

type asvs_fasta :

`str `

param output_dir :

type output_dir :

`str `

param identity :

type identity :

`float `(default: `0.97 `)

param threads :

type threads :

`int `(default: `4 `)

param strand :

type strand :

`str `(default: `'plus' `)

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
