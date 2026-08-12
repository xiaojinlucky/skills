# omicverse.datasets.download_data_requests #

- Package: omicverse
- Language: Python
- Function: `omicverse.datasets.download_data_requests`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.datasets.download_data_requests.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Download data with custom headers to reduce HTTP 403 failures.

## Signature

```text
omicverse.datasets. download_data_requests ( url , file_path = None , dir = './data' )
```

## Parameters

- `url`: ( str ) – Source URL of the dataset file.
- `file_path`: ( Optional [ str ] ) – Target filename. If None , the basename of url is used.
- `dir`: ( str ) – Output directory where file is stored.

## Full Documentation

# omicverse.datasets.download_data_requests #

omicverse.datasets. download_data_requests ( url , file_path = None , dir = './data' ) [source] #

Download data with custom headers to reduce HTTP 403 failures.

Parameters :

-
url ( str ) – Source URL of the dataset file.

-
file_path ( Optional [ str ] ) – Target filename. If `None `, the basename of `url `is used.

-
dir ( str ) – Output directory where file is stored.

Returns :

Local path to downloaded (or cached) file.

Return type :

str
