# omicverse.pl.volcano #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.volcano`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.volcano.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Create a volcano plot for differential expression analysis.

## Signature

```text
omicverse.pl. volcano ( result , pval_name = 'qvalue' , fc_name = 'log2FC' , pval_max = None , FC_max = None , figsize = (4, 4) , title = '' , titlefont = {'size': 14, 'weight': 'normal'} , up_color = 'e25d5d' , down_color = '7388c1' , normal_color = 'd7d7d7' , up_fontcolor = 'e25d5d' , down_fontcolor = '7388c1' , normal_fontcolor = 'd7d7d7' , legend_bbox = (0.8, -0.2) , legend_ncol = 2 , legend_fontsize = 12 , show_thresholds = True , threshold_color = '0.55' , threshold_linewidth = 0.8 , threshold_linestyle = '--' , show_normal_in_legend = True , plot_genes = None , plot_genes_num = 10 , plot_genes_fontsize = 10 , ticks_fontsize = None , pval_threshold = 0.05 , fc_max = 1.5 , fc_min = -1.5 , label_fontsize = None , ax = None )
```

## Parameters

- `result`: ( pd.DataFrame ) – Differential-expression result table containing at least p-value, fold-change, and sig classification columns.
- `pval_name`: ( str ) – Column name of adjusted p-values or q-values.
- `fc_name`: ( str ) – Column name of log fold-change values.
- `pval_max`: ( float or None ) – Optional y-axis upper bound in transformed p-value scale.
- `FC_max`: ( float or None ) – Optional x-axis absolute range cap.
- `figsize`: ( tuple ) – Figure size passed to matplotlib.
- `title`: ( str ) – Plot title.
- `titlefont`: ( dict ) – Font dict for title/axis labels.
- `up_color`: ( str ) – Point color for up-regulated genes.
- `down_color`: ( str ) – Point color for down-regulated genes.
- `normal_color`: ( str ) – Point color for non-significant genes.
- `up_fontcolor`: ( str ) – Label color for up-regulated genes.
- `down_fontcolor`: ( str ) – Label color for down-regulated genes.
- `normal_fontcolor`: ( str ) – Label color for non-significant genes.
- `legend_bbox`: ( tuple ) – Legend anchor position.
- `legend_ncol`: ( int ) – Number of legend columns.
- `legend_fontsize`: ( int ) – Legend font size.
- `show_thresholds`: ( bool ) – Draw the fold-change and p-value guide lines. False omits them.
- `threshold_color`: ( str (default: '0.55' )) – Style of those guides. The default is a thin grey dash; they used to be fixed at 2 pt solid black, which reads as content rather than as an annotation — especially in a small panel.
- `threshold_linewidth`: ( float (default: 0.8 )) – Style of those guides. The default is a thin grey dash; they used to be fixed at 2 pt solid black, which reads as content rather than as an annotation — especially in a small panel.
- `threshold_linestyle`: ( str (default: '--' )) – Style of those guides. The default is a thin grey dash; they used to be fixed at 2 pt solid black, which reads as content rather than as an annotation — especially in a small panel.
- `show_normal_in_legend`: ( bool ) – Include the non-significant count in the legend. It is the majority of the points, so leaving it out left the grey cloud unexplained.
- `plot_genes`: ( list or None ) – Explicit gene list to annotate.
- `plot_genes_num`: ( int ) – Number of top genes automatically annotated when plot_genes is None.
- `plot_genes_fontsize`: ( int ) – Font size for annotated gene labels.
- `ticks_fontsize`: ( int or None ) – Tick label font size. When None follows rcParams['xtick.labelsize'] .
- `pval_threshold`: ( float ) – Significance threshold used to define highlighted genes.
- `fc_max`: ( float ) – Positive fold-change cutoff.
- `fc_min`: ( float ) – Negative fold-change cutoff.
- `label_fontsize`: ( float or None ) – Font size of the x/y axis labels. When None follows rcParams['axes.labelsize'] so the labels match surrounding panels instead of the fixed title font size.
- `ax`: ( matplotlib.axes.Axes or None ) – Existing axes object to draw on.

## Full Documentation

# omicverse.pl.volcano #

omicverse.pl. volcano ( result , pval_name = 'qvalue' , fc_name = 'log2FC' , pval_max = None , FC_max = None , figsize = (4, 4) , title = '' , titlefont = {'size': 14, 'weight': 'normal'} , up_color = '#e25d5d' , down_color = '#7388c1' , normal_color = '#d7d7d7' , up_fontcolor = '#e25d5d' , down_fontcolor = '#7388c1' , normal_fontcolor = '#d7d7d7' , legend_bbox = (0.8, -0.2) , legend_ncol = 2 , legend_fontsize = 12 , show_thresholds = True , threshold_color = '0.55' , threshold_linewidth = 0.8 , threshold_linestyle = '--' , show_normal_in_legend = True , plot_genes = None , plot_genes_num = 10 , plot_genes_fontsize = 10 , ticks_fontsize = None , pval_threshold = 0.05 , fc_max = 1.5 , fc_min = -1.5 , label_fontsize = None , ax = None ) [source] #

Create a volcano plot for differential expression analysis.

Parameters :

-
result ( pd.DataFrame ) – Differential-expression result table containing at least p-value, fold-change, and `sig `classification columns.

-
pval_name ( str ) – Column name of adjusted p-values or q-values.

-
fc_name ( str ) – Column name of log fold-change values.

-
pval_max ( float or None ) – Optional y-axis upper bound in transformed p-value scale.

-
FC_max ( float or None ) – Optional x-axis absolute range cap.

-
figsize ( tuple ) – Figure size passed to matplotlib.

-
title ( str ) – Plot title.

-
titlefont ( dict ) – Font dict for title/axis labels.

-
up_color ( str ) – Point color for up-regulated genes.

-
down_color ( str ) – Point color for down-regulated genes.

-
normal_color ( str ) – Point color for non-significant genes.

-
up_fontcolor ( str ) – Label color for up-regulated genes.

-
down_fontcolor ( str ) – Label color for down-regulated genes.

-
normal_fontcolor ( str ) – Label color for non-significant genes.

-
legend_bbox ( tuple ) – Legend anchor position.

-
legend_ncol ( int ) – Number of legend columns.

-
legend_fontsize ( int ) – Legend font size.

-
show_thresholds ( bool ) – Draw the fold-change and p-value guide lines. `False `omits them.

-
threshold_color ( `str `(default: `'0.55' `)) – Style of those guides. The default is a thin grey dash; they used to be fixed at 2 pt solid black, which reads as content rather than as an annotation — especially in a small panel.

-
threshold_linewidth ( `float `(default: `0.8 `)) – Style of those guides. The default is a thin grey dash; they used to be fixed at 2 pt solid black, which reads as content rather than as an annotation — especially in a small panel.

-
threshold_linestyle ( `str `(default: `'--' `)) – Style of those guides. The default is a thin grey dash; they used to be fixed at 2 pt solid black, which reads as content rather than as an annotation — especially in a small panel.

-
show_normal_in_legend ( bool ) – Include the non-significant count in the legend. It is the majority of the points, so leaving it out left the grey cloud unexplained.

-
plot_genes ( list or None ) – Explicit gene list to annotate.

-
plot_genes_num ( int ) – Number of top genes automatically annotated when `plot_genes `is None.

-
plot_genes_fontsize ( int ) – Font size for annotated gene labels.

-
ticks_fontsize ( int or None ) – Tick label font size. When `None `follows `rcParams['xtick.labelsize'] `.

-
pval_threshold ( float ) – Significance threshold used to define highlighted genes.

-
fc_max ( float ) – Positive fold-change cutoff.

-
fc_min ( float ) – Negative fold-change cutoff.

-
label_fontsize ( float or None ) – Font size of the x/y axis labels. When `None `follows `rcParams['axes.labelsize'] `so the labels match surrounding panels instead of the fixed title font size.

-
ax ( matplotlib.axes.Axes or None ) – Existing axes object to draw on.

Returns :

Axes containing the volcano plot.

Return type :

matplotlib.axes.Axes
