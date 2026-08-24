# 数据来源

本项目的提示词收集自以下开源社区项目和贡献者。我们尊重并保留所有原始许可证。

## 主要来源

### 1. ImgEdify/awesome-nano-banana-pro-prompts

- **仓库**：https://github.com/ImgEdify/awesome-nano-banana-pro-prompts
- **许可证**：MIT License
- **收录数量**：8,485 条（去重后）
- **数据文件**：`data/prompts.json`
- **说明**：这是目前最大的 Nano Banana 提示词社区收集项目，包含丰富的分类和标签

### 2. ZeroLu/awesome-nanobanana-pro

- **仓库**：https://github.com/ZeroLu/awesome-nanobanana-pro
- **许可证**：MIT License
- **收录数量**：73 条
- **数据来源**：README.md
- **说明**：精心策划的提示词列表，质量较高

### 3. Banana-Prompts/awesome-nano-banana-prompts

- **仓库**：https://github.com/Banana-Prompts/awesome-nano-banana-prompts
- **许可证**：MIT License
- **收录数量**：292 条
- **数据来源**：README.md
- **说明**：社区驱动的提示词集合

### 4. YouMind-OpenLab/awesome-nano-banana-pro-prompts

- **仓库**：https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts
- **许可证**：CC BY 4.0
- **收录数量**：126 条（预览片段）
- **数据来源**：README.md
- **说明**：内容管理系统导出的提示词，部分内容受 CC BY 4.0 许可

### 5. JimmyLv/awesome-nano-banana

- **仓库**：https://github.com/JimmyLv/awesome-nano-banana
- **许可证**：CC BY 4.0
- **收录数量**：99 条
- **数据来源**：README.md
- **说明**：精选的 Gemini 2.5 Flash Image（Nano Banana）生成图像和提示词集合

### 6. ZeroLu/awesome-nanobanana-pro（原 ZeroLu/awesome-nanobanana-pro）

- **仓库**：https://github.com/ZeroLu/awesome-nanobanana-pro
- **许可证**：MIT
- **收录数量**：73 条（新增）
- **数据来源**：README.md
- **说明**：策划的 Nano Banana Pro 提示词资源

### 7. EvoLinkAI/Awesome-Nano-Banana-2-prompt

- **仓库**：https://github.com/EvoLinkAI/Awesome-Nano-Banana-2-prompt
- **许可证**：MIT
- **收录数量**：72 条
- **数据来源**：README.md
- **说明**：100+ 高质量 Nano Banana 2 提示词集合

### 8. Transcendo/awesome-nanobanana-prompts

- **仓库**：https://github.com/Transcendo/awesome-nanobanana-prompts
- **许可证**：MIT
- **收录数量**：51 条
- **数据来源**：README.md
- **说明**：Nano Banana / Nano Banana Pro 精选提示词库

### 9. akirakai/awesome-nano-banana

- **仓库**：https://github.com/akirakai/awesome-nano-banana
- **许可证**：MIT
- **收录数量**：1 条
- **数据来源**：README.md
- **说明**：Gemini Nano Banana 用例、提示词和来源精选列表

## 数据处理

### 去重逻辑

- 基于提示词文本内容去重
- 规范化处理（统一空白字符、转小写）
- 保留第一次出现的版本

### 过滤标准

- ❌ 过滤 NSFW 内容
- ❌ 过滤重复提示词
- ❌ 过滤无效或过短的提示词
- ✅ 保留高质量、实用的提示词

### 分类统计

| 分类 | 数量 | 说明 |
|------|------|------|
| Portrait（人像） | ~3,990 | 人物肖像、时尚摄影等 |
| Product（产品） | ~1,100 | 产品摄影、商业拍摄等 |
| Character（角色） | ~900 | 角色设计、插画等 |
| Landscape（风景） | ~560 | 自然风景、建筑摄影等 |
| General（通用） | ~500 | 其他类型 |
| 其他分类 | ~2,149 | 食物、抽象、建筑等 |
| **总计** | **9,199** | 去重后总数 |

## 许可证说明

### 本仓库结构

- **框架代码**：MIT License
- **数据整理**：MIT License
- **README、CONTRIBUTING 等文档**：MIT License

### 第三方内容

- 每条提示词的 `source_license` 字段标注了原始许可证
- 主要许可证类型：
  - MIT License（大部分内容）
  - CC BY 4.0（部分内容）

## 贡献致谢

特别感谢以下开源项目和社区贡献者：

- **ImgEdify** 团队及贡献者
- **ZeroLu**
- **Banana-Prompts** 社区
- **YouMind-OpenLab** 团队
- 所有在 Twitter/X 上分享优质提示词的创作者

## 整理者

[gentpan](https://github.com/gentpan)

- 数据收集与整理
- 去重与分类
- 双语化处理
- 质量控制

## 更新日志

### 2026-08-24（更新 2）

- 🔍 扩展 GitHub 搜索，新增 5 个来源仓库
- 📊 总提示词数增至 9,199 条
- 🧹 清理所有精选 markdown 文件：去除 emoji、闲聊内容
- 🌐 确保中英双语：英文提示词配中文概述，中文配英文概述
- 📝 日文/韩文提示词提供双语说明
- ✨ 简化 YAML 和 footer 格式

### 2026-08-24（初始）

- 🎉 初始版本发布
- 📊 收录 8,976 条提示词
- 🌐 精选 40 个双语示例
- 🏷️ 完成分类和标签

---

如果你发现任何许可证问题或版权争议，请立即联系：

- GitHub Issues：https://github.com/gentpan/nano-banana-prompts/issues
- Email：通过 GitHub 个人资料联系

我们会及时处理并移除有争议的内容。
