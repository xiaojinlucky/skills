# 环境、版本与文档维护

## 目标

把可复用分析方法的环境、函数文档、参数文档和索引当作同一件事维护。任何一个缺失，都不能把该方法写进正式分析路线。

## 决策顺序

1. 列出当前方法真正需要的运行时、包、版本、外部程序和数据交换格式。
2. 先检查现有共享环境能否直接满足；不要为了一个新方法随手升级其核心依赖。
   同一个包在另一套 R library 或 Python 环境中能加载，不等于它在正式运行环境中可用；每个正式 backend 都要在自己的解释器内验收。
3. 若本机版本落后、无法加载，或不能匹配将使用的文档，先最小更新直接相关包与依赖，再运行导入/加载和函数签名检查。
4. 若新方法会改变工作环境的核心依赖，优先建独立环境；共享环境只保留已验证的稳定主路线。
5. 比较环境成本和新增证据价值。重复同一假设的高成本方法不装；能补上独立统计假设、且用户会复用的方法，建立隔离环境。
6. 环境通过验收后才写入 `runtime_index.tsv`，并把官方函数和参数写入第三方索引。

## 更新后的文档纪律

- OmicVerse / SCOP：运行 `scripts/update_docs.py --package all`，再运行索引验证脚本；不要把 `--limit` 的部分结果当正式索引。
- 第三方包：保存官方教程或 API 地址、当前本机版本、正式函数、关键参数、输入输出和原生作图函数；登记到 `third_party_function_index.tsv` 与 `third_party_parameter_index.tsv`。
- 文档版本必须与实际运行时一致。若官方网页领先于本机版本，先更新或明确按本机签名写代码。
- 2026-08-03 已验证基线：`omicverse` 环境为 OmicVerse 2.3.1，`seurat_v5` 环境为 SCOP 0.9.0；完整索引刷新后才把最新函数页作为正式参考。
- 本次 SCOP 0.9.0 源码安装使用了系统 GCC 的 `R_MAKEVARS_USER` 配置，因为当前 R 的 Conda 编译器前缀不可用；这是安装阶段的编译约束，不是运行 SCOP 分析时的必需环境变量。

## 隔离环境最小验收

1. 用环境自身的 Python/R 读取包版本。
2. 导入或加载包。
3. 打印计划使用的函数签名或帮助页关键参数。
4. 只在有真实、已确认输入时运行最小真实数据 smoke test；不要为了验收虚构科研数据。
5. 记录数据交接格式，例如 Seurat -> h5ad、AnnData -> sample x cell-type integer count table，避免以后靠记忆猜路径。

## 运行时登记格式

`runtime_index.tsv` 每行一个已验收环境：

| 字段 | 含义 |
|---|---|
| runtime_id | 稳定、可读的环境名称 |
| runtime_kind | Python / R / mixed |
| environment_path | 精确环境路径 |
| primary_packages | 关键包及版本 |
| status | planned / verified / retired |
| verification_command | 可直接复验的最小命令 |
| updated_at | 最近一次核验时间 |
| notes | 使用边界与数据交接约束 |

不要把未验证、部分安装或已停止维护的后端标记为 `verified`。已停止维护的实现可保留为 `retired` 记录，但正式路线优先登记维护中的替代实现。

## 已验证运行时与兼容桥

- `sccoda_pertpy_py312`：用于当前维护中的 `pertpy.tl.Sccoda` 和 `pertpy.tl.Milo`，与 OmicVerse 环境隔离。交接数据为 AnnData，要求每个细胞有 `sampleID` 与细胞类型列；Milo 的 `pydeseq2` 求解器也在该环境中验收通过。
- `tdeseq_seurat5_bridge`：TDEseq 1.1 的 `CreateTDEseqObject(seurat)` 快捷入口仍使用已被 SeuratObject 5 移除的 `slot=` 参数。不要降级共享 Seurat；在 `seurat_v5` 中用 `LayerData(..., layer = "counts"/"data")` 提取两个矩阵及元数据，再走 TDEseq 的矩阵构造入口。只在 `scripts/verify_tdeseq_seurat5.R` 通过后使用；详情见 `third_party/TDEseq.md`。
