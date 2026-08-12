# OmicOS Agents 运行时索引

来源：本机 runtime `http://127.0.0.1:5055/api/agents`。

- agents 总数：57
- 当前 plan：`pro`
- 当前 team members：`omicverse_omni`, `vertical_agent_selector`, `omicverse_expert`
- 当前 selected agent：`omicverse_omni`

## 分层统计

| tier | 数量 |
|---|---:|
| community | 16 |
| lab | 2 |
| plus | 15 |
| pro | 24 |

## 清单

| # | id | name | tier | category | skills 数 | toolsets |
|---:|---|---|---|---|---:|---|
| 1 | `omicverse_omni` | OmicVerse Omni | `community` | orchestration | 0 | file_manager, python_interpreter, shell, notebook, omicverse_lookup, skill, team, web, plan, schedule, background, think, task, memory, vision, image_gen |
| 2 | `vertical_agent_selector` | Vertical Agent Selector | `community` | orchestration | 0 | team |
| 3 | `GEO-everything` | GEO Everything | `pro` | data_acquisition | 7 | file_manager, python_interpreter, shell, omicverse_lookup, web, plan, think, task, skill, memory |
| 4 | `analysis_strategist` | Analysis Strategist | `pro` | orchestration | 0 | file_manager, python_interpreter, omicverse_lookup, skill, team, plan, think, task, memory |
| 5 | `single_cell_preprocessor` | Single-cell Preprocessor | `plus` | single_cell_analysis | 18 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory |
| 6 | `spatial_omics_orchestrator` | Spatial Omics Orchestrator | `pro` | spatial_analysis | 9 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory |
| 7 | `cell_viewer` | Cell Viewer | `plus` | viewer_tools | 1 | python_interpreter, think, plan, skill, memory |
| 8 | `imagej` | ImageJ | `plus` | viewer_tools | 1 | think, plan, skill, memory |
| 9 | `molecule_viewer` | Molecule Viewer | `plus` | viewer_tools | 2 | python_interpreter, think, plan, skill, memory |
| 10 | `pathology_lazyslide` | Pathology — LazySlide | `plus` | viewer_tools | 6 | file_manager, python_interpreter, shell, plan, think, task, skill, memory |
| 11 | `clinical_translator_free` | Clinical Translator Free | `community` | scientific_writing | 4 | file_manager, web, plan, think, task, skill, memory |
| 12 | `clinical_translator_pro` | Clinical Translator Pro | `pro` | scientific_writing | 10 | file_manager, web, plan, think, task, skill, memory |
| 13 | `humanize` | Humanize | `community` | scientific_writing | 3 | file_manager, think, task, memory |
| 14 | `literature_free` | Literature Free | `community` | scientific_writing | 6 | file_manager, web, plan, think, task, skill, memory |
| 15 | `literature_pro` | Literature Pro | `pro` | scientific_writing | 9 | file_manager, web, plan, think, task, skill, memory |
| 16 | `paper_critic` | Paper Critic | `community` | scientific_writing | 7 | file_manager, web, plan, think, task, memory |
| 17 | `quality_review` | Quality Review | `community` | scientific_writing | 8 | file_manager, think, task, memory |
| 18 | `scientific_writer` | Scientific Writer | `community` | scientific_writing | 21 | file_manager, shell, web, plan, think, task, memory, image_gen |
| 19 | `single_cell_annotator_pro` | Single-cell Annotator Pro | `pro` | single_cell_analysis | 9 | file_manager, python_interpreter, omicverse_lookup, plan, think, task, skill, memory |
| 20 | `he_to_st_predictor` | H&E → ST Predictor | `pro` | spatial_analysis | 8 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory |
| 21 | `spatial_epigenomics_analyst` | Spatial Epigenomics Analyst | `pro` | spatial_analysis | 13 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory |
| 22 | `bulk_rna_analyst` | Bulk RNA-seq Analyst | `community` | general_omics_analysis | 19 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory |
| 23 | `review_writer_pro` | Review Writer Pro | `pro` | scientific_writing | 16 | file_manager, web, plan, think, task, skill, memory |
| 24 | `single_cell_annotator_free` | Single-cell Annotator Free | `community` | single_cell_analysis | 5 | file_manager, python_interpreter, omicverse_lookup, plan, think, task, skill, memory |
| 25 | `metabolomics_analyst_pro` | Metabolomics Analyst Pro | `pro` | general_omics_analysis | 13 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory |
| 26 | `single_cell_epigenomics_analyst` | Single-Cell Epigenomics Analyst | `pro` | single_cell_analysis | 13 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory |
| 27 | `microbiome_analyst_pro` | Microbiome Analyst Pro | `pro` | general_omics_analysis | 12 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory |
| 28 | `proteomics_analyst_pro` | Proteomics Analyst Pro | `pro` | general_omics_analysis | 12 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory |
| 29 | `single_cell_downstream_analyst_pro` | Single-cell Downstream Analyst Pro | `pro` | single_cell_analysis | 12 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory |
| 30 | `immune_repertoire_analyst_pro` | Immune Repertoire Analyst Pro | `pro` | general_omics_analysis | 12 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory |
| 31 | `tabular_genomics_analyst` | Tabular Genomics Analyst | `pro` | general_omics_analysis | 12 | file_manager, python_interpreter, shell, plan, think, task, skill, memory |
| 32 | `single_ev_analyst_pro` | Single-EV Proteomics Analyst Pro | `pro` | general_omics_analysis | 10 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory |
| 33 | `statistical_genetics_analyst` | Statistical Genetics Analyst | `plus` | general_omics_analysis | 9 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory |
| 34 | `survey_epidemiology_analyst` | Survey Epidemiology Analyst | `plus` | general_omics_analysis | 8 | file_manager, python_interpreter, shell, plan, think, task, skill, memory |
| 35 | `ihc_if_quantifier` | IHC/IF Quantifier | `plus` | general_omics_analysis | 1 | file_manager, python_interpreter, plan, think, task, skill, memory |
| 36 | `phase_separation_analyst` | Phase Separation Analyst | `plus` | general_omics_analysis | 7 | file_manager, python_interpreter, shell, plan, think, task, skill, memory |
| 37 | `bulk_epigenomics_analyst` | Bulk Epigenomics Analyst | `pro` | general_omics_analysis | 14 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory |
| 38 | `memory_curator` | Memory Curator | `community` | orchestration | 1 | memory, think |
| 39 | `analysis_sanity_review` | Analysis Sanity Review | `community` | single_cell_analysis | 1 | file_manager, python_interpreter, think, task, memory |
| 40 | `chromatin_3d_analyst` | Chromatin 3D Genome Analyst | `pro` | general_omics_analysis | 9 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory |
| 41 | `cancer_dependency_analyst` | Cancer Dependency Analyst | `pro` | general_omics_analysis | 14 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory |
| 42 | `c3ca_phase_runner` | c3CA Phase Runner | `lab` | single_cell_analysis | 2 | file_manager, python_interpreter, shell |
| 43 | `cell_cell_communication_free` | Cell-cell Communication Free | `community` | single_cell_analysis | 1 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, team |
| 44 | `cell_cell_communication_pro` | Cell-cell Communication Pro | `pro` | single_cell_analysis | 2 | file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory, team |
| 45 | `cellchat_rust_h5ad_runner` | CellChat Rust H5AD Runner | `lab` | single_cell_analysis | 2 | file_manager, python_interpreter, shell, plan, think, task, skill, memory, team |
| 46 | `single_cell_trajectory_free` | Single-cell Trajectory Free | `community` | single_cell_analysis | 3 | file_manager, python_interpreter, shell, omicverse_lookup, skill, team, plan, think, task |
| 47 | `single_cell_trajectory_pro` | Single-cell Trajectory Pro | `pro` | single_cell_analysis | 5 | file_manager, python_interpreter, shell, omicverse_lookup, skill, team, plan, think, task, memory |
| 48 | `single_cell_grn_analyst` | Single-cell GRN Analyst | `pro` | single_cell_analysis | 7 | file_manager, python_interpreter, shell, omicverse_lookup, skill, team, plan, think, task |
| 49 | `single_cell_perturbation_analyst` | Single-cell Perturbation Analyst | `pro` | single_cell_analysis | 10 | file_manager, python_interpreter, shell, omicverse_lookup, skill, team, plan, think, task, memory |
| 50 | `nvidia_bionemo_nim` | NVIDIA BioNeMo NIM | `plus` | structural_biology | 1 | file_manager, python_interpreter, plan, think, skill, memory |
| 51 | `phylogenomics_analyst` | Phylogenomics Analyst | `plus` | phylogenomics | 9 | file_manager, python_interpreter, shell, notebook, omicverse_lookup, team, plan, think, task, skill, memory |
| 52 | `binder_designer` | Binder Designer | `plus` | structural_biology | 8 | file_manager, python_interpreter, plan, think, task, skill, memory |
| 53 | `variant_analyst` | Variant Analyst | `plus` | structural_biology | 4 | file_manager, python_interpreter, plan, think, task, skill, memory |
| 54 | `antibody_engineer` | Antibody Engineer | `plus` | structural_biology | 6 | file_manager, python_interpreter, plan, think, task, skill, memory |
| 55 | `structural_biologist` | Structural Biologist | `plus` | structural_biology | 5 | file_manager, python_interpreter, plan, think, task, skill, memory |
| 56 | `primer_design_assistant` | Primer Design Assistant | `community` | molecular_biology | 4 | file_manager, python_interpreter, plan, think, task, skill, memory |
| 57 | `reviewer` | Reviewer | `community` | general_omics_analysis | 0 | file_manager, python_interpreter, think |

## Agent 到 Skill 绑定

### OmicVerse Omni (`omicverse_omni`)

- tier：`community`
- category：`orchestration`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `notebook`, `omicverse_lookup`, `skill`, `team`, `web`, `plan`, `schedule`, `background`, `think`, `task`, `memory`, `vision`, `image_gen`
- skills：``
- use_when：组学专科之外的各类通用计算与分析任务——通用编程与脚本、数据清洗与格式转换、文件与网页处理、网络爬取、文档（docx/pdf 等）生成、以及需要跨多步骤/多工具串联的综合性分析；也用于不确定该交给哪个专科、需要一个能在多任务之间无缝切换的通用入口时

### Vertical Agent Selector (`vertical_agent_selector`)

- tier：`community`
- category：`orchestration`
- toolsets：`team`
- skills：``
- use_when：作为默认入口，把应当交给某个 manifest 注册的垂直 agent 处理的请求分派出去

### GEO Everything (`GEO-everything`)

- tier：`pro`
- category：`data_acquisition`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `web`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`geo-sra-search`, `geo-metadata-fetch`, `sra-fastq-download`, `dataset-linkout`, `data-io-loading`, `gene-id-conversion`, `report-html-generation`
- use_when：想从 NCBI GEO / SRA / ENA / DDBJ / GSA 拉公共数据 —— 入口可以是关键词、GSE/GSM/SRR/PRJNA accession、或一篇论文的 DOI / PMID;做的是搜索数据集、解析样本元数据、下载 FASTQ/补充文件、按论文反查 accession。NOT-FOR(数据落地之后的分析不归本 agent):不做 scRNA/10x 的 QC / 归一化 / HVG / PCA / 整合 / 聚类 / 注释(这条链给 single_cell_preprocessor,它再串注释与下游)、不做 bulk 差异表达(→ bulk_rna_analyst)、不做空间下游(→ spatial_omics_orchestrator);本 agent 的职责终点是"FASTQ 落盘 + 样本表解析成 AnnData + 下载报告",随后交棒。若落地的是单细胞**原始 FASTQ**(还没有 gene×cell 矩阵):10x 液滴走 `single-cell-kb-alignment`、plate-based Smart-seq2/3 走 `single-cell-smartseq-quantification` 先比对定量成矩阵,再进 `single_cell_preprocessor`。

### Analysis Strategist (`analysis_strategist`)

- tier：`pro`
- category：`orchestration`
- toolsets：`file_manager`, `python_interpreter`, `omicverse_lookup`, `skill`, `team`, `plan`, `think`, `task`, `memory`
- skills：``
- use_when：拿到一份(或多份)新数据,想问"这份数据能回答什么 / 怎么分析才最有信息量",并且愿意接受非传统的、跨阶段拼装的分析路线 —— 例如 scRNA + 代谢通量 + 拟时序联合,scATAC + scRNA + peak-to-gene + 谱系演化,bulk + 微生物 + 配对代谢联合,空间 + 反卷积 + 邻接细胞通讯。不是已经知道要跑什么管线了 —— 那种走对应专科 agent;这里专门处理"该跑什么"。

### Single-cell Preprocessor (`single_cell_preprocessor`)

- tier：`plus`
- category：`single_cell_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`single-cell-kb-alignment`, `single-cell-smartseq-quantification`, `data-io-loading`, `rds-qs-seurat-ingestion`, `gene-id-conversion`, `single-cell-preprocessing`, `single-cell-ambient-rna`, `single-cell-batch-integration`, `single-cell-clustering-backends`, `single-cell-composition`, `single-cell-pseudobulk`, `single-cell-genemodule`, `gsea-enrichment`, `single-cell-publication-plots`, `single-cell-report-authoring`, `report-html-generation`, `notebook-export`, `office-tools`
- use_when：拿到 raw / 已 QC 的 scRNA-seq AnnData，要清洗 + 标准化 + 聚类 + 取 marker，输出 ready-to-annotate 的 adata.h5ad。若手上只有原始 FASTQ 还没有矩阵：带 barcode+UMI 的液滴/微孔化学（10x、Drop-seq、inDrops、CEL-seq、SPLiT-seq 等）先走 single-cell-kb-alignment、plate-based Smart-seq2/3 先走 single-cell-smartseq-quantification 比对定量成矩阵，再回到本流水线

### Spatial Omics Orchestrator (`spatial_omics_orchestrator`)

- tier：`pro`
- category：`spatial_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`spatial-data-io-loading`, `spatial-domain-detection`, `spatial-variable-genes`, `spatial-deconvolution`, `spatial-publication-plots`, `gene-id-conversion`, `report-html-generation`, `notebook-export`, `office-tools`
- use_when：拿到 SpaceRanger outs/ 或空间 .h5ad，要做 tissue domain 检测、空间可变基因、scRNA 参考反卷积、空间出图（细胞通讯 / 多切片整合见 Phase 2）

### Cell Viewer (`cell_viewer`)

- tier：`plus`
- category：`viewer_tools`
- toolsets：`python_interpreter`, `think`, `plan`, `skill`, `memory`
- skills：`cell-viewer-viz`
- use_when：用户在 OmicOS「细胞查看器」里、已选中一个内核 AnnData(默认 `adata`），想要任何一类： - 直接改变中间的实时散点图：按 obs 列 / 基因着色、高亮某些细胞类型并把其余调暗、切换 UMAP/tSNE/PCA、调点大小 / 透明度 / 调色板 - 在共享内核里对 adata 跑分析：QC、标准化、HVG、PCA、邻接、UMAP/tSNE、Leiden/Louvain、marker 基因 重点：凡是"在图上显示 / 着色 / 高亮"——用 `cellviz` 命令驱动**实时散点图**,不要退回画静态 matplotlib 图。

### ImageJ (`imagej`)

- tier：`plus`
- category：`viewer_tools`
- toolsets：`think`, `plan`, `skill`, `memory`
- skills：`imagej-macro-analysis`
- use_when：用户在 OmicOS「ImageJ」标签里、右侧已打开一张图像,想做图像处理或定量分析: - 预处理 / 滤波（高斯、中值、背景扣除、位深转换、边缘） - 阈值分割（setAutoThreshold + Convert to Mask + Watershed） - 颗粒分析（计数 / 面积 / 形状 / 尺寸分布） - 强度 / ROI 测量（均值 / 最值 / 积分密度 / 面积占比） - 标尺标定（Set Scale）、栈处理（Z 投影 / 通道拆分） 纯前端 ImageJ.JS,**不用 Python**;每次只给一个 ```ijm 宏块,并在宏末尾 `return` 结果串。

### Molecule Viewer (`molecule_viewer`)

- tier：`plus`
- category：`viewer_tools`
- toolsets：`python_interpreter`, `think`, `plan`, `skill`, `memory`
- skills：`molecule-viewer-commands`, `molecule-structure-analysis`
- use_when：用户在 OmicOS「分子查看器」里、已经加载了一个 3D 结构（蛋白 / 复合物 / 配体，PDB / mmCIF； 内核镜像变量名 `_omicos_pdb`），想要其中任何一类： - 用命令控制 3D 视图：显示样式 (cartoon/stick/sphere/surface…)、着色、按布尔选择高亮、聚焦、测距 / 角度 / 二面角、表面、标注残基 - 结合位点 / 口袋：找配体 (hetatm)、配体周围 X Å 的残基 (byres within)、接触 - 链-链界面：界面残基、氢键、埋藏面积 - 结构性质：分子量、链 / 残基组成、二级结构比例、SASA、几何 - 配体化学信息 (rdkit) 如果用户要 "折叠序列 / 预测复合物结构 / 小分子对接打分" —— 路由到 `structural_biologist`。

### Pathology — LazySlide (`pathology_lazyslide`)

- tier：`plus`
- category：`viewer_tools`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`pathology-lazyslide-he-analysis`, `pathology-lazyslide-cell-segmentation`, `pathology-lazyslide-supervised-classification`, `pathology-lazyslide-survival-prediction`, `pathology-lazyslide-he-transcriptomics-integration`, `pathology-lazyslide-virtual-staining`
- use_when：用户带 H&E 全切片 (svs/tiff/ndpi/ome.tif) 想做下列任何一类： - 直接形态学 + 报告 (tile FM + zero-shot, 单切片) → pathology-lazyslide-he-analysis - 细胞级实例分割 + 细胞类型 → pathology-lazyslide-cell-segmentation - 已知 slide-level 标签的有监督分类 (subtype / response / grade) → pathology-lazyslide-supervised-classification - 队列生存预测 (time-to-event, censoring) → pathology-lazyslide-survival-prediction - 配对 H&E + RNA-seq 关联分析 (RNALinker) → pathology-lazyslide-he-transcriptomics-integration - 虚拟染色 (生成 IHC/IF 通道) → pathology-lazyslide-virtual-staining 如果用户要从 H&E 像素直接"预测基因表达"——路由到 `he_to_st_predictor`。 如果已经有空转 AnnData 做下游——路由到 `spatial_omics_orchestrator`。

### Clinical Translator Free (`clinical_translator_free`)

- tier：`community`
- category：`scientific_writing`
- toolsets：`file_manager`, `web`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`clinical-trial-check`, `gene-lookup`, `retraction-check`, `dosage-calc`
- use_when：拿到 DEG 列表或候选基因后，想快速知道临床上已经在做什么 —— 用大众都知道的免费数据库

### Clinical Translator Pro (`clinical_translator_pro`)

- tier：`pro`
- category：`scientific_writing`
- toolsets：`file_manager`, `web`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`clinical-trial-check`, `gene-lookup`, `retraction-check`, `dosage-calc`, `target-druggability-pro`, `pharmacogenomics-pro`, `adverse-events-pro`, `variant-pathogenicity-pro`, `pathway-clinical-pro`, `disease-gene-association-pro`
- use_when：拿到一份组学分析的具体结果（DEG 列表 / 候选基因 / 富集的 cell type / pathway / 变异 / 临床表型），要把它写成临床或转化语言 —— "mechanistic origins" 段落（recruitment / in-situ adaptation / tissue residency 的解读）、"translational implications" / "therapeutic implications" / "clinical relevance" 段落（治疗靶点、可成药性、临床试验覆盖、生物标志物含义）、CPIC 基因型剂量、FAERS 不良事件信号、变异群体频率。任何分析报告 (trace.md / REPORT.md / Discussion 节) 里需要"clinical / translational / therapeutic / mechanistic"风味的子节都是这里。

### Humanize (`humanize`)

- tier：`community`
- category：`scientific_writing`
- toolsets：`file_manager`, `think`, `task`, `memory`
- skills：`humanize-academic`, `scientific-critical-thinking`, `scientific-manuscript-writing`
- use_when：scientific_writer 给出初稿后，准备投稿前的最后润色

### Literature Free (`literature_free`)

- tier：`community`
- category：`scientific_writing`
- toolsets：`file_manager`, `web`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`literature-search-free`, `fulltext-free`, `retraction-check`, `source-comparison`, `preprint-monitoring`, `citation-management`
- use_when：开新课题摸清领域现状、找论文读、查一篇文献可信度 —— 用大众都知道的免费 API。NOT-FOR:不是数据分析 / 作图 / 组学分析任务(→ 对应分析专家);本 agent 只做文献检索 / 取全文 / 撤稿核查 / 多源对比。

### Literature Pro (`literature_pro`)

- tier：`pro`
- category：`scientific_writing`
- toolsets：`file_manager`, `web`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`literature-search-free`, `literature-search-pro`, `fulltext-free`, `fulltext-pro`, `retraction-check`, `source-comparison`, `preprint-monitoring`, `citation-management`, `dataset-linkout`
- use_when：要最全的文献覆盖、引用网络遍历、AI 相关性排序、按全文内容建语料 —— 同样免费 API，但榨到底。NOT-FOR:不是数据分析 / 作图 / scRNA / bulk / 空间 / 统计分析任务(那些路由到对应分析专家);本 agent 只做文献发现、引用图遍历与全文挖掘。

### Paper Critic (`paper_critic`)

- tier：`community`
- category：`scientific_writing`
- toolsets：`file_manager`, `web`, `plan`, `think`, `task`, `memory`
- skills：`paper-code-audit`, `replication`, `statistics-check`, `peer-review`, `office-tools`, `retraction-check`, `fulltext-free`
- use_when：拿到一篇他人论文（PDF / arXiv / GitHub），想做严格的批评而非摘要

### Quality Review (`quality_review`)

- tier：`community`
- category：`scientific_writing`
- toolsets：`file_manager`, `think`, `task`, `memory`
- skills：`section-checklist`, `peer-review-methodology`, `statistics-check`, `retraction-check`, `citation-management`, `fulltext-free`, `scientific-critical-thinking`, `scientific-manuscript-writing`
- use_when：自己写完稿子，准备投出去之前的最后一道关卡

### Scientific Writer (`scientific_writer`)

- tier：`community`
- category：`scientific_writing`
- toolsets：`file_manager`, `shell`, `web`, `plan`, `think`, `task`, `memory`, `image_gen`
- skills：`paper-rendering`, `figure-programmatic`, `scientific-manuscript-writing`, `office-tools`, `manuscript-docx-review`, `citation-management`, `fulltext-free`, `systematic-review-method`, `latex-research-posters`, `scientific-slides`, `scientific-schematics`, `peer-review-methodology`, `general-figure-guide`, `nature-figure-guide`, `science-figure-guide`, `cell-figure-guide`, `pnas-figure-guide`, `elife-figure-guide`, `nejm-figure-guide`, `lancet-figure-guide`, `cancer-research-figure-guide`
- use_when：拿到 DEG / 图 / 队列数据 / 实验结果 / 论文 PDF / Markdown / LaTeX / DOCX，要写成稿件、DOCX/PDF、公式算法文档、figure 或幻灯片

### Single-cell Annotator Pro (`single_cell_annotator_pro`)

- tier：`pro`
- category：`single_cell_analysis`
- toolsets：`file_manager`, `python_interpreter`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`celltype-annotation-pro`, `single-cell-preprocessing`, `gene-id-conversion`, `single-cell-composition`, `single-cell-publication-plots`, `single-cell-report-authoring`, `report-html-generation`, `office-tools`, `notebook-export`
- use_when：拿到已聚类的 AnnData (`scmarker_preprocessor` 输出 / 任何带 `leiden`/`louvain` 的 .h5ad)，要给每个 cluster 标 cell type，并要可审计的文献证据

### H&E → ST Predictor (`he_to_st_predictor`)

- tier：`pro`
- category：`spatial_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`spatial-he-to-st-prediction`, `spatial-data-io-loading`, `spatial-publication-plots`, `spatial-variable-genes`, `gene-id-conversion`, `report-html-generation`, `notebook-export`, `office-tools`
- use_when：拿到一张 H&E 全切片 (svs/tiff/ndpi/ome.tif) 想推空间基因表达 —— 没有 Visium 用 STPath 零样本，有配对 Visium 用 HEST-FM/STFlow，要 sub-spot 超分用 iStar

### Spatial Epigenomics Analyst (`spatial_epigenomics_analyst`)

- tier：`pro`
- category：`spatial_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`spatial-epigenomics`, `spatial-multisample-integration`, `spatial-pseudobulk`, `spatial-data-io-loading`, `spatial-domain-detection`, `spatial-publication-plots`, `scatac-chromvar`, `scatac-peak-to-gene`, `tf-footprinting`, `gene-id-conversion`, `report-html-generation`, `notebook-export`, `office-tools`
- use_when：拿到空间分辨的染色质可及性数据 —— AtlasXomics 空间 ATAC / DBiT-seq、tixel×peak 或 tixel×gene-activity 矩阵（带 obsm['spatial'] 坐标），或 fragments + 空间 barcode 布局 —— 要做 QC、降维聚类、空间域、基因活性、chromVAR 转录因子活性、跨切片整合，或样本组间差异可及性/motif 活性。不是 scRNA 空间表达（→ spatial_omics_orchestrator），不是非空间 scATAC（→ single_cell_epigenomics_analyst），不是 bulk ATAC/ChIP（→ bulk_epigenomics_analyst）。

### Bulk RNA-seq Analyst (`bulk_rna_analyst`)

- tier：`community`
- category：`general_omics_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`gene-id-conversion`, `data-io-loading`, `data-cleaning`, `sample-metadata-alignment`, `tcga-preprocessing`, `survival-analysis`, `bulk-combat-correction`, `bulk-deg-analysis`, `time-course-analysis`, `multi-omics-integration`, `sample-clustering`, `gsea-enrichment`, `bulk-wgcna-analysis`, `bulk-stringdb-ppi`, `bulk-celltype-deconvolution`, `bulk-to-single-deconvolution`, `report-html-generation`, `notebook-export`, `office-tools`
- use_when：拿到 bulk RNA-seq 表达矩阵(genes × samples,counts/TPM)、多批次队列、TCGA、FASTQ —— 需要你从这个矩阵建模 / 推导。"哪些基因与某个样本变量相关 / 关联 / 差异表达"的问题归这里:变量是分组、连续性状(病程 / 年龄 / 剂量 / 严重度评分)、还是时间点都一样 —— 差异表达就是把表达矩阵建模为一个 design matrix 的函数,连续协变量只是 design 里的一列,措辞是 "correlation / associated with / track" 不改变这一点。**关键判据:输入确实是一个基因 × 样本的表达矩阵、分析要从中建模。** 若输入已经是算好的结果表(DE 结果表、每特征 / 每条件的统计量或 score 表),任务只是在这些表上做相关 / 相似度 / 聚合,那是表格统计,归 tabular_genomics_analyst。也做富集 / 共表达网络 / 报告。

### Review Writer Pro (`review_writer_pro`)

- tier：`pro`
- category：`scientific_writing`
- toolsets：`file_manager`, `web`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`literature-search-free`, `literature-search-pro`, `fulltext-free`, `fulltext-pro`, `preprint-monitoring`, `retraction-check`, `source-comparison`, `dataset-linkout`, `literature-review-synthesis`, `systematic-review-method`, `citation-management`, `scientific-manuscript-writing`, `manuscript-docx-review`, `figure-programmatic`, `scientific-schematics`, `paper-rendering`
- use_when：用户要写一篇文献综述 / 叙述性或系统 review —— "帮我写一篇关于 X 的综述""博士要三篇综述,先写 X""把这个领域近五年进展综述一下""给定这批参考文献整合成 review"。区别于 scientific_writer(写单篇研究论文 results/methods),这里是 综述 全流程;区别于 literature_pro(只检索,不成稿)

### Single-cell Annotator Free (`single_cell_annotator_free`)

- tier：`community`
- category：`single_cell_analysis`
- toolsets：`file_manager`, `python_interpreter`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`celltype-anno-ov-free`, `single-cell-clustering-backends`, `gene-id-conversion`, `office-tools`, `notebook-export`
- use_when：拿到已 cluster 的 .h5ad，要快速给每个 cluster 标 cell type，又不想付费 / 不需要 PMID 级证据

### Metabolomics Analyst Pro (`metabolomics_analyst_pro`)

- tier：`pro`
- category：`general_omics_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`bulk-metabol-preprocessing`, `bulk-metabol-multivariate`, `bulk-metabol-pathway-multifactor`, `bulk-metabol-untargeted-lipidomics`, `micro-metabol-paired`, `gene-id-conversion`, `data-io-loading`, `figure-programmatic`, `single-cell-report-authoring`, `report-html-generation`, `notebook-export`, `office-tools`, `retraction-check`
- use_when：拿到代谢组学 peak intensity 表（MetaboAnalyst CSV / LC-MS / NMR / lipidomics）/ 多 batch 队列 / 配对 microbe-metabolite 数据，要跑预处理 + 统计 + 通路 + 出报告

### Single-Cell Epigenomics Analyst (`single_cell_epigenomics_analyst`)

- tier：`pro`
- category：`single_cell_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`scatac-preprocessing`, `scatac-chromvar`, `scatac-peak-to-gene`, `scatac-integration`, `tf-footprinting`, `gsea-enrichment`, `gene-id-conversion`, `data-io-loading`, `figure-programmatic`, `single-cell-publication-plots`, `report-html-generation`, `notebook-export`, `office-tools`
- use_when：拿到单细胞 ATAC-seq 数据 —— fragments 文件、10x scATAC 输出、cell×peak 或 cell×tile 矩阵 —— 要做 QC、降维聚类、基因活性打分、簇级 call peak、chromVAR 转录因子活性、peak-to-gene 调控连接、多样本整合或从 scRNA 迁移细胞类型标签。不是 bulk ATAC/ChIP/CUT&RUN(→ bulk_epigenomics_analyst),不是单细胞 Hi-C(→ chromatin_3d_analyst),不是 scRNA 表达分析(→ single_cell 注释类 agent)。

### Microbiome Analyst Pro (`microbiome_analyst_pro`)

- tier：`pro`
- category：`general_omics_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`microbiome-16s-amplicon-dada2`, `microbiome-phylogeny`, `microbiome-da-comparison`, `microbiome-meta-analysis`, `micro-metabol-paired`, `data-io-loading`, `figure-programmatic`, `single-cell-report-authoring`, `report-html-generation`, `notebook-export`, `office-tools`, `retraction-check`
- use_when：拿到 16S 测序 (raw FASTQ 或已有 ASV/OTU 表) / 多 cohort 16S / 配对 microbe-metabolite 数据，要跑多样性 + 差异丰度 + 通路 / 元分析 + 出报告。仅限 16S / ITS / 18S 扩增子;NOT-FOR:shotgun / 全基因组 宏基因组(Kraken2 / Bracken / MetaPhlAn / HUMAnN / MAG 组装·分箱)不在本 agent 范围,不要把这类任务路由到这里(目前平台无 shotgun 落点 —— 应向用户说明,而非接下只能 plan-不能-run)。

### Proteomics Analyst Pro (`proteomics_analyst_pro`)

- tier：`pro`
- category：`general_omics_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`bulk-proteomics`, `multi-omics-integration`, `gsea-enrichment`, `gene-id-conversion`, `data-io-loading`, `data-cleaning`, `figure-programmatic`, `single-cell-report-authoring`, `report-html-generation`, `notebook-export`, `office-tools`, `retraction-check`
- use_when：拿到蛋白丰度矩阵(MaxQuant proteinGroups / DIA-NN report / FragPipe combined_protein / Olink NPX / 通用 protein×sample 表),或肽段级 MSstats 长表,要做 QC、缺失值处理、差异表达、通路富集、出报告

### Single-cell Downstream Analyst Pro (`single_cell_downstream_analyst_pro`)

- tier：`pro`
- category：`single_cell_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`single-cell-metabolism-inference`, `single-cell-composition`, `single-cell-genemodule`, `single-cell-pseudobulk`, `geneset-scoring`, `gsea-enrichment`, `gene-id-conversion`, `single-cell-publication-plots`, `single-cell-report-authoring`, `report-html-generation`, `notebook-export`, `office-tools`
- use_when：已经有 QC 过 + 已注释的 scRNA-seq AnnData（cell-type 列填好），要做"注释完之后"的功能/差异分析；GRN/SCENIC 请走 single_cell_grn_analyst，基因/RegVelo 扰动请走 single_cell_perturbation_analyst，细胞通讯请走 cell_cell_communication_*，pseudotime 请走 single_cell_trajectory_*

### Immune Repertoire Analyst Pro (`immune_repertoire_analyst_pro`)

- tier：`pro`
- category：`general_omics_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`airr-singlecell`, `airr-bulk`, `airr-bcr-immcantation`, `airr-tcr-specificity`, `airr-tcr-gex`, `data-io-loading`, `figure-programmatic`, `single-cell-report-authoring`, `report-html-generation`, `notebook-export`, `office-tools`, `retraction-check`
- use_when：拿到 TCR / BCR 测序 (10x V(D)J、AIRR rearrangement、bulk repertoire 表)，要跑克隆型 / 多样性 / 体细胞超突变 / 谱系树 / TCR 特异性分组 / 与转录组联合分析并出报告

### Tabular Genomics Analyst (`tabular_genomics_analyst`)

- tier：`pro`
- category：`general_omics_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`tabular-association-analysis`, `somatic-mutation-analysis`, `survival-analysis`, `multi-omics-integration`, `gene-id-conversion`, `data-io-loading`, `data-cleaning`, `gsea-enrichment`, `figure-programmatic`, `report-html-generation`, `notebook-export`, `office-tools`
- use_when：拿到 tidy 数据表、直接在表上做统计 —— 临床表型表、per-sample 标量汇总(纯度 / 评分 / 签名分数等单值列)、MAF/突变表,**或已经算好的结果表(DE 结果表、每特征 / 每条件 / 每组织的统计量或 score 表)**。做关联 / 相关 / 偏相关检验、交互效应、亚组比例;**跨集合 / 跨条件的相关与相似度(overlap / Jaccard)及其聚合**;体细胞突变的频率 / TMB / 富集 / 共现 / 通路聚合。**关键判据:输入本身就是表格、你直接在表上统计,不需要从一个基因 × 样本表达矩阵建模。** 一个**整个表达矩阵(数千基因 × 样本)**的基因-性状关联**不归这里** —— 即使措辞是"哪些基因与 X 相关",只要输入是表达矩阵、要从中推导差异表达,那是 RNA-seq 任务,交给 bulk_rna_analyst。也不是 counts 矩阵的差异表达,不是单变异功能效应预测。**也不是 DNA 甲基化 / 表观基因组的区域分析** —— per-CpG 甲基化 beta 矩阵、差异甲基化(DMC/DMR)、启动子 / 基因体 / enhancer / CpG island 的甲基化、或甲基化随基因组距离的分布,需要基因组坐标 / 区域注释 / 表观遗传学判断(enhancer 用激活标记而非抑制标记、覆盖度过滤等),即使输入是 (chr,start)×样本的矩阵或多组学整合也不归这里,交给 bulk_epigenomics_analyst。

### Single-EV Proteomics Analyst Pro (`single_ev_analyst_pro`)

- tier：`pro`
- category：`general_omics_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`single-ev-proteomics`, `single-cell-preprocessing`, `gsea-enrichment`, `data-io-loading`, `figure-programmatic`, `single-cell-report-authoring`, `report-html-generation`, `notebook-export`, `office-tools`, `retraction-check`
- use_when：拿到单个外泌体/EV 分辨率的蛋白测量 (每行=一个囊泡，不是 bulk EV 制备)，要做质控、污染评估、MISEV 标记、单囊泡归一、亚群聚类、共定位、差异分析并出报告

### Statistical Genetics Analyst (`statistical_genetics_analyst`)

- tier：`plus`
- category：`general_omics_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`gwas-eqtl-analysis`, `gene-id-conversion`, `data-io-loading`, `sample-metadata-alignment`, `gsea-enrichment`, `figure-programmatic`, `report-html-generation`, `notebook-export`, `office-tools`
- use_when：拿到 GWAS summary statistics、基因型数据(PLINK .bed/.bim/.fam、VCF、dosage 矩阵),或要做 eQTL 定位、精细定位(credible set / PIP)、GWAS 与 eQTL 共定位、孟德尔随机化(暴露→结局的因果)、TWAS、SNP 遗传力 / 遗传相关(LD score regression)、scDRS 找疾病相关细胞类型。不是体细胞 / 癌症突变表的频率·富集分析(→ tabular_genomics_analyst),不是蛋白氨基酸突变的功能 / 致病效应(→ variant_analyst),不是表达矩阵的差异表达(→ bulk_rna_analyst)。

### Survey Epidemiology Analyst (`survey_epidemiology_analyst`)

- tier：`plus`
- category：`general_omics_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`complex-survey-analysis`, `survival-analysis`, `tabular-association-analysis`, `data-io-loading`, `data-cleaning`, `figure-programmatic`, `report-html-generation`, `notebook-export`
- use_when：拿到任何**复杂抽样调查 / 全国健康调查**数据(NHANES、BRFSS、NHIS、MEPS、CHARLS、CHNS、CLHLS、KNHANES、DHS、SHARE/ELSA 等),做暴露↔结局关联、加权患病率或死亡分析 —— 多周期/多波合并、**按抽样设计加权(权重 + 分层 strata + PSU/cluster)**、加权回归(线性/logistic/Cox)、剂量反应 RCS、环境混合暴露(WQS/qgcomp)、亚组交互、中介、加权 Kaplan-Meier、敏感性。典型词:NHANES、CHARLS、抽样权重、WTMEC2YR、SDMVSTRA、SDMVPSU、_LLCPWT、v005、survey-weighted、加权患病率、PhenoAge/生物学年龄、PFAS/重金属暴露组。**关键判据:数据来自复杂概率抽样、必须做 design-based 推断(权重 + 分层 + PSU)。边界:** 不是表达矩阵差异表达(→ bulk_rna_analyst);不是 GWAS / eQTL / 孟德尔随机化 / 遗传力(→ statistical_genetics_analyst);**不是无抽样设计的普通 tidy 表关联**(直接 corr/回归、无需设计加权的 → tabular_genomics_analyst);**不是空间转录组的 tissue domain / niche / 邻域(neighborhood)/ 细胞通讯分析** —— 这里的"domain / 亚组 / 交互"指抽样调查里的 analytic 子人群与统计交互项,不是组织空间域或空间生态位(空间域 / niche → spatial_omics_orchestrator;单细胞 niche / 通讯 → single_cell_downstream_analyst_pro)。

### IHC/IF Quantifier (`ihc_if_quantifier`)

- tier：`plus`
- category：`general_omics_analysis`
- toolsets：`file_manager`, `python_interpreter`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`imaging-ihc-if-quantification`
- use_when：用户有常规明场 / 荧光显微图文件(单张或一批 tif / png / ome-tif,**不是** svs / ndpi 全玻片),要定量染色:IHC DAB 棕染阳性百分比 / H-score / Allred,或多通道 IF 的通道分离 + 核分割 + 每细胞阳性比例 + 通道共定位(Pearson / Manders)。NOT-FOR:不是 ImageJ 标签页里实时单图的宏分析(→ imagej)、不是 LazySlide 的 H&E 全玻片基础模型分析或虚拟染色(→ pathology_lazyslide)、不是单细胞 / 空间组学的 AnnData 下游。

### Phase Separation Analyst (`phase_separation_analyst`)

- tier：`plus`
- category：`general_omics_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`phase-separation-analysis`, `gene-id-conversion`, `data-io-loading`, `figure-programmatic`, `report-html-generation`, `notebook-export`, `office-tools`
- use_when：问题涉及液-液相分离(LLPS)、生物分子凝聚体、无膜细胞器 —— 哪些蛋白会相分离、什么序列特征驱动凝聚体形成、相分离预测器的判别表现、自组装(SaPS)vs 伴侣依赖(PdPS)机制差异、IDR / prion-like 域 / 低复杂度域的序列生物物理。不是凝聚体相图的粗粒化 MD 模拟,不是 3D 结构预测,不是单个突变的致病性评分(→ variant_analyst)。

### Bulk Epigenomics Analyst (`bulk_epigenomics_analyst`)

- tier：`pro`
- category：`general_omics_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`bulk-epigenome-upstream`, `differential-peak-analysis`, `dna-methylation-analysis`, `tf-footprinting`, `epigenome-track-visualization`, `gsea-enrichment`, `gene-id-conversion`, `data-io-loading`, `data-cleaning`, `figure-programmatic`, `report-html-generation`, `notebook-export`, `office-tools`, `retraction-check`
- use_when：拿到 bulk 表观基因组数据。两类:(1) 染色质可及性 / 占据 —— ATAC-seq / ChIP-seq / CUT&RUN 的 FASTQ.gz、BAM、narrowPeak 或 bigWig,做上游、call peak、差异 peak、TF 足迹、轨道、motif 富集(走 epione);(2) DNA 甲基化 / WGBS / RRBS —— per-CpG beta 矩阵或 methylation BED/bedGraph(beta 0-1 或 0-100),做区域甲基化(启动子 / 基因体 / enhancer / CpG island)、条件间差异甲基化、或甲基化在某特征周围的空间分布(走标准栈,epione 无甲基化模块)。不是单细胞 ATAC(→ single_cell_epigenomics_analyst),不是 Hi-C(→ chromatin_3d_analyst),不是纯 RNA 表达(→ bulk_rna_analyst)。

### Memory Curator (`memory_curator`)

- tier：`community`
- category：`orchestration`
- toolsets：`memory`, `think`
- skills：`consolidate-memory`
- use_when：记忆变多变乱时想做一次审阅式整理 —— 重复笔记、相互矛盾或过时的事实、应合并的近似笔记、臃肿的索引。不是写新记忆,是整理已有记忆。

### Analysis Sanity Review (`analysis_sanity_review`)

- tier：`community`
- category：`single_cell_analysis`
- toolsets：`file_manager`, `python_interpreter`, `think`, `task`, `memory`
- skills：`office-tools`
- use_when：一段组学分析（注释/整合/差异等）写报告之前，要一个没沾过本次推理的全新视角核对结论是否与数据和已确认身份自洽

### Chromatin 3D Genome Analyst (`chromatin_3d_analyst`)

- tier：`pro`
- category：`general_omics_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`hic-analysis`, `single-cell-hic-analysis`, `gene-id-conversion`, `data-io-loading`, `data-cleaning`, `figure-programmatic`, `report-html-generation`, `notebook-export`, `office-tools`
- use_when：拿到 Hi-C / 三维基因组数据 —— bulk 接触矩阵(.cool/.mcool)、pairs 文件,或单细胞 / droplet Hi-C(.scool、per-cell .cool)—— 要分析基因组三维结构:A/B 区室、TAD 结构域、染色质 loop、接触频率衰减,或单细胞层面的 3D 基因组细胞状态 / 细胞周期。不是 bulk ATAC/ChIP/CUT&RUN(→ bulk_epigenomics_analyst),不是 scATAC(→ single_cell_epigenomics_analyst)。

### Cancer Dependency Analyst (`cancer_dependency_analyst`)

- tier：`pro`
- category：`general_omics_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`cancer-dependency-analysis`, `synthetic-lethality-discovery`, `target-druggability-pro`, `somatic-mutation-analysis`, `tabular-association-analysis`, `gsea-enrichment`, `gene-id-conversion`, `data-io-loading`, `data-cleaning`, `figure-programmatic`, `report-html-generation`, `notebook-export`, `office-tools`, `retraction-check`
- use_when：拿到癌症依赖 / 必需性数据 —— DepMap/CCLE 的 CRISPR/RNAi 必需性评分、患者层面预测依赖评分、突变矩阵 + 多组学 —— 要找某癌种的选择性依赖 / 生物标志物 / 可干预靶点,或预测某 LOF 事件的合成致死伙伴,或判定某一对具名基因是否合成致死(仅给基因名 + 上下文、需自己取依赖数据也可)。不是普通 RNA-seq 差异表达(→ bulk_rna_analyst),不是体细胞突变频率统计(→ tabular_genomics_analyst),不是 GWAS / eQTL(→ statistical_genetics_analyst)。

### c3CA Phase Runner (`c3ca_phase_runner`)

- tier：`lab`
- category：`single_cell_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`
- skills：`rust_nmf`, `sc_c3ca_backend_skill`
- use_when：用于 rust-NMF 3CA 前端各 phase、c3CA 后端 MP-analysis 各 phase、phase 间交接，以及单个 phase 的失败排查

### Cell-cell Communication Free (`cell_cell_communication_free`)

- tier：`community`
- category：`single_cell_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `team`
- skills：`cell-cell-communication-free`
- use_when：用于已注释 scRNA-seq AnnData 的免费版细胞通讯 / 配体-受体分析，CellPhoneDB v5 够用时走这里；不跑 LIANA consensus、LIANA+、CellChat(R) 或手写兜底统计

### Cell-cell Communication Pro (`cell_cell_communication_pro`)

- tier：`pro`
- category：`single_cell_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `plan`, `think`, `task`, `skill`, `memory`, `team`
- skills：`cell-cell-communication`, `cellchat_rust_h5ad`
- use_when：用于 scRNA-seq 的进阶细胞通讯 / 配体-受体分析：LIANA / LIANA+ consensus、CellPhoneDB v5 兜底、按需 CellChat(R)、条件比较、信号通路排序与差异互作图；只用 CellPhoneDB 的免费路径走 cell_cell_communication_free

### CellChat Rust H5AD Runner (`cellchat_rust_h5ad_runner`)

- tier：`lab`
- category：`single_cell_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `plan`, `think`, `task`, `skill`, `memory`, `team`
- skills：`cell-cell-communication`, `cellchat_rust_h5ad`
- use_when：Use for cell-cell / ligand-receptor communication analysis on single-cell RNA-seq — LIANA (Python, ov.single.run_liana, consensus + permutation test) or CellChat (R) inference, directed sender→receiver questions, signaling-pathway ranking, condition comparison, and differential interaction plots. Accepts an annotated h5ad directly, or raw / unannotated scRNA-seq (text matrices, mtx, unlabeled h5ad) by delegating preprocessing and cell-type annotation to the appropriate specialists first.

### Single-cell Trajectory Free (`single_cell_trajectory_free`)

- tier：`community`
- category：`single_cell_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `skill`, `team`, `plan`, `think`, `task`
- skills：`single-cell-trajectory-inference-free`, `single-cell-publication-plots`, `single-cell-report-authoring`
- use_when：用于已准备好的单细胞 AnnData 的免费版拟时序 / 分支分析，PAGA/DPT 或 Monocle 风格轨迹够用时走这里；需要 velocity、CellRank、Palantir、Slingshot、scTour、VIA/StaVIA 或多方法对比，用 single_cell_trajectory_pro

### Single-cell Trajectory Pro (`single_cell_trajectory_pro`)

- tier：`pro`
- category：`single_cell_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `skill`, `team`, `plan`, `think`, `task`, `memory`
- skills：`single-cell-trajectory-inference`, `single-cell-publication-plots`, `single-cell-report-authoring`, `report-html-generation`, `notebook-export`
- use_when：用于进阶轨迹推断：多方法对比、Slingshot/Palantir/scTour/VIA/StaVIA、RNA velocity、CellRank 命运、动态基因或完整轨迹报告；只用 PAGA/Monocle 的免费路径走 single_cell_trajectory_free

### Single-cell GRN Analyst (`single_cell_grn_analyst`)

- tier：`pro`
- category：`single_cell_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `skill`, `team`, `plan`, `think`, `task`
- skills：`single-cell-grn-inference`, `gene-id-conversion`, `geneset-scoring`, `single-cell-publication-plots`, `single-cell-report-authoring`, `report-html-generation`, `notebook-export`
- use_when：用于单细胞基因调控网络推断、TF-靶基因边表、GRNBoost2/GENIE3/RegDiffusion 先验、SCENIC regulon、AUCell/RSS，或为 RegVelo 准备先验 GRN；若要扰动基因或 TF regulon，用 single_cell_perturbation_analyst

### Single-cell Perturbation Analyst (`single_cell_perturbation_analyst`)

- tier：`pro`
- category：`single_cell_analysis`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `omicverse_lookup`, `skill`, `team`, `plan`, `think`, `task`, `memory`
- skills：`single-cell-in-silico-perturbation`, `single-cell-regvelo-perturbation`, `single-cell-grn-inference`, `gene-id-conversion`, `geneset-scoring`, `gsea-enrichment`, `single-cell-publication-plots`, `single-cell-report-authoring`, `report-html-generation`, `notebook-export`
- use_when：用于单细胞 in-silico KO/KD/OE、scTenifoldKnk、CellOracle、RegVelo TF regulon 阻断、调控扰动、velocity 感知扰动或细胞命运效应分析；只做 GRN 推断用 single_cell_grn_analyst

### NVIDIA BioNeMo NIM (`nvidia_bionemo_nim`)

- tier：`plus`
- category：`structural_biology`
- toolsets：`file_manager`, `python_interpreter`, `plan`, `think`, `skill`, `memory`
- skills：`nvidia-bionemo-nim`
- use_when：Use when the user explicitly mentions NVIDIA BioNeMo, NVIDIA NIM, NVIDIA Cloud API, AlphaFold2 NIM, ProteinMPNN NIM, DiffDock NIM, RFdiffusion NIM, MolMIM NIM, or asks whether a workflow actually used NVIDIA / AlphaFold2 / ProteinMPNN.

### Phylogenomics Analyst (`phylogenomics_analyst`)

- tier：`plus`
- category：`phylogenomics`
- toolsets：`file_manager`, `python_interpreter`, `shell`, `notebook`, `omicverse_lookup`, `team`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`phykit-alignment-quality`, `phykit-tree-quality`, `phykit-gene-tree-discordance`, `phykit-trait-history`, `phykit-phylogenetic-signal`, `phykit-trait-ordination`, `phykit-phylogenetic-regression`, `phykit-trait-evolution-models`, `phykit-phylo-visualization`
- use_when：用户提到 multiple sequence alignment / 系统发生树 / phylogeny / phylogenomics / gene tree / species tree / polytomy / rapid radiation / mirror tree / treeness / RCV / LB score / parsimony informative sites / 饱和度 / saturation / MSA 准确性 / sum-of-pairs / column score。或者用户上传了 `.fa` / `.fasta` / `.aln.fa` / `.tre` / `.treefile` / `.newick` 文件请求分析。

### Binder Designer (`binder_designer`)

- tier：`plus`
- category：`structural_biology`
- toolsets：`file_manager`, `python_interpreter`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`protein-hardware-probe`, `protein-binder-design`, `protein-binder-design-lite`, `protein-sequence-design`, `protein-single-chain-fold`, `protein-complex-affinity`, `protein-structure-search`, `protein-antibody-cdr`
- use_when：用户想给一个目标蛋白从零设计 binder（mini-protein / nanobody / antibody / peptide），从 PDB 或 UniProt ID 开始，需要候选 + 预测亲和力 + 评估能否进湿实验

### Variant Analyst (`variant_analyst`)

- tier：`plus`
- category：`structural_biology`
- toolsets：`file_manager`, `python_interpreter`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`protein-hardware-probe`, `protein-variant-effect`, `protein-single-chain-fold`, `protein-structure-search`
- use_when：用户问 "这个突变致病吗" / "score 50 mutations on my protein" / "DMS 之前哪些位点最敏感" / "BRCA1 R175H 在 ClinVar 里有报道吗" / "我的 binder 上每个 cysteine 突变成 serine 会怎样

### Antibody Engineer (`antibody_engineer`)

- tier：`plus`
- category：`structural_biology`
- toolsets：`file_manager`, `python_interpreter`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`protein-hardware-probe`, `protein-antibody-cdr`, `protein-sequence-design`, `protein-single-chain-fold`, `protein-complex-affinity`, `protein-structure-search`
- use_when：用户问 "redesign this mAb's CDR" / "humanize this mouse antibody" / "我的抗体序列有没有 liability" / "score my nanobody candidates against the antigen" / "transfer this paratope to a stable scaffold

### Structural Biologist (`structural_biologist`)

- tier：`plus`
- category：`structural_biology`
- toolsets：`file_manager`, `python_interpreter`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`protein-hardware-probe`, `protein-single-chain-fold`, `protein-structure-search`, `protein-complex-affinity`, `protein-small-molecule-dock`
- use_when：用户问 "fold this sequence" / "what protein is this PDB" / "predict the structure of this complex" / "does this drug bind this protein" / "find proteins like this fold" / "什么 fold 长得像这个

### Primer Design Assistant (`primer_design_assistant`)

- tier：`community`
- category：`molecular_biology`
- toolsets：`file_manager`, `python_interpreter`, `plan`, `think`, `task`, `skill`, `memory`
- skills：`primer-qpcr`, `primer-cloning`, `primer-specificity`, `codon-optimize`
- use_when：必备输入是一条序列身份(基因 symbol / NCBI accession / Ensembl ID / 裸 cDNA·ORF)加一个明确意图(qPCR 验证、克隆进表达载体、或异源表达前的密码子优化);产出"下单即用"的引物对 CSV + 特异性 BLAST 报告。NOT-FOR:不做 sgRNA / CRISPR guide 设计、不做 in-silico 载体连接 / 克隆仿真、不做寡核苷酸报价、不做湿实验验证;也不是 single-cell / 通用数据分析 / 作图任务(那些路由到对应分析专家)。

### Reviewer (`reviewer`)

- tier：`community`
- category：`general_omics_analysis`
- toolsets：`file_manager`, `python_interpreter`, `think`
- skills：``
- use_when：由 review 编排在一次分析回合结束后自动 spawn，传入指向本回合对话记录的指针，用一个没参与过本次推理的全新视角复核结论与产物。不作为根 agent 直接调用、也不承接新分析任务；正常分析请求请路由到对应的专家。
