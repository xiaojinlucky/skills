import fs from "node:fs";
import path from "node:path";
import process from "node:process";

const suiteRoot = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const stagingRoot = path.resolve(suiteRoot, "../../..");
const skillsRoot = path.join(stagingRoot, ".codex-shared/skills");
const bioOverlayRoot = path.join(suiteRoot, "integrations/bio_tutor_overlay");
const htmlOverlayRoot = path.join(suiteRoot, "integrations/academic_html_overlay");
const bioRoot = fs.existsSync(bioOverlayRoot) ? bioOverlayRoot : path.join(stagingRoot, "bio_tutorial_factory");
const htmlRoot = fs.existsSync(htmlOverlayRoot) ? htmlOverlayRoot : path.join(skillsRoot, "academic-html-report");
const htmlReferenceRoot = fs.existsSync(htmlOverlayRoot) ? htmlOverlayRoot : path.join(htmlRoot, "references");
const manifest = JSON.parse(fs.readFileSync(path.join(suiteRoot, "suite_manifest.json"), "utf8"));
const envPath = "/hwdata/home/jinqc/env";
const outputPath = path.join(suiteRoot, "tests/deepseek-implementation-audit.json");

function parseEnv(text) {
  const result = {};
  for (const rawLine of text.split("\n")) {
    const line = rawLine.trim();
    if (!line || line.startsWith("#")) continue;
    const split = line.indexOf("=");
    if (split < 1) continue;
    const key = line.slice(0, split).trim();
    let value = line.slice(split + 1).trim();
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }
    result[key] = value;
  }
  return result;
}

function collectFiles() {
  const files = [
    path.join(suiteRoot, "suite_manifest.json"),
    path.join(suiteRoot, "shared/research-core.md"),
    path.join(suiteRoot, "shared/expression-core.md"),
    path.join(suiteRoot, "shared/routing-and-authority.md"),
    path.join(suiteRoot, "shared/research-state.md"),
    path.join(suiteRoot, "methods/method-cards.md"),
    path.join(suiteRoot, "sources/task-expression-cards.md"),
    path.join(suiteRoot, "sources/source-index.json"),
    path.join(suiteRoot, "tests/route_cases.json"),
    path.join(suiteRoot, "tests/validate-suite.mjs"),
    path.join(suiteRoot, "scripts/install-suite.mjs"),
    path.join(suiteRoot, "integrations/integration-baseline.json"),
    path.join(suiteRoot, "integrations/bio-tutor.md"),
    path.join(suiteRoot, "integrations/academic-html-report.md"),
    path.join(bioRoot, "SKILL.md"),
    path.join(bioRoot, "scripts/external_style_reviser.py"),
    path.join(bioRoot, "scripts/reader_artifacts.py"),
    path.join(bioRoot, "scripts/release_provenance.py"),
    path.join(bioRoot, "tests/test_embedded_reader_contract.py"),
    path.join(bioRoot, "tests/test_style_reviser_contract.py"),
    path.join(htmlRoot, "SKILL.md"),
    path.join(htmlReferenceRoot, "personal_report_preferences.md"),
    path.join(htmlReferenceRoot, "quality_checklist.md"),
    path.join(htmlRoot, "scripts/validate_html_report.py"),
    path.join(htmlRoot, "templates/academic_report_template.html")
  ];

  const skillNames = [manifest.orchestrator, ...manifest.method_skills, ...manifest.auxiliary_modules.filter((name) => name !== "bio-tutor")].sort();
  for (const skillName of skillNames) {
    const skillFile = path.join(skillsRoot, skillName, "SKILL.md");
    const yamlFile = path.join(skillsRoot, skillName, "agents/openai.yaml");
    if (fs.existsSync(skillFile)) files.push(skillFile);
    if (fs.existsSync(yamlFile)) files.push(yamlFile);
  }
  return files;
}

function evidenceExcerpts() {
  const specs = [
    [path.join(bioRoot, "scripts/run_pipeline.py"), /external_(?:writer|reviser|style_reviser)|write_release_bundle_manifest|minimum_call_limit|finalize_article_layout|completion_attestation/],
    [path.join(bioRoot, "scripts/completion_attestation.py"), /release_bundle|style_reviser|_NoFigure|article_source\.md|producer_calls/],
    [path.join(bioRoot, "scripts/finalize_article_layout.py"), /article_source|reader_nofigure|embed_reader_markdown_images|reader_html/],
    [path.join(bioRoot, "scripts/reader_facing_output_validator.py"), /article_source|embedded_markdown_delivery_issues|reader HTML/],
    [path.join(htmlRoot, "scripts/render_report.py"), /data-uri|source_asset|original_source|embedded|sha256/]
  ];
  const sections = [];
  for (const [filePath, pattern] of specs) {
    const relative = path.relative(stagingRoot, filePath);
    const lines = fs.readFileSync(filePath, "utf8").split("\n");
    const selected = new Set();
    for (let index = 0; index < lines.length; index += 1) {
      if (!pattern.test(lines[index])) continue;
      for (let nearby = Math.max(0, index - 3); nearby <= Math.min(lines.length - 1, index + 5); nearby += 1) selected.add(nearby);
    }
    const excerpt = [...selected].sort((a, b) => a - b).map((index) => `${index + 1}:${lines[index]}`).join("\n");
    sections.push(`\n===== ${relative}（关键执行片段） =====\n${excerpt}`);
  }
  return sections.join("\n");
}

const env = parseEnv(fs.readFileSync(envPath, "utf8"));
const apiKey = env.DEEPSEEK_API_KEY || env.AGI_API_KEY;
if (!apiKey) throw new Error("env 中没有 DEEPSEEK_API_KEY 或 AGI_API_KEY");

const bundle = collectFiles().map((filePath) => {
  const relative = path.relative(stagingRoot, filePath);
  return `\n===== ${relative} =====\n${fs.readFileSync(filePath, "utf8")}`;
}).join("\n") + evidenceExcerpts();

const system = "你是独立的科研 skill 架构审查员。只报告真实可达、会改变路由正确性、最终速度、可安装性、科研结论、可复现性或用户决策的问题。不要为了显得严格而罗列假设性风险。";
const user = `请对下面的暂存实现做否定性验收。\n\n硬约束：\n1. 相关 skill 数量不设上限；完整生命周期可以使用全部 13 个方法 skill。\n2. 性能只能通过去掉无关 skill、避免重复调用、共享资源每任务只读一次和原材料按需读取获得。\n3. 日常对话不得新增 Agent 或外部模型调用。\n4. 不恢复 sci-mentor 人设；用户始终是研究主体。\n5. BioTutor 固定一次 Writer、一次内容 Reviser、一次最终语言 Reviser，不允许循环；公开 Markdown 和 HTML 都内嵌图片，公开目录没有 _NoFigure.md。\n6. academic-html-report 只在用户明确要求学术 HTML 或大型结构化 HTML 时触发；图证据优先于表格和文字，相关图片必须全部内嵌并保留源图。\n7. 当前只审查，不修改文件。\n\n重点检查：路径安装后是否可解析；是否出现 Superpowers 式强制重流程；skill 进入条件、唯一职责、退出和交接是否冲突或断裂；route_cases 与 validator 是否自证循环；科研硬规则、伪因果、固定阈值或投稿承诺是否残留；BioTutor、文献工具、写作工具和 academic-html-report 的边界是否错误。特别注意：为了迁移旧文件或拒绝旧文件而引用 _NoFigure.md，不等于要求最终交付必须存在它；必须根据真实控制流区分“兼容迁移/发现即报错”和“完成态依赖”。\n\n输出中文，先给总判断，再列严重或重要发现。每项必须包含证据文件、真实失败场景和最小修复。没有严重或重要问题就明确说没有。\n\n实现文件如下：\n${bundle}`;

const response = await fetch("https://api.deepseek.com/chat/completions", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${apiKey}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "deepseek-v4-pro",
    messages: [
      { role: "system", content: system },
      { role: "user", content: user }
    ],
    thinking: { type: "disabled" },
    max_tokens: 8000
  }),
  signal: AbortSignal.timeout(120000)
});

const payload = await response.json();
const result = {
  ok: response.ok,
  checked_at: new Date().toISOString(),
  requested_model: "deepseek-v4-pro",
  response_model: payload.model ?? null,
  finish_reason: payload.choices?.[0]?.finish_reason ?? null,
  content: payload.choices?.[0]?.message?.content ?? null,
  error: payload.error ?? null
};
fs.writeFileSync(outputPath, `${JSON.stringify(result, null, 2)}\n`, "utf8");

if (!response.ok || !result.content) {
  console.error(`deepseek audit failed: ${response.status}`);
  process.exit(1);
}
console.log(`deepseek audit passed: model=${result.response_model} finish_reason=${result.finish_reason}`);
