import fs from "node:fs";
import crypto from "node:crypto";
import path from "node:path";
import process from "node:process";
import { execFileSync } from "node:child_process";
import { acquireExclusiveFileLock, releaseExclusiveFileLock, rollbackPath } from "./transaction-helpers.mjs";

const suiteRoot = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const stagedSharedRoot = path.resolve(suiteRoot, "../..");
const stagingRoot = path.resolve(stagedSharedRoot, "..");
const stagedSkillsRoot = path.join(stagedSharedRoot, "skills");
const liveHome = "/hwdata/home/jinqc";
const liveSharedRoot = path.join(liveHome, ".codex-shared");
const liveSkillsRoot = path.join(liveSharedRoot, "skills");
const liveSuite = path.join(liveSharedRoot, "suites/research-master");
const manifest = JSON.parse(fs.readFileSync(path.join(suiteRoot, "suite_manifest.json"), "utf8"));
const skillNames = [manifest.orchestrator, ...manifest.method_skills, ...manifest.auxiliary_modules.filter((name) => name !== "bio-tutor")];
const directRoots = [".codex", ".codex-ln01", ".claude"];
const nodeRoots = [".codex-nfat01", ".codex-nfat02", ".codex-nfat03"];
const remoteHosts = ["nfat01", "nfat02", "nfat03", "ln01"];
const syncSkillNames = [...skillNames, "bio-tutorial-writer", "academic-html-report"];
const integrationBaselinePath = path.join(suiteRoot, "integrations/integration-baseline.json");
const bioOverlay = path.join(suiteRoot, "integrations/bio_tutor_overlay");
const htmlOverlay = path.join(suiteRoot, "integrations/academic_html_overlay");
const bioProject = path.join(liveHome, "bio_tutorial_factory");
const htmlSkill = path.join(liveSkillsRoot, "academic-html-report");
const bioFiles = [
  "SKILL.md", "README.md", "ARCHITECTURE.md", "CONTEXT.md", "lessons.md",
  "scripts/article_slot_trace_gate.py", "scripts/codex_final_content_arbiter.py", "scripts/completion_attestation.py",
  "scripts/data_fact_gate.py", "scripts/export_reader_package.py", "scripts/external_model_client.py",
  "scripts/external_style_reviser.py", "scripts/figure_auditor.py", "scripts/figure_fact_gate.py",
  "scripts/figure_vision_review.py", "scripts/finalize_article_layout.py", "scripts/markdown_semantic_inventory.py",
  "scripts/model_evidence_pack.py", "scripts/model_facing_authoring.py", "scripts/reader_artifacts.py", "scripts/reader_facing_output_validator.py",
  "scripts/README.md", "scripts/release_provenance.py", "scripts/review_article.py", "scripts/run_pipeline.py",
  "scripts/validate_completion_state.py", "templates/producer_calls_provenance.schema.json",
  "tests/test_completion_attestation.py", "tests/test_embedded_reader_contract.py", "tests/test_export_reader_package.py",
  "tests/test_article_slot_trace_gate.py", "tests/test_data_fact_gate.py", "tests/test_figure_auditor.py",
  "tests/test_figure_fact_gate.py", "tests/test_finalize_article_layout.py", "tests/test_reader_facing_outputs.py",
  "tests/test_review_article.py", "tests/test_style_reviser_contract.py", "tests/test_three_call_authorization_contract.py"
];
const htmlFiles = [
  ["SKILL.md", "SKILL.md"],
  ["personal_report_preferences.md", "references/personal_report_preferences.md"],
  ["quality_checklist.md", "references/quality_checklist.md"],
  ["references/report_spec_schema.md", "references/report_spec_schema.md"],
  ["scripts/render_report.py", "scripts/render_report.py"],
  ["scripts/validate_html_report.py", "scripts/validate_html_report.py"],
  ["templates/academic_report_template.html", "templates/academic_report_template.html"],
  ["tests/test_embedded_figure_delivery.py", "tests/test_embedded_figure_delivery.py"]
];
const integrationTargets = [
  { id: "bio:CLAUDE.md", source: path.join(bioOverlay, "AGENTS.md"), target: path.join(bioProject, "CLAUDE.md") },
  ...bioFiles.map((relative) => ({ id: `bio:${relative}`, source: path.join(bioOverlay, relative), target: path.join(bioProject, relative) })),
  { id: "bio:global_SKILL.md", source: path.join(bioOverlay, "global_SKILL.md"), target: path.join(liveSkillsRoot, "bio-tutorial-writer/SKILL.md") },
  ...htmlFiles.map(([source, target]) => ({ id: `html:${target}`, source: path.join(htmlOverlay, source), target: path.join(htmlSkill, target) }))
];

const mode = process.argv[2];
if (!["--check-staging", "--check-cutover", "--apply"].includes(mode)) {
  console.error("用法：install-suite.mjs --check-staging | --check-cutover | --apply");
  process.exit(2);
}

function run(command, args, options = {}) {
  return execFileSync(command, args, {
    cwd: liveHome,
    encoding: "utf8",
    stdio: options.capture ? ["ignore", "pipe", "pipe"] : "inherit"
  });
}

function pathExists(filePath) {
  return fs.existsSync(filePath) || fs.lstatSync(filePath, { throwIfNoEntry: false }) !== undefined;
}

function resolvedOrNull(filePath) {
  if (!pathExists(filePath)) return null;
  try {
    return fs.realpathSync(filePath);
  } catch {
    return null;
  }
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function sha256(filePath) {
  return crypto.createHash("sha256").update(fs.readFileSync(filePath)).digest("hex");
}

function integrationBaseline() {
  assert(fs.existsSync(integrationBaselinePath), `缺少接入基线：${integrationBaselinePath}`);
  return JSON.parse(fs.readFileSync(integrationBaselinePath, "utf8"));
}

function validateIntegrationSources() {
  const ids = new Set();
  assert(
    !integrationTargets.some((item) => item.target === path.join(bioProject, "AGENTS.md")),
    "BioTutor AGENTS.md 必须继续指向同目录 CLAUDE.md，安装器不得覆盖"
  );
  for (const item of integrationTargets) {
    assert(!ids.has(item.id), `重复接入目标：${item.id}`);
    ids.add(item.id);
    assert(fs.existsSync(item.source), `缺少接入暂存文件：${item.source}`);
  }
}

function validateIntegrationBaseline() {
  const baseline = integrationBaseline();
  for (const item of integrationTargets) {
    const expected = baseline[item.id];
    assert(expected !== undefined, `接入基线缺少：${item.id}`);
    const exists = fs.existsSync(item.target);
    assert(Boolean(expected.exists) === exists, `接入目标存在状态已变化：${item.target}`);
    if (exists) assert(sha256(item.target) === expected.sha256, `接入目标在暂存后被修改，拒绝覆盖：${item.target}`);
  }
}

function validateStaging() {
  validateIntegrationSources();
  run("node", [path.join(suiteRoot, "tests/validate-suite.mjs")]);
  const validator = path.join(liveSharedRoot, "skills/.system/skill-creator/scripts/quick_validate.py");
  const python = path.join(stagingRoot, ".venv/bin/python");
  assert(fs.existsSync(python), `缺少暂存校验环境：${python}`);
  for (const skillName of skillNames) {
    const skillDir = path.join(stagedSkillsRoot, skillName);
    assert(fs.existsSync(path.join(skillDir, "SKILL.md")), `缺少暂存 skill：${skillName}`);
    run(python, [validator, skillDir], { capture: true });
  }
}

function validateCutoverReadiness() {
  assert(manifest.cutover.install_ready === true, "suite_manifest.cutover.install_ready 仍为 false");
  assert(manifest.bio_tutor_binding.integration_status === "ready", "BioTutor 接入尚未验收");
  assert(manifest.adjacent_output_bindings["academic-html-report"].integration_status === "ready", "academic-html-report 接入尚未验收");
  validateIntegrationBaseline();

  for (const rootName of nodeRoots) {
    const nodeSkills = path.join(liveHome, rootName, "skills");
    assert(pathExists(nodeSkills), `缺少节点 skill 根入口：${nodeSkills}`);
    assert(resolvedOrNull(nodeSkills) === fs.realpathSync(liveSkillsRoot), `${nodeSkills} 没有指向 ${liveSkillsRoot}`);
  }

  for (const skillName of skillNames) {
    const canonical = path.join(liveSkillsRoot, skillName);
    for (const rootName of directRoots) {
      const consumer = path.join(liveHome, rootName, "skills", skillName);
      const resolved = resolvedOrNull(consumer);
      assert(resolved === null || resolved === resolvedOrNull(canonical), `入口冲突：${consumer}`);
    }
  }
}

function captureInitialState() {
  const state = {
    suite_existed: pathExists(liveSuite),
    skills: {},
    consumers: {},
    retired: {},
    integrations: {}
  };
  for (const skillName of skillNames) {
    state.skills[skillName] = pathExists(path.join(liveSkillsRoot, skillName));
    state.consumers[skillName] = {};
    for (const rootName of directRoots) {
      state.consumers[skillName][rootName] = pathExists(path.join(liveHome, rootName, "skills", skillName));
    }
  }
  const retiredPaths = {
    canonical: path.join(liveSkillsRoot, "sci-mentor"),
    codex: path.join(liveHome, ".codex/skills/sci-mentor"),
    codex_ln01: path.join(liveHome, ".codex-ln01/skills/sci-mentor"),
    claude: path.join(liveHome, ".claude/skills/sci-mentor")
  };
  for (const [key, filePath] of Object.entries(retiredPaths)) state.retired[key] = pathExists(filePath);
  for (const item of integrationTargets) state.integrations[item.id] = pathExists(item.target);
  return { state, retiredPaths };
}

function prepareInstallTree(tempRoot) {
  fs.mkdirSync(path.join(tempRoot, "skills"), { recursive: true });
  fs.cpSync(suiteRoot, path.join(tempRoot, "suite"), { recursive: true, dereference: false });
  fs.rmSync(path.join(tempRoot, "suite/integrations/bio_tutor_overlay"), { recursive: true, force: true });
  fs.rmSync(path.join(tempRoot, "suite/integrations/academic_html_overlay"), { recursive: true, force: true });
  for (const skillName of skillNames) {
    fs.cpSync(path.join(stagedSkillsRoot, skillName), path.join(tempRoot, "skills", skillName), { recursive: true, dereference: false });
  }
  for (const item of integrationTargets) {
    const staged = path.join(tempRoot, "integrations", Buffer.from(item.id).toString("hex"));
    fs.mkdirSync(path.dirname(staged), { recursive: true });
    fs.copyFileSync(item.source, staged);
  }
}

function moveIfPresent(source, target) {
  if (!pathExists(source)) return false;
  fs.mkdirSync(path.dirname(target), { recursive: true });
  fs.renameSync(source, target);
  return true;
}

function verifyAllNodes(integrationHashes) {
  for (const skillName of syncSkillNames) run("agent-skill-sync", ["verify", skillName, "--no-remote"], { capture: true });

  for (const item of integrationTargets) {
    assert(pathExists(item.target), `接入目标安装后缺失：${item.target}`);
    assert(sha256(item.target) === integrationHashes[item.id], `接入目标安装后哈希不一致：${item.target}`);
  }

  const quotedSkills = syncSkillNames.map((name) => `'${name}'`).join(" ");
  const remoteIntegrationChecks = integrationTargets
    .map((item) => `echo '${integrationHashes[item.id]}  ${item.target}' | sha256sum -c - >/dev/null`)
    .join("\n");
  const remoteScript = `set -e\nfor name in ${quotedSkills}; do\n  for p in .codex-shared/skills .codex/skills .codex-ln01/skills .claude/skills .codex-nfat01/skills .codex-nfat02/skills .codex-nfat03/skills; do\n    test -f '${liveHome}/'\"$p\"'/'\"$name\"'/SKILL.md'\n  done\ndone\ntest -f '${liveSuite}/suite_manifest.json'\ntest ! -e '${liveSkillsRoot}/sci-mentor/SKILL.md'\n${remoteIntegrationChecks}\necho OK`;
  for (const host of remoteHosts) {
    run("ssh", ["-o", "BatchMode=yes", "-o", "ConnectTimeout=8", "-o", "StrictHostKeyChecking=no", host, remoteScript], { capture: true });
  }
}

function rollback(transactionRoot, tempRoot, initial, retiredPaths) {
  for (const skillName of skillNames) {
    for (const rootName of directRoots) {
      const consumer = path.join(liveHome, rootName, "skills", skillName);
      if (!initial.consumers[skillName][rootName] && pathExists(consumer)) moveIfPresent(consumer, path.join(transactionRoot, "failed-created-consumers", rootName, skillName));
    }
  }

  for (const skillName of skillNames) {
    const liveSkill = path.join(liveSkillsRoot, skillName);
    const previous = path.join(transactionRoot, "previous-skills", skillName);
    rollbackPath({
      current: liveSkill,
      backup: previous,
      failed: path.join(transactionRoot, "failed-new-skills", skillName),
      existedInitially: initial.skills[skillName]
    });
  }

  const previousSuite = path.join(transactionRoot, "previous-suite");
  rollbackPath({
    current: liveSuite,
    backup: previousSuite,
    failed: path.join(transactionRoot, "failed-new-suite"),
    existedInitially: initial.suite_existed
  });

  for (const [key, filePath] of Object.entries(retiredPaths)) {
    const backup = path.join(transactionRoot, "retired-sci-mentor", key);
    if (pathExists(backup)) moveIfPresent(backup, filePath);
  }
  for (const item of [...integrationTargets].reverse()) {
    const backup = path.join(transactionRoot, "previous-integrations", Buffer.from(item.id).toString("hex"));
    rollbackPath({
      current: item.target,
      backup,
      failed: path.join(transactionRoot, "failed-new-integrations", Buffer.from(item.id).toString("hex")),
      existedInitially: initial.integrations[item.id]
    });
  }
  for (const skillName of syncSkillNames) {
    if (pathExists(path.join(liveSkillsRoot, skillName))) {
      run("agent-skill-sync", ["install", path.join(liveSkillsRoot, skillName), "--mode", "copy", "--replace", "--no-remote"], { capture: true });
    }
  }
  if (pathExists(tempRoot)) moveIfPresent(tempRoot, path.join(transactionRoot, "unused-staging"));
}

validateStaging();
if (mode === "--check-staging") {
  console.log(`staging check passed: skills=${skillNames.length}`);
  process.exit(0);
}

validateCutoverReadiness();
if (mode === "--check-cutover") {
  console.log(`cutover check passed: skills=${skillNames.length} hosts=${remoteHosts.length}`);
  process.exit(0);
}

const installLock = acquireExclusiveFileLock(
  path.join(liveSharedRoot, "transactions/research-master.install.lock"),
  { pid: process.pid, started_at: new Date().toISOString() }
);
process.once("exit", () => releaseExclusiveFileLock(installLock));
validateIntegrationBaseline();
const applyBaseline = integrationBaseline();
const stamp = new Date().toISOString().replace(/[-:TZ.]/g, "");
const transactionRoot = path.join(liveSharedRoot, "transactions", `research-master-${stamp}`);
const tempRoot = path.join(liveSharedRoot, `.research-master-install-${stamp}`);
const { state: initial, retiredPaths } = captureInitialState();

fs.mkdirSync(transactionRoot, { recursive: true });
fs.writeFileSync(path.join(transactionRoot, "initial-state.json"), `${JSON.stringify(initial, null, 2)}\n`, "utf8");
prepareInstallTree(tempRoot);
validateIntegrationBaseline();

try {
  moveIfPresent(liveSuite, path.join(transactionRoot, "previous-suite"));
  fs.mkdirSync(path.dirname(liveSuite), { recursive: true });
  fs.renameSync(path.join(tempRoot, "suite"), liveSuite);

  for (const skillName of skillNames) {
    const liveSkill = path.join(liveSkillsRoot, skillName);
    moveIfPresent(liveSkill, path.join(transactionRoot, "previous-skills", skillName));
    fs.renameSync(path.join(tempRoot, "skills", skillName), liveSkill);
  }

  const installedIntegrationHashes = {};
  for (const item of integrationTargets) {
    const staged = path.join(tempRoot, "integrations", Buffer.from(item.id).toString("hex"));
    const backup = path.join(transactionRoot, "previous-integrations", Buffer.from(item.id).toString("hex"));
    const expected = applyBaseline[item.id];
    const stagedHash = sha256(staged);
    const moved = moveIfPresent(item.target, backup);
    assert(moved === Boolean(expected.exists), `接入目标在覆盖瞬间发生存在状态变化：${item.target}`);
    if (moved) assert(sha256(backup) === expected.sha256, `接入目标在覆盖瞬间被修改：${item.target}`);
    fs.mkdirSync(path.dirname(item.target), { recursive: true });
    fs.renameSync(staged, item.target);
    assert(sha256(item.target) === stagedHash, `接入目标写入后哈希不一致：${item.target}`);
    installedIntegrationHashes[item.id] = stagedHash;
  }

  for (const [key, filePath] of Object.entries(retiredPaths)) moveIfPresent(filePath, path.join(transactionRoot, "retired-sci-mentor", key));

  for (const skillName of syncSkillNames) {
    run("agent-skill-sync", ["install", path.join(liveSkillsRoot, skillName), "--mode", "copy", "--replace", "--no-remote"], { capture: true });
  }
  verifyAllNodes(installedIntegrationHashes);
  if (pathExists(tempRoot)) fs.renameSync(tempRoot, path.join(transactionRoot, "unused-staging"));
  fs.writeFileSync(path.join(transactionRoot, "COMPLETED"), `${new Date().toISOString()}\n`, "utf8");
  console.log(`suite install passed: skills=${skillNames.length} hosts=${remoteHosts.length} transaction=${transactionRoot}`);
} catch (error) {
  rollback(transactionRoot, tempRoot, initial, retiredPaths);
  fs.writeFileSync(path.join(transactionRoot, "ROLLED_BACK"), `${new Date().toISOString()}\n${error.stack ?? error}\n`, "utf8");
  console.error(`suite install failed and rolled back: ${error.message}`);
  process.exit(1);
}
