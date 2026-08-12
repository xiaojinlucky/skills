#!/usr/bin/env python3
"""Validate the OmicOS reference layer used by omics-coding."""

import csv
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references" / "omicos"
ROOT_REFERENCES = ROOT / "references"
RAW = REFERENCES / "raw_skills"
ROUTE_CARDS = REFERENCES / "route_cards"
INDEX = REFERENCES / "skill_index.tsv"
RAW_AGENTS = REFERENCES / "raw_agents"
AGENT_ROUTE_CARDS = REFERENCES / "agent_route_cards"
AGENT_INDEX = REFERENCES / "agent_index.tsv"
POLICY = REFERENCES / "integration_policy.md"
MAIN_SKILL = ROOT / "SKILL.md"

EXPECTED_COUNT = 60
EXPECTED_AGENT_COUNT = 32
RAW_SAFETY_MARKER = "omics-coding-omicos-raw-safety"
RAW_AGENT_SAFETY_MARKER = "omics-coding-omicos-agent-raw-safety"
INDEX_START = "<!-- omicos-reference:begin -->"
INDEX_END = "<!-- omicos-reference:end -->"
REQUIRED_CONFIRMATION_FIELDS = [
    "analysis_stage",
    "dataset_id",
    "input_files",
    "input_fingerprints",
    "output_files",
    "official_sources",
    "doc_paths",
    "source_urls",
    "planned_functions",
    "key_parameters",
    "package_versions",
    "visualization_gate",
    "omicos_route_role",
    "confirmed_by_user",
    "user_confirmation",
    "confirmed_at",
    "project_root",
    "allowed_commands",
    "allowed_files",
]
ALLOWED_ROLES = {
    "route_card",
    "candidate_reminder",
    "glue_helper",
    "fallback_only",
    "excluded_from_core",
}
ALLOWED_CONFIRMATION = {"always", "conditional", "not_core_analysis"}
ALLOWED_AGENT_ROLES = {
    "data_acquisition",
    "strategy_planning",
    "single_cell_analysis",
    "spatial_analysis",
    "general_omics_analysis",
    "phylogenomics_analysis",
    "review_gate",
}
ALLOWED_AGENT_ROUTE_ROLES = {
    "route_card",
    "candidate_reminder",
    "review_only",
}

EXPECTED_AGENT_IDS = {
    "GEO-everything",
    "analysis_sanity_review",
    "analysis_strategist",
    "bulk_epigenomics_analyst",
    "bulk_rna_analyst",
    "c3ca_phase_runner",
    "cancer_dependency_analyst",
    "cell_cell_communication_free",
    "cell_cell_communication_pro",
    "cellchat_rust_h5ad_runner",
    "chromatin_3d_analyst",
    "he_to_st_predictor",
    "immune_repertoire_analyst_pro",
    "metabolomics_analyst_pro",
    "microbiome_analyst_pro",
    "phylogenomics_analyst",
    "proteomics_analyst_pro",
    "reviewer",
    "single_cell_annotator_free",
    "single_cell_annotator_pro",
    "single_cell_downstream_analyst_pro",
    "single_cell_epigenomics_analyst",
    "single_cell_grn_analyst",
    "single_cell_perturbation_analyst",
    "single_cell_preprocessor",
    "single_cell_trajectory_free",
    "single_cell_trajectory_pro",
    "single_ev_analyst_pro",
    "spatial_epigenomics_analyst",
    "spatial_omics_orchestrator",
    "statistical_genetics_analyst",
    "tabular_genomics_analyst",
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

EXPECTED_HIGH_RISK = {
    "data-viz-plots": "fallback_only",
    "plotting-visualization": "candidate_reminder",
    "data-stats-analysis": "fallback_only",
    "data-transform": "glue_helper",
    "data-export-excel": "glue_helper",
    "data-export-pdf": "glue_helper",
}


def fail(message):
    print(f"FAIL: {message}")
    raise SystemExit(1)


def read_index():
    if not INDEX.exists():
        fail(f"missing {INDEX}")
    with INDEX.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if not rows:
        fail("skill_index.tsv has no rows")
    return rows


def read_agent_index():
    if not AGENT_INDEX.exists():
        fail(f"missing {AGENT_INDEX}")
    with AGENT_INDEX.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if not rows:
        fail("agent_index.tsv has no rows")
    return rows


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except ValueError as exc:
        fail(f"invalid JSON in {path}: {exc}")


def validate_files():
    if ROOT_REFERENCES.exists() and ROOT_REFERENCES.is_symlink():
        fail(f"references must not be a symlink: {ROOT_REFERENCES}")
    skill_root = ROOT.resolve()
    references_root = ROOT_REFERENCES.resolve()
    if not str(references_root).startswith(str(skill_root) + "/"):
        fail(f"references directory must stay under skill root: {references_root}")
    if REFERENCES.exists() and REFERENCES.is_symlink():
        fail(f"references/omicos must not be a symlink: {REFERENCES}")
    if not RAW.exists():
        fail(f"missing raw skill directory {RAW}")
    raw_skill_files = sorted(RAW.glob("*/SOURCE.md"))
    if len(raw_skill_files) != EXPECTED_COUNT:
        fail(f"expected {EXPECTED_COUNT} raw skills, found {len(raw_skill_files)}")
    legacy_raw_skill_files = sorted(RAW.glob("*/SKILL.md"))
    if legacy_raw_skill_files:
        fail("raw OmicOS source material must not use SKILL.md")
    if not POLICY.exists():
        fail(f"missing {POLICY}")
    if not ROUTE_CARDS.exists():
        fail(f"missing {ROUTE_CARDS}")
    card_files = sorted([p for p in ROUTE_CARDS.glob("*.md") if p.name != "README.md"])
    if len(card_files) != EXPECTED_COUNT:
        fail(f"expected {EXPECTED_COUNT} route cards, found {len(card_files)}")
    if not RAW_AGENTS.exists():
        fail(f"missing raw agent directory {RAW_AGENTS}")
    if not (RAW_AGENTS / "README.md").exists():
        fail("missing raw_agents/README.md")
    public_agent_files = sorted((RAW_AGENTS / "public_cloud_agents").glob("*.json"))
    if len(public_agent_files) != EXPECTED_AGENT_COUNT:
        fail(f"expected {EXPECTED_AGENT_COUNT} raw public agent JSON files, found {len(public_agent_files)}")
    required_raw_agent_files = [
        RAW_AGENTS / "runtime_api" / "agents.json",
        RAW_AGENTS / "AGENTS_INDEX.md",
        RAW_AGENTS / "SYSTEM_PROMPT_AGENT_ROSTER.md",
    ]
    for path in required_raw_agent_files:
        if not path.exists():
            fail(f"missing raw agent source file {path}")
    raw_agent_readme = (RAW_AGENTS / "README.md").read_text(encoding="utf-8")
    if RAW_AGENT_SAFETY_MARKER not in raw_agent_readme:
        fail("raw_agents/README.md missing safety marker")
    if not AGENT_ROUTE_CARDS.exists():
        fail(f"missing {AGENT_ROUTE_CARDS}")
    agent_card_files = sorted([p for p in AGENT_ROUTE_CARDS.glob("*.md") if p.name != "README.md"])
    if len(agent_card_files) != EXPECTED_AGENT_COUNT:
        fail(f"expected {EXPECTED_AGENT_COUNT} agent route cards, found {len(agent_card_files)}")
    for stale in [REFERENCES / ".raw_skills.tmp", REFERENCES / ".raw_skills.bak",
                  REFERENCES / ".route_cards.tmp", REFERENCES / ".route_cards.bak",
                  REFERENCES / ".raw_agents.tmp", REFERENCES / ".raw_agents.bak",
                  REFERENCES / ".agent_route_cards.tmp", REFERENCES / ".agent_route_cards.bak"]:
        if stale.exists():
            fail(f"stale staging directory exists: {stale}")
    for stale in [
        REFERENCES / ".skill_index.tsv.tmp",
        REFERENCES / ".agent_index.tsv.tmp",
        REFERENCES / ".integration_policy.md.tmp",
        ROOT_REFERENCES / ".index.md.tmp",
    ]:
        if stale.exists():
            fail(f"stale temp file exists: {stale}")


def validate_index(rows):
    if len(rows) != EXPECTED_COUNT:
        fail(f"expected {EXPECTED_COUNT} index rows, found {len(rows)}")

    required = {
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
    }
    missing_columns = required.difference(rows[0].keys())
    if missing_columns:
        fail(f"missing index columns: {sorted(missing_columns)}")

    seen = set()
    for row in rows:
        name = row["skill_name"]
        if name in seen:
            fail(f"duplicate index row: {name}")
        seen.add(name)
        if row["route_role"] not in ALLOWED_ROLES:
            fail(f"{name} has invalid route_role={row['route_role']!r}")
        if row["requires_official_confirmation"] not in ALLOWED_CONFIRMATION:
            fail(
                f"{name} has invalid requires_official_confirmation="
                f"{row['requires_official_confirmation']!r}"
            )
        for key in required:
            if not row[key].strip():
                fail(f"{name} has empty {key}")

        expected_raw = f"raw_skills/{name}/SOURCE.md"
        expected_card = f"route_cards/{name}.md"
        if row["source_raw_skill"] != expected_raw:
            fail(f"{name} has invalid source_raw_skill={row['source_raw_skill']!r}")
        if row["route_card"] != expected_card:
            fail(f"{name} has invalid route_card={row['route_card']!r}")
        if ".." in row["source_raw_skill"].split("/") or ".." in row["route_card"].split("/"):
            fail(f"{name} uses a path traversal segment")

        raw_file = REFERENCES / row["source_raw_skill"]
        if not raw_file.exists():
            fail(f"{name} points to missing raw skill file")
        raw_text = raw_file.read_text(encoding="utf-8")
        if RAW_SAFETY_MARKER not in raw_text[:1000]:
            fail(f"{name} raw skill is missing safety banner")

        card = REFERENCES / row["route_card"]
        if not card.exists():
            fail(f"{name} points to missing route card {card}")
        card_text = card.read_text(encoding="utf-8")
        required_card_phrases = [
            f"Source raw material: `../raw_skills/{name}/SOURCE.md`",
            f"Domain: `{row['domain']}`",
            f"Route role: `{row['route_role']}`",
            f"Object route: `{row['object_route']}`",
            f"Primary authority: {row['primary_authority']}",
            f"Official confirmation: `{row['requires_official_confirmation']}`",
            "Use this OmicOS card only as a workflow reminder",
            "Role Boundaries",
            "Murphy Checks",
            "Analysis-Native Visualization Gate",
            "Formal Analysis Route Confirmation",
            row["risk_note"],
        ]
        for phrase in required_card_phrases:
            if phrase not in card_text:
                fail(f"{name} route card missing phrase: {phrase}")
        if row["route_role"] in {"fallback_only", "glue_helper"}:
            if "must not replace core" not in card_text and "fallback only" not in card_text:
                fail(f"{name} route card lacks fallback/glue safety boundary")

    by_name = {row["skill_name"]: row for row in rows}
    for name, expected_role in EXPECTED_HIGH_RISK.items():
        row = by_name.get(name)
        if row is None:
            fail(f"missing high-risk skill {name}")
        if row["route_role"] != expected_role:
            fail(f"{name} must be {expected_role}, got {row['route_role']}")
        if row["primary_authority"] == "OmicOS":
            fail(f"{name} must not make OmicOS the primary authority")

    expected_cards = {f"{row['skill_name']}.md" for row in rows}
    actual_cards = {p.name for p in ROUTE_CARDS.glob("*.md") if p.name != "README.md"}
    orphan_cards = sorted(actual_cards.difference(expected_cards))
    missing_cards = sorted(expected_cards.difference(actual_cards))
    if orphan_cards:
        fail(f"orphan route cards found: {orphan_cards}")
    if missing_cards:
        fail(f"missing route cards found: {missing_cards}")

    readme = ROUTE_CARDS / "README.md"
    if not readme.exists():
        fail("missing route_cards/README.md")
    readme_text = readme.read_text(encoding="utf-8")
    table_rows = [line for line in readme_text.splitlines() if line.startswith("| `")]
    if len(table_rows) != EXPECTED_COUNT:
        fail(f"route_cards/README.md expected {EXPECTED_COUNT} table rows, found {len(table_rows)}")
    for row in rows:
        expected = "| `{skill}` | `{role}` | `{domain}` | `{card}` |".format(
            skill=row["skill_name"],
            role=row["route_role"],
            domain=row["domain"],
            card=row["route_card"],
        )
        if expected not in readme_text:
            fail(f"route_cards/README.md missing exact row for {row['skill_name']}")


def validate_agent_index(rows):
    if len(rows) != EXPECTED_AGENT_COUNT:
        fail(f"expected {EXPECTED_AGENT_COUNT} agent index rows, found {len(rows)}")

    required = {
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
    }
    missing_columns = required.difference(rows[0].keys())
    if missing_columns:
        fail(f"missing agent index columns: {sorted(missing_columns)}")

    seen = set()
    runtime_json = read_json(RAW_AGENTS / "runtime_api" / "agents.json")
    runtime_agents = runtime_json.get("agents")
    if not isinstance(runtime_agents, list):
        fail("raw_agents/runtime_api/agents.json must contain an agents list")
    runtime_by_id = {}
    for agent in runtime_agents:
        agent_id = agent.get("id")
        if not agent_id:
            fail("raw runtime roster contains an agent without id")
        if agent_id in runtime_by_id:
            fail(f"raw runtime roster has duplicate id: {agent_id}")
        runtime_by_id[agent_id] = agent
    runtime_ids = set(runtime_by_id.keys())
    if runtime_ids != EXPECTED_AGENT_IDS:
        fail(
            "raw runtime roster ids must match expected selected agents; "
            f"missing={sorted(EXPECTED_AGENT_IDS.difference(runtime_ids))}, "
            f"extra={sorted(runtime_ids.difference(EXPECTED_AGENT_IDS))}"
        )
    leaked_forbidden = sorted(runtime_ids.intersection(FORBIDDEN_AGENT_IDS))
    if leaked_forbidden:
        fail(f"forbidden agents leaked into raw runtime roster: {leaked_forbidden}")

    for row in rows:
        agent_id = row["agent_id"]
        if agent_id in seen:
            fail(f"duplicate agent index row: {agent_id}")
        seen.add(agent_id)
        if agent_id in FORBIDDEN_AGENT_IDS:
            fail(f"forbidden agent included: {agent_id}")
        if row["agent_role"] not in ALLOWED_AGENT_ROLES:
            fail(f"{agent_id} has invalid agent_role={row['agent_role']!r}")
        if row["route_role"] not in ALLOWED_AGENT_ROUTE_ROLES:
            fail(f"{agent_id} has invalid route_role={row['route_role']!r}")
        if row["requires_official_confirmation"] not in ALLOWED_CONFIRMATION:
            fail(
                f"{agent_id} has invalid requires_official_confirmation="
                f"{row['requires_official_confirmation']!r}"
            )
        for key in required:
            if not row[key].strip():
                fail(f"{agent_id} has empty {key}")

        expected_raw = f"raw_agents/public_cloud_agents/{agent_id}.json"
        expected_card = f"agent_route_cards/{agent_id}.md"
        if row["source_agent_json"] != expected_raw:
            fail(f"{agent_id} has invalid source_agent_json={row['source_agent_json']!r}")
        if row["route_card"] != expected_card:
            fail(f"{agent_id} has invalid route_card={row['route_card']!r}")
        if ".." in row["source_agent_json"].split("/") or ".." in row["route_card"].split("/"):
            fail(f"{agent_id} uses a path traversal segment")

        raw_file = REFERENCES / row["source_agent_json"]
        if not raw_file.exists():
            fail(f"{agent_id} points to missing raw agent JSON")
        public_json = read_json(raw_file)
        if public_json.get("id") != agent_id:
            fail(f"{agent_id} public JSON id mismatch: {public_json.get('id')!r}")
        for key in ["name", "tier", "category"]:
            value = public_json.get(key)
            if not value:
                fail(f"{agent_id} public JSON missing {key}")
            if str(value) != row[key]:
                fail(f"{agent_id} public JSON {key} mismatch: {value!r} != {row[key]!r}")
        runtime_agent = runtime_by_id.get(agent_id)
        if runtime_agent is None:
            fail(f"{agent_id} missing from filtered raw runtime roster")
        for key in ["name", "tier", "category"]:
            if str(runtime_agent.get(key, "")) != row[key]:
                fail(f"{agent_id} runtime roster {key} mismatch: {runtime_agent.get(key)!r} != {row[key]!r}")
        card = REFERENCES / row["route_card"]
        if not card.exists():
            fail(f"{agent_id} points to missing agent route card {card}")
        card_text = card.read_text(encoding="utf-8")
        required_card_phrases = [
            f"Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/{agent_id}.json`",
            f"Category: `{row['category']}`",
            f"Agent role: `{row['agent_role']}`",
            f"Route role: `{row['route_role']}`",
            f"Primary authority: {row['primary_authority']}",
            f"Official confirmation: `{row['requires_official_confirmation']}`",
            "OmicOS agent is not an authority layer",
            "OmicVerse/SCOP",
            "Formal Analysis Route Confirmation",
            "Murphy Checks",
            "NOT-FOR",
            "Handoff",
            row["risk_note"],
        ]
        for phrase in required_card_phrases:
            if phrase not in card_text:
                fail(f"{agent_id} agent route card missing phrase: {phrase}")

    missing_agents = sorted(EXPECTED_AGENT_IDS.difference(seen))
    extra_agents = sorted(seen.difference(EXPECTED_AGENT_IDS))
    if missing_agents:
        fail(f"missing expected agent ids: {missing_agents}")
    if extra_agents:
        fail(f"unexpected agent ids: {extra_agents}")

    for agent_id in FORBIDDEN_AGENT_IDS:
        if (AGENT_ROUTE_CARDS / ("%s.md" % agent_id)).exists():
            fail(f"forbidden agent route card exists: {agent_id}")
        if (RAW_AGENTS / "public_cloud_agents" / ("%s.json" % agent_id)).exists():
            fail(f"forbidden raw agent JSON exists: {agent_id}")

    expected_cards = {f"{row['agent_id']}.md" for row in rows}
    actual_cards = {p.name for p in AGENT_ROUTE_CARDS.glob("*.md") if p.name != "README.md"}
    orphan_cards = sorted(actual_cards.difference(expected_cards))
    missing_cards = sorted(expected_cards.difference(actual_cards))
    if orphan_cards:
        fail(f"orphan agent route cards found: {orphan_cards}")
    if missing_cards:
        fail(f"missing agent route cards found: {missing_cards}")

    readme = AGENT_ROUTE_CARDS / "README.md"
    if not readme.exists():
        fail("missing agent_route_cards/README.md")
    readme_text = readme.read_text(encoding="utf-8")
    table_rows = [line for line in readme_text.splitlines() if line.startswith("| `")]
    if len(table_rows) != EXPECTED_AGENT_COUNT:
        fail(f"agent_route_cards/README.md expected {EXPECTED_AGENT_COUNT} table rows, found {len(table_rows)}")
    for row in rows:
        expected = "| `{agent}` | `{role}` | `{category}` | `{card}` |".format(
            agent=row["agent_id"],
            role=row["route_role"],
            category=row["category"],
            card=row["route_card"],
        )
        if expected not in readme_text:
            fail(f"agent_route_cards/README.md missing exact row for {row['agent_id']}")


def validate_policy():
    text = POLICY.read_text(encoding="utf-8")
    required_phrases = [
        "OmicVerse/SCOP",
        "OmicOS",
        "agent_index.tsv",
        "agent_route_cards",
        "analysis_route_confirmed.json",
        "official tutorial",
        "fallback",
        "allowed_commands",
        "allowed_files",
        "glob patterns",
        "Confirmation Meanings",
    ]
    required_phrases.extend(REQUIRED_CONFIRMATION_FIELDS)
    for phrase in required_phrases:
        if phrase not in text:
            fail(f"integration policy missing phrase: {phrase}")
    if "OmicOS route cards as workflow reminders" not in text:
        fail("integration policy must keep OmicOS as workflow reminders")


def validate_main_skill():
    text = MAIN_SKILL.read_text(encoding="utf-8")
    required_phrases = [
        "OmicOS Internal Reference Layer",
        "references/omicos/skill_index.tsv",
        "references/omicos/agent_index.tsv",
        "references/omicos/agent_route_cards/*.md",
        "OmicOS is not an authority layer",
        "analysis_route_confirmed.json",
        "allowed_commands",
        "allowed_files",
    ]
    required_phrases.extend(REQUIRED_CONFIRMATION_FIELDS)
    for phrase in required_phrases:
        if phrase not in text:
            fail(f"SKILL.md missing phrase: {phrase}")
    if "@references/omicos" in text:
        fail("SKILL.md must not force-load OmicOS references with @ links")


def validate_reference_index():
    text = (ROOT / "references" / "index.md").read_text(encoding="utf-8")
    if text.count(INDEX_START) != 1 or text.count(INDEX_END) != 1:
        fail("references/index.md must contain exactly one OmicOS begin/end block")
    if text.index(INDEX_START) > text.index(INDEX_END):
        fail("references/index.md OmicOS markers are out of order")
    required_phrases = [
        "OmicOS raw skills: 60",
        "OmicOS strict omics agents: 32",
        "omicos/agent_index.tsv",
        "omicos/agent_route_cards/*.md",
        "omicos/raw_agents/",
    ]
    for phrase in required_phrases:
        if phrase not in text:
            fail(f"references/index.md missing phrase: {phrase}")


def main():
    validate_files()
    rows = read_index()
    validate_index(rows)
    agent_rows = read_agent_index()
    validate_agent_index(agent_rows)
    validate_policy()
    validate_main_skill()
    validate_reference_index()
    print("OK: OmicOS reference layer validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
