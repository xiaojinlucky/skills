# omicverse.pp.binary_search #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.binary_search`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.binary_search.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Infer a size factor from one normalized expression vector.

## Signature

```text
omicverse.pp. binary_search ( vec , min_r = 0 , max_r = 100000 )
```

## Parameters

- `vec`: ( array-like ) – Normalized expression vector for one cell (or one profile), where the minimum non-zero value is assumed to correspond to one raw count after multiplying by the unknown size factor.
- `min_r`: ( int , default=0 ) – Lower bound of the integer search interval.
- `max_r`: ( int , default=100000 ) – Upper bound of the integer search interval.

## Full Documentation

# omicverse.pp.binary_search #

omicverse.pp. binary_search ( vec , min_r = 0 , max_r = 100000 ) [source] #

Infer a size factor from one normalized expression vector.

Parameters :

-
vec ( array-like ) – Normalized expression vector for one cell (or one profile), where the minimum non-zero value is assumed to correspond to one raw count after multiplying by the unknown size factor.

-
min_r ( int , default=0 ) – Lower bound of the integer search interval.

-
max_r ( int , default=100000 ) – Upper bound of the integer search interval.

Returns :

Estimated integer size factor that best maps the minimum non-zero value back to one count.

Return type :

int
