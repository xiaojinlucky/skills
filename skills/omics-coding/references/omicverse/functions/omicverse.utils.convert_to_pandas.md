# omicverse.utils.convert_to_pandas #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.convert_to_pandas`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.convert_to_pandas.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Convert Rust-backed dataframe-like objects to pandas.DataFrame .

## Signature

```text
omicverse.utils. convert_to_pandas ( df_obj )
```

## Parameters

- `df_obj`: ( Any ) – Input dataframe-like object. Supported objects include wrappers that expose to_pandas() , slicing-based dataframe access, or column-based retrieval.

## Full Documentation

# omicverse.utils.convert_to_pandas #

omicverse.utils. convert_to_pandas ( df_obj ) [source] #

Convert Rust-backed dataframe-like objects to `pandas.DataFrame `.

Parameters :

df_obj ( Any ) – Input dataframe-like object. Supported objects include wrappers that expose `to_pandas() `, slicing-based dataframe access, or column-based retrieval.

Returns :

Converted pandas DataFrame. Returns an empty DataFrame when conversion fails.

Return type :

pandas.DataFrame
