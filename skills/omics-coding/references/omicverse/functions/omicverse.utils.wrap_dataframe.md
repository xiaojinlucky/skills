# omicverse.utils.wrap_dataframe #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.wrap_dataframe`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.wrap_dataframe.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Wrap a Rust-backed dataframe-like object with a pandas-style interface.

## Signature

```text
omicverse.utils. wrap_dataframe ( df_obj )
```

## Parameters

- `df_obj`: ( Any ) – Input dataframe-like object (for example, Rust backend obs / var ).

## Full Documentation

# omicverse.utils.wrap_dataframe #

omicverse.utils. wrap_dataframe ( df_obj ) [source] #

Wrap a Rust-backed dataframe-like object with a pandas-style interface.

Parameters :

df_obj ( Any ) – Input dataframe-like object (for example, Rust backend `obs `/ `var `).

Returns :

Wrapper object that lazily converts content to pandas and exposes common DataFrame methods ( `head `, `tail `, `shape `, `columns `, etc.).

Return type :

PyDataFrameElemWrapper
