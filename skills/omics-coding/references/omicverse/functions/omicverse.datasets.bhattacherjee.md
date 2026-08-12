# omicverse.datasets.bhattacherjee #

- Package: omicverse
- Language: Python
- Function: `omicverse.datasets.bhattacherjee`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.datasets.bhattacherjee.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Processed single-cell data PFC adult mice under cocaine self-administration.

## Signature

```text
omicverse.datasets. bhattacherjee ( processed = True )
```

## Parameters

- `processed`: ( bool ) – Whether to return processed-style fallback mock data on failure.
- `References`: – Bhattacherjee A, Djekidel MN, Chen R, Chen W, Tuesta LM, Zhang Y. Cell type-specific transcriptional programs in mouse prefrontal cortex during adolescence and addiction. Nat Commun. 2019 Sep 13;10(1):4169. doi: 10.1038/s41467-019-12054-3. PMID: 31519873; PMCID: PMC6744514.

## Full Documentation

# omicverse.datasets.bhattacherjee #

omicverse.datasets. bhattacherjee ( processed = True ) [source] #

Processed single-cell data PFC adult mice under cocaine self-administration.

Adult mice were subject to cocaine self-administration, samples were collected at three time points: Maintenance, 48h after cocaine withdrawal and 15 days after cocaine withdrawal.

Parameters :

-
processed ( bool ) – Whether to return processed-style fallback mock data on failure.

-
References – Bhattacherjee A, Djekidel MN, Chen R, Chen W, Tuesta LM, Zhang Y. Cell type-specific transcriptional programs in mouse prefrontal cortex during adolescence and addiction. Nat Commun. 2019 Sep 13;10(1):4169. doi: 10.1038/s41467-019-12054-3. PMID: 31519873; PMCID: PMC6744514.

Returns :

-
AnnData – Single-cell RNA-seq dataset from Bhattacherjee et al. or mock fallback.

-
Examples – >>> import omicverse as ov >>> adata = ov.datasets.bhattacherjee() >>> print(adata)
