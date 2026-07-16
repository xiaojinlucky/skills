# Skills

本仓库用于保存彼此独立的 Agent Skill、项目规则、交接上下文和验收规范。

仓库为 Private，但仍不作为原始资料、账号凭据、运行日志或本机状态的备份盘。

## 目录

```text
skills/
├── skills/
│   └── sci-mentor/          当前可运行 Skill 的版本快照
└── projects/
    └── sci-mentor/          项目规则、上下文、决策记录与总控交接
```

## Sci Mentor

Sci Mentor 的固定目标是一条三层递进主线。

1. 表层先把文献讲清楚
2. 深层提炼并培养科研思维
3. 最终帮助用户设计和推进自己的课题

项目入口见 [projects/sci-mentor/README.md](projects/sci-mentor/README.md)。

网页版 GPT 的总控指令见 [WEB_GPT_CONTROLLER_PROMPT.md](projects/sci-mentor/docs/WEB_GPT_CONTROLLER_PROMPT.md)。

## 快照边界

仓库中的 `skills/sci-mentor/` 是本地运行版本在提交时的精确文件快照，但 GitHub 不是本机运行环境。

以下内容不进入仓库。

- 原始课程 PDF、公众号导出、知识星球数据库和附件
- B 站音频、视频和完整本地转写
- 本机虚拟环境、缓存、临时脚本和调试产物
- Codex memory 原文件、账号凭据、Token 和私有配置

GitHub 中保留的是可审查的 Skill、经提炼的参考文件、已经进入正式 Skill 的派生证据层、测试资产和项目文档。派生证据层包括来源账本和基础版页级 OCR，但不包含原始 PDF、外部私有数据库或完整音视频语料库。
