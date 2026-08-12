# NMF similarity heatmap

- Package: scop
- Language: R
- Function: `NMFHeatmap`
- Source: https://mengxu98.github.io/scop/reference/NMFHeatmap.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/NMFHeatmap.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

NMF similarity heatmap

## Signature

```text
NMFHeatmap( srt, plot_type = c("cells", "features"), reduction = "nmf", dims = NULL, cells = NULL, features = NULL, similarity_metric = "cosine", cell_annotation = NULL, feature_annotation = NULL, assay = NULL, border = TRUE, heatmap_border = NULL, cell_annotation_border = NULL, feature_annotation_border = NULL, heatmap_border_palcolor = "black", cell_annotation_border_palcolor = "black", feature_annotation_border_palcolor = "black", heatmap_border_size = 1, cell_annotation_border_size = 1, feature_annotation_border_size = 1, show_row_names = FALSE, row_names_wrap = NULL, show_column_names = FALSE, row_names_side = "left", column_names_side = "top", row_names_rot = 0, column_names_rot = 90, row_title = NULL, column_title = NULL, anno_terms = FALSE, anno_keys = FALSE, anno_features = FALSE, terms_width = grid::unit(4, "in"), terms_stat_width = grid::unit(1.35, "in"), terms_fontsize = 8, terms_stat = "none", terms_stat_digits = 2, terms_stat_label = "value", terms_stat_axis = FALSE, terms_stat_background_palcolor = NULL, terms_stat_border = NULL, terms_stat_border_palcolor = NULL, terms_stat_border_size = NULL, terms_stat_label_palcolor = NULL, terms_group_background = FALSE, terms_background_palcolor = "grey98", terms_background_alpha = 1, terms_border = TRUE, terms_border_palcolor = "black", terms_border_size = 0.8, terms_text_palcolor = NULL, terms_bar_palcolor = NULL, keys_width = grid::unit(2, "in"), keys_fontsize = c(6, 10), features_width = grid::unit(2, "in"), features_fontsize = c(6, 10), IDtype = "symbol", species = "Homo_sapiens", db_update = FALSE, db_version = "latest", db_combine = FALSE, convert_species = FALSE, Ensembl_version = NULL, mirror = NULL, db = "GO_BP", TERM2GENE = NULL, TERM2NAME = NULL, minGSSize = 10, maxGSSize = 500, GO_simplify = FALSE, GO_simplify_cutoff = "p.adjust < 0.05", simplify_method = "Wang", simplify_similarityCutoff = 0.7, pvalueCutoff = NULL, padjustCutoff = 0.05, topTerm = 5, show_termid = FALSE, topWord = 20, words_excluded = NULL, heatmap_palette = "simspec", heatmap_palcolor = c("#ffffe5", "#d9f0d3", "#74add1", "#2166ac"), heatmap_limits = NULL, cluster_palette = "simspec", cluster_palcolor = NULL, cell_annotation_palette = "Chinese", cell_annotation_palcolor = NULL, feature_annotation_palette = "Dark2", feature_annotation_palcolor = NULL, use_raster = NULL, raster_device = "png", raster_by_magick = FALSE, height = NULL, width = NULL, units = "inch", cores = 1, seed = 11, legend.position = "right", ht_params = list(), verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object containing an NMF dimensional reduction.
- `plot_type`: Plot type. "cells" plots cell/spot similarity from NMF embeddings. "features" plots feature similarity from NMF loadings.
- `reduction`: Name of the NMF reduction. Default is "nmf".
- `dims`: Dimensions/components from the NMF reduction to use. If NULL, all available dimensions are used.
- `cells`: Cells/spots to include when plot_type = "cells".
- `features`: Features to include when plot_type = "features". If NULL, variable features shared with the loading matrix are used; if none are found, all features in the loading matrix are used.
- `similarity_metric`: Similarity metric.
- `cell_annotation`: Metadata columns to show as column annotations in cell mode.
- `feature_annotation`: Feature metadata columns to show as column annotations in feature mode.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `border`: Whether to add borders to the heatmap body and annotations. Kept for backward compatibility. The more specific heatmap_border, cell_annotation_border, and feature_annotation_border arguments inherit from this value when left as NULL.
- `heatmap_border, cell_annotation_border, feature_annotation_border`: Whether to draw borders for the heatmap body, cell annotations, and feature annotations, respectively. Defaults inherit from border.
- `heatmap_border_palcolor, cell_annotation_border_palcolor, feature_annotation_border_palcolor`: Border colors for the heatmap body, cell annotations, and feature annotations when their matching border argument is TRUE. Default is "black".
- `heatmap_border_size, cell_annotation_border_size, feature_annotation_border_size`: Border line widths for the heatmap body, cell annotations, and feature annotations when their matching border argument is TRUE. Default is 1.
- `show_row_names`: Whether to show row names in the heatmap. Default is FALSE.
- `row_names_wrap`: Maximum number of characters per displayed row-name line. When set to a positive number, underscores are displayed as spaces and labels are wrapped without changing the underlying item identifiers. NULL disables wrapping.
- `show_column_names`: Whether to show column names in the heatmap. Default is FALSE.
- `row_names_side`: A character vector specifying the side to place row names.
- `column_names_side`: A character vector specifying the side to place column names.
- `row_names_rot`: The rotation angle for row names. Default is 0.
- `column_names_rot`: The rotation angle for column names. Default is 90.
- `row_title`: A character vector specifying the title for rows. Default is NULL.
- `column_title`: A character vector specifying the title for columns. Default is NULL.
- `anno_terms`: Whether to include term annotations. Default is FALSE.
- `anno_keys`: Whether to include key annotations. Default is FALSE.
- `anno_features`: Whether to include feature annotations. Default is FALSE.
- `terms_width`: A unit specifying the width of term annotations. Default is unit(4, "in").
- `terms_stat_width`: A unit specifying the width of the independent term-statistic bar-chart annotation.
- `terms_fontsize`: A numeric vector specifying the font size(s) for term annotations. Default is 8.
- `terms_stat`: Which enrichment statistic controls the term bars. Use "none" to hide the bar background, "score" for -log10 of the active p-value metric, or any column from the enrichment result such as "p.adjust", "pvalue", "qvalue", "GeneRatio", "RichFactor", "FoldEnrichment", "zScore", or "Count".
- `terms_stat_digits`: Number of significant digits for statistic labels and axis tick labels.
- `terms_stat_label`: Label placed on or beside each statistic bar: "none", "value", "significance", or "both".
- `terms_stat_axis`: Logical. Whether to draw a shared statistic axis outside and below the final enrichment block.
- `terms_stat_background_palcolor`: Background color of the independent statistic panels. NULL inherits the corresponding term-panel background.
- `terms_stat_border`: Logical. Whether to draw borders around statistic panels. NULL inherits terms_border.
- `terms_stat_border_palcolor`: Border color of statistic panels. NULL inherits terms_border_palcolor.
- `terms_stat_border_size`: Border line width of statistic panels. NULL inherits terms_border_size.
- `terms_stat_label_palcolor`: Color of labels drawn on statistic bars. NULL automatically uses black or white according to bar luminance.
- `terms_group_background`: Logical. Whether term blocks use translucent feature_split colors as their backgrounds.
- `terms_background_palcolor`: Background color used when terms_group_background = FALSE.
- `terms_background_alpha`: Alpha transparency of term-block backgrounds.
- `terms_border`: Logical. Whether to draw borders around term blocks.
- `terms_border_palcolor`: Border color of term blocks.
- `terms_border_size`: Border line width of term blocks.
- `terms_text_palcolor`: Fixed term text color. NULL retains colors mapped from enrichment significance.
- `terms_bar_palcolor`: Fixed statistic-bar color. NULL makes each bar use the same color as its corresponding term text.
- `keys_width`: A unit specifying the width of key annotations. Default is unit(2, "in").
- `keys_fontsize`: A two-length numeric vector specifying the minimum and maximum font size(s) for key annotations. Default is c(6, 10).
- `features_width`: A unit specifying the width of feature annotations. Default is unit(2, "in").
- `features_fontsize`: A two-length numeric vector specifying the minimum and maximum font size(s) for feature annotations. Default is c(6, 10).
- `IDtype`: A character vector specifying the type of IDs for features. Default is "symbol".
- `species`: A character vector specifying the species for features. Default is "Homo_sapiens".
- `db_update`: Whether the gene annotation databases should be forcefully updated. If set to FALSE, the function will attempt to load the cached databases instead. Default is FALSE.
- `db_version`: A character vector specifying the version of the gene annotation databases to be retrieved. Default is "latest".
- `db_combine`: Whether to use a combined database. Default is FALSE.
- `convert_species`: Whether to use a species-converted database when the annotation is missing for the specified species. Default is TRUE.
- `Ensembl_version`: An integer specifying the Ensembl version. Default is NULL. If NULL, the latest version will be used.
- `mirror`: A character vector specifying the mirror for the Ensembl database. Default is NULL.
- `db`: A character vector specifying the database to use. Default is "GO_BP".
- `TERM2GENE`: A data.frame specifying the TERM2GENE mapping for the database. Default is NULL.
- `TERM2NAME`: A data.frame specifying the TERM2NAME mapping for the database. Default is NULL.
- `minGSSize`: An integer specifying the minimum gene set size for the database. Default is 10.
- `maxGSSize`: An integer specifying the maximum gene set size for the database. Default is 500.
- `GO_simplify`: Whether to simplify gene ontology terms. Default is FALSE.
- `GO_simplify_cutoff`: A character vector specifying the cutoff for GO simplification. Default is "p.adjust < 0.05".
- `simplify_method`: A character vector specifying the method for GO simplification. Default is "Wang".
- `simplify_similarityCutoff`: The similarity cutoff for GO simplification. Default is 0.7.
- `pvalueCutoff`: A numeric vector specifying the p-value cutoff(s) for significance. Default is NULL.
- `padjustCutoff`: The adjusted p-value cutoff for significance. Default is 0.05.
- `topTerm`: A number of top terms to include. Default is 5.
- `show_termid`: Whether to show term IDs. Default is FALSE.
- `topWord`: A number of top words to include. Default is 20.
- `words_excluded`: A character vector specifying the words to exclude. Default is NULL.
- `heatmap_palette`: A character vector specifying the palette to use for the heatmap. Default is "RdBu".
- `heatmap_palcolor`: A character vector specifying the heatmap color to use. Default is NULL.
- `heatmap_limits`: Numeric breaks for the heatmap color scale. If NULL, defaults to c(0, 0.35, 0.75, 1).
- `cluster_palette`: Palette used for NMF cluster/program annotations.
- `cluster_palcolor`: Optional custom colors for NMF cluster/program annotations.
- `cell_annotation_palette`: A character vector specifying the palette to use for cell annotations. The length of the vector should match the number of cell_annotation. Default is "Chinese".
- `cell_annotation_palcolor`: A list of character vector specifying the cell annotation color(s) to use. The length of the list should match the number of cell_annotation. Default is NULL.
- `feature_annotation_palette`: A character vector specifying the palette to use for feature annotations. The length of the vector should match the number of feature_annotation. Default is "Dark2".
- `feature_annotation_palcolor`: A list of character vector specifying the feature annotation color to use. The length of the list should match the number of feature_annotation. Default is NULL.
- `use_raster`: Whether to use a raster device for plotting. Default is NULL.
- `raster_device`: A character vector specifying the raster device to use. Default is "png".
- `raster_by_magick`: Whether to use the 'magick' package for raster. Default is FALSE.
- `height`: The height of the heatmap in the specified units. If not provided, the height will be automatically determined based on the number of rows in the heatmap and the default unit.
- `width`: The width of the heatmap in the specified units. If not provided, the width will be automatically determined based on the number of columns in the heatmap and the default unit.
- `units`: The units to use for the width and height of the heatmap. Default is "inch", Options are "mm", "cm", or "inch".
- `cores`: The number of worker processes to use for parallelization. Default is 1.
- `seed`: Random seed for reproducibility. Default is 11.
- `legend.position`: A character vector specifying the side to place the legends. Options are "right", "left", "top", or "bottom". Default is "right". When row names are long and shown on the right side, the gap between the heatmap and the legend is automatically increased to avoid overlap.
- `ht_params`: Additional parameters to customize the appearance of the heatmap. This should be a list with named elements, where the names correspond to parameter names in the [ComplexHeatmap:Heatmap]{ComplexHeatmap::Heatmap} function. Any conflicting parameters will override the defaults set by this function. Default is list().
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# NMF similarity heatmap

## Usage

```text
NMFHeatmap( srt, plot_type = c("cells", "features"), reduction = "nmf", dims = NULL, cells = NULL, features = NULL, similarity_metric = "cosine", cell_annotation = NULL, feature_annotation = NULL, assay = NULL, border = TRUE, heatmap_border = NULL, cell_annotation_border = NULL, feature_annotation_border = NULL, heatmap_border_palcolor = "black", cell_annotation_border_palcolor = "black", feature_annotation_border_palcolor = "black", heatmap_border_size = 1, cell_annotation_border_size = 1, feature_annotation_border_size = 1, show_row_names = FALSE, row_names_wrap = NULL, show_column_names = FALSE, row_names_side = "left", column_names_side = "top", row_names_rot = 0, column_names_rot = 90, row_title = NULL, column_title = NULL, anno_terms = FALSE, anno_keys = FALSE, anno_features = FALSE, terms_width = grid::unit(4, "in"), terms_stat_width = grid::unit(1.35, "in"), terms_fontsize = 8, terms_stat = "none", terms_stat_digits = 2, terms_stat_label = "value", terms_stat_axis = FALSE, terms_stat_background_palcolor = NULL, terms_stat_border = NULL, terms_stat_border_palcolor = NULL, terms_stat_border_size = NULL, terms_stat_label_palcolor = NULL, terms_group_background = FALSE, terms_background_palcolor = "grey98", terms_background_alpha = 1, terms_border = TRUE, terms_border_palcolor = "black", terms_border_size = 0.8, terms_text_palcolor = NULL, terms_bar_palcolor = NULL, keys_width = grid::unit(2, "in"), keys_fontsize = c(6, 10), features_width = grid::unit(2, "in"), features_fontsize = c(6, 10), IDtype = "symbol", species = "Homo_sapiens", db_update = FALSE, db_version = "latest", db_combine = FALSE, convert_species = FALSE, Ensembl_version = NULL, mirror = NULL, db = "GO_BP", TERM2GENE = NULL, TERM2NAME = NULL, minGSSize = 10, maxGSSize = 500, GO_simplify = FALSE, GO_simplify_cutoff = "p.adjust < 0.05", simplify_method = "Wang", simplify_similarityCutoff = 0.7, pvalueCutoff = NULL, padjustCutoff = 0.05, topTerm = 5, show_termid = FALSE, topWord = 20, words_excluded = NULL, heatmap_palette = "simspec", heatmap_palcolor = c("#ffffe5", "#d9f0d3", "#74add1", "#2166ac"), heatmap_limits = NULL, cluster_palette = "simspec", cluster_palcolor = NULL, cell_annotation_palette = "Chinese", cell_annotation_palcolor = NULL, feature_annotation_palette = "Dark2", feature_annotation_palcolor = NULL, use_raster = NULL, raster_device = "png", raster_by_magick = FALSE, height = NULL, width = NULL, units = "inch", cores = 1, seed = 11, legend.position = "right", ht_params = list(), verbose = TRUE )
```

## Description

NMF similarity heatmap

## Value

A list with the following elements: plot: The heatmap plot as a patchwork/ggplot object. similarity_matrix: The ordered similarity matrix used for plotting. nmf_cluster: The ordered NMF cluster/program assignment. order: The ordered row/column names. metadata: Ordered cell or feature metadata used for annotations. enrichment: Enrichment results for feature mode when requested, otherwise NULL.

## Examples

```r
library(Matrix)
data(pancreas_sub)
pancreas_sub <- NormalizeData(pancreas_sub)
pancreas_sub <- FindVariableFeatures(
  pancreas_sub,
  nfeatures = 1000
)
pancreas_sub <- RunNMF(
  pancreas_sub,
  features = SeuratObject::VariableFeatures(pancreas_sub),
  nbes = 5,
  maxit = 50
)
ht_cells <- NMFHeatmap(
  pancreas_sub,
  plot_type = "cells",
  cell_annotation = "CellType"
)
ht_cells$plot

ht_features <- NMFHeatmap(
  pancreas_sub,
  plot_type = "features"
)
ht_features$plot
```
