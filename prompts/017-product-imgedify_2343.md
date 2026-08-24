---
id: imgedify_2343
category: product
style: 3d
tags: ["フィギュア製品紹介風", "Nano Banana Pro", "1/7スケール", "レイアウトプロンプト", "商品名ロゴ"]
source: ImgEdify/awesome-nano-banana-pro-prompts
license: MIT
---

# Nano Banana Proフィギュア製品紹介

## 中文

**产品摄影 - 详细型提示词**

这是一个关于 超写实、影棚拍摄、灯光 的 Gemini 图像生成提示词。

**关键特征：**
- 提示词长度：约 5083 字符
- 风格分类：产品摄影
- 标签：フィギュア製品紹介風, Nano Banana Pro, 1/7スケール, レイアウトプロンプト, 商品名ロゴ

**使用说明：**
这个提示词设计用于 Google Gemini 的图像生成功能（Nano Banana），可以直接复制使用或根据需求调整参数。

---

*完整英文提示词见下方。*

## English

Nano Banana Proで遊ぼう
【フィギュア製品紹介風
レイアウトプロンプト　多言語対応版】
⠀
参照画像のキャラクターをフィギュア化して、製品紹介風にレイアウトするプロンプトを表示言語を『日・英・独・仏』の4言語から選択して生成できるようにしました。
⠀
⚠️必ず最後までお読みください。
※Nano Banana Pro専用のプロンプトです。
※プロンプトの無断転載は禁止します。
⠀
◆概要
・表示言語（language）
『日・英・独・仏』の4言語から選択できます。
⠀
・商品名（product_name）
・メーカー名（manufacturer_name）
それぞれ任意の文字列を指定できます。
商品名ロゴ：
商品名の文字列と参照画像の雰囲気から推論します。
メーカーロゴ：
メーカー名の文字列から推論します。
※表示言語に翻訳されることがあります。
⠀
・サイズ
キャラクターの体型と1/7スケール設定から推論した全高をセンチメートル表記で表示します。
⠀
・材質
フィギュアとして妥当な材質を推論して表示します。
⠀
・価格
フィギュアのスケール、造形密度、塗装表現から推論します。
⠀
・部分拡大図
拡大図には、それぞれ異なる部位または特徴について説明する日本語キャプションを付与します。
⠀
◆使い方
・表示言語（language）
下記の『""』内を例に倣って書き換えてください。
language: "ja"
ja : Japanese
en : English
de : German
fr : French
・商品名（product_name）
・メーカー名（manufacturer_name）
それぞれ下記の『""』内を任意の文字列に書き換えてください。
メーカー名は「Sculptor / Production」にも反映されます。
product_name: "{ARBITRARY_PRODUCT_NAME}"
manufacturer_name: "{ARBITRARY_MANUFACTURER_NAME}"
⠀
⚠️プロンプト使用上の注意⚠️
本プロンプトには、特定の作品名・作者名・キャラクター名等は一切含まれていませんが、生成モデルの内部処理や学習データに起因する連想まではコントロールできないため、結果として既存作品のキャラクター・商標・ブランドロゴ等に類似または該当する画像が生成される可能性があります。
⠀
生成された画像の利用・公開にあたっては、十分ご注意ください。
⠀
なお、本プロンプトの利用により生成された一切の成果物およびそれに起因するトラブル・損害等について、当方は一切の責任を負いかねます。ご自身の責任と判断においてご利用ください。
⠀
◆プロンプト（全文をコピペしてください）
language: "ja"
# Supported values:
# - ja : Japanese
# - en : English
# - de : German
# - fr : French
# The selected language determines all displayed product text.
product_name: "{ARBITRARY_PRODUCT_NAME}"
manufacturer_name: "{ARBITRARY_MANUFACTURER_NAME}"
subject: >
The character from reference image A, faithfully preserved in design, proportions,
facial features, hairstyle, outfit details, and color palette.
The character is transformed into a highly detailed, photorealistic PVC figure.
Sculpting style and overall aesthetic are inferred directly from the reference image.
The figure is presented as a 1/7 scale collectible.
composition: >
Product introduction layout inferred based on the selected language.
Vertical composition with a 3:4 aspect ratio.
A large main visual of the full figure.
A single, clearly defined product information area containing all textual elements.
Product name logo and manufacturer name logo are each displayed exactly once.
Multiple inset close-up panels are included.
Each inset focuses on a different physical area or feature of the figure.
No two inset panels depict the same part or the same visual characteristic.
Inset panels must be visually and conceptually distinct.
action: >
Static collectible figure pose with no movement.
Emphasis on sculpt accuracy, proportions, and surface detail.
location: >
Neutral studio-like environment inferred for product photography.
Minimal, non-distracting background.
style: >
Photorealistic product rendering and photography style.
Artistic tone and mood inferred entirely from the reference image.
camera_lighting: >
Camera angle and lighting optimized for collectible figure presentation.
Realistic studio lighting interacting with PVC surfaces.
Glossy highlights on hair and clothing.
Matte finish on skin.
Sharp focus with natural depth of field.
Soft shadow beneath the figure on a flat surface.
colors: >
Exact color reproduction based on the reference image.
Background and graphic elements support text readability
according to the selected language.
text: >
Language-dependent product description.
All labels, headings, and captions must be generated
strictly in the language specified by "language".
Required information (translated appropriately):
- Product Name:
"{{product_name}}"
Displayed once as a logo.
- Manufacturer:
"{{manufacturer_name}}"
Displayed once as a logo.
- Scale:
1/7 scale collectible figure.
- Sculptor / Production:
"{{manufacturer_name}}"
- Price:
Inferred retail price based on scale, sculpt density,
and paint complexity.
Displayed in:
- Japanese yen if language is "ja"
- US dollars if language is "en"
- Euros if language is "de" or "fr"
- Size:
Total height inferred from character proportions
and 1/7 scale.
Displayed in centimeters.
- Material:
Plausible figure materials inferred and displayed.
- Close-up captions:
Each inset panel includes a unique caption describing
a different physical area or sculpting characteristic.
No repetition of body parts, viewpoints, or intent.
No proper nouns allowed.
No real-world brands, trademarks, or companies may be referenced.
edit_instructions: >
Transform the illustration into a photorealistic PVC figure.
Preserve the original character’s design, pose, proportions,
and colors exactly.
Render realistic painted surfaces with detailed shading.
Include subtle seam lines typical of manufactured figures.
Apply glossy highlights on hair and clothing,
matte finish on skin.
Do not include display bases, stands, or supports.
references: >
Reference image A defines character design, pose, proportions,
color palette, and overall artistic direction.
Product name and manufacturer name generate fictional logos
and are displayed exactly once each.
No real-world brands, trademarks, or logos.
extras: >
4K resolution.
Aspect ratio 3:4.
Clean final image with no watermarks or artifacts.
Professional collectible figure product presentation.

---

**整理：** Yep（[gentpan](https://github.com/gentpan)）  
**来源：** [ImgEdify/awesome-nano-banana-pro-prompts](https://x.com/munou_ac/status/2004408308850217043)  
**许可：** MIT
