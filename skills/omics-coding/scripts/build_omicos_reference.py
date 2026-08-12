#!/usr/bin/env python3
"""Build the OmicOS internal reference layer for omics-coding."""

import csv
import json
import re
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROOT_REFERENCES = ROOT / "references"
SOURCE = Path(
    "/hwdata/home/jinqc/omicos-workspace/omicos/"
    "recovered/omicverse_skills/skills"
)
AGENT_SOURCE = Path(
    "/hwdata/home/jinqc/omicos-workspace/omicos/"
    "recovered/runtime_api/agents.json"
)
AGENT_PUBLIC_SOURCE = Path(
    "/hwdata/home/jinqc/omicos-workspace/omicos/"
    "recovered/public_cloud_agents"
)
AGENT_INDEX_SOURCE = Path(
    "/hwdata/home/jinqc/omicos-workspace/omicos/"
    "recovered/AGENTS_INDEX.md"
)
AGENT_ROSTER_SOURCE = Path(
    "/hwdata/home/jinqc/omicos-workspace/omicos/"
    "recovered/SYSTEM_PROMPT_AGENT_ROSTER.md"
)
REFERENCES = ROOT / "references" / "omicos"
RAW = REFERENCES / "raw_skills"
ROUTE_CARDS = REFERENCES / "route_cards"
INDEX = REFERENCES / "skill_index.tsv"
RAW_AGENTS = REFERENCES / "raw_agents"
AGENT_ROUTE_CARDS = REFERENCES / "agent_route_cards"
AGENT_INDEX = REFERENCES / "agent_index.tsv"
POLICY = REFERENCES / "integration_policy.md"
REFERENCE_INDEX = ROOT / "references" / "index.md"

EXPECTED_COUNT = 60
EXPECTED_AGENT_COUNT = 32
RAW_SAFETY_BANNER = """<!-- omics-coding-omicos-raw-safety
This file is preserved source material from OmicOS for audit and reference.
It is not a callable authority layer for omics-coding.
Before using any workflow, function, parameter, statistic, or plot idea from
this file, return to omics-coding gates: OmicVerse/SCOP docs first, official
tutorial/API docs when needed, Analysis-Native Visualization Gate for figures,
and Formal Analysis Route Confirmation before formal code or analysis runs.
-->

"""
RAW_AGENT_SAFETY_README = """# OmicOS Raw Agent Sources

<!-- omics-coding-omicos-agent-raw-safety -->

These files are preserved source material from OmicOS for audit and reference.
They are not callable authority docs for `omics-coding`.

Use `agent_index.tsv` and `agent_route_cards/*.md` only as routing and handoff
reminders after OmicVerse/SCOP function docs, official tutorial/API docs, and
Formal Analysis Route Confirmation have been checked.
"""


POLICIES = {
    "biocontext-knowledge": {
        "domain": "knowledge_annotation",
        "route_role": "candidate_reminder",
        "object_route": "gene_list_or_query_terms",
        "primary_authority": "OmicVerse/SCOP function docs plus upstream database docs",
        "requires_official_confirmation": "conditional",
        "risk_note": "Use as annotation support only; database facts need source-aware reporting.",
    },
    "bulk-celltype-deconvolution": {
        "domain": "bulk_deconvolution",
        "route_role": "route_card",
        "object_route": "bulk_matrix_plus_single_cell_reference",
        "primary_authority": "OmicVerse/SCOP function docs and selected backend official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Backend choice changes assumptions; confirm paired reference and output fraction semantics.",
    },
    "bulk-combat-correction": {
        "domain": "bulk_batch_correction",
        "route_role": "route_card",
        "object_route": "bulk_expression_matrix",
        "primary_authority": "OmicVerse/SCOP function docs and pyComBat official docs if used",
        "requires_official_confirmation": "always",
        "risk_note": "Batch correction can remove biology; require design columns before running.",
    },
    "bulk-deg-analysis": {
        "domain": "bulk_differential_expression",
        "route_role": "route_card",
        "object_route": "bulk_expression_matrix",
        "primary_authority": "OmicVerse/SCOP function docs and DESeq2 or PyDESeq2 official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Do not mix normalized and count-scale inputs without confirming method requirements.",
    },
    "bulk-deseq2-analysis": {
        "domain": "bulk_differential_expression",
        "route_role": "route_card",
        "object_route": "bulk_count_matrix",
        "primary_authority": "OmicVerse/SCOP function docs and PyDESeq2 official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Confirm raw counts, contrast, design, and independent filtering behavior.",
    },
    "bulk-metabol-multivariate": {
        "domain": "metabolomics_multivariate",
        "route_role": "route_card",
        "object_route": "metabolomics_anndata",
        "primary_authority": "OmicVerse function docs and metabolomics method docs",
        "requires_official_confirmation": "always",
        "risk_note": "PLS/OPLS can overfit; require nested validation or permutation when used for claims.",
    },
    "bulk-metabol-pathway-multifactor": {
        "domain": "metabolomics_pathway_multifactor",
        "route_role": "route_card",
        "object_route": "metabolomics_anndata",
        "primary_authority": "OmicVerse function docs and pathway database docs",
        "requires_official_confirmation": "always",
        "risk_note": "Pathway and multifactor claims need metadata design checked before analysis.",
    },
    "bulk-metabol-preprocessing": {
        "domain": "metabolomics_preprocessing",
        "route_role": "route_card",
        "object_route": "metabolomics_peak_table",
        "primary_authority": "OmicVerse function docs and preprocessing method docs",
        "requires_official_confirmation": "always",
        "risk_note": "Imputation, normalization, and transformation choices must be declared before downstream tests.",
    },
    "bulk-metabol-untargeted-lipidomics": {
        "domain": "metabolomics_lipidomics",
        "route_role": "route_card",
        "object_route": "mz_rt_or_lipidomics_feature_table",
        "primary_authority": "OmicVerse function docs and metabolomics database docs",
        "requires_official_confirmation": "always",
        "risk_note": "Annotation confidence and adduct matching must not be reported as definitive identity.",
    },
    "bulk-stringdb-ppi": {
        "domain": "ppi_network",
        "route_role": "route_card",
        "object_route": "gene_or_protein_list",
        "primary_authority": "OmicVerse/SCOP function docs and STRING official docs",
        "requires_official_confirmation": "always",
        "risk_note": "STRING edges are database evidence, not direct experimental proof for this dataset.",
    },
    "bulk-to-single-deconvolution": {
        "domain": "bulk_to_single",
        "route_role": "route_card",
        "object_route": "bulk_matrix_plus_single_cell_reference",
        "primary_authority": "OmicVerse function docs",
        "requires_official_confirmation": "always",
        "risk_note": "Synthetic single cells need explicit validation against reference distributions.",
    },
    "bulk-trajblend-interpolation": {
        "domain": "bulk_trajectory_interpolation",
        "route_role": "candidate_reminder",
        "object_route": "bulk_and_single_cell_developmental_series",
        "primary_authority": "OmicVerse function docs and method paper or official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Generated intermediate states are model outputs, not directly observed cells.",
    },
    "bulk-wgcna-analysis": {
        "domain": "bulk_coexpression_network",
        "route_role": "route_card",
        "object_route": "bulk_expression_matrix_with_traits",
        "primary_authority": "OmicVerse/SCOP function docs and WGCNA official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Module-trait associations require sample-level design and multiple-testing handling.",
    },
    "cross-modal-celltype-transfer": {
        "domain": "cross_modal_label_transfer",
        "route_role": "route_card",
        "object_route": "reference_anndata_plus_query_anndata",
        "primary_authority": "OmicVerse function docs",
        "requires_official_confirmation": "always",
        "risk_note": "Shared embedding and feature overlap must be checked before transfer.",
    },
    "data-export-excel": {
        "domain": "export",
        "route_role": "glue_helper",
        "object_route": "tables",
        "primary_authority": "project output contract and library docs",
        "requires_official_confirmation": "not_core_analysis",
        "risk_note": "Export only; must not decide biological methods.",
    },
    "data-export-pdf": {
        "domain": "export",
        "route_role": "glue_helper",
        "object_route": "report_assets",
        "primary_authority": "project output contract and library docs",
        "requires_official_confirmation": "not_core_analysis",
        "risk_note": "Export only; use academic-html-report for scientific HTML closeout when required.",
    },
    "data-io-loading": {
        "domain": "data_io",
        "route_role": "glue_helper",
        "object_route": "h5ad_10x_spatial_csv",
        "primary_authority": "OmicVerse/SCOP function docs and project input contract",
        "requires_official_confirmation": "conditional",
        "risk_note": "Read/write helpers are allowed, but object schema still needs validation.",
    },
    "datasets-loading": {
        "domain": "demo_datasets",
        "route_role": "glue_helper",
        "object_route": "built_in_demo_dataset",
        "primary_authority": "OmicVerse/SCOP function docs",
        "requires_official_confirmation": "not_core_analysis",
        "risk_note": "Demo datasets are for smoke tests, not a substitute for user data.",
    },
    "data-stats-analysis": {
        "domain": "generic_statistics",
        "route_role": "fallback_only",
        "object_route": "generic_table",
        "primary_authority": "analysis package docs or statistical library docs after native gap",
        "requires_official_confirmation": "conditional",
        "risk_note": "Generic stats must not replace package-native differential or enrichment methods.",
    },
    "data-transform": {
        "domain": "data_wrangling",
        "route_role": "glue_helper",
        "object_route": "generic_table",
        "primary_authority": "project data contract",
        "requires_official_confirmation": "conditional",
        "risk_note": "Use only for metadata or table reshape. Expression normalization, filtering, scaling, log transform, CPM, or other matrix-changing transforms require OmicVerse/SCOP or a confirmed official route.",
    },
    "data-viz-plots": {
        "domain": "generic_visualization",
        "route_role": "fallback_only",
        "object_route": "generic_table_or_array",
        "primary_authority": "analysis-native plotting docs after native options are rejected",
        "requires_official_confirmation": "conditional",
        "risk_note": "Custom matplotlib/seaborn must not replace core evidence plots without the visualization gate.",
    },
    "fastq-analysis": {
        "domain": "fastq_alignment",
        "route_role": "route_card",
        "object_route": "sra_fastq_reference_genome",
        "primary_authority": "OmicVerse function docs and aligner official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Raw FASTQ workflows require reference genome, chemistry, and output matrix contract.",
    },
    "fm-foundation-models": {
        "domain": "foundation_models",
        "route_role": "candidate_reminder",
        "object_route": "anndata_or_cells_for_embedding",
        "primary_authority": "OmicVerse function docs and model official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Foundation model outputs need version, checkpoint, species, and training-domain checks.",
    },
    "gsea-enrichment": {
        "domain": "enrichment",
        "route_role": "route_card",
        "object_route": "ranked_gene_list_or_deg_table",
        "primary_authority": "OmicVerse/SCOP function docs and gene set database docs",
        "requires_official_confirmation": "always",
        "risk_note": "Gene ID space, ranking statistic, and gene set source must be checked.",
    },
    "microbiome-16s-amplicon-dada2": {
        "domain": "microbiome_16s",
        "route_role": "route_card",
        "object_route": "amplicon_fastq_or_asv_table",
        "primary_authority": "OmicVerse function docs and DADA2 or vsearch official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Primer, denoising, taxonomy, and sample metadata choices define the result.",
    },
    "microbiome-da-comparison": {
        "domain": "microbiome_differential_abundance",
        "route_role": "route_card",
        "object_route": "microbiome_anndata",
        "primary_authority": "OmicVerse function docs and DA method official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Zero inflation and compositionality can change which method is defensible.",
    },
    "microbiome-meta-analysis": {
        "domain": "microbiome_meta_analysis",
        "route_role": "route_card",
        "object_route": "multi_cohort_microbiome_results",
        "primary_authority": "OmicVerse function docs and meta-analysis method docs",
        "requires_official_confirmation": "always",
        "risk_note": "Cohort heterogeneity must be reported, not averaged away.",
    },
    "microbiome-phylogeny": {
        "domain": "microbiome_phylogeny",
        "route_role": "route_card",
        "object_route": "asv_sequences_or_asv_table",
        "primary_authority": "OmicVerse function docs and phylogeny tool docs",
        "requires_official_confirmation": "always",
        "risk_note": "Tree-aware metrics require a valid ASV tree linked to the same features.",
    },
    "micro-metabol-paired": {
        "domain": "microbiome_metabolomics_integration",
        "route_role": "route_card",
        "object_route": "paired_microbiome_and_metabolomics_anndata",
        "primary_authority": "OmicVerse function docs and selected integration method docs",
        "requires_official_confirmation": "always",
        "risk_note": "Sample pairing and modality-specific normalization must be verified before integration.",
    },
    "plotting-visualization": {
        "domain": "omicverse_visualization",
        "route_role": "candidate_reminder",
        "object_route": "analysis_result_or_anndata",
        "primary_authority": "OmicVerse/SCOP plotting function docs",
        "requires_official_confirmation": "conditional",
        "risk_note": "Treat as a reminder to find native plotting docs, not as a standalone plotting authority.",
    },
    "reference-label-transfer": {
        "domain": "reference_label_transfer",
        "route_role": "route_card",
        "object_route": "reference_anndata_plus_query_anndata",
        "primary_authority": "OmicVerse function docs",
        "requires_official_confirmation": "always",
        "risk_note": "Reference labels, shared features, and transfer backend must match the biological question.",
    },
    "single-cell-annotation": {
        "domain": "single_cell_annotation",
        "route_role": "route_card",
        "object_route": "annotated_or_clustered_anndata",
        "primary_authority": "OmicVerse/SCOP function docs and backend official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Automated labels need marker-level sanity checks before biological claims.",
    },
    "single-cell-batch-integration": {
        "domain": "single_cell_integration",
        "route_role": "route_card",
        "object_route": "preprocessed_anndata_with_batch",
        "primary_authority": "OmicVerse/SCOP function docs and selected backend official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Integration can erase biology; require batch and condition separation check.",
    },
    "single-cell-cellmatch-ontology": {
        "domain": "cell_ontology_mapping",
        "route_role": "route_card",
        "object_route": "cell_type_labels",
        "primary_authority": "OmicVerse function docs and Cell Ontology source docs",
        "requires_official_confirmation": "always",
        "risk_note": "Ontology mapping standardizes labels; it does not validate the original annotation.",
    },
    "single-cell-cellphonedb-communication": {
        "domain": "cell_cell_communication",
        "route_role": "route_card",
        "object_route": "annotated_anndata",
        "primary_authority": "OmicVerse function docs and CellPhoneDB official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Communication results are inference from expression; require sender/receiver and visualization semantics.",
    },
    "single-cell-cellrank-fate": {
        "domain": "cell_fate",
        "route_role": "route_card",
        "object_route": "velocity_anndata",
        "primary_authority": "OmicVerse function docs and CellRank official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Requires valid velocity graph; fate probabilities are model outputs.",
    },
    "single-cell-cellvote-consensus": {
        "domain": "single_cell_annotation_consensus",
        "route_role": "route_card",
        "object_route": "multiple_annotation_results",
        "primary_authority": "OmicVerse function docs and annotator backend docs",
        "requires_official_confirmation": "always",
        "risk_note": "Consensus can hide systematic annotator bias; inspect disagreements.",
    },
    "single-cell-clustering-backends": {
        "domain": "single_cell_clustering",
        "route_role": "route_card",
        "object_route": "prepared_anndata_embedding",
        "primary_authority": "OmicVerse/SCOP function docs",
        "requires_official_confirmation": "always",
        "risk_note": "Clustering resolution and embedding choice must be tied to the question.",
    },
    "single-cell-cnmf-program-discovery": {
        "domain": "gene_program_discovery",
        "route_role": "route_card",
        "object_route": "normalized_single_cell_anndata",
        "primary_authority": "OmicVerse function docs and cNMF method docs",
        "requires_official_confirmation": "always",
        "risk_note": "Program number and stability must be checked before naming gene programs.",
    },
    "single-cell-cytotrace2": {
        "domain": "developmental_potency",
        "route_role": "route_card",
        "object_route": "single_cell_anndata",
        "primary_authority": "OmicVerse function docs and CytoTRACE2 official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Potency score is a model estimate and species/preprocessing dependent.",
    },
    "single-cell-differential-abundance": {
        "domain": "single_cell_differential_abundance",
        "route_role": "route_card",
        "object_route": "annotated_anndata_with_samples",
        "primary_authority": "OmicVerse/SCOP function docs and selected method official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Use sample-level design; pooled cells are not biological replicates.",
    },
    "single-cell-differential-expression": {
        "domain": "single_cell_differential_expression",
        "route_role": "route_card",
        "object_route": "annotated_anndata_with_groups",
        "primary_authority": "OmicVerse/SCOP function docs and selected method official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Confirm contrast, cell type scope, covariates, and replicate strategy.",
    },
    "single-cellfate-analysis": {
        "domain": "cell_fate",
        "route_role": "candidate_reminder",
        "object_route": "pseudotime_or_lineage_anndata",
        "primary_authority": "OmicVerse function docs and method docs",
        "requires_official_confirmation": "always",
        "risk_note": "Lineage and pseudotime assumptions must be verified before gene trend claims.",
    },
    "single-cell-kb-alignment": {
        "domain": "single_cell_fastq_quantification",
        "route_role": "route_card",
        "object_route": "single_cell_fastq_reference",
        "primary_authority": "OmicVerse function docs and kallisto|bustools official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Chemistry, reference, and barcode handling determine count matrix validity.",
    },
    "single-cell-lda-topic-clustering": {
        "domain": "topic_model_clustering",
        "route_role": "route_card",
        "object_route": "count_like_anndata",
        "primary_authority": "OmicVerse function docs and MIRA official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Topic number and count scale must be checked before interpreting topics.",
    },
    "single-cell-liana-communication": {
        "domain": "cell_cell_communication",
        "route_role": "route_card",
        "object_route": "annotated_anndata",
        "primary_authority": "OmicVerse function docs and LIANA official docs",
        "requires_official_confirmation": "always",
        "risk_note": "LIANA score semantics and OmicVerse wrapper parameters must be read before plotting.",
    },
    "single-cell-metatime-annotation": {
        "domain": "tumor_microenvironment_annotation",
        "route_role": "route_card",
        "object_route": "tumor_single_cell_anndata",
        "primary_authority": "OmicVerse function docs and MetaTiME source docs",
        "requires_official_confirmation": "always",
        "risk_note": "Pretrained components are tumor-context specific; inspect marker support.",
    },
    "single-cell-monocle2-trajectory": {
        "domain": "trajectory",
        "route_role": "route_card",
        "object_route": "annotated_anndata",
        "primary_authority": "OmicVerse function docs and Monocle official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Root state and branch definition must be biologically justified.",
    },
    "single-cell-preprocessing": {
        "domain": "single_cell_preprocessing",
        "route_role": "route_card",
        "object_route": "raw_or_loaded_anndata",
        "primary_authority": "OmicVerse/SCOP function docs",
        "requires_official_confirmation": "always",
        "risk_note": "QC thresholds, normalization, HVG, PCA, neighbors, and clustering must be planned before running.",
    },
    "single-cell-rna-velocity": {
        "domain": "rna_velocity",
        "route_role": "route_card",
        "object_route": "spliced_unspliced_anndata",
        "primary_authority": "OmicVerse function docs and velocity backend official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Velocity requires compatible layers and model assumptions; do not infer direction without checks.",
    },
    "single-cell-scenic": {
        "domain": "gene_regulatory_network",
        "route_role": "route_card",
        "object_route": "single_cell_anndata_plus_motif_resources",
        "primary_authority": "OmicVerse function docs and SCENIC resource docs",
        "requires_official_confirmation": "always",
        "risk_note": "Resource species, motif database, and GRN backend determine regulon credibility.",
    },
    "single-cell-sctour-trajectory": {
        "domain": "trajectory",
        "route_role": "route_card",
        "object_route": "raw_count_anndata",
        "primary_authority": "OmicVerse function docs and scTour official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Use only when scTour assumptions match raw-count input and trajectory question.",
    },
    "single-cell-trajectory-inference": {
        "domain": "trajectory",
        "route_role": "route_card",
        "object_route": "cluster_ready_anndata",
        "primary_authority": "OmicVerse/SCOP function docs and selected method official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Branch method choice must match topology and biological starting point.",
    },
    "single-cell-via-trajectory": {
        "domain": "trajectory",
        "route_role": "route_card",
        "object_route": "anndata_with_optional_velocity",
        "primary_authority": "OmicVerse function docs and VIA official docs",
        "requires_official_confirmation": "always",
        "risk_note": "VIA terminal states and velocity weighting need explicit sensitivity checks.",
    },
    "single-downstream-analysis": {
        "domain": "single_cell_downstream",
        "route_role": "candidate_reminder",
        "object_route": "processed_anndata",
        "primary_authority": "OmicVerse/SCOP function docs",
        "requires_official_confirmation": "always",
        "risk_note": "Mixed downstream menu; choose one verified method per question, not a bundle.",
    },
    "single-multiomics": {
        "domain": "single_cell_multiomics",
        "route_role": "route_card",
        "object_route": "paired_or_unpaired_multiome_objects",
        "primary_authority": "OmicVerse/SCOP function docs and selected method official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Modality pairing, feature mapping, and integration objective must be explicit.",
    },
    "single-popv-annotation": {
        "domain": "population_level_annotation",
        "route_role": "route_card",
        "object_route": "query_anndata_plus_reference_or_hub",
        "primary_authority": "OmicVerse function docs and PopV official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Consensus labels need reference provenance and confidence inspection.",
    },
    "single-to-spatial-mapping": {
        "domain": "single_to_spatial_mapping",
        "route_role": "route_card",
        "object_route": "single_cell_reference_plus_spatial_object",
        "primary_authority": "OmicVerse/SCOP function docs and selected mapping method docs",
        "requires_official_confirmation": "always",
        "risk_note": "Spot/cell resolution and marker validation must be checked before spatial claims.",
    },
    "spatial-tutorials": {
        "domain": "spatial_transcriptomics",
        "route_role": "route_card",
        "object_route": "visium_hd_stereo_slideseq_or_spatial_anndata",
        "primary_authority": "OmicVerse/SCOP function docs and platform official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Platform geometry, image registration, deconvolution, and native plotting route must be confirmed.",
    },
    "tcga-preprocessing": {
        "domain": "tcga_preprocessing",
        "route_role": "route_card",
        "object_route": "tcga_expression_and_clinical_archives",
        "primary_authority": "OmicVerse function docs and GDC/TCGA official docs",
        "requires_official_confirmation": "always",
        "risk_note": "Sample barcode handling and clinical endpoint definitions must be verified.",
    },
}


FORBIDDEN_AGENT_IDS = {
    "antibody_engineer",
    "binder_designer",
    "cell_viewer",
    "clinical_translator_free",
    "clinical_translator_pro",
    "humanize",
    "ihc_if_quantifier",
    "imagej",
    "literature_free",
    "literature_pro",
    "memory_curator",
    "molecule_viewer",
    "nvidia_bionemo_nim",
    "omicverse_omni",
    "paper_critic",
    "pathology_lazyslide",
    "phase_separation_analyst",
    "primer_design_assistant",
    "quality_review",
    "review_writer_pro",
    "scientific_writer",
    "structural_biologist",
    "survey_epidemiology_analyst",
    "variant_analyst",
    "vertical_agent_selector",
}

COMMON_AGENT_AUTHORITY = "OmicVerse/SCOP function docs plus official package/tutorial docs"

AGENT_POLICIES = {
    "GEO-everything": {
        "agent_role": "data_acquisition",
        "route_role": "route_card",
        "primary_authority": "public archive docs plus OmicVerse/SCOP data-loading docs",
        "requires_official_confirmation": "always",
        "not_for": "Not for QC, normalization, DEG, spatial downstream, or biological interpretation after files are landed.",
        "handoff": "Hand off landed matrices/files to single-cell, bulk, spatial, microbiome, proteomics, or other specialist routes.",
        "risk_note": "Data acquisition stops at files and metadata; downstream analysis must use specialist route cards and official docs.",
    },
    "analysis_strategist": {
        "agent_role": "strategy_planning",
        "route_role": "candidate_reminder",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for executing code, selecting final parameters, or bypassing specialist route confirmation.",
        "handoff": "Hand off each proposed stage to the matching specialist agent card and verified package docs.",
        "risk_note": "Strategy proposals are hypotheses; every stage still needs official source review and user confirmation.",
    },
    "bulk_epigenomics_analyst": {
        "agent_role": "general_omics_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for single-cell ATAC, spatial epigenomics, or structural variant interpretation without a matching specialist route.",
        "handoff": "Hand off single-cell epigenomics to single_cell_epigenomics_analyst and spatial assays to spatial_epigenomics_analyst.",
        "risk_note": "Assay type, genome build, feature definition, normalization, and peak or bin provenance define valid conclusions.",
    },
    "bulk_rna_analyst": {
        "agent_role": "general_omics_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for raw scRNA matrices, generic result-table statistics, or spatial transcriptomics downstream.",
        "handoff": "Hand off scRNA to single_cell_preprocessor and existing result tables to tabular_genomics_analyst.",
        "risk_note": "Counts versus TPM, design matrix, contrasts, batch variables, and replicate structure define the valid route.",
    },
    "cancer_dependency_analyst": {
        "agent_role": "general_omics_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for unvalidated causal claims or clinical actionability without external evidence.",
        "handoff": "Hand off expression, mutation, or pathway-specific substeps to the relevant omics route card.",
        "risk_note": "Screen design, dependency score model, lineage covariates, and batch structure must be declared before claims.",
    },
    "chromatin_3d_analyst": {
        "agent_role": "general_omics_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for ordinary bulk epigenomics or single-cell epigenomics when no 3D chromatin data are present.",
        "handoff": "Hand off non-3D epigenomics to bulk_epigenomics_analyst or single_cell_epigenomics_analyst.",
        "risk_note": "Resolution, genome build, binning, normalization, and loop or domain caller choices determine interpretation.",
    },
    "immune_repertoire_analyst_pro": {
        "agent_role": "general_omics_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for ordinary transcriptome annotation unless receptor clonotypes or immune repertoire fields are central.",
        "handoff": "Hand off paired expression analysis to the single-cell or bulk specialist route.",
        "risk_note": "Clonotype definition, receptor chain pairing, sample identity, and diversity metrics change the result semantics.",
    },
    "metabolomics_analyst_pro": {
        "agent_role": "general_omics_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for microbiome-only, transcriptome-only, or proteomics-only analysis without paired metabolomics evidence.",
        "handoff": "Hand off paired microbiome-metabolomics to the matching multi-omics skill route if used.",
        "risk_note": "Feature annotation confidence, imputation, normalization, transformation, and validation design affect every claim.",
    },
    "microbiome_analyst_pro": {
        "agent_role": "general_omics_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for host transcriptomics or metabolomics unless microbiome features are explicitly modeled.",
        "handoff": "Hand off paired host or metabolite analysis to the relevant omics integration route.",
        "risk_note": "Compositionality, zero inflation, taxonomy database, ASV/OTU provenance, and batch effects must be explicit.",
    },
    "phylogenomics_analyst": {
        "agent_role": "phylogenomics_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for generic gene-list enrichment, expression analysis, or structure modeling without phylogenomic inputs.",
        "handoff": "Hand off expression or pathway interpretation to bulk, single-cell, or enrichment route cards.",
        "risk_note": "Orthology, alignment, tree model, genome build, and taxon sampling drive phylogenomic conclusions.",
    },
    "proteomics_analyst_pro": {
        "agent_role": "general_omics_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for RNA expression analysis or metabolomics unless paired proteomics is part of the design.",
        "handoff": "Hand off paired transcriptome, metabolome, or EV-specific steps to the matching route card.",
        "risk_note": "Quantification scale, missingness, normalization, peptide-to-protein rollup, and batch correction are route-defining.",
    },
    "single_ev_analyst_pro": {
        "agent_role": "general_omics_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for general proteomics without EV isolation/provenance or for vesicle biology claims without markers.",
        "handoff": "Hand off general proteomics to proteomics_analyst_pro when EV-specific assumptions are absent.",
        "risk_note": "EV isolation method, marker support, contamination controls, and proteomics missingness determine credibility.",
    },
    "statistical_genetics_analyst": {
        "agent_role": "general_omics_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for expression-matrix DEG or pathway analysis when no genetic association data are present.",
        "handoff": "Hand off downstream expression or functional interpretation to the matching omics specialist route.",
        "risk_note": "Genome build, ancestry, LD reference, covariates, variant QC, and multiple testing define valid inference.",
    },
    "tabular_genomics_analyst": {
        "agent_role": "general_omics_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for raw omics matrices that need preprocessing, normalization, differential testing, or modeling.",
        "handoff": "Hand off raw matrices to the data-type specialist before using table-level statistics.",
        "risk_note": "Use only for existing result tables; raw expression, count, intensity, or peak matrices need specialist routes.",
    },
    "analysis_sanity_review": {
        "agent_role": "review_gate",
        "route_role": "review_only",
        "primary_authority": "project evidence files plus OmicVerse/SCOP and official docs already cited by the route",
        "requires_official_confirmation": "conditional",
        "not_for": "Not for starting a new analysis or choosing methods; only reviews an existing analysis handoff.",
        "handoff": "Return blocking findings to the responsible specialist route before release.",
        "risk_note": "Review can catch omissions but cannot replace rerunning official docs, notebooks, or formal validation commands.",
    },
    "c3ca_phase_runner": {
        "agent_role": "single_cell_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for generic cell-cycle scoring unless c3CA phase workflow is explicitly intended.",
        "handoff": "Hand off upstream QC and clustering to single_cell_preprocessor first.",
        "risk_note": "Phase labels depend on preprocessing, marker sets, species, and cell-state confounders.",
    },
    "cell_cell_communication_free": {
        "agent_role": "single_cell_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for unannotated objects, unsupported species databases, or causal signaling claims.",
        "handoff": "Hand off annotation and preprocessing gaps to single_cell_preprocessor and annotation agents first.",
        "risk_note": "Communication scores are expression-derived inference; sender, receiver, database, and plot semantics need review.",
    },
    "cell_cell_communication_pro": {
        "agent_role": "single_cell_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for unannotated objects, unsupported species databases, or causal signaling claims.",
        "handoff": "Hand off annotation and preprocessing gaps to single_cell_preprocessor and annotation agents first.",
        "risk_note": "Multi-method communication results need database, score, permutation, and visualization semantics checked.",
    },
    "cellchat_rust_h5ad_runner": {
        "agent_role": "single_cell_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for CellChat interpretation when the h5ad schema, species, or cell labels are unconfirmed.",
        "handoff": "Hand off schema and annotation issues before running communication inference.",
        "risk_note": "H5AD schema, species database, cell labels, and CellChat wrapper version control the output semantics.",
    },
    "single_cell_annotator_free": {
        "agent_role": "single_cell_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for final biological labels without marker-level and reference provenance checks.",
        "handoff": "Hand off poor QC or missing clustering to single_cell_preprocessor before annotation.",
        "risk_note": "Automated labels require reference provenance, marker sanity checks, confidence review, and ambiguity reporting.",
    },
    "single_cell_annotator_pro": {
        "agent_role": "single_cell_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for final biological labels without marker-level and reference provenance checks.",
        "handoff": "Hand off poor QC or missing clustering to single_cell_preprocessor before annotation.",
        "risk_note": "Consensus or model labels can hide systematic bias; inspect disagreements and marker support.",
    },
    "single_cell_downstream_analyst_pro": {
        "agent_role": "single_cell_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for raw matrix preprocessing or final annotation when those stages are incomplete.",
        "handoff": "Hand off raw or unannotated objects to preprocessing and annotation route cards first.",
        "risk_note": "Downstream menus must be split into one verified method per question, not run as an unreviewed bundle.",
    },
    "single_cell_epigenomics_analyst": {
        "agent_role": "single_cell_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for scRNA-only workflows or bulk epigenomics without single-cell epigenomic data.",
        "handoff": "Hand off paired scRNA integration to single_cell_preprocessor or single-multiomics skill routes as needed.",
        "risk_note": "Peak set, genome build, fragments, modality pairing, and accessibility normalization determine interpretability.",
    },
    "single_cell_grn_analyst": {
        "agent_role": "single_cell_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for causal TF claims without motif/resource support and sensitivity checks.",
        "handoff": "Hand off preprocessing and annotation gaps before GRN inference.",
        "risk_note": "GRN outputs depend on species resources, motif database, expression scale, and regulator filtering.",
    },
    "single_cell_perturbation_analyst": {
        "agent_role": "single_cell_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for ordinary differential expression if perturbation design, guide assignment, or controls are absent.",
        "handoff": "Hand off non-perturbation scRNA tasks to preprocessing and downstream analysis routes.",
        "risk_note": "Guide calling, perturbation design, replicate structure, controls, and batch define valid perturbation inference.",
    },
    "single_cell_preprocessor": {
        "agent_role": "single_cell_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for bulk RNA-seq, spatial objects, final annotation claims, or downstream biology without specialist handoff.",
        "handoff": "Hand off ready-to-annotate objects to annotation, communication, trajectory, GRN, or downstream route cards.",
        "risk_note": "QC thresholds, normalization, HVG, PCA, integration, neighbors, and clustering must be planned before running.",
    },
    "single_cell_trajectory_free": {
        "agent_role": "single_cell_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for unrelated clustering or final lineage claims without root, topology, and marker validation.",
        "handoff": "Hand off preprocessing and annotation prerequisites before trajectory inference.",
        "risk_note": "Trajectory results depend on root choice, topology, batch effects, cell cycle, and method assumptions.",
    },
    "single_cell_trajectory_pro": {
        "agent_role": "single_cell_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for unrelated clustering or final lineage claims without root, topology, and marker validation.",
        "handoff": "Hand off preprocessing, annotation, or velocity prerequisites before trajectory inference.",
        "risk_note": "Multi-method trajectory or fate models need root, topology, velocity/layer checks, and sensitivity review.",
    },
    "he_to_st_predictor": {
        "agent_role": "spatial_analysis",
        "route_role": "candidate_reminder",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "use_when_override": "Use only as a candidate-search reminder for H&E-to-spatial-transcriptomics questions. Candidate search terms or possible method families include STPath, HEST-FM, STFlow, and iStar, but model choice requires OmicVerse/SCOP and official documentation confirmation before any route is selected.",
        "not_for": "Not for treating predicted spatial expression as measured ST or replacing real spatial transcriptomics QC.",
        "handoff": "Hand off predicted matrices to spatial_omics_orchestrator only with prediction provenance clearly marked.",
        "risk_note": "H&E-derived expression is model output, not measured transcriptomics; report model, training domain, and uncertainty.",
    },
    "spatial_epigenomics_analyst": {
        "agent_role": "spatial_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for standard spatial transcriptomics when no epigenomic modality is present.",
        "handoff": "Hand off transcriptomic-only spatial work to spatial_omics_orchestrator.",
        "risk_note": "Spatial coordinates, epigenomic modality, genome build, feature definition, and registration quality are critical.",
    },
    "spatial_omics_orchestrator": {
        "agent_role": "spatial_analysis",
        "route_role": "route_card",
        "primary_authority": COMMON_AGENT_AUTHORITY,
        "requires_official_confirmation": "always",
        "not_for": "Not for pure scRNA, bulk RNA, or H&E-only prediction without measured or explicitly predicted spatial omics data.",
        "handoff": "Hand off single-cell reference tasks to single-cell specialists and H&E prediction to he_to_st_predictor first.",
        "risk_note": "Platform geometry, image registration, spot or cell resolution, SVGs, deconvolution, and native plots must be confirmed.",
    },
    "reviewer": {
        "agent_role": "review_gate",
        "route_role": "review_only",
        "primary_authority": "project evidence files plus OmicVerse/SCOP and official docs already cited by the route",
        "requires_official_confirmation": "conditional",
        "not_for": "Not for direct user routing, new analysis execution, or method selection.",
        "handoff": "Return pass, warning, or fail findings to the responsible route owner before release.",
        "risk_note": "Independent review reduces hallucination risk but does not replace reproducible commands or source verification.",
    },
}


def fail(message):
    print("FAIL: %s" % message)
    raise SystemExit(1)


def ensure_references_base():
    skill_root_resolved = ROOT.resolve()
    if ROOT_REFERENCES.exists() and ROOT_REFERENCES.is_symlink():
        fail("refusing to use symlink references directory: %s" % ROOT_REFERENCES)
    root_references_resolved = ROOT_REFERENCES.resolve()
    prefix = str(skill_root_resolved) + "/"
    if not str(root_references_resolved).startswith(prefix):
        fail("refusing references directory outside skill root: %s" % root_references_resolved)
    if REFERENCES.exists() and REFERENCES.is_symlink():
        fail("refusing to use symlink references/omicos directory: %s" % REFERENCES)
    if REFERENCES.parent.resolve() != root_references_resolved:
        fail("refusing unexpected OmicOS parent directory: %s" % REFERENCES.parent)
    if REFERENCES.exists():
        references_resolved = REFERENCES.resolve()
        prefix = str(root_references_resolved) + "/"
        if not str(references_resolved).startswith(prefix):
            fail("refusing references/omicos outside skill references directory: %s" % references_resolved)


def atomic_write_text(path, text):
    if path.exists() and path.is_symlink():
        fail("refusing to overwrite symlink file: %s" % path)
    tmp = path.with_name(".%s.tmp" % path.name)
    if tmp.exists():
        if tmp.is_symlink():
            fail("refusing to overwrite symlink temp file: %s" % tmp)
        tmp.unlink()
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        fail("missing frontmatter in %s" % path)
    data = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]
        data[key.strip()] = value
    return data


def plain_title(name, meta):
    title = meta.get("title", "").strip()
    if title:
        return title
    return name.replace("-", " ").title()


def slug_to_card(name):
    return "route_cards/%s.md" % name


def ensure_managed_directory(target, expected_name):
    references_resolved = REFERENCES.resolve()
    if target.name != expected_name:
        fail("refusing to manage unexpected directory name: %s" % target)
    if target.parent.resolve() != references_resolved:
        fail("refusing to manage directory outside references/omicos: %s" % target)
    if target.exists() and target.is_symlink():
        fail("refusing to replace symlink directory: %s" % target)


def prepare_staging_directory(target, expected_name):
    ensure_managed_directory(target, expected_name)
    staging = target.with_name(".%s.tmp" % expected_name)
    backup = target.with_name(".%s.bak" % expected_name)
    if backup.exists():
        fail(
            "backup directory exists from an incomplete previous rebuild; "
            "inspect before retrying: %s" % backup
        )
    if not target.exists() and backup.exists():
        fail("target is missing and backup exists; refusing to discard backup: %s" % backup)
    if staging.exists():
        if staging.is_symlink():
            fail("refusing to remove symlink staging path: %s" % staging)
        shutil.rmtree(str(staging))
    staging.mkdir(parents=True)
    return staging


def commit_staging_directory(staging, target, expected_name):
    ensure_managed_directory(target, expected_name)
    backup = target.with_name(".%s.bak" % expected_name)
    try:
        if target.exists():
            target.rename(backup)
        staging.rename(target)
        if backup.exists():
            shutil.rmtree(str(backup))
    except BaseException:
        if target.exists():
            if target.is_symlink():
                fail("refusing to clean symlink after failed rebuild: %s" % target)
            shutil.rmtree(str(target))
        if backup.exists():
            backup.rename(target)
        if staging.exists():
            shutil.rmtree(str(staging))
        raise


def copy_raw_skills(skill_dirs):
    staging = prepare_staging_directory(RAW, "raw_skills")
    for skill_dir in skill_dirs:
        target = staging / skill_dir.name
        target.mkdir()
        source_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        (target / "SOURCE.md").write_text(RAW_SAFETY_BANNER + source_text, encoding="utf-8")
    commit_staging_directory(staging, RAW, "raw_skills")


def write_index(rows):
    if INDEX.exists() and INDEX.is_symlink():
        fail("refusing to overwrite symlink file: %s" % INDEX)
    fields = [
        "skill_name",
        "title",
        "description",
        "domain",
        "route_role",
        "object_route",
        "primary_authority",
        "requires_official_confirmation",
        "route_card",
        "risk_note",
        "source_raw_skill",
    ]
    tmp = INDEX.with_name(".%s.tmp" % INDEX.name)
    if tmp.exists():
        if tmp.is_symlink():
            fail("refusing to overwrite symlink temp file: %s" % tmp)
        tmp.unlink()
    with tmp.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    tmp.replace(INDEX)


def one_line(value):
    if isinstance(value, list):
        value = ", ".join([str(item) for item in value])
    elif value is None:
        value = ""
    else:
        value = str(value)
    value = re.sub(r"\s+", " ", value).strip()
    return value or "none"


def agent_slug_to_card(agent_id):
    return "agent_route_cards/%s.md" % agent_id


def agent_source_json(agent_id):
    return "raw_agents/public_cloud_agents/%s.json" % agent_id


def copy_raw_agents(agent_rows):
    staging = prepare_staging_directory(RAW_AGENTS, "raw_agents")
    (staging / "runtime_api").mkdir()
    (staging / "public_cloud_agents").mkdir()
    (staging / "README.md").write_text(RAW_AGENT_SAFETY_README, encoding="utf-8")
    source_data = json.loads(AGENT_SOURCE.read_text(encoding="utf-8"))
    selected_ids = set([row["agent_id"] for row in agent_rows])
    filtered_agents = []
    for agent in source_data.get("agents", []):
        if agent.get("id") in selected_ids:
            filtered_agents.append(agent)
    if len(filtered_agents) != len(agent_rows):
        fail("filtered runtime roster does not match selected agent rows")
    filtered_data = dict(source_data)
    filtered_data["agents"] = sorted(filtered_agents, key=lambda agent: agent.get("id", ""))
    (staging / "runtime_api" / "agents.json").write_text(
        json.dumps(filtered_data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    shutil.copy2(str(AGENT_INDEX_SOURCE), str(staging / "AGENTS_INDEX.md"))
    shutil.copy2(str(AGENT_ROSTER_SOURCE), str(staging / "SYSTEM_PROMPT_AGENT_ROSTER.md"))
    for row in agent_rows:
        agent_id = row["agent_id"]
        source = AGENT_PUBLIC_SOURCE / ("%s.json" % agent_id)
        if not source.exists():
            fail("missing public agent JSON: %s" % source)
        shutil.copy2(str(source), str(staging / "public_cloud_agents" / source.name))
    commit_staging_directory(staging, RAW_AGENTS, "raw_agents")


def write_agent_index(rows):
    if AGENT_INDEX.exists() and AGENT_INDEX.is_symlink():
        fail("refusing to overwrite symlink file: %s" % AGENT_INDEX)
    fields = [
        "agent_id",
        "name",
        "tier",
        "category",
        "agent_role",
        "route_role",
        "skills",
        "toolsets",
        "use_when",
        "not_for",
        "handoff",
        "primary_authority",
        "requires_official_confirmation",
        "route_card",
        "source_agent_json",
        "risk_note",
    ]
    tmp = AGENT_INDEX.with_name(".%s.tmp" % AGENT_INDEX.name)
    if tmp.exists():
        if tmp.is_symlink():
            fail("refusing to overwrite symlink temp file: %s" % tmp)
        tmp.unlink()
    with tmp.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    tmp.replace(AGENT_INDEX)


def write_policy():
    atomic_write_text(
        POLICY,
        """# OmicOS Integration Policy

OmicOS is an internal reference layer for `omics-coding`, not an authority layer.
The authority order is:

1. User-confirmed biological question, object format, grouping, and expected outputs.
2. OmicVerse/SCOP local function and parameter docs.
3. Official tutorial, official notebook, vignette, or official API docs for
   OmicVerse/SCOP workflows and any third-party backend.
4. OmicOS skill route cards as workflow reminders.
5. OmicOS `agent_index.tsv` and `agent_route_cards/*.md` as routing and
   handoff reminders.
6. Generic fallback utilities only after native or wrapper options are rejected.

Use OmicOS route cards as workflow reminders only; this applies to both skill
route cards and agent route cards.

## Hard Gates

- OmicOS may suggest a workflow branch, but it must not override OmicVerse/SCOP
  function docs, parameter docs, package versions, or official tutorial choices.
- OmicOS agent cards may suggest a specialist, handoff, or review gate, but they
  must not become an execution authority or method source.
- Before formal analysis code or any real analysis run, the route must be
  confirmed by the user and recorded in `scratch/analysis_route_confirmed.json`.
- That confirmation file must record `analysis_stage`, `dataset_id`,
  `input_files`, `input_fingerprints`, `output_files`, `official_sources`,
  `doc_paths`, `source_urls`, `planned_functions`, `key_parameters`,
  `package_versions`, `visualization_gate`, `omicos_route_role`,
  `confirmed_by_user`, `user_confirmation`, `confirmed_at`, `project_root`,
  `allowed_commands`, and `allowed_files` for the exact current route.
- `allowed_commands` and `allowed_files` are both required. They must be exact
  commands and exact files. Do not use glob patterns, parent directories, broad
  project roots, or catch-all shell fragments as authorization.
- A route pass is narrow. It does not authorize a different dataset, method,
  package, visualization family, analysis stage, input file, output file,
  parameter set, function, command, or route role.

## Role Meanings

| route_role | meaning |
|---|---|
| route_card | Can be used as a compact workflow reminder after authority docs are checked. |
| candidate_reminder | Can remind the agent to search a method family, but never selects the method alone. |
| glue_helper | Can help with file I/O, reshaping, export, or small object handling. |
| fallback_only | Can only be used after analysis-native or wrapper options are checked and rejected. |
| excluded_from_core | Preserved for audit, not used for formal omics route planning. |

## Agent Layer Meanings

`agent_index.tsv` and `agent_route_cards/*.md` are strict-omics routing aids.
They include only data acquisition, strategy planning, single-cell analysis,
spatial omics, general omics analysis, phylogenomics, and review-gate agents.
Writing, viewer, structural biology, molecular-biology utility, generic memory,
and broad selector agents are excluded from the omics-coding route layer.

Agent route roles:

| agent route_role | meaning |
|---|---|
| route_card | Can suggest the matching specialist route after OmicVerse/SCOP docs are checked. |
| candidate_reminder | Can remind the agent to consider a branch, but cannot select methods alone. |
| review_only | Can challenge completed work; cannot start, approve, or execute analysis. |

## Confirmation Meanings

| requires_official_confirmation | meaning |
|---|---|
| always | Any formal use must go through official source review, user confirmation, and `analysis_route_confirmed.json`. |
| conditional | Confirmation is required when the step affects an analysis result, evidence figure, statistic, biological conclusion, or object matrix. |
| not_core_analysis | Only pure export, pure layout, or smoke-test use; if it touches formal analysis outputs, treat as `conditional`. |

## Murphy Acceptance Questions

Before using any OmicOS-derived card, ask:

1. Could this bypass an official tutorial or function doc?
2. Could this replace a native OmicVerse/SCOP plot with a custom fallback plot?
3. Could this treat pooled cells as biological replicates?
4. Could this hide version or backend differences?
5. Could this make generated/model-inferred output look directly observed?

If any answer is yes, stop and return to the relevant `omics-coding` gate.
""",
    )


def role_boundary_text(row):
    role = row["route_role"]
    if role == "fallback_only":
        return (
            "- This is fallback only. Use it only after native/wrapper functions are checked, "
            "rejected with reasons, and the user confirms the custom route.\n"
            "- For figures, the Analysis-Native Visualization Gate must be completed first.\n"
            "- For formal analysis, the Formal Analysis Route Confirmation file is required."
        )
    if role == "glue_helper":
        return (
            "- This is glue only. It may handle metadata, tables, export, or object plumbing around verified methods.\n"
            "- It must not replace core analysis, core visualization, statistical testing, normalization, filtering, scaling, or biological interpretation.\n"
            "- If it changes an expression/count/intensity matrix or evidence figure, return to Formal Analysis Route Confirmation."
        )
    if role == "candidate_reminder":
        return (
            "- This only expands search terms or reminds the agent of a method family.\n"
            "- It cannot choose a method, function, parameter, backend, or figure family without authority docs."
        )
    if role == "excluded_from_core":
        return "- Preserved for audit only. Do not use for formal route planning."
    return (
        "- Use this as route ordering help only after OmicVerse/SCOP and official docs are checked.\n"
        "- It cannot override version checks, function docs, parameter docs, visualization gates, or route confirmation."
    )


def card_text(row):
    return """# {title}

- Source raw material: `../raw_skills/{name}/SOURCE.md`
- Domain: `{domain}`
- Route role: `{route_role}`
- Object route: `{object_route}`
- Primary authority: {primary_authority}
- Official confirmation: `{confirmation}`

## How To Use

1. Clarify the user question, input object, species, grouping columns, and outputs.
2. Search `references/function_index.tsv` and `references/parameter_index.tsv` first.
3. Open the shortlisted OmicVerse/SCOP docs and verify exact function and parameters.
4. Use this OmicOS card only as a workflow reminder.
5. Complete the Analysis-Native Visualization Gate before any fallback or custom figure.
6. Before formal code or analysis run, complete Formal Analysis Route Confirmation and write
   `scratch/analysis_route_confirmed.json` for this exact route.

## Role Boundaries

{role_boundaries}

## Murphy Checks

- Does this route bypass OmicVerse/SCOP or official third-party docs?
- Does it turn a generic plotting/statistics helper into a core evidence step?
- Does it depend on an object, layer, batch column, sample column, species, or backend
  that has not been confirmed?
- Does it make model-inferred or database-derived output sound directly observed?

## Risk Note

{risk_note}
""".format(
        title=row["title"],
        name=row["skill_name"],
        domain=row["domain"],
        route_role=row["route_role"],
        object_route=row["object_route"],
        primary_authority=row["primary_authority"],
        confirmation=row["requires_official_confirmation"],
        role_boundaries=role_boundary_text(row),
        risk_note=row["risk_note"],
    )


def write_route_cards(rows):
    staging = prepare_staging_directory(ROUTE_CARDS, "route_cards")
    readme_lines = [
        "# OmicOS Route Cards",
        "",
        "These cards are internal workflow reminders for `omics-coding`.",
        "They are not authority docs and must be used after OmicVerse/SCOP discovery.",
        "",
        "| skill | role | domain | card |",
        "|---|---|---|---|",
    ]
    for row in rows:
        card_path = staging / ("%s.md" % row["skill_name"])
        card_path.write_text(card_text(row), encoding="utf-8")
        readme_lines.append(
            "| `{skill}` | `{role}` | `{domain}` | `{card}` |".format(
                skill=row["skill_name"],
                role=row["route_role"],
                domain=row["domain"],
                card=row["route_card"],
            )
        )
    (staging / "README.md").write_text("\n".join(readme_lines) + "\n", encoding="utf-8")
    commit_staging_directory(staging, ROUTE_CARDS, "route_cards")


def agent_role_boundary_text(row):
    route_role = row["route_role"]
    if route_role == "review_only":
        return (
            "- This agent card is review only. It may challenge evidence, route drift, missing docs, and hallucinated outputs.\n"
            "- It must not start a new analysis, choose methods, change parameters, or approve results without reproducible evidence."
        )
    if route_role == "candidate_reminder":
        return (
            "- This agent card only expands routing options or prompts a specialist handoff.\n"
            "- It cannot select functions, parameters, models, or plots without OmicVerse/SCOP and official source review."
        )
    return (
        "- Use this agent card as routing and handoff help only after OmicVerse/SCOP and official docs are checked.\n"
        "- It cannot override function docs, parameter docs, package versions, visualization gates, or route confirmation."
    )


def agent_card_text(row):
    return """# {name}

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/{agent_id}.json`
- Category: `{category}`
- Tier: `{tier}`
- Agent role: `{agent_role}`
- Route role: `{route_role}`
- Primary authority: {primary_authority}
- Official confirmation: `{confirmation}`

OmicOS agent is not an authority layer. Use this card only as an internal
routing and handoff reminder after OmicVerse/SCOP and official docs have been
checked.

## Use When

{use_when}

## NOT-FOR

{not_for}

## Handoff

{handoff}

## Source Skills And Toolsets

- Skills: {skills}
- Toolsets: {toolsets}

## Role Boundaries

{role_boundaries}

## Murphy Checks

- Could this agent bypass OmicVerse/SCOP or official package docs?
- Could this agent turn a planning suggestion into executed analysis without
  Formal Analysis Route Confirmation?
- Could this agent hide missing object schema, species, genome build, sample
  design, layer, modality, batch, or version checks?
- Could this agent make model-inferred, database-derived, or review-only output
  sound directly observed?

## Risk Note

{risk_note}
""".format(
        name=row["name"],
        agent_id=row["agent_id"],
        category=row["category"],
        tier=row["tier"],
        agent_role=row["agent_role"],
        route_role=row["route_role"],
        primary_authority=row["primary_authority"],
        confirmation=row["requires_official_confirmation"],
        use_when=row["use_when"],
        not_for=row["not_for"],
        handoff=row["handoff"],
        skills=row["skills"],
        toolsets=row["toolsets"],
        role_boundaries=agent_role_boundary_text(row),
        risk_note=row["risk_note"],
    )


def write_agent_route_cards(rows):
    staging = prepare_staging_directory(AGENT_ROUTE_CARDS, "agent_route_cards")
    readme_lines = [
        "# OmicOS Agent Route Cards",
        "",
        "These cards are internal routing and handoff reminders for `omics-coding`.",
        "They are not authority docs and must be used after OmicVerse/SCOP discovery.",
        "",
        "| agent | role | category | card |",
        "|---|---|---|---|",
    ]
    for row in rows:
        card_path = staging / ("%s.md" % row["agent_id"])
        card_path.write_text(agent_card_text(row), encoding="utf-8")
        readme_lines.append(
            "| `{agent}` | `{role}` | `{category}` | `{card}` |".format(
                agent=row["agent_id"],
                role=row["route_role"],
                category=row["category"],
                card=row["route_card"],
            )
        )
    (staging / "README.md").write_text("\n".join(readme_lines) + "\n", encoding="utf-8")
    commit_staging_directory(staging, AGENT_ROUTE_CARDS, "agent_route_cards")


def update_reference_index(rows, agent_rows):
    text = REFERENCE_INDEX.read_text(encoding="utf-8")
    start = "<!-- omicos-reference:begin -->"
    end = "<!-- omicos-reference:end -->"
    legacy_marker = "## OmicOS Reference Layer"
    block = """{start}
## OmicOS Reference Layer

- OmicOS raw skills: {count}
- OmicOS strict omics agents: {agent_count}
- `omicos/skill_index.tsv`: one row per OmicOS skill with route role and risk note.
- `omicos/agent_index.tsv`: one row per strict omics OmicOS agent with routing, NOT-FOR, handoff, and risk note.
- `omicos/integration_policy.md`: authority order and Murphy acceptance checks.
- `omicos/route_cards/*.md`: compact workflow reminders; use only after OmicVerse/SCOP function discovery.
- `omicos/agent_route_cards/*.md`: compact agent handoff reminders; not an authority layer.
- `omicos/raw_agents/`: selected public agent JSON plus runtime roster for audit.
{end}
""".format(
        start=start,
        count=len(rows),
        agent_count=len(agent_rows),
        end=end,
    )
    has_start = start in text
    has_end = end in text
    if has_start and has_end:
        pattern = re.escape(start) + r".*?" + re.escape(end)
        text = re.sub(pattern, block.rstrip(), text, count=1, flags=re.S)
    elif has_start or has_end:
        fail("references/index.md has incomplete OmicOS begin/end markers")
    else:
        if legacy_marker in text:
            fail("references/index.md has an unmarked legacy OmicOS block; add begin/end markers before rebuild")
        if not text.endswith("\n"):
            text += "\n"
        text += "\n" + block
    atomic_write_text(REFERENCE_INDEX, text)


def load_agent_rows():
    if not AGENT_SOURCE.exists():
        fail("missing OmicOS runtime agent source: %s" % AGENT_SOURCE)
    if not AGENT_PUBLIC_SOURCE.exists():
        fail("missing OmicOS public agent source directory: %s" % AGENT_PUBLIC_SOURCE)
    if not AGENT_INDEX_SOURCE.exists():
        fail("missing OmicOS agent index source: %s" % AGENT_INDEX_SOURCE)
    if not AGENT_ROSTER_SOURCE.exists():
        fail("missing OmicOS agent roster source: %s" % AGENT_ROSTER_SOURCE)

    if len(AGENT_POLICIES) != EXPECTED_AGENT_COUNT:
        fail("expected %s explicit agent policies, found %s" % (EXPECTED_AGENT_COUNT, len(AGENT_POLICIES)))
    accidental_forbidden = sorted(set(AGENT_POLICIES.keys()).intersection(FORBIDDEN_AGENT_IDS))
    if accidental_forbidden:
        fail("agent policy includes forbidden agents: %s" % ", ".join(accidental_forbidden))

    data = json.loads(AGENT_SOURCE.read_text(encoding="utf-8"))
    agents = data.get("agents")
    if not isinstance(agents, list):
        fail("runtime agents.json must contain an agents list")
    by_id = {}
    for agent in agents:
        agent_id = agent.get("id")
        if not agent_id:
            fail("runtime agents.json has an agent without id")
        if agent_id in by_id:
            fail("duplicate runtime agent id: %s" % agent_id)
        by_id[agent_id] = agent

    missing_runtime = sorted(set(AGENT_POLICIES.keys()).difference(by_id.keys()))
    if missing_runtime:
        fail("selected agents missing from runtime source: %s" % ", ".join(missing_runtime))
    classified = set(AGENT_POLICIES.keys()).union(FORBIDDEN_AGENT_IDS)
    unclassified = sorted(set(by_id.keys()).difference(classified))
    stale_forbidden = sorted(FORBIDDEN_AGENT_IDS.difference(by_id.keys()))
    if unclassified:
        fail("runtime agents without explicit include/exclude policy: %s" % ", ".join(unclassified))
    if stale_forbidden:
        fail("forbidden agent ids no longer present in runtime source: %s" % ", ".join(stale_forbidden))

    rows = []
    for agent_id in sorted(AGENT_POLICIES.keys()):
        agent = by_id[agent_id]
        policy = AGENT_POLICIES[agent_id]
        public_json = AGENT_PUBLIC_SOURCE / ("%s.json" % agent_id)
        if not public_json.exists():
            fail("selected agent missing public JSON: %s" % public_json)
        rows.append(
            {
                "agent_id": agent_id,
                "name": one_line(agent.get("name")),
                "tier": one_line(agent.get("tier")),
                "category": one_line(agent.get("category")),
                "agent_role": policy["agent_role"],
                "route_role": policy["route_role"],
                "skills": one_line(agent.get("skills")),
                "toolsets": one_line(agent.get("toolsets")),
                "use_when": one_line(
                    policy.get("use_when_override")
                    or agent.get("use_when")
                    or agent.get("description")
                    or agent.get("summary")
                ),
                "not_for": policy["not_for"],
                "handoff": policy["handoff"],
                "primary_authority": policy["primary_authority"],
                "requires_official_confirmation": policy["requires_official_confirmation"],
                "route_card": agent_slug_to_card(agent_id),
                "source_agent_json": agent_source_json(agent_id),
                "risk_note": policy["risk_note"],
            }
        )
    return rows


def main():
    if not SOURCE.exists():
        fail("missing OmicOS source directory: %s" % SOURCE)
    skill_dirs = sorted([p for p in SOURCE.iterdir() if (p / "SKILL.md").exists()])
    if len(skill_dirs) != EXPECTED_COUNT:
        fail("expected %s source skills, found %s" % (EXPECTED_COUNT, len(skill_dirs)))

    names = set([p.name for p in skill_dirs])
    policy_names = set(POLICIES.keys())
    missing = sorted(names.difference(policy_names))
    extra = sorted(policy_names.difference(names))
    if missing:
        fail("source skills without explicit policy: %s" % ", ".join(missing))
    if extra:
        fail("policies without source skills: %s" % ", ".join(extra))

    agent_rows = load_agent_rows()

    ensure_references_base()
    REFERENCES.mkdir(parents=True, exist_ok=True)
    ensure_references_base()
    copy_raw_skills(skill_dirs)
    copy_raw_agents(agent_rows)

    rows = []
    for skill_dir in skill_dirs:
        meta = parse_frontmatter(skill_dir / "SKILL.md")
        policy = POLICIES[skill_dir.name]
        route_card = slug_to_card(skill_dir.name)
        rows.append(
            {
                "skill_name": skill_dir.name,
                "title": plain_title(skill_dir.name, meta),
                "description": meta.get("description", "").strip(),
                "domain": policy["domain"],
                "route_role": policy["route_role"],
                "object_route": policy["object_route"],
                "primary_authority": policy["primary_authority"],
                "requires_official_confirmation": policy["requires_official_confirmation"],
                "route_card": route_card,
                "risk_note": policy["risk_note"],
                "source_raw_skill": "raw_skills/%s/SOURCE.md" % skill_dir.name,
            }
        )

    write_index(rows)
    write_agent_index(agent_rows)
    write_policy()
    write_route_cards(rows)
    write_agent_route_cards(agent_rows)
    update_reference_index(rows, agent_rows)
    print("OK: built OmicOS reference layer with %s skills and %s agents" % (len(rows), len(agent_rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
