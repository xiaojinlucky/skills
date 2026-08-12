# omicverse.pl.ccc_heatmap #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.ccc_heatmap`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.ccc_heatmap.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot communication matrices as heatmaps, dot plots, or bubble maps.

## Signature

```text
omicverse.pl. ccc_heatmap ( adata , * , plot_type = 'heatmap' , comparison_adata = None , display_by = 'aggregation' , sender_use = None , receiver_use = None , signaling = None , interaction_use = None , pair_lr_use = None , sample_key = 'sample' , ncols = None , nrows = None , result_uns_key = 'liana_res' , score_key = 'specificity_rank' , pvalue_key = 'specificity_rank' , inverse_score = True , inverse_pvalue = False , classification = None , classification_reference = 'cellchat' , classification_fallback = 'family' , pvalue_threshold = 0.05 , pattern = 'all' , color_by = 'score' , value = 'sum' , top_n = 20 , top_n_pairs = None , top_anno = 'bar' , bottom_anno = 'cell' , left_anno = 'bar' , right_anno = 'cell' , bar_value = 'sum' , facet_by = None , pathway_method = 'mean' , min_lr_pairs = 1 , min_expression = 0.1 , group_pathways = True , transpose = False , add_violin = False , remove_isolate = False , min_interaction_threshold = 0.0 , cluster_rows = False , cluster_columns = False , show_row_names = False , show_col_names = False , add_text = None , border = False , cmap = 'Reds' , figsize = None , title = None , verbose = True , show = False , save = False )
```

## Parameters

- `adata`: ( anndata.AnnData ) – Communication AnnData produced by the OmicVerse CCC workflow, or a regular AnnData containing a LIANA result table in adata.uns[result_uns_key] . LIANA inputs are adapted internally to the communication format expected by ccc_* .
- `plot_type`: ( str , default="heatmap" ) – Matrix view to render. 'dot' is the primary LIANA-style source / target interaction dotplot. 'source_target_dot' is kept only as a backward-compatible alias of the same layout. Other supported values include aggregated heatmaps, focused heatmaps, bubble summaries, pathway-level bubble plots, source-target tile/sample views, signaling role maps, and differential heatmaps.
- `comparison_adata`: ( anndata.AnnData or None , default=None ) – Second communication AnnData used when plotting condition-to-condition differential heatmaps.
- `display_by`: ( {"aggregation" , "interaction"} , default="aggregation" ) – Whether to summarize the matrix at the signaling/pathway level or at the interaction level.
- `sender_use`: ( str , sequence of str , or None , default=None ) – Optional sender cell types retained in sender-aware heatmap views.
- `receiver_use`: ( str , sequence of str , or None , default=None ) – Optional receiver cell types retained in receiver-aware heatmap views.
- `signaling`: ( str , sequence of str , or None , default=None ) – Signaling pathway name or names to visualize.
- `interaction_use`: ( str , sequence of str , or None , default=None ) – Interaction names used to restrict interaction-level dot or bubble plots.
- `pair_lr_use`: ( str , sequence of str , or None , default=None ) – Ligand-receptor pair identifiers used by pair-resolved bubble views.
- `sample_key`: ( str , default="sample" ) – Observation/sample column used by plot_type='sample_dot' after LIANA results are converted to communication AnnData. If this column is not present but LIANA conversion stored a detected sample/context key in adata.uns['liana_sample_key'] , that key is used automatically.
- `ncols`: ( int or None , default=None ) – Number of source facets per row/column for LIANA-style dot layouts. These parameters are used by plot_type='dot' (and the backward-compatible alias 'source_target_dot' ) to avoid a single excessively wide row when many source panels are shown.
- `nrows`: ( int or None , default=None ) – Number of source facets per row/column for LIANA-style dot layouts. These parameters are used by plot_type='dot' (and the backward-compatible alias 'source_target_dot' ) to avoid a single excessively wide row when many source panels are shown.
- `result_uns_key`: ( str , default="liana_res" ) – adata.uns key searched when adata is not already a communication AnnData. If a compatible LIANA result table is found, it is converted automatically.
- `score_key`: ( str , default="specificity_rank" ) – Columns used when auto-converting LIANA results to communication scores and p-value-like support values.
- `pvalue_key`: ( str , default="specificity_rank" ) – Columns used when auto-converting LIANA results to communication scores and p-value-like support values.
- `inverse_score`: ( bool , default= ( True , False ) ) – Whether the LIANA score or p-value columns should be inverted during automatic conversion.
- `inverse_pvalue`: ( bool , default= ( True , False ) ) – Whether the LIANA score or p-value columns should be inverted during automatic conversion.
- `classification`: ( str , mapping , or None , default=None ) – Optional LIANA classification override used only during automatic conversion.
- `classification_reference`: ( str , pandas.DataFrame , or None , default="cellchat" ) – Reference used to backfill pathway labels during automatic LIANA conversion. This mainly affects pathway/signaling summaries such as display_by='aggregation' and plot_type='pathway_summary' . Pure interaction-level views do not depend on this label unless the plotted layout groups interactions by pathway.
- `classification_fallback`: ( str or None , default="family" ) – Fallback pathway label strategy used during automatic LIANA conversion when a pair is not found in classification_reference . Supported values are 'family' , 'unclassified' , 'label:<name>' , or None .
- `pvalue_threshold`: ( float , default=0.05 ) – Maximum p-value retained as a significant communication event.
- `pattern`: ( {"outgoing" , "incoming" , "all"} , default="all" ) – Signaling role pattern used by role-specific heatmap summaries.
- `color_by`: ( {"score" , "pvalue"} , default="score" ) – Quantity encoded by the heatmap color scale when the selected view supports alternative coloring modes.
- `value`: ( {"sum" , "mean" , "max" , "count"} , default="sum" ) – Aggregation statistic used to summarize communication strengths before plotting.
- `top_n`: ( int , default=20 ) – Number of top pathways or interactions retained in ranked views.
- `top_n_pairs`: ( int or None , default=None ) – Reserved for dense interaction matrix layouts. It is not used by the LIANA-style plot_type='dot' view.
- `top_anno`: ( str , sequence of str , or None , default="bar" ) – Annotation layer(s) displayed above the matrix, such as cell-color or summary-bar annotations.
- `bottom_anno`: ( str , sequence of str , or None , default="cell" ) – Annotation layer(s) displayed below the matrix.
- `left_anno`: ( str , sequence of str , or None , default="bar" ) – Annotation layer(s) displayed on the left side of the matrix.
- `right_anno`: ( str , sequence of str , or None , default="cell" ) – Annotation layer(s) displayed on the right side of the matrix.
- `bar_value`: ( {"count" , "sum" , "mean" , "max"} , default="sum" ) – Summary statistic used in bar-style annotations.
- `facet_by`: ( {"sender" , "receiver"} or None , default=None ) – Split matrix-style views into sender- or receiver-specific facets when the selected plot type supports faceting.
- `pathway_method`: ( str , default="mean" ) – Method used to summarize multiple ligand-receptor pairs into pathway level scores.
- `min_lr_pairs`: ( int , default=1 ) – Minimum number of ligand-receptor pairs required for a pathway to be retained.
- `min_expression`: ( float , default=0.1 ) – Minimum grouped expression threshold used by pathway-level summaries.
- `group_pathways`: ( bool , default=True ) – Whether to combine related pathways in pathway-focused bubble views.
- `transpose`: ( bool , default=False ) – Whether to transpose the plotted matrix when supported by the selected plot type.
- `add_violin`: ( bool , default=False ) – Whether to append violin summaries in compatible bubble-style plots.
- `remove_isolate`: ( bool , default=False ) – Whether to remove isolated rows or columns with no retained signal.
- `min_interaction_threshold`: ( float , default=0.0 ) – Minimum interaction strength shown in focused heatmap views.
- `cluster_rows`: ( bool , default=False ) – Whether to cluster matrix rows before plotting.
- `cluster_columns`: ( bool , default=False ) – Whether to cluster matrix columns before plotting.
- `show_row_names`: ( bool , default=False ) – Whether to display explicit row/cell-type labels in Marsilea-backed plot_type='heatmap' and plot_type='focused_heatmap' views.
- `show_col_names`: ( bool , default=False ) – Whether to display explicit column/cell-type labels in Marsilea-backed plot_type='heatmap' and plot_type='focused_heatmap' views.
- `add_text`: ( bool or None , default=None ) – Whether to overlay text labels on matrix entries when the selected plot type supports annotation text.
- `border`: ( bool , default=False ) – Whether to draw borders around matrix cells.
- `cmap`: ( str , default="Reds" ) – Colormap used for the matrix color scale.
- `figsize`: ( tuple of float or None , default=None ) – Figure size in inches. For plot_type='dot' and 'source_target_dot' and 'tile' / 'source_target_tile' , None enables automatic sizing based on the number of source panels, targets, and interactions. When an explicit tuple is provided, the dot plot uses that final size directly without enforcing an internal minimum. Other heatmap-style views fall back to their historical default size when None is given.
- `title`: ( str or None , default=None ) – Custom title for the generated figure. When omitted, a plot-specific default title is used.
- `verbose`: ( bool , default=True ) – Whether pathway-ranking helper steps should print textual summaries to standard output. This currently matters for views that auto-rank pathways from summary statistics.
- `show`: ( bool , default=False ) – Whether to immediately display the figure.
- `save`: ( str or bool , default=False ) – File path for saving the figure, or False to skip saving.

## Full Documentation

# omicverse.pl.ccc_heatmap #

omicverse.pl. ccc_heatmap ( adata , * , plot_type = 'heatmap' , comparison_adata = None , display_by = 'aggregation' , sender_use = None , receiver_use = None , signaling = None , interaction_use = None , pair_lr_use = None , sample_key = 'sample' , ncols = None , nrows = None , result_uns_key = 'liana_res' , score_key = 'specificity_rank' , pvalue_key = 'specificity_rank' , inverse_score = True , inverse_pvalue = False , classification = None , classification_reference = 'cellchat' , classification_fallback = 'family' , pvalue_threshold = 0.05 , pattern = 'all' , color_by = 'score' , value = 'sum' , top_n = 20 , top_n_pairs = None , top_anno = 'bar' , bottom_anno = 'cell' , left_anno = 'bar' , right_anno = 'cell' , bar_value = 'sum' , facet_by = None , pathway_method = 'mean' , min_lr_pairs = 1 , min_expression = 0.1 , group_pathways = True , transpose = False , add_violin = False , remove_isolate = False , min_interaction_threshold = 0.0 , cluster_rows = False , cluster_columns = False , show_row_names = False , show_col_names = False , add_text = None , border = False , cmap = 'Reds' , figsize = None , title = None , verbose = True , show = False , save = False ) [source] #

Plot communication matrices as heatmaps, dot plots, or bubble maps.

Parameters :

-
adata ( anndata.AnnData ) – Communication AnnData produced by the OmicVerse CCC workflow, or a regular AnnData containing a LIANA result table in `adata.uns[result_uns_key] `. LIANA inputs are adapted internally to the communication format expected by `ccc_* `.

-
plot_type ( str , default="heatmap" ) – Matrix view to render. `'dot' `is the primary LIANA-style source / target interaction dotplot. `'source_target_dot' `is kept only as a backward-compatible alias of the same layout. Other supported values include aggregated heatmaps, focused heatmaps, bubble summaries, pathway-level bubble plots, source-target tile/sample views, signaling role maps, and differential heatmaps.

-
comparison_adata ( anndata.AnnData or None , default=None ) – Second communication AnnData used when plotting condition-to-condition differential heatmaps.

-
display_by ( {"aggregation" , "interaction"} , default="aggregation" ) – Whether to summarize the matrix at the signaling/pathway level or at the interaction level.

-
sender_use ( str , sequence of str , or None , default=None ) – Optional sender cell types retained in sender-aware heatmap views.

-
receiver_use ( str , sequence of str , or None , default=None ) – Optional receiver cell types retained in receiver-aware heatmap views.

-
signaling ( str , sequence of str , or None , default=None ) – Signaling pathway name or names to visualize.

-
interaction_use ( str , sequence of str , or None , default=None ) – Interaction names used to restrict interaction-level dot or bubble plots.

-
pair_lr_use ( str , sequence of str , or None , default=None ) – Ligand-receptor pair identifiers used by pair-resolved bubble views.

-
sample_key ( str , default="sample" ) – Observation/sample column used by `plot_type='sample_dot' `after LIANA results are converted to communication AnnData. If this column is not present but LIANA conversion stored a detected sample/context key in `adata.uns['liana_sample_key'] `, that key is used automatically.

-
ncols ( int or None , default=None ) – Number of source facets per row/column for LIANA-style dot layouts. These parameters are used by `plot_type='dot' `(and the backward-compatible alias `'source_target_dot' `) to avoid a single excessively wide row when many source panels are shown.

-
nrows ( int or None , default=None ) – Number of source facets per row/column for LIANA-style dot layouts. These parameters are used by `plot_type='dot' `(and the backward-compatible alias `'source_target_dot' `) to avoid a single excessively wide row when many source panels are shown.

-
result_uns_key ( str , default="liana_res" ) – `adata.uns `key searched when `adata `is not already a communication AnnData. If a compatible LIANA result table is found, it is converted automatically.

-
score_key ( str , default="specificity_rank" ) – Columns used when auto-converting LIANA results to communication scores and p-value-like support values.

-
pvalue_key ( str , default="specificity_rank" ) – Columns used when auto-converting LIANA results to communication scores and p-value-like support values.

-
inverse_score ( bool , default= ( True , False ) ) – Whether the LIANA score or p-value columns should be inverted during automatic conversion.

-
inverse_pvalue ( bool , default= ( True , False ) ) – Whether the LIANA score or p-value columns should be inverted during automatic conversion.

-
classification ( str , mapping , or None , default=None ) – Optional LIANA classification override used only during automatic conversion.

-
classification_reference ( str , pandas.DataFrame , or None , default="cellchat" ) – Reference used to backfill pathway labels during automatic LIANA conversion. This mainly affects pathway/signaling summaries such as `display_by='aggregation' `and `plot_type='pathway_summary' `. Pure interaction-level views do not depend on this label unless the plotted layout groups interactions by pathway.

-
classification_fallback ( str or None , default="family" ) – Fallback pathway label strategy used during automatic LIANA conversion when a pair is not found in `classification_reference `. Supported values are `'family' `, `'unclassified' `, `'label:<name>' `, or `None `.

-
pvalue_threshold ( float , default=0.05 ) – Maximum p-value retained as a significant communication event.

-
pattern ( {"outgoing" , "incoming" , "all"} , default="all" ) – Signaling role pattern used by role-specific heatmap summaries.

-
color_by ( {"score" , "pvalue"} , default="score" ) – Quantity encoded by the heatmap color scale when the selected view supports alternative coloring modes.

-
value ( {"sum" , "mean" , "max" , "count"} , default="sum" ) – Aggregation statistic used to summarize communication strengths before plotting.

-
top_n ( int , default=20 ) – Number of top pathways or interactions retained in ranked views.

-
top_n_pairs ( int or None , default=None ) – Reserved for dense interaction matrix layouts. It is not used by the LIANA-style `plot_type='dot' `view.

-
top_anno ( str , sequence of str , or None , default="bar" ) – Annotation layer(s) displayed above the matrix, such as cell-color or summary-bar annotations.

-
bottom_anno ( str , sequence of str , or None , default="cell" ) – Annotation layer(s) displayed below the matrix.

-
left_anno ( str , sequence of str , or None , default="bar" ) – Annotation layer(s) displayed on the left side of the matrix.

-
right_anno ( str , sequence of str , or None , default="cell" ) – Annotation layer(s) displayed on the right side of the matrix.

-
bar_value ( {"count" , "sum" , "mean" , "max"} , default="sum" ) – Summary statistic used in bar-style annotations.

-
facet_by ( {"sender" , "receiver"} or None , default=None ) – Split matrix-style views into sender- or receiver-specific facets when the selected plot type supports faceting.

-
pathway_method ( str , default="mean" ) – Method used to summarize multiple ligand-receptor pairs into pathway level scores.

-
min_lr_pairs ( int , default=1 ) – Minimum number of ligand-receptor pairs required for a pathway to be retained.

-
min_expression ( float , default=0.1 ) – Minimum grouped expression threshold used by pathway-level summaries.

-
group_pathways ( bool , default=True ) – Whether to combine related pathways in pathway-focused bubble views.

-
transpose ( bool , default=False ) – Whether to transpose the plotted matrix when supported by the selected plot type.

-
add_violin ( bool , default=False ) – Whether to append violin summaries in compatible bubble-style plots.

-
remove_isolate ( bool , default=False ) – Whether to remove isolated rows or columns with no retained signal.

-
min_interaction_threshold ( float , default=0.0 ) – Minimum interaction strength shown in focused heatmap views.

-
cluster_rows ( bool , default=False ) – Whether to cluster matrix rows before plotting.

-
cluster_columns ( bool , default=False ) – Whether to cluster matrix columns before plotting.

-
show_row_names ( bool , default=False ) – Whether to display explicit row/cell-type labels in Marsilea-backed `plot_type='heatmap' `and `plot_type='focused_heatmap' `views.

-
show_col_names ( bool , default=False ) – Whether to display explicit column/cell-type labels in Marsilea-backed `plot_type='heatmap' `and `plot_type='focused_heatmap' `views.

-
add_text ( bool or None , default=None ) – Whether to overlay text labels on matrix entries when the selected plot type supports annotation text.

-
border ( bool , default=False ) – Whether to draw borders around matrix cells.

-
cmap ( str , default="Reds" ) – Colormap used for the matrix color scale.

-
figsize ( tuple of float or None , default=None ) – Figure size in inches. For `plot_type='dot' `and `'source_target_dot' `and `'tile' `/ `'source_target_tile' `, `None `enables automatic sizing based on the number of source panels, targets, and interactions. When an explicit tuple is provided, the dot plot uses that final size directly without enforcing an internal minimum. Other heatmap-style views fall back to their historical default size when `None `is given.

-
title ( str or None , default=None ) – Custom title for the generated figure. When omitted, a plot-specific default title is used.

-
verbose ( bool , default=True ) – Whether pathway-ranking helper steps should print textual summaries to standard output. This currently matters for views that auto-rank pathways from summary statistics.

-
show ( bool , default=False ) – Whether to immediately display the figure.

-
save ( str or bool , default=False ) – File path for saving the figure, or `False `to skip saving.

Returns :

A `(fig, ax) `tuple containing the Matplotlib figure and the main axes used for the rendered heatmap-style view.

Return type :

tuple
