# omicverse.io.load #

- Package: omicverse
- Language: Python
- Function: `omicverse.io.load`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.io.load.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Load serialized Python object from disk.

## Signature

```text
omicverse.io. load ( path , backend = None )
```

## Parameters

- `path`: ( str ) – Input file path.
- `backend`: ( {'pickle' , 'cloudpickle'} or None , default=None ) – Preferred deserializer backend ( 'pickle' or 'cloudpickle' ).

## Full Documentation

# omicverse.io.load #

omicverse.io. load ( path , backend = None ) [source] #

Load serialized Python object from disk.

Parameters :

-
path ( str ) – Input file path.

-
backend ( {'pickle' , 'cloudpickle'} or None , default=None ) – Preferred deserializer backend ( `'pickle' `or `'cloudpickle' `).

Returns :

Deserialized Python object.

Return type :

Any

Raises :

ValueError – If `backend `is not one of `None `, `'pickle' `, or `'cloudpickle' `.
