# PDF 解析与全文获取（按需）

从原始长稿抽出。缺少全文时不能装作完整读过。

## 工具使用

### PDF 解析（优先用 MinerU 云端 API）

MinerU 是 74k stars 的成熟开源 PDF 解析引擎（opendatalab/MinerU），一次性解决文本提取加图片提取加表格（转 HTML）加公式（转 LaTeX）加 OCR（109 种语言，扫描版 PDF 也能处理）。所有高质量文献解读工具底层都用它。不重复造轮子，优先用它。

#### MinerU 安装与使用指南

如果你自己都没用过 MinerU，按下面两条路走。**第一次用建议先走路1（云端 API 免安装），跑通一篇文献再考虑路2（本地安装）**。

**路1 云端 API（推荐，免安装，免 GPU）**

不需要在本地装任何东西，直接调云端服务。分两档：

档A flash-extract（免 Token，开箱即用）：
- 限制：单文件最大 10MB、最多 20 页
- 输出：Markdown（公式和表格默认开启，OCR 默认关闭）
- 适合：大多数 SCI 文献（一般 5-8MB、10-15 页）
- 安装 CLI（零依赖单二进制）：
  ```bash
  npm install -g mineru-open-api
  # 或 Go 安装（macOS/Linux）
  go install github.com/opendatalab/MinerU-Ecosystem/cli/mineru-open-api@latest
  ```
- 最小可跑命令（文本版 PDF）：
  ```bash
  mineru-open-api flash-extract paper.pdf -o ./output/
  ```
- 扫描版 PDF（必须加 `--ocr` 开启 OCR，否则只输出空 Markdown）：
  ```bash
  mineru-open-api flash-extract paper.pdf --ocr -o ./output/
  ```
- Python SDK（免装 CLI，直接 pip）：
  ```bash
  uv pip install mineru-open-sdk
  ```
  ```python
  from mineru import MinerU
  client = MinerU()  # 无需 token
  result = client.flash_extract("paper.pdf")
  print(result.markdown)
  # result.images 是提取出的图片列表
  ```

档B extract 精准模式（需 Token，免费申请）：
- 限制：单文件最大 200MB、最多 200 页，支持批量（≤200 个）
- 输出：Markdown/HTML/LaTeX/DOCX/JSON，可选 vlm 模型（精度更高）或 pipeline 模型（零幻觉）
- 适合：超 20 页的长文献、需要图片资产、需要批量处理
- 申请 Token：访问 https://mineru.net/apiManage/token ，登录后创建 token（免费）
- 配置 Token（三选一，优先级从高到低）：
  ```bash
  # 方式1 命令行 flag
  mineru-open-api extract paper.pdf --token <你的token>
  # 方式2 环境变量
  export MINERU_TOKEN="your-token"
  # 方式3 配置文件（一次配置永久生效）
  mineru-open-api auth  # 交互式配置，写入 ~/.mineru/config.yaml
  ```
- 最小可跑命令：
  ```bash
  mineru-open-api extract paper.pdf -o ./output/ --model vlm
  ```
- Python SDK：
  ```python
  from mineru import MinerU
  client = MinerU("your-api-token")  # 或设 MINERU_TOKEN 环境变量后 MinerU()
  result = client.extract("paper.pdf")
  print(result.markdown)
  print(result.images)  # 提取出的图片列表
  ```

**路2 本地安装（大文件或离线场景）**

云端 API 够用就不需要装本地版。只有当你要处理超大文件、或离线环境、或不想依赖云端服务时才装。

```bash
uv pip install magic-pdf[full]
```

本地版需要模型权重，首次运行会自动下载。GPU 可选（有 GPU 更快，没 GPU CPU 也能跑，只是慢）。具体安装细节看 MinerU GitHub README：https://github.com/opendatalab/MinerU

**降级方案**（MinerU 云端和本地都不可用时）：
- 文本版 PDF：pdftotext 提取文本 + PyMuPDF（fitz）提取图片
- 扫描版 PDF：pdftoppm 转 200dpi 图像 + tesseract OCR（chi_sim+eng 语言包）
- 降级方案图片提取能力弱，能提取但质量不如 MinerU，推文里要标注「图片提取为降级方案，质量可能受限」

**第一次用的建议**：拿一篇你熟悉的 10 页以内 SCI 文献，用路1 档A（flash-extract）跑一遍，看输出的 Markdown 和图片是否完整。跑通了再拿来做完整深度解读。遇到 429 错误是 IP 限频，等几分钟再试或换档B。

### DOI/链接全文获取
- LiteratureSearch 获取摘要和元数据
- WebFetch 获取开放获取的全文
- 看不到全文时先提醒用户上传 PDF

### 通讯作者信息
- WebSearch 搜索通讯作者研究领域和代表性成果

---
