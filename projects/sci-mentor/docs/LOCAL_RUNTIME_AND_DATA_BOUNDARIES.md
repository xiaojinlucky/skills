# 本机运行环境与数据边界

## 四个层次

### GitHub 快照

用途是版本记录、远程审查和网页版 GPT 规划。

包含当前 Skill、参考文件、必要证据资产、测试和项目文档。

### 本机运行源

当前路径为 `F:\科研大师兄\sci-mentor\skills\sci-mentor`。

本机 `.codex`、`.agents` 和 `.claude` 的 `sci-mentor` 入口指向该目录。

### 本机私有语料

包括原始课程、知识星球数据库、B 站转写、PDF、图片、附件和处理过程。它们不进入 GitHub。

私有知识星球数据库位于本机项目 `corpus/private-index/`。GitHub 中只保留其存在性、质量状态和必要指纹说明。

### 远端节点

远端共享源为 `/hwdata/home/jinqc/.codex-shared/skills/sci-mentor`。

当前节点包括 `ln01`、`nfat01`、`nfat02` 和 `nfat03`。远端系统默认 Python 3.6，随附脚本必须使用 `/hwdata/home/jinqc/.local/bin/python3.11`。

## 网页版 GPT 看不到什么

- 本机 Codex 的已安装 Skills
- Codex memory 和旧会话原始记录
- 本机文件系统的实时变化
- 私有知识星球数据库
- B 站完整转写与音频
- 原始 PDF、图片和附件
- 本机软链接、进程和虚拟环境
- 四个远端节点的实时状态

因此，网页版 GPT 不得把 GitHub 中没有的能力写成已存在，也不得断言某个本机命令已经验证通过。

## 网页版 GPT 可以可靠判断什么

- 当前 Skill 的目标、目录结构和显式规则
- GitHub 快照中的参考文件、证据索引和测试资产
- 用户已经确认的需求与纠偏
- 当前公开记录的完成项和未完成项
- 仓库内部是否自洽
- 下一轮工作应解决的科学、任务或验收问题

## 工单进入本地后的转换协议

本地 Codex 收到网页版 GPT 工单后，按以下顺序处理。

1. 核对工单引用的 GitHub commit
2. 比较 GitHub 快照与本机运行源
3. 读取本机当前可用 Skills、项目规则、`CONTEXT.md` 和 `lessons.md`
4. 核对工单依赖的原始语料、脚本、Python 和远端节点
5. 标出与本机实际情况不符的步骤
6. 在不改变工单目标的前提下修订实现路径和验收命令
7. 若修订会改变目标、范围或关键判据，再向用户确认

不得因为网页版 GPT 使用了更复杂的工具名，就自动引入新的框架。工具只能由明确瓶颈驱动。

## GitHub 提交边界

允许提交。

- `skills/sci-mentor/` 当前正式文件
- 项目规则、上下文、决策和测试摘要
- 当前正式 Skill 随附的派生证据层，包括基础版页级 OCR、短证据摘录、来源定位和聚合统计
- 确定性验证脚本

禁止提交。

- `corpus/`
- `scratch/`
- `.venv/`
- 原始 PDF、Word、PPT、压缩包、音频和视频
- SQLite 数据库
- Token、Cookie、密钥和认证配置
- Codex memory 原文件
