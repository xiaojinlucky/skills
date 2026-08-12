# scDist 1.1.5

## 适用问题

用于比较两个条件下不同细胞类型或亚型的整体转录组扰动距离，并通过线性混合模型纳入生物学样本之间的差异。适合回答“哪类细胞的整体转录状态变化更大”，不直接检验两个细胞类型的距离是否彼此显著不同。

## 官方来源

- 作者仓库与演示：https://github.com/phillipnicol/scDist
- 原始论文：https://www.nature.com/articles/s41467-024-51649-3

## 已验证运行时

- 基础环境：`/hwdata/home/jinqc/miniconda3/envs/seurat_v5`
- 附加 R library：`/hwdata/home/jinqc/.codex-shared/runtimes/scdist_r44/Rlib`
- 版本：R 4.4.3，Seurat 5.4.0，scDist 1.1.5
- 复验：

```bash
R_LIBS_USER=/hwdata/home/jinqc/.codex-shared/runtimes/scdist_r44/Rlib \
  conda run -n seurat_v5 Rscript \
  /hwdata/home/jinqc/.codex-shared/skills/omics-coding/scripts/verify_scdist.R
```

## 正式路线

作者真实数据示例使用标准化后的 `scale.data`。Seurat 对象可直接提供基因 × 细胞矩阵和逐细胞元数据：

```r
expression_matrix <- SeuratObject::LayerData(
  seurat,
  assay = "RNA",
  layer = "scale.data"
)

result <- scDist::scDist(
  normalized_counts = expression_matrix,
  meta.data = seurat[[]],
  fixed.effects = "group",
  random.effects = "sampleID",
  clusters = "celltype",
  d = 20,
  min.count.per.cell = 21,
  weights = NULL
)
```

- `normalized_counts` 必须是基因 × 细胞矩阵，列顺序必须与 `meta.data` 行顺序一致。
- `fixed.effects` 的第一个变量必须是目标条件。当前实现固定读取模型的第二个系数，并通过删除第一个固定效应构造零模型。
- `random.effects` 应写真实生物学样本列，不能写分组名。
- `clusters` 是细胞类型或亚型列。
- `d = 20` 是作者论文建议的常用设置。
- 源码中的 `min.count.per.cell` 实际检查整个 cluster 的总细胞数，不是逐样本最低细胞数。逐样本覆盖仍需分析前单独审核。
- 设置 `min.count.per.cell = 21` 是为了避免总细胞数恰好等于 20 时，`prcomp_irlba(n = 20)` 接近矩阵最小维度的边界。
- 论文建议默认使用不加权距离；没有很强的先验信息时保持 `weights = NULL`。

## 原生输出与图形

- `result$results`：每个亚型的距离、中位数后验区间和 P 值。
- `scDist::DistPlot(result)`：距离及区间。
- `scDist::FDRDistPlot(result)`：距离与多重校正结果。
- `scDist::distGenes(result, cluster = "目标亚型")`：对整体扰动贡献较大的基因方向。

这些结果可以比较距离大小和排序，但当前包没有提供“亚型 A 的距离是否显著大于亚型 B”的直接检验。

- `FDRDistPlot()` 的默认虚线是 FDR 0.1，不是 FDR 0.05。
- `distGenes()` 展示的是哪些基因方向对整体距离贡献较大，不是逐基因差异检验，不能称为显著差异基因或驱动基因。

## 已验证失败点

- `simData()` 的 `G` 参数没有继续传入内部 `simCellType()`；修改非默认 `G` 会造成矩阵行数不一致。复验脚本保留默认 `G = 1000`。
- `min.count.per.cell` 名称容易被误解成逐细胞或逐样本阈值；当前实现只检查每个 cluster 的总细胞数。
- 稀有亚型即使总细胞数通过，逐样本极低覆盖仍可能得到很宽的区间，不能只按距离排名解释。
- 当疾病组与测序复杂度强相关时，可把标准化后的 `nFeature_RNA` 作为第二个固定效应做一次敏感性分析。`nFeature_RNA` 也可能包含真实生物学变化，因此该模型回答“固定检出基因数后还剩多少残余差异”，不是“校正后的真实结果”，不能替代未调整模型。
