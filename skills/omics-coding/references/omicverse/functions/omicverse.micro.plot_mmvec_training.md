# omicverse.micro.plot_mmvec_training #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.plot_mmvec_training`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.plot_mmvec_training.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Training (and validation) loss curve for a fitted MMvec .

## Signature

```text
omicverse.micro. plot_mmvec_training ( mmvec , ax = None )
```

## Parameters

- `mmvec`: ( MMvec ) – Fitted model.
- `ax`: ( matplotlib axes , optional ) – Axes to draw on; created if not provided.

## Full Documentation

# omicverse.micro.plot_mmvec_training #

omicverse.micro. plot_mmvec_training ( mmvec , ax = None ) [source] #

Training (and validation) loss curve for a fitted `MMvec `.

Plots `mmvec.loss_history_ `(and `val_loss_history_ `if a validation split was kept) per epoch. Marks the best-validation epoch with a vertical line — that’s where the saved checkpoint came from. A monotonically falling validation loss is healthy; a rising val loss while train keeps falling is overfitting.

Parameters :

-
mmvec ( MMvec ) – Fitted model.

-
ax ( matplotlib axes , optional ) – Axes to draw on; created if not provided.

Return type :

matplotlib axes.
