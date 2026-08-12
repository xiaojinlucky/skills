.libPaths(c(
  "/hwdata/home/jinqc/.codex-shared/runtimes/scdist_r44/Rlib",
  .libPaths()
))

library(scDist)

set.seed(1126490984)
simulated <- scDist::simData(
  nct = 2,
  J = 30,
  N1 = 3,
  N2 = 3
)
rownames(simulated$Y) <- paste0("gene_", seq_len(nrow(simulated$Y)))

result <- scDist::scDist(
  normalized_counts = simulated$Y,
  meta.data = simulated$meta.data,
  fixed.effects = "response",
  random.effects = "patient",
  clusters = "clusters",
  d = 10,
  min.count.per.cell = 21
)

stopifnot(nrow(result$results) == 2)
stopifnot(all(c("Dist.", "95% CI (low)", "95% CI (upper)", "p.val") %in%
  colnames(result$results)))

cat("scDist", as.character(packageVersion("scDist")), "verified\n")
