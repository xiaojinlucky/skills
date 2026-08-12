# Extract SecAct pattern-associated secreted proteins

- Package: scop
- Language: R
- Function: `RunSecActPatternGenes`
- Source: https://mengxu98.github.io/scop/reference/RunSecActPatternGenes.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunSecActPatternGenes.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run SecAct.signaling.pattern.gene on a SpaCET object after {[=RunSecActSignalingPattern]{RunSecActSignalingPattern()}}.

## Signature

```text
RunSecActPatternGenes(SpaCET_obj, n, verbose = TRUE)
```

## Parameters

- `SpaCET_obj`: A SpaCET object.
- `n`: Pattern index.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Extract SecAct pattern-associated secreted proteins

## Usage

```text
RunSecActPatternGenes(SpaCET_obj, n, verbose = TRUE)
```

## Description

Run SecAct.signaling.pattern.gene on a SpaCET object after {[=RunSecActSignalingPattern]{RunSecActSignalingPattern()}}.

## Value

A matrix of pattern-associated secreted proteins.
