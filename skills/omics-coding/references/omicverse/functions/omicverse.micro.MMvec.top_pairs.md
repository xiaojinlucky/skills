# omicverse.micro.MMvec.top_pairs #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.MMvec.top_pairs`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.MMvec.top_pairs.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Top- n (microbe, metabolite) pairs ranked by |log-odds| .

## Signature

```text
MMvec. top_pairs ( n = 20 )
```

## Parameters

- `n`: ( int (default: 20 ))

## Full Documentation

# omicverse.micro.MMvec.top_pairs #

MMvec. top_pairs ( n = 20 ) [source] #

Top- `n `(microbe, metabolite) pairs ranked by `|log-odds| `.

Stacks `cooccurrence() `into long format and sorts by the absolute score, so the top of the list mixes strong positive and strong negative pairs (read the `score `column to see the sign). Returns a DataFrame with columns `microbe `, `metabolite `, `score `.

Parameters :

n ( `int `(default: `20 `))
