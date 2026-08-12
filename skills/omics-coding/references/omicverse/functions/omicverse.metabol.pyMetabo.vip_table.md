# omicverse.metabol.pyMetabo.vip_table #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.pyMetabo.vip_table`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.pyMetabo.vip_table.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Return VIP scores per metabolite — requires a prior PLS-DA / OPLS-DA fit.

## Signature

```text
pyMetabo. vip_table ( )
```

## Parameters

No parameters detected.

## Full Documentation

# omicverse.metabol.pyMetabo.vip_table #

pyMetabo. vip_table ( ) [source] #

Return VIP scores per metabolite — requires a prior PLS-DA / OPLS-DA fit.

VIP > 1 is the canonical importance threshold; metabolites are sorted descending. Raises `RuntimeError `if `plsda() `or `opls_da() `hasn’t been called yet.
