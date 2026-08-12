import fs from "node:fs";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";

const suiteRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const codexSharedRoot = path.resolve(suiteRoot, "../..");
const skillsRoot = path.join(codexSharedRoot, "skills");
const manifest = JSON.parse(fs.readFileSync(path.join(suiteRoot, "suite_manifest.json"), "utf8"));
const routes = JSON.parse(fs.readFileSync(path.join(suiteRoot, "tests/route_cases.json"), "utf8"));
const sourceIndex = JSON.parse(fs.readFileSync(path.join(suiteRoot, "sources/source-index.json"), "utf8"));

const failures = [];
const checks = [];

function check(condition, message) {
  checks.push(message);
  if (!condition) failures.push(message);
}

function read(filePath) {
  return fs.readFileSync(filePath, "utf8");
}

function frontmatter(markdown) {
  const match = markdown.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return {};
  const result = {};
  for (const line of match[1].split("\n")) {
    const field = line.match(/^([a-z_]+):\s*(.+)$/);
    if (field) result[field[1]] = field[2].trim();
  }
  return result;
}

const manifestSkills = [manifest.orchestrator, ...manifest.method_skills, ...manifest.auxiliary_modules.filter((name) => name !== "bio-tutor")].sort();
const skillNames = manifestSkills
  .filter((name) => fs.existsSync(path.join(skillsRoot, name, "SKILL.md")))
  .sort();

check(skillNames.length === manifest.new_skills, "17 个新 skill 目录齐全");
check(manifest.logical_modules === 18, "逻辑模块总数为 18");
check(manifest.runtime_contract.relevant_skill_limit === null, "相关 skill 没有数量上限");
check(manifest.runtime_contract.full_lifecycle_may_use_all_13_method_skills === true, "全流程允许 13 个方法 skill 全部参与");
check(manifest.runtime_contract.ordinary_dialogue_added_agent_calls === 0, "日常对话不新增 Agent 或外部模型调用");
check(manifest.shared_resources_are_callable_skills === false, "公共内核不是第 19 个可调用 skill");

check(JSON.stringify(skillNames) === JSON.stringify(manifestSkills), "目录与 manifest 中的 17 个 skill 完全一致");

for (const sharedPath of manifest.shared) {
  check(fs.existsSync(path.join(suiteRoot, sharedPath)), `公共资源存在：${sharedPath}`);
}

const ownedDecisions = new Map();
const longParagraphOwners = new Map();
const sharedParagraphOwners = new Map();
const negativeMarkers = ["不", "禁止", "不能", "不得", "不要", "避免", "拒绝", "移除"];
const dangerousRules = [
  /没有.*rescue.*不可能.*(一区|10\+)/i,
  /必须.*(?:40\s*[%％].*60\s*[%％]|60\s*[%％].*40\s*[%％])/,
  /(?:一篇|三篇).*撞题.*(?:没创新|死亡)/,
  /P\s*[>＞]\s*0\.05.*(?:证明|完全中介)/i,
  /固定.*(?:六|6).*Figure/i,
  /固定.*(?:2v2|3v3)/i,
  /差异基因.*数量.*(?:功能|意义)/,
  /批次校正.*差异消失.*(?:不用|不做)校正/
];

for (const sharedPath of manifest.shared.filter((filePath) => filePath.endsWith(".md"))) {
  const sharedBody = read(path.join(suiteRoot, sharedPath));
  for (const paragraph of sharedBody.split(/\n\s*\n/).map((text) => text.trim()).filter((text) => text.length >= 180)) {
    sharedParagraphOwners.set(paragraph, sharedPath);
  }
}

for (const skillName of skillNames) {
  const skillPath = path.join(skillsRoot, skillName, "SKILL.md");
  const yamlPath = path.join(skillsRoot, skillName, "agents/openai.yaml");
  const body = read(skillPath);
  const meta = frontmatter(body);

  check(meta.name === skillName, `${skillName} 的 frontmatter 名称正确`);
  check(Boolean(meta.description) && /Use when|Route and coordinate|Help a new/.test(meta.description), `${skillName} 的描述包含触发条件`);
  check(!body.includes("TODO"), `${skillName} 没有模板残留`);
  check(body.includes("**进入条件**"), `${skillName} 写明进入条件`);
  check(body.includes("**唯一负责的决定**"), `${skillName} 写明唯一职责`);
  check(body.includes("**退出条件**"), `${skillName} 写明退出条件`);
  check(body.includes("**交接对象**"), `${skillName} 写明交接对象`);
  check(fs.existsSync(yamlPath), `${skillName} 存在 agents/openai.yaml`);

  const resourceReferences = [...body.matchAll(/`([^`]+\.(?:md|json))`/g)].map((match) => match[1]);
  check(resourceReferences.length > 0, `${skillName} 至少引用一项套件级公共资源`);
  for (const reference of resourceReferences) {
    check(reference.startsWith("../../suites/research-master/"), `${skillName} 的资源引用使用完整套件相对路径：${reference}`);
    check(fs.existsSync(path.resolve(path.dirname(skillPath), reference)), `${skillName} 的公共资源引用可解析：${reference}`);
  }
  check(!body.includes("/hwdata/home/jinqc/Reference/0 做科研的大师兄 四份资料"), `${skillName} 运行时不直连扫描四份原材料`);

  const yaml = read(yamlPath);
  check(yaml.includes(`$${skillName}`), `${skillName} 的默认提示显式点名 skill`);
  check(yaml.includes("allow_implicit_invocation: true"), `${skillName} 允许灵敏的隐式触发`);
  const shortDescription = yaml.match(/short_description:\s*"([^"]+)"/)?.[1] ?? "";
  const shortDescriptionLength = Array.from(shortDescription).length;
  check(shortDescriptionLength >= 25 && shortDescriptionLength <= 64, `${skillName} 的 short_description 长度为 25–64 个字符`);

  const decision = body.match(/\*\*唯一负责的决定\*\*：(.+)/)?.[1]?.trim();
  if (decision) {
    const previous = ownedDecisions.get(decision);
    check(!previous, `${skillName} 的唯一职责不与 ${previous ?? "其他 skill"} 完全重复`);
    ownedDecisions.set(decision, skillName);
  }

  for (const line of body.split("\n")) {
    if (negativeMarkers.some((marker) => line.includes(marker))) continue;
    for (const pattern of dangerousRules) {
      check(!pattern.test(line), `${skillName} 未把禁用硬规则写成正向要求`);
    }
  }

  for (const paragraph of body.split(/\n\s*\n/).map((text) => text.trim()).filter((text) => text.length >= 180)) {
    if (paragraph.startsWith("---")) continue;
    if (paragraph.startsWith("本任务尚未加载时")) continue;
    const previous = longParagraphOwners.get(paragraph);
    check(!previous, `${skillName} 没有复制 ${previous ?? "其他 skill"} 的长段公共内核`);
    const sharedSource = sharedParagraphOwners.get(paragraph);
    check(!sharedSource, `${skillName} 没有内联复制 ${sharedSource ?? "shared 资源"} 的长段公共内核`);
    longParagraphOwners.set(paragraph, skillName);
  }
}

const orchestrator = read(path.join(skillsRoot, "meta-research-hub/SKILL.md"));
const researchCore = read(path.join(suiteRoot, "shared/research-core.md"));
check(/调动所有真正相关的方法论 skill，不限制数量/.test(orchestrator) && /不设数量上限/.test(orchestrator), "总调度描述明确禁止限制相关 skill 数量");
check(/13 个方法 skill 可以全部参与/.test(read(path.join(suiteRoot, "shared/routing-and-authority.md"))), "路由合同明确全流程可用全部 13 个方法 skill");
check(/同一任务中，同一份共享内核、方法卡或来源摘录只读取一次/.test(read(path.join(suiteRoot, "shared/routing-and-authority.md"))), "路由合同明确共享资源每个任务只读取一次");
check(/文献可以决定怎么找，不能默认决定要找到什么/.test(researchCore), "科研共同内核明确文献不能预填本课题答案");
for (const role of ["METHOD_REFERENCE", "DISCOVERY_PATH_REFERENCE", "KNOWN_SPACE_EVIDENCE", "GAP_SOURCE", "POST_DISCOVERY_INTERPRETATION", "EXPLICIT_REPLICATION_TARGET"]) {
  check(researchCore.includes(role), `科研共同内核包含文献角色 ${role}`);
}
check(/不得默认走“论文给出已知候选/.test(researchCore), "科研共同内核阻断论文结论到本项目候选的默认路径");
check(/不得只因缺少高水平论文先例而降级/.test(researchCore), "科研共同内核保护缺少先例但证据可信的新发现");
check(/不要求重新发明工具/.test(researchCore), "科研创新隔离墙不会错杀成熟工具复用");
check(!skillNames.includes("sci-mentor"), "正式套件不包含 sci-mentor");

check(routes.cases.length >= 25, "路由测试不少于 25 个正例、反例和组合场景");
check(routes.policy.relevant_skill_limit === null, "路由测试策略没有 skill 数量上限");
const allowedRequired = new Set(skillNames);
for (const testCase of routes.cases) {
  check(["direct", "orchestrated", "composite_direct", "style_only", "non_research"].includes(testCase.route), `${testCase.id} 的 route 类型有效`);
  check(typeof testCase.request === "string" && testCase.request.length > 0, `${testCase.id} 有真实请求文本`);
  const forbidden = new Set(testCase.forbidden ?? []);
  for (const required of testCase.required ?? []) {
    check(allowedRequired.has(required), `${testCase.id} 的必需 skill 存在：${required}`);
    check(!forbidden.has(required), `${testCase.id} 不会同时要求和禁止 ${required}`);
  }
  for (const field of ["requires_current_official_rules", "must_retain_evidence", "must_reject_p_value_shortcut", "requires_validity_gate"]) {
    check(testCase[field] === undefined || typeof testCase[field] === "boolean", `${testCase.id} 的 ${field} 条件字段类型正确`);
  }
}

check(Array.isArray(routes.novelty_firewall_cases) && routes.novelty_firewall_cases.length === 6, "科研创新隔离墙包含主场景和 A-E 六个回归案例");
const noveltyCaseIds = new Set();
for (const testCase of routes.novelty_firewall_cases ?? []) {
  check(typeof testCase.id === "string" && testCase.id.length > 0 && !noveltyCaseIds.has(testCase.id), `${testCase.id ?? "unknown"} 的回归案例 ID 唯一`);
  noveltyCaseIds.add(testCase.id);
  check(["discovery", "replication", "method-selection"].includes(testCase.mode), `${testCase.id} 的科研模式有效`);
  check(typeof testCase.input === "string" && testCase.input.length > 0, `${testCase.id} 有真实输入`);
  check(Array.isArray(testCase.literature_roles) && testCase.literature_roles.length > 0, `${testCase.id} 明确文献角色`);
  check(Array.isArray(testCase.expected_behaviors) && testCase.expected_behaviors.length > 0, `${testCase.id} 明确正确行为`);
  check(Array.isArray(testCase.forbidden_behaviors) && testCase.forbidden_behaviors.length > 0, `${testCase.id} 明确禁止行为`);
}
const leakageRegression = (routes.novelty_firewall_cases ?? []).find((testCase) => testCase.id === "discovery-related-literature-does-not-seed-answer");
check(leakageRegression?.forbidden_behaviors.includes("论文 A 报道 X，所以本项目优先筛 X。"), "CZM 类错误模式被固定为禁止行为");
const replicationRegression = (routes.novelty_firewall_cases ?? []).find((testCase) => testCase.id === "explicit-replication-can-test-published-conclusion");
check(replicationRegression?.literature_roles.includes("EXPLICIT_REPLICATION_TARGET"), "明确复现任务允许把论文结论作为验证对象");
const toolReuseRegression = (routes.novelty_firewall_cases ?? []).find((testCase) => testCase.id === "mature-analysis-tool-still-reused");
check(toolReuseRegression?.expected_behaviors.some((text) => text.includes("优先复用成熟工具")), "科学答案原创不会被误用为重复造分析工具");

const fullLifecycle = routes.cases.find((testCase) => testCase.id === "full-lifecycle-all-methods");
check(Boolean(fullLifecycle), "存在用户明确要求全部 13 个方法的路由案例");
check(fullLifecycle?.required.includes(manifest.orchestrator), "完整科研生命周期明确经过总调度入口");
for (const method of manifest.method_skills) {
  check(fullLifecycle?.required.includes(method), `完整生命周期覆盖 ${method}`);
}

const styleOnly = routes.cases.find((testCase) => testCase.id === "dialogue-style-only");
check(styleOnly?.required.length === 0 && styleOnly?.forbidden.includes("meta-research-hub"), "仅调整对话语感时不启动科研工作流");
const simplePlots = routes.cases.find((testCase) => testCase.id === "simple-two-plots");
check(simplePlots?.forbidden.includes("academic-html-report"), "一两张简单结果图不触发学术 HTML");
const zeroToOpening = routes.cases.find((testCase) => testCase.id === "zero-to-opening");
check(zeroToOpening?.route === "composite_direct" && zeroToOpening?.forbidden.includes(manifest.orchestrator), "从零到第一版开题由 meta-sci-init 直接编排，不双重调度");
const selectiveLifecycle = routes.cases.find((testCase) => testCase.id === "full-lifecycle-selective");
check(selectiveLifecycle?.forbidden.includes("review-writing"), "普通全流程任务不会为了凑齐 13 个方法而强制调用综述 skill");
const bioTutor = routes.cases.find((testCase) => testCase.id === "biotutor-official-tutorial");
check(bioTutor?.dependencies.includes("bio-tutorial-writer") && bioTutor?.forbidden.includes("xhs-bioinfo-writing"), "BioTutor 继续走现有工程入口，不走普通文案 skill");
check(fs.existsSync(path.join(suiteRoot, manifest.bio_tutor_binding.integration_contract)), "BioTutor 存在明确的套件接入合同");
check(fs.existsSync(manifest.bio_tutor_binding.project_implementation), "BioTutor 项目实现入口存在");
check(fs.existsSync(path.join("/hwdata/home/jinqc/.codex-shared/skills", manifest.bio_tutor_binding.global_entry, "SKILL.md")), "BioTutor 全局入口 skill 存在");
check(manifest.bio_tutor_binding.integration_status === "ready", "BioTutor 接入已通过验收");
const htmlBinding = manifest.adjacent_output_bindings["academic-html-report"];
check(fs.existsSync(path.join(suiteRoot, htmlBinding.integration_contract)), "academic-html-report 存在明确的套件接入合同");
check(fs.existsSync(htmlBinding.live_skill), "academic-html-report 线上 skill 入口存在");
check(htmlBinding.integration_status === "ready", "academic-html-report 接入已通过验收");
check(manifest.cutover.install_ready === true, "套件已满足原子切换条件");
check(fs.existsSync(path.join(suiteRoot, manifest.cutover.installer)), "存在套件级事务安装脚本");

check(fs.existsSync(sourceIndex.skill_sources.root), "来源 skill 根目录存在");
for (const corpus of sourceIndex.corpora) {
  check(fs.existsSync(corpus.root), `原材料目录存在：${corpus.id}`);
  check(fs.existsSync(path.resolve(corpus.root, corpus.index)), `原材料索引存在：${corpus.id}`);
}
for (const outputTarget of ["bio-tutor", "xhs-bioinfo-writing", "academic-html-report"]) {
  check(Boolean(sourceIndex.task_map[outputTarget]), `来源索引覆盖长文输出：${outputTarget}`);
  check(sourceIndex.task_map[outputTarget].priority.length >= 3, `${outputTarget} 会从多份原材料选取相关表达与方法`);
}

if (failures.length > 0) {
  console.error(`suite validation failed: ${failures.length}/${checks.length}`);
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log(`suite validation passed: ${checks.length}/${checks.length}`);
