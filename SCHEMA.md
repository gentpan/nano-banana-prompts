# Nano Banana Prompts 数据结构规范

本文档定义了 `nano-banana-prompts` 仓库的数据结构和文件组织规范。

**管理者 / 整理者**: Yep ([gentpan](https://github.com/gentpan))

## 目录结构

```
nano-banana-prompts/
├── README.md                    # 项目介绍
├── SCHEMA.md                    # 本文档：数据结构规范
├── CONTRIBUTING.md              # 贡献指南
├── LICENSE                      # MIT 许可证
├── sources.md                   # 数据来源说明
│
├── data/                        # 完整语料库
│   └── imgedify-prompts.jsonl  # 所有提示词（JSONL 格式）
│
├── prompts/                     # 精选提示词（按分类组织）
│   ├── 人像/                    # 人像摄影
│   │   ├── 0001.md
│   │   ├── 0002.md
│   │   └── ...
│   ├── 产品/                    # 产品摄影
│   ├── 风景/                    # 风景摄影
│   ├── 角色/                    # 角色设计
│   ├── 建筑/                    # 建筑摄影
│   ├── 食物/                    # 食物摄影
│   ├── 抽象/                    # 抽象艺术
│   └── 其它/                    # 其他类型
│
└── scripts/                     # 工具脚本
    └── generate_images.py      # 图像生成脚本（存根）
```

## 数据格式

### JSONL 语料库 (`data/imgedify-prompts.jsonl`)

每行一个 JSON 对象，包含以下字段：

```json
{
  "id": "唯一标识符",
  "title": "提示词标题",
  "prompt": "原始提示词完整文本",
  "prompt_zh": "中文版本",
  "prompt_en": "英文版本",
  "needs_translation": true/false,
  "category": "分类（英文）",
  "tags": ["标签1", "标签2"],
  "style": "风格描述",
  "source_repo": "来源仓库",
  "source_url": "原始链接",
  "source_license": "许可证类型",
  "organizer": {
    "name": "Yep",
    "github": "gentpan",
    "note": "整理"
  }
}
```

### Markdown 提示词文件 (`prompts/<category>/NNNN.md`)

#### 文件命名

- 格式：`<4位数字>.md`
- 示例：`0001.md`, `0042.md`, `0123.md`
- 每个分类独立编号，从 `0001` 开始

#### 文件结构

```markdown
---
id: 唯一标识符
category: 分类（英文）
category_zh: 分类（中文）
model: nano-banana
source_repo: 来源仓库名
source_url: 来源链接
source_license: 许可证
organizer:
  name: Yep
  github: gentpan
---

## 中文

```
中文提示词内容（代码块包裹）
```

## English

```
English prompt content (wrapped in code block)
```

---

**整理：** Yep（[gentpan](https://github.com/gentpan)）  
**来源：** [仓库名](链接)
```

#### YAML 字段说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | string | ✅ | 唯一标识符（通常为哈希值或原始 ID） |
| `category` | string | ✅ | 英文分类名 |
| `category_zh` | string | ✅ | 中文分类名 |
| `model` | string | ✅ | 固定值：`nano-banana` |
| `source_repo` | string | ✅ | 来源仓库（格式：`owner/repo`） |
| `source_url` | string | ✅ | 原始来源链接 |
| `source_license` | string | ✅ | 原始内容许可证 |
| `organizer.name` | string | ✅ | 整理者姓名 |
| `organizer.github` | string | ✅ | 整理者 GitHub 用户名 |

## 分类体系

### 中英文对照

| 中文 | 英文 | 说明 |
|------|------|------|
| 人像 | portrait | 人物肖像、时尚摄影 |
| 产品 | product | 产品摄影、商业拍摄 |
| 风景 | landscape | 自然风景、城市景观 |
| 角色 | character | 角色设计、插画 |
| 建筑 | architecture | 建筑摄影、室内设计 |
| 食物 | food | 食物摄影、美食 |
| 抽象 | abstract | 抽象艺术、概念设计 |
| 其它 | general | 未分类或其他类型 |

## 内容要求

### 提示词内容

1. **纯文本**：不包含图片、链接、emoji
2. **双语**：必须包含中文和英文两个版本
3. **代码块**：提示词必须用代码块（` ``` `）包裹
4. **完整性**：保留原始提示词的完整内容

### 翻译规范

- 英文提示词 → 翻译为中文
- 中文提示词 → 翻译为英文
- 日文/韩文/其他语言 → 同时翻译为中英文
- 待翻译内容标注 `[Translation pending]` 或 `[待翻译]`

### 来源追溯

- 每个提示词必须注明原始来源
- 保留原始许可证信息
- 在 YAML 和 footer 中标注整理者

## 许可证

### 仓库框架

- MIT License

### 第三方内容

- 每条提示词保留原始许可证（见 `source_license` 字段）
- 主要许可证类型：MIT、CC BY 4.0

## 工具脚本

### `scripts/generate_images.py`

图像生成脚本（当前为存根），用于：

1. 遍历所有 markdown 文件
2. 提取提示词内容
3. 调用图像生成 API
4. 保存生成的图像（TODO）

## 贡献流程

1. 在 `data/imgedify-prompts.jsonl` 中添加新提示词
2. 运行脚本生成精选 markdown 文件
3. 确保符合本规范的格式要求
4. 提交 Pull Request

## 更新日志

- **2026-08-24**：建立规范化目录结构
  - 按分类组织精选提示词
  - 统一 YAML 格式
  - 代码块包裹提示词内容
  - 创建 SCHEMA.md 文档

---

**维护者：** Yep（[@gentpan](https://github.com/gentpan)）  
**最后更新：** 2026-08-24
