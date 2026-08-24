# 贡献指南

感谢你对 Nano Banana Prompts 项目的关注！

**管理者 / 整理者**: Yep ([gentpan](https://github.com/gentpan))

## 数据格式

### JSONL 记录结构

每条提示词记录包含以下字段：

```json
{
  "id": "唯一标识符",
  "title": "提示词标题",
  "prompt": "原始提示词文本",
  "prompt_zh": "中文版本",
  "prompt_en": "英文版本",
  "needs_translation": true/false,
  "category": "portrait|product|landscape|general",
  "tags": ["标签1", "标签2"],
  "style": "realistic|cinematic|artistic|etc",
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

### 字段说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | string | ✅ | 唯一标识符 |
| `title` | string | ✅ | 简短标题 |
| `prompt` | string | ✅ | 原始提示词完整文本 |
| `prompt_zh` | string | ✅ | 中文版本（如无翻译则为空字符串） |
| `prompt_en` | string | ✅ | 英文版本（如无翻译则为空字符串） |
| `needs_translation` | boolean | ❌ | 是否需要进一步翻译 |
| `category` | string | ✅ | 分类：portrait/product/landscape/general |
| `tags` | array | ❌ | 标签数组 |
| `style` | string | ❌ | 风格描述 |
| `source_repo` | string | ✅ | 来源仓库名称 |
| `source_url` | string | ✅ | 原始来源链接 |
| `source_license` | string | ✅ | 原始许可证 |
| `organizer` | object | ✅ | 整理者信息（固定值） |

## 贡献新提示词

### 1. 提交要求

- ✅ 必须是 **Google Gemini Nano Banana** 的提示词
- ❌ 不接受 GPT Image 2 或 Grok 的提示词
- ❌ 不接受 NSFW 内容
- ✅ 必须注明原始来源和许可证
- ✅ 鼓励提供双语版本

### 2. 提交方式

#### 方式 A：提交 Issue

在 GitHub Issues 中提交，包含：

- 提示词文本
- 原始来源链接
- 许可证信息
- 分类和标签建议

#### 方式 B：提交 Pull Request

1. Fork 本仓库
2. 编辑 `data/imgedify-prompts.jsonl`
3. 添加新记录（遵循上述格式）
4. 提交 PR

## 改进翻译

如果你发现某些提示词的翻译质量不佳，欢迎提交改进：

1. 找到对应的记录（通过 `id` 定位）
2. 改进 `prompt_zh` 或 `prompt_en` 字段
3. 将 `needs_translation` 设置为 `false`
4. 提交 PR

## 精选提示词

如果你的提示词特别优秀，可能会被选入 `prompts/` 目录作为精选示例！

精选标准：

- 高质量的双语内容
- 清晰的分类和标签
- 实用性强
- 结果效果好

## 许可证

你提交的内容应：

- 明确注明原始来源
- 尊重原始许可证
- 不侵犯他人版权

## 联系方式

- GitHub Issues：[提交问题或建议](https://github.com/gentpan/nano-banana-prompts/issues)
- 整理者：[@gentpan](https://github.com/gentpan)

---

感谢你的贡献！🎉
