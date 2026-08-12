# omicverse.io.read_csv #

- Package: omicverse
- Language: Python
- Function: `omicverse.io.read_csv`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.io.read_csv.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read a CSV / TSV file via pandas.read_csv with a mandatory duplicate-column scan on the raw header.

## Signature

```text
omicverse.io. read_csv ( filepath_or_buffer = None , * , sep = None , on_duplicate = 'warn' , ** kwargs )
```

## Parameters

- `filepath_or_buffer`: (default: None ) – Same as pandas.read_csv . Accepts a path-like, a URL, or a file-like object. The duplicate scan only runs when the input is a real on-disk file path.
- `sep`: ( Optional [ str ] (default: None )) – Delimiter. Inferred from extension when None ( .csv → , , .tsv / .txt / .tab → \t ).
- `on_duplicate`: ( str (default: 'warn' )) – Action when duplicate column labels are found in the raw header. One of: "warn" (default) — print a remediation-pointing message to stdout and continue with pandas’s auto-rename.
- `**kwargs`: – Any other keyword argument accepted by pandas.read_csv (for example index_col , dtype , usecols , comment ).

## Full Documentation

# omicverse.io.read_csv #

omicverse.io. read_csv ( filepath_or_buffer = None , * , sep = None , on_duplicate = 'warn' , ** kwargs ) [source] #

Read a CSV / TSV file via `pandas.read_csv `with a mandatory duplicate-column scan on the raw header.

Parameters :

-
filepath_or_buffer (default: `None `) – Same as `pandas.read_csv `. Accepts a path-like, a URL, or a file-like object. The duplicate scan only runs when the input is a real on-disk file path.

-
sep ( `Optional `[ `str `] (default: `None `)) – Delimiter. Inferred from extension when `None `( `.csv `→ `, `, `.tsv `/ `.txt `/ `.tab `→ `\t `).

-
on_duplicate ( `str `(default: `'warn' `)) –
Action when duplicate column labels are found in the raw header. One of:

-
`"warn" ` (default) — print a remediation-pointing message to stdout and continue with pandas’s auto-rename.

-
`"raise" `— raise `ValueError `with the same message.

-
`"ignore" `— silent passthrough; identical to `pandas.read_csv `.

-
**kwargs – Any other keyword argument accepted by `pandas.read_csv `(for example `index_col `, `dtype `, `usecols `, `comment `).

Return type :

pandas.DataFrame
