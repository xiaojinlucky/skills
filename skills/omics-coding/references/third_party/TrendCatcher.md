# TrendCatcher 1.0.0

## 适用问题

用于原始 RNA-seq 计数的纵向动态分析。单细胞场景需先按细胞类型和生物学样本汇总成 pseudo-bulk 原始计数矩阵；它不把单细胞直接作为独立 RNA-seq 样本。

## 官方来源

- 教程：https://jaleesr.github.io/TrendCatcher/
- 源码与示例：https://github.com/jaleesr/TrendCatcher

## 当前本机状态

- `omicverse` 环境已安装 TrendCatcher 1.0.0，且已能加载和读取 `run_TrendCatcher()` 签名。
- 尚未完成当前项目的正式输入 smoke test；只有在 TDEseq 主分析出现需要独立复核的信号时，再按该项目的原始 pseudo-bulk 计数和样本覆盖运行。

## 官方入口

```r
master.list <- TrendCatcher::run_TrendCatcher(
  count.table.path = "raw_pseudobulk_counts.csv",
  baseline.t = 0,
  time.unit = "stage",
  min.low.count = 1,
  para.core.n = 1,
  dyn.p.thres = 0.05
)
```

- 输入列名需同时编码项目名、数值时间和重复样本，首列为基因名。
- `baseline.t` 必须是最小的时间点。
- 三个阶段可以运行，但拟合和拐点判断的信息量有限；本项目只把它作为 TDEseq 的备用复核，不当主结论来源。
- 原生可视化包括 `draw_GeneTraj()`、`draw_TrajClusterGrid()` 和 `draw_TimeHeatmap_GO()`。
