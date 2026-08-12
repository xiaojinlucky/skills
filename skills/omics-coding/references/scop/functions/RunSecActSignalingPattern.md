# Run SecAct spatial signaling pattern analysis

- Package: scop
- Language: R
- Function: `RunSecActSignalingPattern`
- Source: https://mengxu98.github.io/scop/reference/RunSecActSignalingPattern.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunSecActSignalingPattern.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run SecAct.signaling.pattern on a SpaCET object with existing SecAct activity results.

## Signature

```text
RunSecActSignalingPattern( SpaCET_obj, scale.factor = 1e+05, radius = 200, k, verbose = TRUE )
```

## Parameters

- `SpaCET_obj`: A SpaCET object.
- `scale.factor`: Spot-level scale factor passed to SecAct.activity.inference.ST.
- `radius`: Radius cutoff.
- `k`: Number of NMF patterns, or candidate pattern numbers.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Run SecAct spatial signaling pattern analysis

## Usage

```text
RunSecActSignalingPattern( SpaCET_obj, scale.factor = 1e+05, radius = 200, k, verbose = TRUE )
```

## Description

Run SecAct.signaling.pattern on a SpaCET object with existing SecAct activity results.

## Value

A SpaCET object with SecAct signaling pattern results.
