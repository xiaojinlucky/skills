suppressPackageStartupMessages({
  library(TDEseq)
  library(Seurat)
})

data(exampledata)

# TDEseq 1.1 的 Seurat 快捷构造器仍使用已删除的 slot= API；
# 在 SeuratObject 5 中改用稳定的 layer 接口后，将矩阵和元数据传给 TDEseq。
counts <- SeuratObject::LayerData(seurat[["RNA"]], layer = "counts")
data_norm <- SeuratObject::LayerData(seurat[["RNA"]], layer = "data")
meta_data <- seurat[[]]

tde <- TDEseq::CreateTDEseqObject(
  counts = counts,
  data = data_norm,
  meta.data = meta_data
)

tde <- TDEseq::tdeseq(
  object = tde,
  tde.method = "cell",
  tde.param = list(
    sample.var = "batch",
    stage.var = "stage",
    fit.model = "lmm",
    pct = 0.1,
    lfc = 0.1,
    tde.thr = 0.05,
    max.gcells = Inf,
    min.tcells = 3,
    mod = "FastLMM"
  ),
  num.core = 1,
  verbose = FALSE
)

result <- TDEseq::GetTDEseqAssayData(tde, slot = "tde")
required_columns <- c(
  "increasing.pvalue", "decreasing.pvalue", "convex.pvalue",
  "concave.pvalue", "pvalue", "padj", "pattern", "logFC"
)

if (!all(required_columns %in% colnames(result))) {
  stop("TDEseq smoke test returned an incomplete result table.")
}

cat("TDEseq", as.character(utils::packageVersion("TDEseq")), "\n")
cat("Seurat", as.character(utils::packageVersion("Seurat")), "\n")
cat("SeuratObject", as.character(utils::packageVersion("SeuratObject")), "\n")
cat("tested_genes", nrow(result), "\n")
print(table(result$pattern, useNA = "ifany"))
cat("PASS: TDEseq 1.1 matrix-constructor bridge works with SeuratObject 5.\n")
