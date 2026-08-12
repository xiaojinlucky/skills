# omicverse.alignment.mafft #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.mafft`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.mafft.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run MAFFT multiple sequence alignment.

## Signature

```text
omicverse.alignment. mafft ( input_fasta , output_dir , output_name = 'aligned.fasta' , mode = 'auto' , threads = 4 , extra_args = None , mafft_path = None , auto_install = True , overwrite = False )
```

## Parameters

- `input_fasta`: ( str ) – Path to unaligned FASTA (ASV centroids, 16S sequences, …).
- `output_dir`: ( str ) – Directory for the aligned FASTA + log. Required (no $HOME ).
- `output_name`: ( str (default: 'aligned.fasta' )) – Filename for the aligned FASTA inside output_dir .
- `mode`: ( str (default: 'auto' )) – MAFFT strategy flag: 'auto' (default; --auto picks FFT-NS-1 / L-INS-i depending on size), 'fftns' , 'linsi' , 'einsi' , 'ginsi' , or 'retree1' (fastest).
- `threads`: ( int (default: 4 )) – Passed as --thread . MAFFT supports --thread -1 for auto-detect.
- `extra_args`: ( Optional [ Sequence [ str ]] (default: None )) – Appended verbatim to the mafft command line (coerced to str ).
- `mafft_path`: ( Optional [ str ] (default: None )) – Explicit path to the mafft binary.
- `auto_install`: ( bool (default: True )) – Try conda install -c bioconda mafft if absent.
- `overwrite`: ( bool (default: False )) – Re-run even if the aligned file already exists.

## Full Documentation

# omicverse.alignment.mafft #

omicverse.alignment. mafft ( input_fasta , output_dir , output_name = 'aligned.fasta' , mode = 'auto' , threads = 4 , extra_args = None , mafft_path = None , auto_install = True , overwrite = False ) [source] #

Run MAFFT multiple sequence alignment.

Parameters :

-
input_fasta ( `str `) – Path to unaligned FASTA (ASV centroids, 16S sequences, …).

-
output_dir ( `str `) – Directory for the aligned FASTA + log. Required (no `$HOME `).

-
output_name ( `str `(default: `'aligned.fasta' `)) – Filename for the aligned FASTA inside `output_dir `.

-
mode ( `str `(default: `'auto' `)) – MAFFT strategy flag: `'auto' `(default; `--auto `picks FFT-NS-1 / L-INS-i depending on size), `'fftns' `, `'linsi' `, `'einsi' `, `'ginsi' `, or `'retree1' `(fastest).

-
threads ( `int `(default: `4 `)) – Passed as `--thread `. MAFFT supports `--thread -1 `for auto-detect.

-
extra_args ( `Optional `[ `Sequence `[ `str `]] (default: `None `)) – Appended verbatim to the mafft command line (coerced to `str `).

-
mafft_path ( `Optional `[ `str `] (default: `None `)) – Explicit path to the `mafft `binary.

-
auto_install ( `bool `(default: `True `)) – Try `conda install -c bioconda mafft `if absent.

-
overwrite ( `bool `(default: `False `)) – Re-run even if the aligned file already exists.

Return type :

`{"input": …, "aligned": …, "log": …} `— absolute paths.
