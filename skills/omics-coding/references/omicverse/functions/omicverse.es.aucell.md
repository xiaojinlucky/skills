# omicverse.es.aucell

- Package: omicverse
- Version: 2.2.4
- Language: Python
- Source: local://omicverse/2.2.4/runtime-signature
- Verified at: 2026-07-22

## Summary

Score one or more named gene signatures by AUCell and save the resulting score matrix in `adata.obsm["score_aucell"]`.

## Verified signature

```text
ov.es.aucell(data, signatures=None, tmin=5, raw=False, empty=True, bsize=250000, verbose=False, engine="auto", n_up=None)
```

## Parameters used in formal workflows

- `data`: AnnData object.
- `signatures`: named dictionary mapping each signature to its gene vector.
- `tmin`: minimum number of present genes required for a signature score.
- `raw`: use `adata.raw` instead of the active matrix when `TRUE`.
- `engine`: set `"cpu"` for a reproducible CPU route; `"auto"` may choose a different available backend.
- `n_up`: optional cap on the top ranked genes used by the score.

## Runtime note

Use this interface for multiple signatures. It supersedes the legacy single-gene-set wrapper `ov.single.geneset_aucell()` in OmicVerse 2.2.4.
