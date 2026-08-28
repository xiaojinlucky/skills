import fs from "node:fs";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";

const suiteRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const codexSharedRoot = path.resolve(suiteRoot, "../..");
const activeRoot = path.join(codexSharedRoot, "active-global-skills");
const localMethodRoot = "F:\\科研大师兄\\my skills\\0 metasci-skills";
const repositoryMethodRoot = path.join(codexSharedRoot, "skills");
const methodRoot = fs.existsSync(path.join(repositoryMethodRoot, "meta-research-hub", "SKILL.md"))
  ? repositoryMethodRoot
  : fs.existsSync(localMethodRoot)
    ? localMethodRoot
    : repositoryMethodRoot;
const localScopeManifestPath = path.join(codexSharedRoot, "skill-scopes", "local-scope-manifest.json");
const serverScopeManifestPath = path.join(codexSharedRoot, "skill-scopes", "server-scope-manifest.json");
const scopeManifestPath = fs.existsSync(localScopeManifestPath)
  ? localScopeManifestPath
  : fs.existsSync(serverScopeManifestPath)
    ? serverScopeManifestPath
    : null;
const manifest = JSON.parse(fs.readFileSync(path.join(suiteRoot, "suite_manifest.json"), "utf8"));
const routes = JSON.parse(fs.readFileSync(path.join(suiteRoot, "tests", "route_cases.json"), "utf8"));
const sourceIndex = JSON.parse(fs.readFileSync(path.join(suiteRoot, "sources", "source-index.json"), "utf8"));
const scopeManifest = scopeManifestPath
  ? JSON.parse(fs.readFileSync(scopeManifestPath, "utf8"))
  : null;

const failures = [];
const checks = [];

function check(condition, message) {
  checks.push(message);
  if (!condition) failures.push(message);
}

function read(filePath) {
  return fs.readFileSync(filePath, "utf8");
}

function skillDir(name) {
  const shared = path.join(activeRoot, name);
  if (fs.existsSync(path.join(shared, "SKILL.md"))) return shared;
  const method = path.join(methodRoot, name);
  if (fs.existsSync(path.join(method, "SKILL.md"))) return method;
  return null;
}

function skillBody(name) {
  const directory = skillDir(name);
  return directory ? read(path.join(directory, "SKILL.md")) : "";
}

function frontmatterName(markdown) {
  return markdown.match(/^---\r?\n[\s\S]*?^name:\s*([a-z0-9-]+)\s*$/m)?.[1] ?? "";
}

const expectedSkills = [
  manifest.orchestrator,
  ...manifest.method_skills,
  ...manifest.auxiliary_modules.filter((name) => name !== "bio-tutor"),
];
const resolvedSkills = expectedSkills.filter((name) => skillDir(name));

check(manifest.status === "active", "Research Suite 状态为 active");
check(manifest.method_skills.length === 13, "Research Suite 包含 13 个方法 Skill");
check(new Set(expectedSkills).size === 17, "17 个可调用逻辑 Skill 名称唯一");
check(resolvedSkills.length === expectedSkills.length, "17 个现役 canonical 均可解析");
check(manifest.runtime_contract.relevant_skill_limit === null, "相关 Skill 不设机械数量上限");
check(manifest.runtime_contract.ordinary_dialogue_added_agent_calls === 0, "普通科研对话不固定增加 Agent");
check(manifest.shared_resources_are_callable_skills === false, "shared canonical 不伪装成可调用 Skill");

for (const sharedPath of manifest.shared) {
  check(fs.existsSync(path.join(suiteRoot, sharedPath)), "共享资源存在：" + sharedPath);
}

const dangerousPositiveRules = [
  "rescue 是 10+ 必要条件",
  "没有 rescue 实验设计的文章基本不可能上一区或 10+",
  "文献先给候选",
  "论文 A 报道 X，所以本项目优先筛 X",
];

for (const name of expectedSkills) {
  const body = skillBody(name);
  check(Boolean(body), name + " 正文可读取");
  check(frontmatterName(body) === name, name + " frontmatter 名称正确");
  check(/^description:\s*(?:\||>|["']|[^\r\n])/m.test(body), name + " 有触发与职责描述");
  check(!body.includes("TODO"), name + " 没有模板 TODO");
  for (const rule of dangerousPositiveRules) {
    check(!body.includes(rule), name + " 不包含旧的有害硬规则：" + rule);
  }
}

for (const name of [...manifest.method_skills, "xhs-bioinfo-writing"]) {
  const body = skillBody(name);
  check(body.includes("research-core.md"), name + " 继承 Research shared canonical");
  check(!body.includes("## 审计信息"), name + " 不保留历史自评审计块");
}

const xhs = skillBody("xhs-bioinfo-writing");
check(xhs.includes("**唯一负责的决定**"), "xhs-bioinfo-writing 只负责平台表达适配");
check(xhs.includes("当前课题的候选、机制和故事只能由当前课题证据产生"), "xhs-bioinfo-writing 继承 Novelty Firewall");
check(xhs.includes("不要固定 3000–5000 字"), "xhs-bioinfo-writing 不再固定篇幅和标题数量");
check(!xhs.includes("## 师兄表达规范（全系列统一）"), "xhs-bioinfo-writing 不复制 shared 表达内核");

const researchCore = read(path.join(suiteRoot, "shared", "research-core.md"));
const routingCore = read(path.join(suiteRoot, "shared", "routing-and-authority.md"));
check(researchCore.includes("文献可以决定怎么找，不能默认决定要找到什么"), "Research shared canonical 包含 Novelty Firewall");
for (const role of [
  "METHOD_REFERENCE",
  "DISCOVERY_PATH_REFERENCE",
  "KNOWN_SPACE_EVIDENCE",
  "GAP_SOURCE",
  "POST_DISCOVERY_INTERPRETATION",
  "EXPLICIT_REPLICATION_TARGET",
]) {
  check(researchCore.includes(role), "Research shared canonical 包含文献角色 " + role);
}
check(/不得默认走“论文给出已知候选/.test(researchCore), "默认路径阻断 prior-conclusion leakage");
check(/不得只因缺少高水平论文先例而降级/.test(researchCore), "保护 literature-negative discovery");
check(/不要求重新发明工具/.test(researchCore), "Novelty Firewall 不错杀成熟工具复用");
check(
  /所有拥有独立、会改变结果的未决问题的方法论 skill 都是上游内容决策者/.test(routingCore)
    && routingCore.includes("不设数量上限")
    && manifest.runtime_contract.full_lifecycle_may_use_all_13_method_skills === true,
  "复杂全流程按独立未决问题调用所有真正相关的方法 Skill",
);
check(routingCore.includes("同一份共享内核、方法卡或来源摘录只读取一次"), "共享材料每个任务只读取一次");

check(Array.isArray(routes.cases) && routes.cases.length >= 25, "路由回归至少包含 25 个真实场景");
const allowedRequired = new Set(expectedSkills);
for (const testCase of routes.cases) {
  check(typeof testCase.id === "string" && testCase.id.length > 0, "每个路由案例都有 ID");
  for (const required of testCase.required ?? []) {
    check(allowedRequired.has(required), testCase.id + " 的必需 Skill 存在：" + required);
    check(!(testCase.forbidden ?? []).includes(required), testCase.id + " 不会同时要求和禁止 " + required);
  }
}

const fullLifecycle = routes.cases.find((item) => item.id === "full-lifecycle-all-methods");
check(Boolean(fullLifecycle), "存在完整科研生命周期案例");
for (const method of manifest.method_skills) {
  check(fullLifecycle?.required.includes(method), "完整生命周期覆盖 " + method);
}
const publicPost = routes.cases.find((item) => item.id === "public-bioinfo-post");
check(publicPost?.required.includes("xhs-bioinfo-writing"), "中文生信社区推文路由到 xhs-bioinfo-writing");
const bioTutor = routes.cases.find((item) => item.id === "biotutor-official-tutorial");
check(
  bioTutor?.dependencies.includes("bio-tutorial-writer")
    && bioTutor?.forbidden.includes("xhs-bioinfo-writing"),
  "完整 BioTutor 教程不误入短推文 Skill",
);

check(
  Array.isArray(routes.novelty_firewall_cases)
    && routes.novelty_firewall_cases.length === 6,
  "Novelty Firewall 包含主场景与 A–E 回归",
);
const leakage = routes.novelty_firewall_cases.find(
  (item) => item.id === "discovery-related-literature-does-not-seed-answer",
);
check(
  leakage?.forbidden_behaviors.includes("论文 A 报道 X，所以本项目优先筛 X。"),
  "CZM 类 prior-conclusion leakage 固定为禁止行为",
);
const replication = routes.novelty_firewall_cases.find(
  (item) => item.id === "explicit-replication-can-test-published-conclusion",
);
check(
  replication?.literature_roles.includes("EXPLICIT_REPLICATION_TARGET"),
  "明确复现允许验证已发表结论",
);
const toolReuse = routes.novelty_firewall_cases.find(
  (item) => item.id === "mature-analysis-tool-still-reused",
);
check(
  toolReuse?.expected_behaviors.some((text) => text.includes("优先复用成熟工具")),
  "科学答案原创不被误用为重新造分析工具",
);

if (scopeManifest) {
  const taskRoutes = scopeManifest.routing?.task_routes ?? scopeManifest.task_routes ?? [];
  const activeOwnerNames = new Set([
    ...Object.values(scopeManifest.profiles ?? {}).flat(),
    ...taskRoutes.flatMap((route) => route.skills ?? []),
  ]);
  const metaRoute = taskRoutes.find(
    (item) => item.id === "research-tutorial.meta" || item.skills?.includes("meta-research-hub"),
  );
  check(
    JSON.stringify(metaRoute?.skills) === JSON.stringify(["meta-research-hub"]),
    "旧 MetaSci 名称统一路由到 meta-research-hub",
  );
  const xhsRoute = taskRoutes.find((item) => item.id === "research-tutorial.public-bioinfo-post");
  check(
    JSON.stringify(xhsRoute?.skills) === JSON.stringify(["xhs-bioinfo-writing"])
      || activeOwnerNames.has("xhs-bioinfo-writing"),
    "scope router 可发现 xhs-bioinfo-writing",
  );
  for (const name of [manifest.orchestrator, ...manifest.method_skills, "xhs-bioinfo-writing"]) {
    check(
      Boolean(scopeManifest.sources?.[name]) || activeOwnerNames.has(name),
      "scope manifest 声明 canonical：" + name,
    );
    check(skillDir(name) !== null, "scope manifest 对应 canonical 存在：" + name);
  }
  check(!activeOwnerNames.has("meta-superpowers"), "active owner 不包含 meta-superpowers");
  check(!activeOwnerNames.has("research-orchestrator"), "active owner 不包含 research-orchestrator");
} else {
  check(
    true,
    "纯仓库快照不打包宿主私有 scope manifest，公开套件门禁保持可独立运行",
  );
}
check(
  !fs.existsSync(path.join(methodRoot, "meta-superpowers"))
    && !fs.existsSync(path.join(methodRoot, "research-orchestrator")),
  "旧 Research orchestrator 目录已移除",
);

check(
  fs.existsSync(path.join(suiteRoot, manifest.bio_tutor_binding.integration_contract)),
  "BioTutor 本地接入合同存在",
);
const htmlBinding = manifest.adjacent_output_bindings["academic-html-report"];
check(
  fs.existsSync(path.join(suiteRoot, htmlBinding.integration_contract)),
  "academic-html-report 本地接入合同存在",
);
check(manifest.bio_tutor_binding.integration_status === "ready", "BioTutor 绑定状态为 ready");
check(htmlBinding.integration_status === "ready", "academic-html-report 绑定状态为 ready");
check(fs.existsSync(path.join(suiteRoot, manifest.cutover.installer)), "套件事务安装脚本仍存在");

for (const target of ["bio-tutor", "xhs-bioinfo-writing", "academic-html-report"]) {
  check(Boolean(sourceIndex.task_map[target]), "来源索引覆盖输出：" + target);
  check(
    Array.isArray(sourceIndex.task_map[target].priority)
      && sourceIndex.task_map[target].priority.length > 0,
    target + " 有按需来源优先级",
  );
}

if (failures.length > 0) {
  console.error("suite validation failed: " + failures.length + "/" + checks.length);
  for (const failure of failures) console.error("- " + failure);
  process.exit(1);
}

console.log("suite validation passed: " + checks.length + "/" + checks.length);
