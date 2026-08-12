# omicverse.datasets.download_data #

- Package: omicverse
- Language: Python
- Function: `omicverse.datasets.download_data`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.datasets.download_data.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Download a dataset file to local storage.

## Signature

```text
omicverse.datasets. download_data ( url , file_path = None , dir = './data' )
```

## Parameters

- `url`: ( str ) – Source URL of the dataset file.
- `file_path`: ( Optional [ str ] ) – Target filename. If None , the basename of url is used.
- `dir`: ( str ) – Output directory where file is stored.

## Full Documentation

# omicverse.datasets.download_data #

omicverse.datasets. download_data ( url , file_path = None , dir = './data' ) [source] #

Download a dataset file to local storage.

Parameters :

-
url ( str ) – Source URL of the dataset file.

-
file_path ( Optional [ str ] ) – Target filename. If `None `, the basename of `url `is used.

-
dir ( str ) – Output directory where file is stored.

Returns :

Absolute/relative local path of downloaded file.

Return type :

str
