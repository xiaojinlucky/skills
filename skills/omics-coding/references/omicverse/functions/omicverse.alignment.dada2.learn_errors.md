# omicverse.alignment.dada2.learn_errors #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.dada2.learn_errors`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.dada2.learn_errors.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Learn a DADA2 error model from one or several filtered FASTQs.

## Signature

```text
omicverse.alignment.dada2. learn_errors ( fastqs , nbases = 100000000 , random_state = 0 )
```

## Parameters

- `fastqs`: ( Union [ str , Sequence [ str ]] )
- `nbases`: ( int (default: 100000000 ))
- `random_state`: ( int (default: 0 ))

## Full Documentation

# omicverse.alignment.dada2.learn_errors #

omicverse.alignment.dada2. learn_errors ( fastqs , nbases = 100000000 , random_state = 0 ) [source] #

Learn a DADA2 error model from one or several filtered FASTQs.

Returns the `(nuc, nuc, qual) `error-rate tensor that `denoise() `consumes.

Parameters :

-
fastqs ( `Union `[ `str `, `Sequence `[ `str `]] )

-
nbases ( `int `(default: `100000000 `))

-
random_state ( `int `(default: `0 `))
