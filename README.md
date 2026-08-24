# Nano Banana Prompts

> Google Gemini 图像生成（Nano Banana）提示词收藏集

## 📖 简介

这是一个精心整理的 **Nano Banana**（Google Gemini 图像生成）提示词集合，由 [Yep](https://github.com/gentpan) 维护。

本项目专注于 **Google Gemini 的图像生成功能**，不包含 GPT Image 2 或 Grok 的提示词。

## 🌐 双语支持

所有收录的提示词都经过整理，提供：

- **中文版本**：适合中文用户理解和使用
- **英文版本**：保留原始英文提示词，或提供英文翻译

### 数据结构

- `data/imgedify-prompts.jsonl`：包含所有提示词的 JSONL 格式数据（仅文本，无图像）
  - 每行一条提示词记录
  - 包含 `prompt_zh`（中文）和 `prompt_en`（英文）字段
  - 部分提示词标记为 `needs_translation: true`，表示需要进一步完善翻译

- `prompts/`：精选 40 个高质量提示词的双语 Markdown 文件
  - 人像摄影（Portrait）
  - 产品摄影（Product）
  - 风景摄影（Landscape）
  - 通用场景（General）

## 📊 数据统计

- **总提示词数**：8,976 条
- **精选示例**：40 个双语 Markdown 文件
- **主要来源**：ImgEdify（8,485 条）+ 其他社区贡献（491 条）
- **已过滤**：NSFW 内容，重复提示词

## 📝 贡献指南

查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何贡献新的提示词。

## 📚 数据来源

详细来源信息请查看 [sources.md](sources.md)。

主要来源包括：

1. **ImgEdify/awesome-nano-banana-pro-prompts**（MIT）
2. **ZeroLu/awesome-nanobanana-pro**（MIT）
3. **Banana-Prompts/awesome-nano-banana-prompts**（MIT）
4. **YouMind-OpenLab/awesome-nano-banana-pro-prompts**（CC BY 4.0）

## 📄 许可证

- 本仓库框架代码：[MIT License](LICENSE)
- 第三方提示词内容：保留原始许可证（在每条记录的 `source_license` 字段中标注）

## 👤 整理者

**Yep**（[@gentpan](https://github.com/gentpan)）

## ⭐ 使用方法

### 1. 浏览精选提示词

访问 `prompts/` 目录，查看 40 个精心挑选的双语提示词示例。

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

## 🔗 相关链接

- [Google Gemini](https://gemini.google.com/)
- [Nano Banana 介绍](https://deepmind.google/technologies/gemini/)

## 🙏 致谢

感谢所有开源社区贡献者分享的优质提示词！

---

**Star ⭐ 本项目以获取更新！**
