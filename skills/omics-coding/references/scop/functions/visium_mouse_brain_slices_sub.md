# A mouse brain Visium two-slice spatial example dataset

- Package: scop
- Language: R
- Function: `visium_mouse_brain_slices_sub`
- Source: https://mengxu98.github.io/scop/reference/visium_mouse_brain_slices_sub.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/visium_mouse_brain_slices_sub.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

A compact two-slice subset of the 10x Genomics mouse brain serial sagittal Visium dataset distributed as stxBrain.SeuratData. The object contains 1000 tissue spots from each of the anterior serial sections anterior1 and anterior2, with a Spatial assay, two Visium images, and tissue coordinates in metadata columns x and y. Metadata column sample stores the original slice label and is intended for multi-slice spatial integration examples that require a real sample.by column. To keep the package data small, the object retains the top 4000 genes ranked by total counts across the two selected slices.

## Signature

```text
visium_mouse_brain_slices_sub
```

## Parameters

No parameters detected.

## Full Documentation

# A mouse brain Visium two-slice spatial example dataset

## Usage

```text
visium_mouse_brain_slices_sub
```

## Description

A compact two-slice subset of the 10x Genomics mouse brain serial sagittal Visium dataset distributed as stxBrain.SeuratData. The object contains 1000 tissue spots from each of the anterior serial sections anterior1 and anterior2, with a Spatial assay, two Visium images, and tissue coordinates in metadata columns x and y. Metadata column sample stores the original slice label and is intended for multi-slice spatial integration examples that require a real sample.by column. To keep the package data small, the object retains the top 4000 genes ranked by total counts across the two selected slices.

## Examples

```r
data(visium_mouse_brain_slices_sub)
table(visium_mouse_brain_slices_sub$sample)
SeuratObject::Images(visium_mouse_brain_slices_sub)
head(visium_mouse_brain_slices_sub@meta.data[, c("sample", "x", "y")])
SpatialSpotPlot(
  visium_mouse_brain_slices_sub,
  group.by = "sample",
  split.by = "sample",
  image = "anterior1",
  overlay_image = FALSE
)
```
