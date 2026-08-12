# OmicOS Runtime Agent Roster

Source: `/api/agents` and current selector system prompt.

- Runtime API agents: 57
- Selector roster ids found: 57
- Missing from selector vs API: 0
- Extra in selector vs API: 0

## Agents

### GEO-everything
- Name: GEO Everything
- Tier: pro
- Category: data_acquisition
- Summary: GEO / SRA 端到端 —— 搜索、解析元数据、下载 FASTQ、桥接论文 DOI；自动判断从哪一阶段开始
- Skills: geo-sra-search, geo-metadata-fetch, sra-fastq-download, dataset-linkout, data-io-loading, gene-id-conversion, report-html-generation
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, web, plan, think, task, skill, memory
- Use when: 想从 NCBI GEO / SRA / ENA / DDBJ / GSA 拉公共数据 —— 入口可以是关键词、GSE/GSM/SRR/PRJNA accession、或一篇论文的 DOI / PMID;做的是搜索数据集、解析样本元数据、下载 FASTQ/补充文件、按论文反查 accession。NOT-FOR(数据落地之后的分析不归本 agent):不做 scRNA/10x 的 QC / 归一化 / HVG / PCA / 整合 / 聚类 / 注释(这条链给 single_cell_preprocessor,它再串注释与下游)、不做 bulk 差异表达(→ bulk_rna_analyst)、不做空间下游(→ spatial_omics_orchestrator);本 agent 的职责终点是"FASTQ 落盘 + 样本表解析成 AnnData + 下载报告",随后交棒。若落地的是单细胞**原始 FASTQ**(还没有 gene×cell 矩阵):10x 液滴走 `single-cell-kb-alignment`、plate-based Smart-seq2/3 走 `single-cell-smartseq-quantification` 先比对定量成矩阵,再进 `single_cell_preprocessor`。

### analysis_sanity_review
- Name: Analysis Sanity Review
- Tier: community
- Category: single_cell_analysis
- Summary: 分析定稿前的生物学一致性闸 —— 用全新上下文核对「报告结论 ↔ 产物 ↔ identity.json」，标出反常与无据断言
- Skills: office-tools
- Toolsets: file_manager, python_interpreter, think, task, memory
- Use when: 一段组学分析（注释/整合/差异等）写报告之前，要一个没沾过本次推理的全新视角核对结论是否与数据和已确认身份自洽

### analysis_strategist
- Name: Analysis Strategist
- Tier: pro
- Category: orchestration
- Summary: 跨模态分析策略架构师 —— 给定一份新数据 + 一个科学问题，遍历 OmicVerse 全函数表与全部 skill / specialist agent，组合出一个能回答该问题的、可能非传统的多阶段分析方案,再交给专科 agent 逐段执行
- Skills:
- Toolsets: file_manager, python_interpreter, omicverse_lookup, skill, team, plan, think, task, memory
- Use when: 拿到一份(或多份)新数据,想问"这份数据能回答什么 / 怎么分析才最有信息量",并且愿意接受非传统的、跨阶段拼装的分析路线 —— 例如 scRNA + 代谢通量 + 拟时序联合,scATAC + scRNA + peak-to-gene + 谱系演化,bulk + 微生物 + 配对代谢联合,空间 + 反卷积 + 邻接细胞通讯。不是已经知道要跑什么管线了 —— 那种走对应专科 agent;这里专门处理"该跑什么"。

### antibody_engineer
- Name: Antibody Engineer
- Tier: plus
- Category: structural_biology
- Summary: 抗体 / nanobody 工程 — 已有抗体的 CDR 重设计 / 人源化 / liability 扫描 / Ab-antigen 复合物亲和力评估，覆盖从设计到 developability 的完整序列工程链
- Skills: protein-hardware-probe, protein-antibody-cdr, protein-sequence-design, protein-single-chain-fold, protein-complex-affinity, protein-structure-search
- Toolsets: file_manager, python_interpreter, plan, think, task, skill, memory
- Use when: 用户问 "redesign this mAb's CDR" / "humanize this mouse antibody" / "我的抗体序列有没有 liability" / "score my nanobody candidates against the antigen" / "transfer this paratope to a stable scaffold

### binder_designer
- Name: Binder Designer
- Tier: plus
- Category: structural_biology
- Summary: 蛋白 binder 从头设计端到端 —— 按硬件选引擎（CUDA 用 BindCraft/RFantibody，Apple Silicon 用 BoltzGen-MPS），生成候选、Boltz-2 亲和力打分、折叠新颖性校验、抗体成药性风险扫描
- Skills: protein-hardware-probe, protein-binder-design, protein-binder-design-lite, protein-sequence-design, protein-single-chain-fold, protein-complex-affinity, protein-structure-search, protein-antibody-cdr
- Toolsets: file_manager, python_interpreter, plan, think, task, skill, memory
- Use when: 用户想给一个目标蛋白从零设计 binder（mini-protein / nanobody / antibody / peptide），从 PDB 或 UniProt ID 开始，需要候选 + 预测亲和力 + 评估能否进湿实验

### bulk_epigenomics_analyst
- Name: Bulk Epigenomics Analyst
- Tier: pro
- Category: general_omics_analysis
- Summary: 块体表观基因组分析 —— bulk ATAC-seq / ChIP-seq / CUT&RUN 走 epione(FASTQ → call peak → 差异可及性 → TF 足迹 → 轨道 / motif);以及 bulk DNA 甲基化 / WGBS(per-CpG beta 矩阵 → 区域甲基化、差异甲基化 DMC/DMR + FDR、随距离的甲基化空间剖面,走标准栈 pandas/scipy/statsmodels/pybedtools)
- Skills: bulk-epigenome-upstream, differential-peak-analysis, dna-methylation-analysis, tf-footprinting, epigenome-track-visualization, gsea-enrichment, gene-id-conversion, data-io-loading, data-cleaning, figure-programmatic, report-html-generation, notebook-export, office-tools, retraction-check
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory
- Use when: 拿到 bulk 表观基因组数据。两类:(1) 染色质可及性 / 占据 —— ATAC-seq / ChIP-seq / CUT&RUN 的 FASTQ.gz、BAM、narrowPeak 或 bigWig,做上游、call peak、差异 peak、TF 足迹、轨道、motif 富集(走 epione);(2) DNA 甲基化 / WGBS / RRBS —— per-CpG beta 矩阵或 methylation BED/bedGraph(beta 0-1 或 0-100),做区域甲基化(启动子 / 基因体 / enhancer / CpG island)、条件间差异甲基化、或甲基化在某特征周围的空间分布(走标准栈,epione 无甲基化模块)。不是单细胞 ATAC(→ single_cell_epigenomics_analyst),不是 Hi-C(→ chromatin_3d_analyst),不是纯 RNA 表达(→ bulk_rna_analyst)。

### bulk_rna_analyst
- Name: Bulk RNA-seq Analyst
- Tier: community
- Category: general_omics_analysis
- Summary: Bulk RNA-seq 端到端分析 —— 表达矩阵 → 基因-变量关联(分组 / 连续性状,DEG·limma)→ 富集 → 网络 → 报告
- Skills: gene-id-conversion, data-io-loading, data-cleaning, sample-metadata-alignment, tcga-preprocessing, survival-analysis, bulk-combat-correction, bulk-deg-analysis, time-course-analysis, multi-omics-integration, sample-clustering, gsea-enrichment, bulk-wgcna-analysis, bulk-stringdb-ppi, bulk-celltype-deconvolution, bulk-to-single-deconvolution, report-html-generation, notebook-export, office-tools
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory
- Use when: 拿到 bulk RNA-seq 表达矩阵(genes × samples,counts/TPM)、多批次队列、TCGA、FASTQ —— 需要你从这个矩阵建模 / 推导。"哪些基因与某个样本变量相关 / 关联 / 差异表达"的问题归这里:变量是分组、连续性状(病程 / 年龄 / 剂量 / 严重度评分)、还是时间点都一样 —— 差异表达就是把表达矩阵建模为一个 design matrix 的函数,连续协变量只是 design 里的一列,措辞是 "correlation / associated with / track" 不改变这一点。**关键判据:输入确实是一个基因 × 样本的表达矩阵、分析要从中建模。** 若输入已经是算好的结果表(DE 结果表、每特征 / 每条件的统计量或 score 表),任务只是在这些表上做相关 / 相似度 / 聚合,那是表格统计,归 tabular_genomics_analyst。也做富集 / 共表达网络 / 报告。

### c3ca_phase_runner
- Name: c3CA Phase Runner
- Tier: lab
- Category: single_cell_analysis
- Summary: 逐阶段执行 3CA 前端与后端工作流（一次只跑一个 phase）
- Skills: rust_nmf, sc_c3ca_backend_skill
- Toolsets: file_manager, python_interpreter, shell
- Use when: 用于 rust-NMF 3CA 前端各 phase、c3CA 后端 MP-analysis 各 phase、phase 间交接，以及单个 phase 的失败排查

### cancer_dependency_analyst
- Name: Cancer Dependency Analyst
- Tier: pro
- Category: general_omics_analysis
- Summary: 癌症依赖图谱分析 —— DepMap/CCLE 必需性评分、患者层面预测依赖评分、合成致死(发现/排序 + 成对判定):选择性依赖(NormLRT)、转化依赖图谱(患者 vs 细胞系)、可成药靶点优先级、Lasso + 互斥 + 旁系同源 SL、给定基因对的 SL/non-SL 判定(LOF 分层依赖位移,非相关性)
- Skills: cancer-dependency-analysis, synthetic-lethality-discovery, target-druggability-pro, somatic-mutation-analysis, tabular-association-analysis, gsea-enrichment, gene-id-conversion, data-io-loading, data-cleaning, figure-programmatic, report-html-generation, notebook-export, office-tools, retraction-check
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory
- Use when: 拿到癌症依赖 / 必需性数据 —— DepMap/CCLE 的 CRISPR/RNAi 必需性评分、患者层面预测依赖评分、突变矩阵 + 多组学 —— 要找某癌种的选择性依赖 / 生物标志物 / 可干预靶点,或预测某 LOF 事件的合成致死伙伴,或判定某一对具名基因是否合成致死(仅给基因名 + 上下文、需自己取依赖数据也可)。不是普通 RNA-seq 差异表达(→ bulk_rna_analyst),不是体细胞突变频率统计(→ tabular_genomics_analyst),不是 GWAS / eQTL(→ statistical_genetics_analyst)。

### cell_cell_communication_free
- Name: Cell-cell Communication Free
- Tier: community
- Category: single_cell_analysis
- Summary: 细胞通讯 Free —— 仅 OmicVerse CellPhoneDB v5；使用 ov.pl.ccc_* 出图
- Skills: cell-cell-communication-free
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, team
- Use when: 用于已注释 scRNA-seq AnnData 的免费版细胞通讯 / 配体-受体分析，CellPhoneDB v5 够用时走这里；不跑 LIANA consensus、LIANA+、CellChat(R) 或手写兜底统计

### cell_cell_communication_pro
- Name: Cell-cell Communication Pro
- Tier: pro
- Category: single_cell_analysis
- Summary: 细胞通讯 Pro —— LIANA/LIANA+、CellPhoneDB v5 fallback、CellChat(R)，并使用 ov.pl.ccc_* 出图
- Skills: cell-cell-communication, cellchat_rust_h5ad
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory, team
- Use when: 用于 scRNA-seq 的进阶细胞通讯 / 配体-受体分析：LIANA / LIANA+ consensus、CellPhoneDB v5 兜底、按需 CellChat(R)、条件比较、信号通路排序与差异互作图；只用 CellPhoneDB 的免费路径走 cell_cell_communication_free

### cell_viewer
- Name: Cell Viewer
- Tier: plus
- Category: viewer_tools
- Summary: 细胞查看器专属 agent — 用 `cellviz` 命令驱动实时 UMAP 散点图（着色/高亮/调暗/换降维）+ 对 `adata` 跑 scanpy/omicverse 分析
- Skills: cell-viewer-viz
- Toolsets: python_interpreter, think, plan, skill, memory
- Use when: 用户在 OmicOS「细胞查看器」里、已选中一个内核 AnnData(默认 `adata`），想要任何一类：
- 直接改变中间的实时散点图：按 obs 列 / 基因着色、高亮某些细胞类型并把其余调暗、切换 UMAP/tSNE/PCA、调点大小 / 透明度 / 调色板
- 在共享内核里对 adata 跑分析：QC、标准化、HVG、PCA、邻接、UMAP/tSNE、Leiden/Louvain、marker 基因
重点：凡是"在图上显示 / 着色 / 高亮"——用 `cellviz` 命令驱动**实时散点图**,不要退回画静态 matplotlib 图。

### cellchat_rust_h5ad_runner
- Name: CellChat Rust H5AD Runner
- Tier: lab
- Category: single_cell_analysis
- Summary: Cell-cell communication —— LIANA (Python) 或 CellChat (R) 配体-受体推断;原始/未注释数据先委派预处理+注释。
- Skills: cell-cell-communication, cellchat_rust_h5ad
- Toolsets: file_manager, python_interpreter, shell, plan, think, task, skill, memory, team
- Use when: Use for cell-cell / ligand-receptor communication analysis on single-cell RNA-seq — LIANA (Python, ov.single.run_liana, consensus + permutation test) or CellChat (R) inference, directed sender→receiver questions, signaling-pathway ranking, condition comparison, and differential interaction plots. Accepts an annotated h5ad directly, or raw / unannotated scRNA-seq (text matrices, mtx, unlabeled h5ad) by delegating preprocessing and cell-type annotation to the appropriate specialists first.

### chromatin_3d_analyst
- Name: Chromatin 3D Genome Analyst
- Tier: pro
- Category: general_omics_analysis
- Summary: 三维基因组分析 —— bulk Hi-C 与单细胞 Hi-C 端到端:接触矩阵 QC → A/B 区室 / saddle → TAD / insulation → loop → 单细胞 scHiCluster 插补 / 嵌入 / 聚类 → REPORT.html;全程走 epione
- Skills: hic-analysis, single-cell-hic-analysis, gene-id-conversion, data-io-loading, data-cleaning, figure-programmatic, report-html-generation, notebook-export, office-tools
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory
- Use when: 拿到 Hi-C / 三维基因组数据 —— bulk 接触矩阵(.cool/.mcool)、pairs 文件,或单细胞 / droplet Hi-C(.scool、per-cell .cool)—— 要分析基因组三维结构:A/B 区室、TAD 结构域、染色质 loop、接触频率衰减,或单细胞层面的 3D 基因组细胞状态 / 细胞周期。不是 bulk ATAC/ChIP/CUT&RUN(→ bulk_epigenomics_analyst),不是 scATAC(→ single_cell_epigenomics_analyst)。

### clinical_translator_free
- Name: Clinical Translator Free
- Tier: community
- Category: scientific_writing
- Summary: 把组学发现对照临床证据（免费版）—— 基因/试验/标签剂量/撤稿四件套，全部走真免费 API
- Skills: clinical-trial-check, gene-lookup, retraction-check, dosage-calc
- Toolsets: file_manager, web, plan, think, task, skill, memory
- Use when: 拿到 DEG 列表或候选基因后，想快速知道临床上已经在做什么 —— 用大众都知道的免费数据库

### clinical_translator_pro
- Name: Clinical Translator Pro
- Tier: pro
- Category: scientific_writing
- Summary: 把组学发现对照临床证据 —— 写转化解读段落、可成药性评分、CPIC 基因型剂量、FAERS 真实信号、机制起源、治疗含义；输入可以是 DEG 列表、候选基因、富集的 cell type、enrichment 结果、变异、通路
- Skills: clinical-trial-check, gene-lookup, retraction-check, dosage-calc, target-druggability-pro, pharmacogenomics-pro, adverse-events-pro, variant-pathogenicity-pro, pathway-clinical-pro, disease-gene-association-pro
- Toolsets: file_manager, web, plan, think, task, skill, memory
- Use when: 拿到一份组学分析的具体结果（DEG 列表 / 候选基因 / 富集的 cell type / pathway / 变异 / 临床表型），要把它写成临床或转化语言 —— "mechanistic origins" 段落（recruitment / in-situ adaptation / tissue residency 的解读）、"translational implications" / "therapeutic implications" / "clinical relevance" 段落（治疗靶点、可成药性、临床试验覆盖、生物标志物含义）、CPIC 基因型剂量、FAERS 不良事件信号、变异群体频率。任何分析报告 (trace.md / REPORT.md / Discussion 节) 里需要"clinical / translational / therapeutic / mechanistic"风味的子节都是这里。

### he_to_st_predictor
- Name: H&E → ST Predictor
- Tier: pro
- Category: spatial_analysis
- Summary: 从 H&E 切片预测空间转录组（STPath zero-shot / STFlow / HEST-FM / iStar 超分）
- Skills: spatial-he-to-st-prediction, spatial-data-io-loading, spatial-publication-plots, spatial-variable-genes, gene-id-conversion, report-html-generation, notebook-export, office-tools
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory
- Use when: 拿到一张 H&E 全切片 (svs/tiff/ndpi/ome.tif) 想推空间基因表达 —— 没有 Visium 用 STPath 零样本，有配对 Visium 用 HEST-FM/STFlow，要 sub-spot 超分用 iStar

### humanize
- Name: Humanize
- Tier: community
- Category: scientific_writing
- Summary: 去 AI 味的润色器 —— 不改事实、不动数据，只调文风
- Skills: humanize-academic, scientific-critical-thinking, scientific-manuscript-writing
- Toolsets: file_manager, think, task, memory
- Use when: scientific_writer 给出初稿后，准备投稿前的最后润色

### ihc_if_quantifier
- Name: IHC/IF Quantifier
- Tier: plus
- Category: general_omics_analysis
- Summary: 实采 IHC / 免疫荧光显微图定量(非全玻片、非 ImageJ 宏)—— 明场 IHC:DAB 颜色解卷积→阳性%/H-score/Allred;荧光 IF:多通道分离→核分割→每细胞阳性%/强度→共定位。Python(scikit-image/cellpose),单张或成批
- Skills: imaging-ihc-if-quantification
- Toolsets: file_manager, python_interpreter, plan, think, task, skill, memory
- Use when: 用户有常规明场 / 荧光显微图文件(单张或一批 tif / png / ome-tif,**不是** svs / ndpi 全玻片),要定量染色:IHC DAB 棕染阳性百分比 / H-score / Allred,或多通道 IF 的通道分离 + 核分割 + 每细胞阳性比例 + 通道共定位(Pearson / Manders)。NOT-FOR:不是 ImageJ 标签页里实时单图的宏分析(→ imagej)、不是 LazySlide 的 H&E 全玻片基础模型分析或虚拟染色(→ pathology_lazyslide)、不是单细胞 / 空间组学的 AnnData 下游。

### imagej
- Name: ImageJ
- Tier: plus
- Category: viewer_tools
- Summary: ImageJ 查看器专属 agent — 写 ImageJ 宏(IJM)驱动浏览器里的实时 ImageJ:滤波 / 阈值分割 / 颗粒分析 / 强度·ROI 测量 / 标尺 / 栈,结果用 `return` 串回传
- Skills: imagej-macro-analysis
- Toolsets: think, plan, skill, memory
- Use when: 用户在 OmicOS「ImageJ」标签里、右侧已打开一张图像,想做图像处理或定量分析:
- 预处理 / 滤波（高斯、中值、背景扣除、位深转换、边缘）
- 阈值分割（setAutoThreshold + Convert to Mask + Watershed）
- 颗粒分析（计数 / 面积 / 形状 / 尺寸分布）
- 强度 / ROI 测量（均值 / 最值 / 积分密度 / 面积占比）
- 标尺标定（Set Scale）、栈处理（Z 投影 / 通道拆分）
纯前端 ImageJ.JS,**不用 Python**;每次只给一个 ```ijm 宏块,并在宏末尾 `return` 结果串。

### immune_repertoire_analyst_pro
- Name: Immune Repertoire Analyst Pro
- Tier: pro
- Category: general_omics_analysis
- Summary: 免疫组库 (AIRR-seq: TCR/BCR) 端到端分析 —— 单细胞 / bulk / B 细胞 SHM·谱系 / TCR 特异性 / TCR-GEX 联合 → REPORT.html
- Skills: airr-singlecell, airr-bulk, airr-bcr-immcantation, airr-tcr-specificity, airr-tcr-gex, data-io-loading, figure-programmatic, single-cell-report-authoring, report-html-generation, notebook-export, office-tools, retraction-check
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory
- Use when: 拿到 TCR / BCR 测序 (10x V(D)J、AIRR rearrangement、bulk repertoire 表)，要跑克隆型 / 多样性 / 体细胞超突变 / 谱系树 / TCR 特异性分组 / 与转录组联合分析并出报告

### literature_free
- Name: Literature Free
- Tier: community
- Category: scientific_writing
- Summary: 文献侦察（免费版）—— 检索 + 取全文 + 撤稿核查 + 多源对比，全部走免费公共 API
- Skills: literature-search-free, fulltext-free, retraction-check, source-comparison, preprint-monitoring, citation-management
- Toolsets: file_manager, web, plan, think, task, skill, memory
- Use when: 开新课题摸清领域现状、找论文读、查一篇文献可信度 —— 用大众都知道的免费 API。NOT-FOR:不是数据分析 / 作图 / 组学分析任务(→ 对应分析专家);本 agent 只做文献检索 / 取全文 / 撤稿核查 / 多源对比。

### literature_pro
- Name: Literature Pro
- Tier: pro
- Category: scientific_writing
- Summary: 文献侦察（专业版）—— 穷尽式发现：OpenAlex 全学科 + Semantic Scholar AI 层 + 引用图滚雪球 + 跨语料全文挖掘
- Skills: literature-search-free, literature-search-pro, fulltext-free, fulltext-pro, retraction-check, source-comparison, preprint-monitoring, citation-management, dataset-linkout
- Toolsets: file_manager, web, plan, think, task, skill, memory
- Use when: 要最全的文献覆盖、引用网络遍历、AI 相关性排序、按全文内容建语料 —— 同样免费 API，但榨到底。NOT-FOR:不是数据分析 / 作图 / scRNA / bulk / 空间 / 统计分析任务(那些路由到对应分析专家);本 agent 只做文献发现、引用图遍历与全文挖掘。

### memory_curator
- Name: Memory Curator
- Tier: community
- Category: orchestration
- Summary: 整理你的 agent 记忆 —— 去重 / 合并 / 取代过时事实 / rollup / 修剪,逐条确认,绝不臆造或静默覆盖
- Skills: consolidate-memory
- Toolsets: memory, think
- Use when: 记忆变多变乱时想做一次审阅式整理 —— 重复笔记、相互矛盾或过时的事实、应合并的近似笔记、臃肿的索引。不是写新记忆,是整理已有记忆。

### metabolomics_analyst_pro
- Name: Metabolomics Analyst Pro
- Tier: pro
- Category: general_omics_analysis
- Summary: 代谢组学 / 脂质组学端到端分析 —— peak 表 → QC + batch → 单变量/多变量统计 → 通路 / 脂质 / biomarker / 多组学 → REPORT.html
- Skills: bulk-metabol-preprocessing, bulk-metabol-multivariate, bulk-metabol-pathway-multifactor, bulk-metabol-untargeted-lipidomics, micro-metabol-paired, gene-id-conversion, data-io-loading, figure-programmatic, single-cell-report-authoring, report-html-generation, notebook-export, office-tools, retraction-check
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory
- Use when: 拿到代谢组学 peak intensity 表（MetaboAnalyst CSV / LC-MS / NMR / lipidomics）/ 多 batch 队列 / 配对 microbe-metabolite 数据，要跑预处理 + 统计 + 通路 + 出报告

### microbiome_analyst_pro
- Name: Microbiome Analyst Pro
- Tier: pro
- Category: general_omics_analysis
- Summary: 16S/扩增子 微生物组端到端分析(仅 16S/ITS/18S 扩增子,NOT 宏基因组 shotgun/WGS)—— FASTQ / ASV 表 → α/β/UniFrac/DA → 跨 cohort meta + 跨模态 → REPORT.html
- Skills: microbiome-16s-amplicon-dada2, microbiome-phylogeny, microbiome-da-comparison, microbiome-meta-analysis, micro-metabol-paired, data-io-loading, figure-programmatic, single-cell-report-authoring, report-html-generation, notebook-export, office-tools, retraction-check
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory
- Use when: 拿到 16S 测序 (raw FASTQ 或已有 ASV/OTU 表) / 多 cohort 16S / 配对 microbe-metabolite 数据，要跑多样性 + 差异丰度 + 通路 / 元分析 + 出报告。仅限 16S / ITS / 18S 扩增子;NOT-FOR:shotgun / 全基因组 宏基因组(Kraken2 / Bracken / MetaPhlAn / HUMAnN / MAG 组装·分箱)不在本 agent 范围,不要把这类任务路由到这里(目前平台无 shotgun 落点 —— 应向用户说明,而非接下只能 plan-不能-run)。

### molecule_viewer
- Name: Molecule Viewer
- Tier: plus
- Category: viewer_tools
- Summary: 分子查看器专属 agent — 用真 PyMOL 命令驱动 3D 视图 + 对 `_omicos_pdb` 做结合位点 / 界面 / 性质等结构分析
- Skills: molecule-viewer-commands, molecule-structure-analysis
- Toolsets: python_interpreter, think, plan, skill, memory
- Use when: 用户在 OmicOS「分子查看器」里、已经加载了一个 3D 结构（蛋白 / 复合物 / 配体，PDB / mmCIF；
内核镜像变量名 `_omicos_pdb`），想要其中任何一类：
- 用命令控制 3D 视图：显示样式 (cartoon/stick/sphere/surface…)、着色、按布尔选择高亮、聚焦、测距 / 角度 / 二面角、表面、标注残基
- 结合位点 / 口袋：找配体 (hetatm)、配体周围 X Å 的残基 (byres within)、接触
- 链-链界面：界面残基、氢键、埋藏面积
- 结构性质：分子量、链 / 残基组成、二级结构比例、SASA、几何
- 配体化学信息 (rdkit)
如果用户要 "折叠序列 / 预测复合物结构 / 小分子对接打分" —— 路由到 `structural_biologist`。

### nvidia_bionemo_nim
- Name: NVIDIA BioNeMo NIM
- Tier: plus
- Category: structural_biology
- Summary: NVIDIA BioNeMo / NIM Cloud API specialist for direct AlphaFold2, ProteinMPNN, DiffDock, RFdiffusion, MolMIM, and related NVIDIA-hosted biology endpoints.
- Skills: nvidia-bionemo-nim
- Toolsets: file_manager, python_interpreter, plan, think, skill, memory
- Use when: Use when the user explicitly mentions NVIDIA BioNeMo, NVIDIA NIM, NVIDIA Cloud API, AlphaFold2 NIM, ProteinMPNN NIM, DiffDock NIM, RFdiffusion NIM, MolMIM NIM, or asks whether a workflow actually used NVIDIA / AlphaFold2 / ProteinMPNN.

### omicverse_omni
- Name: OmicVerse Omni
- Tier: community
- Category: orchestration
- Summary: 通用全能助手 —— 文件读写、Python 计算、shell、网页搜索、计划编排一气呵成
- Skills:
- Toolsets: file_manager, python_interpreter, shell, notebook, omicverse_lookup, skill, team, web, plan, schedule, background, think, task, memory, vision, image_gen
- Use when: 组学专科之外的各类通用计算与分析任务——通用编程与脚本、数据清洗与格式转换、文件与网页处理、网络爬取、文档（docx/pdf 等）生成、以及需要跨多步骤/多工具串联的综合性分析；也用于不确定该交给哪个专科、需要一个能在多任务之间无缝切换的通用入口时

### paper_critic
- Name: Paper Critic
- Tier: community
- Category: scientific_writing
- Summary: 端到端审稿 —— 代码、统计、复现路径、结构化同行评议
- Skills: paper-code-audit, replication, statistics-check, peer-review, office-tools, retraction-check, fulltext-free
- Toolsets: file_manager, web, plan, think, task, memory
- Use when: 拿到一篇他人论文（PDF / arXiv / GitHub），想做严格的批评而非摘要

### pathology_lazyslide
- Name: Pathology — LazySlide
- Tier: plus
- Category: viewer_tools
- Summary: H&E 全切片分析的 LazySlide 门面 agent — tile FM / 细胞分割 / slide 分类 / 生存 / 转录组整合 / 虚拟染色 一站式
- Skills: pathology-lazyslide-he-analysis, pathology-lazyslide-cell-segmentation, pathology-lazyslide-supervised-classification, pathology-lazyslide-survival-prediction, pathology-lazyslide-he-transcriptomics-integration, pathology-lazyslide-virtual-staining
- Toolsets: file_manager, python_interpreter, shell, plan, think, task, skill, memory
- Use when: 用户带 H&E 全切片 (svs/tiff/ndpi/ome.tif) 想做下列任何一类：
- 直接形态学 + 报告 (tile FM + zero-shot, 单切片) → pathology-lazyslide-he-analysis
- 细胞级实例分割 + 细胞类型 → pathology-lazyslide-cell-segmentation
- 已知 slide-level 标签的有监督分类 (subtype / response / grade) → pathology-lazyslide-supervised-classification
- 队列生存预测 (time-to-event, censoring) → pathology-lazyslide-survival-prediction
- 配对 H&E + RNA-seq 关联分析 (RNALinker) → pathology-lazyslide-he-transcriptomics-integration
- 虚拟染色 (生成 IHC/IF 通道) → pathology-lazyslide-virtual-staining
如果用户要从 H&E 像素直接"预测基因表达"——路由到 `he_to_st_predictor`。
如果已经有空转 AnnData 做下游——路由到 `spatial_omics_orchestrator`。

### phase_separation_analyst
- Name: Phase Separation Analyst
- Tier: plus
- Category: general_omics_analysis
- Summary: 相分离 / 生物分子凝聚体专家 —— IDR/PLD/LCR 注释、氨基酸组成与富集、sticker-spacer 序列 patterning(localCIDER)、PS 预测器(PScore/PLAAC/catGRANULE/FuzDrop/PSPire)benchmark,区分 SaPS / PdPS
- Skills: phase-separation-analysis, gene-id-conversion, data-io-loading, figure-programmatic, report-html-generation, notebook-export, office-tools
- Toolsets: file_manager, python_interpreter, shell, plan, think, task, skill, memory
- Use when: 问题涉及液-液相分离(LLPS)、生物分子凝聚体、无膜细胞器 —— 哪些蛋白会相分离、什么序列特征驱动凝聚体形成、相分离预测器的判别表现、自组装(SaPS)vs 伴侣依赖(PdPS)机制差异、IDR / prion-like 域 / 低复杂度域的序列生物物理。不是凝聚体相图的粗粒化 MD 模拟,不是 3D 结构预测,不是单个突变的致病性评分(→ variant_analyst)。

### phylogenomics_analyst
- Name: Phylogenomics Analyst
- Tier: plus
- Category: phylogenomics
- Summary: 多序列比对与系统发生树的质量评估、共变与多歧分析，全部用 PhyKIT 落地。
- Skills: phykit-alignment-quality, phykit-tree-quality, phykit-gene-tree-discordance, phykit-trait-history, phykit-phylogenetic-signal, phykit-trait-ordination, phykit-phylogenetic-regression, phykit-trait-evolution-models, phykit-phylo-visualization
- Toolsets: file_manager, python_interpreter, shell, notebook, omicverse_lookup, team, plan, think, task, skill, memory
- Use when: 用户提到 multiple sequence alignment / 系统发生树 / phylogeny / phylogenomics / gene tree / species tree / polytomy / rapid radiation / mirror tree / treeness / RCV / LB score / parsimony informative sites / 饱和度 / saturation / MSA 准确性 / sum-of-pairs / column score。或者用户上传了 `.fa` / `.fasta` / `.aln.fa` / `.tre` / `.treefile` / `.newick` 文件请求分析。

### primer_design_assistant
- Name: Primer Design Assistant
- Tier: community
- Category: molecular_biology
- Summary: 引物设计端到端助手 — qPCR / 克隆（酶切·Gibson·Golden Gate）/ 特异性 BLAST / 密码子优化 一站式
- Skills: primer-qpcr, primer-cloning, primer-specificity, codon-optimize
- Toolsets: file_manager, python_interpreter, plan, think, task, skill, memory
- Use when: 必备输入是一条序列身份(基因 symbol / NCBI accession / Ensembl ID / 裸 cDNA·ORF)加一个明确意图(qPCR 验证、克隆进表达载体、或异源表达前的密码子优化);产出"下单即用"的引物对 CSV + 特异性 BLAST 报告。NOT-FOR:不做 sgRNA / CRISPR guide 设计、不做 in-silico 载体连接 / 克隆仿真、不做寡核苷酸报价、不做湿实验验证;也不是 single-cell / 通用数据分析 / 作图任务(那些路由到对应分析专家)。

### proteomics_analyst_pro
- Name: Proteomics Analyst Pro
- Tier: pro
- Category: general_omics_analysis
- Summary: 蛋白组学端到端分析 —— 蛋白丰度矩阵 → QC → 缺失机制诊断 → 归一/插补 → 差异表达(limma/DEqMS/proDA)→ 富集 → REPORT.html;质谱与 Olink 都覆盖
- Skills: bulk-proteomics, multi-omics-integration, gsea-enrichment, gene-id-conversion, data-io-loading, data-cleaning, figure-programmatic, single-cell-report-authoring, report-html-generation, notebook-export, office-tools, retraction-check
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory
- Use when: 拿到蛋白丰度矩阵(MaxQuant proteinGroups / DIA-NN report / FragPipe combined_protein / Olink NPX / 通用 protein×sample 表),或肽段级 MSstats 长表,要做 QC、缺失值处理、差异表达、通路富集、出报告

### quality_review
- Name: Quality Review
- Tier: community
- Category: scientific_writing
- Summary: 投稿前自查 —— 逐节打分、跨节一致性检查、出 PASS / FAIL 判定
- Skills: section-checklist, peer-review-methodology, statistics-check, retraction-check, citation-management, fulltext-free, scientific-critical-thinking, scientific-manuscript-writing
- Toolsets: file_manager, think, task, memory
- Use when: 自己写完稿子，准备投出去之前的最后一道关卡

### review_writer_pro
- Name: Review Writer Pro
- Tier: pro
- Category: scientific_writing
- Summary: 端到端写文献综述(综述)—— 检索(PubMed 带 key/OpenAlex/Semantic Scholar)→筛选→读全文→主题合成→证据表→gap 分析→逐节初稿+引文+示意图。给个主题就能产出一篇有据可查的 review
- Skills: literature-search-free, literature-search-pro, fulltext-free, fulltext-pro, preprint-monitoring, retraction-check, source-comparison, dataset-linkout, literature-review-synthesis, systematic-review-method, citation-management, scientific-manuscript-writing, manuscript-docx-review, figure-programmatic, scientific-schematics, paper-rendering
- Toolsets: file_manager, web, plan, think, task, skill, memory
- Use when: 用户要写一篇文献综述 / 叙述性或系统 review —— "帮我写一篇关于 X 的综述""博士要三篇综述,先写 X""把这个领域近五年进展综述一下""给定这批参考文献整合成 review"。区别于 scientific_writer(写单篇研究论文 results/methods),这里是 综述 全流程;区别于 literature_pro(只检索,不成稿)

### reviewer
- Name: Reviewer
- Tier: community
- Category: general_omics_analysis
- Summary: 每轮分析结束后由系统自动触发的独立「对话审查器」—— 用全新上下文复核本回合的记录，专抓捏造 / 幻觉 / 偏离计划，产出「通过 / 提示 / 不通过」检查项，并保留可查看的审阅过程
- Skills:
- Toolsets: file_manager, python_interpreter, think
- Use when: 由 review 编排在一次分析回合结束后自动 spawn，传入指向本回合对话记录的指针，用一个没参与过本次推理的全新视角复核结论与产物。不作为根 agent 直接调用、也不承接新分析任务；正常分析请求请路由到对应的专家。

### scientific_writer
- Name: Scientific Writer
- Tier: community
- Category: scientific_writing
- Summary: 把分析结果写成论文 —— 支持手稿、DOCX/PDF、公式文档、海报、答辩 PPT、中英文期刊
- Skills: paper-rendering, figure-programmatic, scientific-manuscript-writing, office-tools, manuscript-docx-review, citation-management, fulltext-free, systematic-review-method, latex-research-posters, scientific-slides, scientific-schematics, peer-review-methodology, general-figure-guide, nature-figure-guide, science-figure-guide, cell-figure-guide, pnas-figure-guide, elife-figure-guide, nejm-figure-guide, lancet-figure-guide, cancer-research-figure-guide
- Toolsets: file_manager, shell, web, plan, think, task, memory, image_gen
- Use when: 拿到 DEG / 图 / 队列数据 / 实验结果 / 论文 PDF / Markdown / LaTeX / DOCX，要写成稿件、DOCX/PDF、公式算法文档、figure 或幻灯片

### single_cell_annotator_free
- Name: Single-cell Annotator Free
- Tier: community
- Category: single_cell_analysis
- Summary: 提示词驱动的 cell-type 注释（免费）—— celltype_anno_ov 四步 prompt 链 + agent 自身 LLM 推理 + ov.single.get_celltype_marker，零外呼、零账号
- Skills: celltype-anno-ov-free, single-cell-clustering-backends, gene-id-conversion, office-tools, notebook-export
- Toolsets: file_manager, python_interpreter, omicverse_lookup, plan, think, task, skill, memory
- Use when: 拿到已 cluster 的 .h5ad，要快速给每个 cluster 标 cell type，又不想付费 / 不需要 PMID 级证据

### single_cell_annotator_pro
- Name: Single-cell Annotator Pro
- Tier: pro
- Category: single_cell_analysis
- Summary: 文献证据 cell-type 注释 —— OmicosAnno 89 万条标注 + signed-template 评分 + 本会话 LLM 生物学仲裁 + PubMed 句子级证据
- Skills: celltype-annotation-pro, single-cell-preprocessing, gene-id-conversion, single-cell-composition, single-cell-publication-plots, single-cell-report-authoring, report-html-generation, office-tools, notebook-export
- Toolsets: file_manager, python_interpreter, omicverse_lookup, plan, think, task, skill, memory
- Use when: 拿到已聚类的 AnnData (`scmarker_preprocessor` 输出 / 任何带 `leiden`/`louvain` 的 .h5ad)，要给每个 cluster 标 cell type，并要可审计的文献证据

### single_cell_downstream_analyst_pro
- Name: Single-cell Downstream Analyst Pro
- Tier: pro
- Category: single_cell_analysis
- Summary: scRNA-seq 下游功能分析总管 —— 代谢推断 / 组成检验 / 基因模块 / pseudobulk DEG / 通路富集；GRN/扰动交给专门 agent
- Skills: single-cell-metabolism-inference, single-cell-composition, single-cell-genemodule, single-cell-pseudobulk, geneset-scoring, gsea-enrichment, gene-id-conversion, single-cell-publication-plots, single-cell-report-authoring, report-html-generation, notebook-export, office-tools
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory
- Use when: 已经有 QC 过 + 已注释的 scRNA-seq AnnData（cell-type 列填好），要做"注释完之后"的功能/差异分析；GRN/SCENIC 请走 single_cell_grn_analyst，基因/RegVelo 扰动请走 single_cell_perturbation_analyst，细胞通讯请走 cell_cell_communication_*，pseudotime 请走 single_cell_trajectory_*

### single_cell_epigenomics_analyst
- Name: Single-Cell Epigenomics Analyst
- Tier: pro
- Category: single_cell_analysis
- Summary: 单细胞表观基因组分析 —— scATAC-seq 端到端:fragments → QC → tile 矩阵 → iterative LSI → 聚类 → 基因活性 → call peak → chromVAR motif 活性 → peak-to-gene 连接 → 整合 / 标签迁移 → REPORT.html;全程走 epione
- Skills: scatac-preprocessing, scatac-chromvar, scatac-peak-to-gene, scatac-integration, tf-footprinting, gsea-enrichment, gene-id-conversion, data-io-loading, figure-programmatic, single-cell-publication-plots, report-html-generation, notebook-export, office-tools
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory
- Use when: 拿到单细胞 ATAC-seq 数据 —— fragments 文件、10x scATAC 输出、cell×peak 或 cell×tile 矩阵 —— 要做 QC、降维聚类、基因活性打分、簇级 call peak、chromVAR 转录因子活性、peak-to-gene 调控连接、多样本整合或从 scRNA 迁移细胞类型标签。不是 bulk ATAC/ChIP/CUT&RUN(→ bulk_epigenomics_analyst),不是单细胞 Hi-C(→ chromatin_3d_analyst),不是 scRNA 表达分析(→ single_cell 注释类 agent)。

### single_cell_grn_analyst
- Name: Single-cell GRN Analyst
- Tier: pro
- Category: single_cell_analysis
- Summary: 单细胞基因调控网络（GRN）—— GRNBoost2、GENIE3、RegDiffusion、SCENIC regulon、AUCell/RSS 与 GRN 可视化
- Skills: single-cell-grn-inference, gene-id-conversion, geneset-scoring, single-cell-publication-plots, single-cell-report-authoring, report-html-generation, notebook-export
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, skill, team, plan, think, task
- Use when: 用于单细胞基因调控网络推断、TF-靶基因边表、GRNBoost2/GENIE3/RegDiffusion 先验、SCENIC regulon、AUCell/RSS，或为 RegVelo 准备先验 GRN；若要扰动基因或 TF regulon，用 single_cell_perturbation_analyst

### single_cell_perturbation_analyst
- Name: Single-cell Perturbation Analyst
- Tier: pro
- Category: single_cell_analysis
- Summary: 单细胞扰动模拟 —— scTenifoldKnk、CellOracle、RegVelo TF 阻断，下游效应表与 OmicVerse 风格图
- Skills: single-cell-in-silico-perturbation, single-cell-regvelo-perturbation, single-cell-grn-inference, gene-id-conversion, geneset-scoring, gsea-enrichment, single-cell-publication-plots, single-cell-report-authoring, report-html-generation, notebook-export
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, skill, team, plan, think, task, memory
- Use when: 用于单细胞 in-silico KO/KD/OE、scTenifoldKnk、CellOracle、RegVelo TF regulon 阻断、调控扰动、velocity 感知扰动或细胞命运效应分析；只做 GRN 推断用 single_cell_grn_analyst

### single_cell_preprocessor
- Name: Single-cell Preprocessor
- Tier: plus
- Category: single_cell_analysis
- Summary: scRNA-seq 端到端预处理 —— 10x/.h5ad/.mtx → QC → 归一 → HVG → PCA → 批次校正 → 聚类 → 标记基因
- Skills: single-cell-kb-alignment, single-cell-smartseq-quantification, data-io-loading, rds-qs-seurat-ingestion, gene-id-conversion, single-cell-preprocessing, single-cell-ambient-rna, single-cell-batch-integration, single-cell-clustering-backends, single-cell-composition, single-cell-pseudobulk, single-cell-genemodule, gsea-enrichment, single-cell-publication-plots, single-cell-report-authoring, report-html-generation, notebook-export, office-tools
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory
- Use when: 拿到 raw / 已 QC 的 scRNA-seq AnnData，要清洗 + 标准化 + 聚类 + 取 marker，输出 ready-to-annotate 的 adata.h5ad。若手上只有原始 FASTQ 还没有矩阵：带 barcode+UMI 的液滴/微孔化学（10x、Drop-seq、inDrops、CEL-seq、SPLiT-seq 等）先走 single-cell-kb-alignment、plate-based Smart-seq2/3 先走 single-cell-smartseq-quantification 比对定量成矩阵，再回到本流水线

### single_cell_trajectory_free
- Name: Single-cell Trajectory Free
- Tier: community
- Category: single_cell_analysis
- Summary: 单细胞轨迹 Free —— 仅 PAGA/DPT 与 Monocle；不调用 velocity、CellRank 或高级多方法
- Skills: single-cell-trajectory-inference-free, single-cell-publication-plots, single-cell-report-authoring
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, skill, team, plan, think, task
- Use when: 用于已准备好的单细胞 AnnData 的免费版拟时序 / 分支分析，PAGA/DPT 或 Monocle 风格轨迹够用时走这里；需要 velocity、CellRank、Palantir、Slingshot、scTour、VIA/StaVIA 或多方法对比，用 single_cell_trajectory_pro

### single_cell_trajectory_pro
- Name: Single-cell Trajectory Pro
- Tier: pro
- Category: single_cell_analysis
- Summary: 单细胞轨迹 Pro —— DPT/PAGA、Monocle2、Slingshot、Palantir、scTour、VIA/StaVIA、CellRank/velocity
- Skills: single-cell-trajectory-inference, single-cell-publication-plots, single-cell-report-authoring, report-html-generation, notebook-export
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, skill, team, plan, think, task, memory
- Use when: 用于进阶轨迹推断：多方法对比、Slingshot/Palantir/scTour/VIA/StaVIA、RNA velocity、CellRank 命运、动态基因或完整轨迹报告；只用 PAGA/Monocle 的免费路径走 single_cell_trajectory_free

### single_ev_analyst_pro
- Name: Single-EV Proteomics Analyst Pro
- Tier: pro
- Category: general_omics_analysis
- Summary: 单囊泡(single-EV/外泌体)蛋白组端到端分析 —— per-EV 蛋白矩阵 (PBA 计数 / ExoView 强度 / Simoa 二值 / NanoFCM) → QC → 污染评分 → MISEV 标记 → 归一 → 亚群聚类 → 注释 → 共定位/组合 → 差异 → REPORT.html
- Skills: single-ev-proteomics, single-cell-preprocessing, gsea-enrichment, data-io-loading, figure-programmatic, single-cell-report-authoring, report-html-generation, notebook-export, office-tools, retraction-check
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory
- Use when: 拿到单个外泌体/EV 分辨率的蛋白测量 (每行=一个囊泡，不是 bulk EV 制备)，要做质控、污染评估、MISEV 标记、单囊泡归一、亚群聚类、共定位、差异分析并出报告

### spatial_epigenomics_analyst
- Name: Spatial Epigenomics Analyst
- Tier: pro
- Category: spatial_analysis
- Summary: 空间表观基因组分析 —— 空间 ATAC / DBiT-seq 端到端：tixel QC → 基因活性矩阵 → iterative LSI（非 PCA）→ 多切片整合 → 空间聚类/域 → chromVAR motif 活性 → peak-to-gene → 空间出图 → REPORT.html；全程走 epione
- Skills: spatial-epigenomics, spatial-multisample-integration, spatial-pseudobulk, spatial-data-io-loading, spatial-domain-detection, spatial-publication-plots, scatac-chromvar, scatac-peak-to-gene, tf-footprinting, gene-id-conversion, report-html-generation, notebook-export, office-tools
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory
- Use when: 拿到空间分辨的染色质可及性数据 —— AtlasXomics 空间 ATAC / DBiT-seq、tixel×peak 或 tixel×gene-activity 矩阵（带 obsm['spatial'] 坐标），或 fragments + 空间 barcode 布局 —— 要做 QC、降维聚类、空间域、基因活性、chromVAR 转录因子活性、跨切片整合，或样本组间差异可及性/motif 活性。不是 scRNA 空间表达（→ spatial_omics_orchestrator），不是非空间 scATAC（→ single_cell_epigenomics_analyst），不是 bulk ATAC/ChIP（→ bulk_epigenomics_analyst）。

### spatial_omics_orchestrator
- Name: Spatial Omics Orchestrator
- Tier: pro
- Category: spatial_analysis
- Summary: 空间转录组端到端 —— Visium/Xenium/CosMx → QC → 空间图 → 域检测 → SVG → 空间出图 → 报告
- Skills: spatial-data-io-loading, spatial-domain-detection, spatial-variable-genes, spatial-deconvolution, spatial-publication-plots, gene-id-conversion, report-html-generation, notebook-export, office-tools
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory
- Use when: 拿到 SpaceRanger outs/ 或空间 .h5ad，要做 tissue domain 检测、空间可变基因、scRNA 参考反卷积、空间出图（细胞通讯 / 多切片整合见 Phase 2）

### statistical_genetics_analyst
- Name: Statistical Genetics Analyst
- Tier: plus
- Category: general_omics_analysis
- Summary: 统计遗传学专家 —— GWAS 关联、eQTL 定位、SuSiE 精细定位、GWAS×eQTL 共定位、孟德尔随机化、TWAS、LDSC 遗传力、scDRS 单细胞疾病相关性,全程 ov.genetics
- Skills: gwas-eqtl-analysis, gene-id-conversion, data-io-loading, sample-metadata-alignment, gsea-enrichment, figure-programmatic, report-html-generation, notebook-export, office-tools
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory
- Use when: 拿到 GWAS summary statistics、基因型数据(PLINK .bed/.bim/.fam、VCF、dosage 矩阵),或要做 eQTL 定位、精细定位(credible set / PIP)、GWAS 与 eQTL 共定位、孟德尔随机化(暴露→结局的因果)、TWAS、SNP 遗传力 / 遗传相关(LD score regression)、scDRS 找疾病相关细胞类型。不是体细胞 / 癌症突变表的频率·富集分析(→ tabular_genomics_analyst),不是蛋白氨基酸突变的功能 / 致病效应(→ variant_analyst),不是表达矩阵的差异表达(→ bulk_rna_analyst)。

### structural_biologist
- Name: Structural Biologist
- Tier: plus
- Category: structural_biology
- Summary: 结构生物学通才 — 单链折叠、结构搜索、复合物预测、小分子对接，回答 "这是什么蛋白 / 它长什么样 / 跟什么相互作用" 这类一般性结构问题
- Skills: protein-hardware-probe, protein-single-chain-fold, protein-structure-search, protein-complex-affinity, protein-small-molecule-dock
- Toolsets: file_manager, python_interpreter, plan, think, task, skill, memory
- Use when: 用户问 "fold this sequence" / "what protein is this PDB" / "predict the structure of this complex" / "does this drug bind this protein" / "find proteins like this fold" / "什么 fold 长得像这个

### survey_epidemiology_analyst
- Name: Survey Epidemiology Analyst
- Tier: plus
- Category: general_omics_analysis
- Summary: 复杂抽样流行病学端到端(NHANES / BRFSS / NHIS / MEPS / CHARLS / CHNS / CLHLS / KNHANES / DHS 等)—— 按个体 ID 合并 + 死亡链接 → 设计加权(权重 + 分层 + PSU)→ 加权回归(statsmodels 线性/logistic + 按 PSU 的 cluster-robust = design-based;Cox)+ RCS 剂量反应 + 混合暴露(WQS/qgcomp)+ 亚组/交互/中介 + 敏感性。纯 Python。
- Skills: complex-survey-analysis, survival-analysis, tabular-association-analysis, data-io-loading, data-cleaning, figure-programmatic, report-html-generation, notebook-export
- Toolsets: file_manager, python_interpreter, shell, plan, think, task, skill, memory
- Use when: 拿到任何**复杂抽样调查 / 全国健康调查**数据(NHANES、BRFSS、NHIS、MEPS、CHARLS、CHNS、CLHLS、KNHANES、DHS、SHARE/ELSA 等),做暴露↔结局关联、加权患病率或死亡分析 —— 多周期/多波合并、**按抽样设计加权(权重 + 分层 strata + PSU/cluster)**、加权回归(线性/logistic/Cox)、剂量反应 RCS、环境混合暴露(WQS/qgcomp)、亚组交互、中介、加权 Kaplan-Meier、敏感性。典型词:NHANES、CHARLS、抽样权重、WTMEC2YR、SDMVSTRA、SDMVPSU、_LLCPWT、v005、survey-weighted、加权患病率、PhenoAge/生物学年龄、PFAS/重金属暴露组。**关键判据:数据来自复杂概率抽样、必须做 design-based 推断(权重 + 分层 + PSU)。边界:** 不是表达矩阵差异表达(→ bulk_rna_analyst);不是 GWAS / eQTL / 孟德尔随机化 / 遗传力(→ statistical_genetics_analyst);**不是无抽样设计的普通 tidy 表关联**(直接 corr/回归、无需设计加权的 → tabular_genomics_analyst);**不是空间转录组的 tissue domain / niche / 邻域(neighborhood)/ 细胞通讯分析** —— 这里的"domain / 亚组 / 交互"指抽样调查里的 analytic 子人群与统计交互项,不是组织空间域或空间生态位(空间域 / niche → spatial_omics_orchestrator;单细胞 niche / 通讯 → single_cell_downstream_analyst_pro)。

### tabular_genomics_analyst
- Name: Tabular Genomics Analyst
- Tier: pro
- Category: general_omics_analysis
- Summary: 表格基因组学分析 —— 临床/组学数据表的统计关联(相关、偏相关、交互效应、多特征关联)与体细胞突变分析(频率、TMB、富集、共现、通路聚合)
- Skills: tabular-association-analysis, somatic-mutation-analysis, survival-analysis, multi-omics-integration, gene-id-conversion, data-io-loading, data-cleaning, gsea-enrichment, figure-programmatic, report-html-generation, notebook-export, office-tools
- Toolsets: file_manager, python_interpreter, shell, plan, think, task, skill, memory
- Use when: 拿到 tidy 数据表、直接在表上做统计 —— 临床表型表、per-sample 标量汇总(纯度 / 评分 / 签名分数等单值列)、MAF/突变表,**或已经算好的结果表(DE 结果表、每特征 / 每条件 / 每组织的统计量或 score 表)**。做关联 / 相关 / 偏相关检验、交互效应、亚组比例;**跨集合 / 跨条件的相关与相似度(overlap / Jaccard)及其聚合**;体细胞突变的频率 / TMB / 富集 / 共现 / 通路聚合。**关键判据:输入本身就是表格、你直接在表上统计,不需要从一个基因 × 样本表达矩阵建模。** 一个**整个表达矩阵(数千基因 × 样本)**的基因-性状关联**不归这里** —— 即使措辞是"哪些基因与 X 相关",只要输入是表达矩阵、要从中推导差异表达,那是 RNA-seq 任务,交给 bulk_rna_analyst。也不是 counts 矩阵的差异表达,不是单变异功能效应预测。**也不是 DNA 甲基化 / 表观基因组的区域分析** —— per-CpG 甲基化 beta 矩阵、差异甲基化(DMC/DMR)、启动子 / 基因体 / enhancer / CpG island 的甲基化、或甲基化随基因组距离的分布,需要基因组坐标 / 区域注释 / 表观遗传学判断(enhancer 用激活标记而非抑制标记、覆盖度过滤等),即使输入是 (chr,start)×样本的矩阵或多组学整合也不归这里,交给 bulk_epigenomics_analyst。

### variant_analyst
- Name: Variant Analyst
- Tier: plus
- Category: structural_biology
- Summary: 蛋白突变效应分析 — 临床致病性（AlphaMissense + ClinVar）和研究 fitness（ESM-2 zero-shot LLR）两种语境下的突变评分，含 ACMG 阈值校准
- Skills: protein-hardware-probe, protein-variant-effect, protein-single-chain-fold, protein-structure-search
- Toolsets: file_manager, python_interpreter, plan, think, task, skill, memory
- Use when: 用户问 "这个突变致病吗" / "score 50 mutations on my protein" / "DMS 之前哪些位点最敏感" / "BRCA1 R175H 在 ClinVar 里有报道吗" / "我的 binder 上每个 cysteine 突变成 serine 会怎样

### vertical_agent_selector
- Name: Vertical Agent Selector
- Tier: community
- Category: orchestration
- Summary: 在正式分析前，把每条自然语言请求路由给最合适的专业 agent
- Skills:
- Toolsets: team
- Use when: 作为默认入口，把应当交给某个 manifest 注册的垂直 agent 处理的请求分派出去
