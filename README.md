# Nano Banana Prompts

> Google Gemini 图像生成（Nano Banana）提示词收藏集

## 📖 简介

这是一个精心整理的 **Nano Banana**（Google Gemini 图像生成）提示词集合，由 [Yep](https://github.com/gentpan) 维护。

本项目专注于 **Google Gemini 的图像生成功能**，不包含 GPT Image 2 或 Grok 的提示词。

## 🌐 双语支持

所有收录的提示词都经过整理，提供：

- **中文版本**：适合中文用户理解和使用
- **英文版本**：保留原始英文提示词，或提供英文翻译

### 目录结构

```
nano-banana-prompts/
├── data/
│   └── imgedify-prompts.jsonl    # 完整语料库（9,199 条）
├── prompts/                       # 精选提示词（按分类）
│   ├── 人像/                      # 人像摄影（50 个）
│   ├── 产品/                      # 产品摄影（50 个）
│   ├── 风景/                      # 风景摄影（50 个）
│   ├── 角色/                      # 角色设计（50 个）
│   ├── 建筑/                      # 建筑摄影（50 个）
│   ├── 食物/                      # 食物摄影（50 个）
│   ├── 抽象/                      # 抽象艺术（50 个）
│   └── 其它/                      # 其他类型（50 个）
├── scripts/
│   └── generate_images.py        # 图像生成脚本（存根）
├── SCHEMA.md                      # 数据结构规范
├── README.md
├── CONTRIBUTING.md
├── sources.md
└── LICENSE
```

### 数据格式

- **JSONL 语料库** (`data/imgedify-prompts.jsonl`)：包含所有 9,199 条提示词
  - 每行一个 JSON 对象，包含完整元数据
  - 中英双语字段：`prompt_zh` 和 `prompt_en`
  
- **精选 Markdown** (`prompts/<分类>/NNNN.md`)：400 个精选双语提示词
  - 按 8 个分类组织
  - 每个分类 50 个精选示例
  - 4 位数字编号（0001-0050）
  - YAML 元数据 + 代码块包裹的双语提示词

## 📊 数据统计

- **总提示词数**：9,199 条（完整语料库）
- **精选示例**：400 个双语 Markdown 文件
  - 人像：50 个 | 产品：50 个 | 风景：50 个 | 角色：50 个
  - 建筑：50 个 | 食物：50 个 | 抽象：50 个 | 其它：50 个
- **主要来源**：ImgEdify（8,485 条）+ 其他社区贡献（714 条）
- **已过滤**：NSFW 内容，重复提示词

## 📝 数据结构规范

查看 [SCHEMA.md](SCHEMA.md) 了解完整的数据结构和文件格式规范。

## 🤝 贡献指南

查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何贡献新的提示词。

## 📚 数据来源

详细来源信息请查看 [sources.md](sources.md)。

主要来源包括：

1. **ImgEdify/awesome-nano-banana-pro-prompts**（MIT）- 8,485 条
2. **Banana-Prompts/awesome-nano-banana-prompts**（MIT）- 292 条
3. **YouMind-OpenLab/awesome-nano-banana-pro-prompts**（CC BY 4.0）- 126 条
4. **JimmyLv/awesome-nano-banana**（CC BY 4.0）- 99 条
5. **ZeroLu/awesome-nanobanana-pro**（MIT）- 73 条
6. **EvoLinkAI/Awesome-Nano-Banana-2-prompt**（MIT）- 72 条
7. **Transcendo/awesome-nanobanana-prompts**（MIT）- 51 条
8. **akirakai/awesome-nano-banana**（MIT）- 1 条

## 📄 许可证

- 本仓库框架代码：[MIT License](LICENSE)
- 第三方提示词内容：保留原始许可证（在每条记录的 `source_license` 字段中标注）

## 👤 整理者

**Yep**（[@gentpan](https://github.com/gentpan)）

## ⭐ 使用方法

### 1. 浏览精选提示词

访问 `prompts/<分类>/` 目录，查看 400 个精心挑选的双语提示词：

```bash
# 浏览人像摄影提示词
ls prompts/人像/

# 查看第一个产品摄影提示词
cat prompts/产品/0001.md
```

### 2. 使用 JSONL 数据

```bash
# 查看所有提示词
cat data/imgedify-prompts.jsonl | jq

# 按类别筛选
cat data/imgedify-prompts.jsonl | jq 'select(.category == "portrait")'

# 统计分类
cat data/imgedify-prompts.jsonl | jq -r '.category' | sort | uniq -c
```

### 3. 直接使用提示词

复制你喜欢的提示词，粘贴到 Google Gemini 的图像生成功能中即可使用。

### 4. 生成图像（TODO）

```bash
# 设置 API 密钥
export GEMINI_API_KEY='your-api-key'

# 运行图像生成脚本
python scripts/generate_images.py
```

*注意：图像生成功能当前为存根，等待实现。*

## 🔗 相关链接

- [Google Gemini](https://gemini.google.com/)
- [Nano Banana 介绍](https://deepmind.google/technologies/gemini/)

## 🙏 致谢

感谢所有开源社区贡献者分享的优质提示词！

---

**Star ⭐ 本项目以获取更新！**
