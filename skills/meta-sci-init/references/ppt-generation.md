# 开题答辩 PPT（按需，默认关闭）

只有用户明确要求生成开题答辩 PPT 时才读本附件。完整原件见 `archive-original-SKILL.md`。

## ⑦ 按需生成开题答辩 PPT（默认关闭）

### 硬触发条件

只有用户在当前对话中明确要求生成、制作、导出或整理开题答辩 PPT，才执行本节。没有明确指令时立即停留在前六个阶段，不进行任何 PPT 准备工作。

用户明确触发后，再把已经确定的开题方案汇总成一份开题答辩 PPT。
用户明确触发后，**优先使用 Anthropic 官方 `pptx` 技能**生成高质量 PowerPoint；仅当该技能不可用
且用户不同意安装、或安装失败时，才降级用内置脚本。详细排版规则见 `references/ppt_structure.md`。

### 通用内容组织原则（两条生成路径都遵循）
- 把开题报告压缩成 **7-9 页正文**（另加封面/目录/致谢），**不要照搬报告全文。**
- 每页只承担一个主要信息，优先呈现结论、关键数字、研究对象与证据关系。
- 每页 ≤ 6 条、短语化、用层级表达从属、完整话术和术语解释放演讲者备注。
- 图表或技术路线不能只放图名。备注中说明听众应该看哪里、这张图支持什么判断、与下一页怎样衔接。
- 幻灯到报告章节的映射见 `references/ppt_structure.md`（背景意义 / 研究现状 / 问题与目标 /
  研究内容与技术路线 / 创新点 / 可行性 / 计划与预期成果）。

### 第 0 步 · 确认 PPT 生成能力（做 PPT 前必做）
1. 先判断官方 `pptx` 技能是否可用：在可用技能列表中查找名为 `pptx` 的技能，或检查
   `~/.claude/skills/pptx/SKILL.md`（Windows：`%USERPROFILE%\.claude\skills\pptx\SKILL.md`）是否存在。
2. **若已可用** → 直接走「路径 A」。
3. **若不可用** → 向用户说明并**征得明确许可**，须清楚列出三项：
   - **要安装的技能**：`pptx`（Anthropic 官方文档技能，可直接产出专业 PowerPoint，效果优于内置脚本）
   - **来源**：`github.com/anthropics/skills`
   - **安装位置**：`~/.claude/skills/pptx/`（Windows 为 `%USERPROFILE%\.claude\skills\pptx\`）

   话术示例：
   > 要生成排版更精美的开题答辩 PPT，建议安装 Anthropic 官方 **`pptx` 技能**。它来自
   > github.com/anthropics/skills，会被装到 `~/.claude/skills/pptx/`。**是否允许我现在自动安装？**

   用户**同意** → 走「路径 A」；用户**拒绝** → 走「路径 B」。

### 路径 A（首选）· 安装并使用官方 `pptx` 技能
得到许可后，**自动执行安装**（用 Bash 工具）：
```bash
# 1) 克隆官方技能库到临时目录（浅克隆）
git clone --depth 1 https://github.com/anthropics/skills.git /tmp/anthropic-skills
# 2) 定位其中的 pptx 技能目录（含 SKILL.md）并复制到用户技能目录
mkdir -p ~/.claude/skills
cp -r "$(dirname "$(find /tmp/anthropic-skills -name SKILL.md -path '*pptx*' | head -1)")" ~/.claude/skills/pptx
# 3) 校验
ls ~/.claude/skills/pptx/SKILL.md
```
- 安装后确认 `~/.claude/skills/pptx/SKILL.md` 存在。**克隆失败**（无网络 / 无 git）或找不到目录
  → 如实告知用户，转「路径 B」。
- 由于技能列表通常在会话开始时加载，**不要依赖 Skill 工具自动识别新装技能**；应直接
  **Read 读取 `~/.claude/skills/pptx/SKILL.md` 并遵循其指令**，把开题方案交给它生成
  `开题报告PPT.pptx`，写入用户当前工作目录。内容仍按上面「通用内容组织原则」组织。

### 路径 B（降级）· 内置脚本
仅当用户拒绝安装、或路径 A 安装失败时使用：
1. 按 `references/ppt_structure.md` 的 JSON 结构，生成 `content.json` 写入用户工作目录
   （meta 填题目/汇报人/导师/单位/日期；slides 逐页填 title + bullets + notes）。
2. 运行技能内置脚本：
   ```
   python <技能目录>/scripts/build_pptx.py content.json 开题报告PPT.pptx
   ```
   - 已装 `python-pptx` → 直接得到 `.pptx`（16:9，含封面、目录、正文、致谢、演讲者备注）。
   - 未装 → 脚本自动降级生成 Marp 幻灯 `.md`，并提示 `pip install python-pptx`
     或用 `npx @marp-team/marp-cli xxx.md --pptx` 渲染。按提示告知用户即可。

### 完成后
向用户说明每页要点，并提示可自行替换模板配色、加入技术路线图/甘特图等图示。
若用户在报告未完全定稿时就想要 PPT，用当前已定内容生成，未定处在 bullets 里标「【待补充】」。

---
