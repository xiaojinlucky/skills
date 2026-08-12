# TDEseq 1.1

## 适用问题

用于多样本、多个离散阶段的单细胞转录组时间动态基因筛选。它用混合模型将同一生物学样本内的细胞相关性纳入模型，并把显著基因分为 `Growth`、`Recession`、`Peak`、`Trough` 四种模式。

## 官方来源

- 教程：https://fanyue322.github.io/TDEseq
- 源码与示例：https://github.com/fanyue322/TDEseq

## 已验证运行时

- 环境：`/hwdata/home/jinqc/miniconda3/envs/seurat_v5`
- 版本：TDEseq 1.1，Seurat 5.4.0，SeuratObject 5.3.0
- 复验：`conda run -n seurat_v5 Rscript /hwdata/home/jinqc/.codex-shared/skills/omics-coding/scripts/verify_tdeseq_seurat5.R`

## SeuratObject 5 兼容桥

不要调用 `CreateTDEseqObject(seurat)`。TDEseq 1.1 的该快捷入口仍调用已移除的 `slot=` API。改为从 RNA assay 取 `counts` 与 `data` layer，并连同 `seurat[[]]` 传入矩阵构造入口：

```r
counts <- SeuratObject::LayerData(seurat[["RNA"]], layer = "counts")
data_norm <- SeuratObject::LayerData(seurat[["RNA"]], layer = "data")
tde <- TDEseq::CreateTDEseqObject(
  counts = counts,
  data = data_norm,
  meta.data = seurat[[]]
)
```

该桥已用包内官方示例跑通。若 TDEseq、Seurat 或 SeuratObject 更新，先重新运行复验脚本；复验失败才评估独立环境，不直接降级共享 Seurat。

## 正式路线

```r
tde <- TDEseq::tdeseq(
  object = tde,
  tde.method = "cell",
  tde.param = list(
    sample.var = "sampleID",
    stage.var = "stage_order",
    fit.model = "lmm",
    pct = 0.1,
    lfc = 0.1,
    tde.thr = 0.05,
    max.gcells = Inf,
    min.tcells = 3
  ),
  mod = "FastLMM",
  num.core = 1
)
result <- TDEseq::GetTDEseqAssayData(tde, slot = "tde")
```

- `sample.var` 必须是生物学样本 ID，不能写三组名称。
- `stage.var` 必须是已固定顺序的阶段编码；离散三阶段可用 `1, 2, 3`。
- `fit.model = "lmm"` 保留样本层随机效应；只有确认没有样本层相关性时才用 `lm`。
- TDEseq 1.1 的内部 `tdeseq.Assay()` 不会把 `tde.param$mod` 转交给底层 `tdeseq.default()`；因此 `mod = "FastLMM"` 必须写在外层 `TDEseq::tdeseq()` 调用中。仅写进 `tde.param` 不会控制混合模型后端。
- `min.tcells` 只按一个阶段的总细胞数剔除整段，不替代样本覆盖审计。
- `pattern == "Recession"` 的前提是该基因已通过 `padj < tde.thr`；`decreasing.pvalue` 是对应下降形状检验的 P 值。
- 正式图先检查 `PatternHeatmap` 和 `PatternLine`；跨亚型比较图再评估 SCOP 或最小自定义图。

## 输出字段

核心字段为 `increasing.pvalue`、`decreasing.pvalue`、`convex.pvalue`、`concave.pvalue`、`pvalue`、`padj`、`SignificantDE`、`pattern`、`logFC` 和 `ChangePoint`。`pattern` 是按模型拟合结果分配，不应仅凭三个均值点肉眼重写。
