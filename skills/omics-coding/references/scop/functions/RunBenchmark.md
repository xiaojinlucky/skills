# Benchmark spatial domain clustering methods

- Package: scop
- Language: R
- Function: `RunBenchmark`
- Source: https://mengxu98.github.io/scop/reference/RunBenchmark.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunBenchmark.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run registered spatial domain clustering methods from the same immutable input, compare their aligned labels with a gold standard, and record classification quality, elapsed time, and sampled peak process-tree memory. Each method runs in an isolated R process so one failed backend does not corrupt the input or prevent the remaining methods from being assessed.

## Signature

```text
RunBenchmark( srt, gold_standard, methods = NULL, method_params = list(), n_clusters = NULL, metrics = c("ARI", "NMI"), keep_objects = FALSE, install_missing = FALSE, seed = 1, timeout = Inf, poll_interval = 0.1, verbose = TRUE )
```

## Parameters

- `srt`: A spatial Seurat object.
- `gold_standard`: Either one metadata column in srt or a named vector whose names match the spot names in srt.
- `methods`: Spatial domain methods to benchmark. NULL uses every stable registered domain producer. Use "all" to additionally include supported legacy baselines such as GiottoCluster, or select them explicitly. Method names may be written with or without the Run prefix.
- `method_params`: Named list of per-method argument lists. Arguments are passed to the corresponding SCOP producer, never directly to its backend.
- `n_clusters`: Optional common number of domains. When NULL, methods that require a cluster count use the number of non-missing gold-standard classes. A method-specific q or n_clusters in method_params wins.
- `metrics`: Quality metrics selected by default when plotting. Supported values are "ARI", "NMI", and "purity". All three are retained in the result summary.
- `keep_objects`: Whether to keep each successful method's full producer result, including standalone legacy results when explicitly selected. The default keeps only aligned labels and compact run metadata.
- `install_missing`: Whether missing optional backends may enter their producer's normal check_r() installation path. The default records them as unavailable without changing the R library.
- `seed`: Seed set inside each isolated method process and forwarded to producers with a public seed argument unless overridden in method_params.
- `timeout`: Maximum wall time in seconds for each isolated run, including process start and result serialization. Inf disables the timeout.
- `poll_interval`: Seconds between process-tree memory samples.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Benchmark spatial domain clustering methods

## Usage

```text
RunBenchmark( srt, gold_standard, methods = NULL, method_params = list(), n_clusters = NULL, metrics = c("ARI", "NMI"), keep_objects = FALSE, install_missing = FALSE, seed = 1, timeout = Inf, poll_interval = 0.1, verbose = TRUE )
```

## Description

Run registered spatial domain clustering methods from the same immutable input, compare their aligned labels with a gold standard, and record classification quality, elapsed time, and sampled peak process-tree memory. Each method runs in an isolated R process so one failed backend does not corrupt the input or prevent the remaining methods from being assessed.

## Value

A benchmark_result object. Use as.data.frame() for its summary, plot() or {[=BenchmarkPlot]{BenchmarkPlot()}} for visualization, and $predictions for the aligned labels.

## Examples

```r
\dontrun{
data(visium_human_pancreas_sub)
visium_human_pancreas_sub$gold_domain <- factor(
  paste0("domain_", (seq_len(ncol(visium_human_pancreas_sub)) - 1) \%\% 3 + 1)
)
bench <- RunBenchmark(
  visium_human_pancreas_sub,
  gold_standard = "gold_domain",
  method_params = list(
    BayesSpace = list(n.PCs = 5, n.HVGs = 200),
    BANKSY = list(layer = "counts"),
    SmoothClust = list(layer = "counts", min_spots = 1)
  )
)
bench
BenchmarkPlot(data = bench)
}
```
