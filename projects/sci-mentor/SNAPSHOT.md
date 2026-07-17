# Sci Mentor 快照说明

## 快照来源

- 本机运行源为 `F:\科研大师兄\sci-mentor\skills\sci-mentor`

- GitHub 快照目录为 `skills/sci-mentor`

- 生成日期为 `2026-07-17`

## 一致性

- 正式文件数为 28

- 文件总字节数为 8124046

- 相对路径与逐文件 SHA256 清单的合并 SHA256 为 `1e3ec09abb9972facb28f071850c0f770a371cc1653df7cfa59ccf773eb216a7`

上述 SHA256 对应 Git 暂存前的本机运行源和本地仓库工作区，复制后逐文件比较为 0 个不一致。

- Git 暂存区中的 `skills/sci-mentor` 子树 SHA-1 为 `b73ec35f51c7622fe6184ace581ff52490c1055a`

Git 会按照仓库 `.gitattributes` 统一文本换行。远端提交内容应使用 Git 子树 SHA-1 核验，本机原始文件复制过程使用前述 SHA256 清单核验。

哈希算法如下。

1. 对每个文件计算 SHA256
2. 生成 `<sha256><两个空格><正斜杠相对路径>` 格式
3. 按完整行排序
4. 使用 UTF-8 和 LF 连接，末尾保留一个 LF
5. 对连接结果再次计算 SHA256

## 不包含的本机资产

- `corpus/`
- `scratch/`
- `.venv/`
- `shixiong_writer_v1_kit.zip`
- 原始 PDF、图片、附件、音频和视频
- 私有知识星球 SQLite 数据库
- Codex memory 原文件

这些资产的存在性、质量状态和处理进度通过 `CONTEXT.md`、`lessons.md` 和 Skill 内聚合证据记录，而不是原样上传。
