---
id: imgedify_8616
category: landscape
style: cinematic
tags: ["punk generator", "cinematic", "world building", "photorealistic", "atmospheric"]
source: ImgEdify/awesome-nano-banana-pro-prompts
license: MIT
---

# A random punk scene generated using Nano banana 2  Prompt  UNIVERSAL MONO PUNK SCENE GENERATOR  VARI

## 中文

**风景摄影 - 详细型提示词**

这是一个关于 超写实、电影感、灯光 的 Gemini 图像生成提示词。

**关键特征：**
- 提示词长度：约 5644 字符
- 风格分类：风景摄影
- 标签：punk generator, cinematic, world building, photorealistic, atmospheric

**使用说明：**
这个提示词设计用于 Google Gemini 的图像生成功能（Nano Banana），可以直接复制使用或根据需求调整参数。

---

*完整英文提示词见下方。*

## English

UNIVERSAL MONO PUNK SCENE GENERATOR

VARIABLE GUIDE

1. PUNK_STYLE =
   [Choose one punk aesthetic. If left blank, one style will be automatically selected at random from LIST_OF_PUNK_STYLES.]

2. LIST_OF_PUNK_STYLES =
   [Steampunk, Dieselpunk, Atompunk, Cyberpunk, Biopunk, Nanopunk, Solarpunk, Decopunk, Clockpunk, Coalpunk, Raypunk, Stonepunk, Sailpunk, Cassettepunk, Teslapunk, Mythpunk, Sandalpunk, Oceanpunk, Frostpunk, Junglepunk, Desertpunk, Gothicpunk, Ironpunk, Crystalpunk, Rustpunk, Vaporwavepunk, Neonpunk, Skypunk, Aquapunk, Arborpunk, Astropunk, QuantumPunk, Mechanopunk, Technopunk, Retrocomputingpunk]

3. SUBSTYLE =
   • If a specific SUBSTYLE is provided → use it exactly as written.
   • If SUBSTYLE is set to **none** → do not apply a substyle layer.
   • If SUBSTYLE is left **blank** → automatically infer a logical SUBSTYLE based on the chosen PUNK_STYLE.

4. TECHNOLOGY_LEVEL =
   • If a specific TECHNOLOGY_LEVEL is provided → use it exactly as written.
   • If TECHNOLOGY_LEVEL is set to **none** → do not apply a technology modifier.
   • If TECHNOLOGY_LEVEL is left **blank** → automatically infer an appropriate technology level based on the chosen PUNK_STYLE.

5. ENVIRONMENT =
   • If a specific ENVIRONMENT is provided → use it exactly as written.
   • If ENVIRONMENT is set to **none** → do not apply an environmental modifier.
   • If ENVIRONMENT is left **blank** → automatically infer a logical environment based on the other active layers.

6. CULTURE =
   • If a specific CULTURE is provided → use it exactly as written.
   • If CULTURE is set to **none** → do not apply a cultural modifier.
   • If CULTURE is left **blank** → automatically infer a cultural framework appropriate to the world.

7. ROOM_OR_SETTING =
   [IF BLANK: Generate a compelling location consistent with the active world layers.]

8. LIST_OF_OBJECTS =
   [IF BLANK: Infer 4–6 logical objects belonging to the environment.]

9. CAMERA_FRAMEWORK =
   [IF BLANK: Infer the best cinematic framing for the environment.]

10. LIGHTING_FRAMEWORK =
    [IF BLANK: Infer lighting derived from the technology and environment.]

11. MATERIAL_SYSTEM =
    [IF BLANK: Infer dominant materials and structural systems derived from the style layers.]

---

### STYLE SELECTION DIRECTIVE

If **PUNK_STYLE is left blank**, randomly select **one style from LIST_OF_PUNK_STYLES** and apply it as the active world aesthetic.

All subsequent inference systems must use the chosen PUNK_STYLE.

---

### WORLD INTERPRETER ENGINE

Analyze all active layers:

PUNK_STYLE

* optional SUBSTYLE
* optional TECHNOLOGY_LEVEL
* optional ENVIRONMENT
* optional CULTURE

From these layers infer:

• dominant materials
• architectural forms
• infrastructure systems
• lighting technology
• environmental atmosphere
• cultural design motifs

All visual elements must remain internally consistent with this world model.

---

### SCENE ENGINE

Generate a highly detailed, cinematic, photorealistic scene centered around:

[ROOM_OR_SETTING]

The entire environment must strictly adhere to the world defined by the active layers.

---

### COMPOSITION & ORGANIC STAGING (CRITICAL)

Seamlessly integrate:

[LIST_OF_OBJECTS]

Objects must be distributed naturally throughout the environment at varying depths, heights, and angles.

They should appear as functional parts of a believable, lived-in environment.

---

### ARCHITECTURE & ENVIRONMENTAL LOCK

All structures must reflect the materials, engineering logic, and design language derived from the world layers.

Exterior views must reveal environments belonging to the same universe.

The world must never appear generic or inconsistent with the chosen aesthetic paradigm.

---

### TECHNOLOGY & MATERIAL SYSTEMS

All devices, infrastructure, and structural elements must follow the technological paradigm defined by the world layers.

Replace modern generic materials with those appropriate to the world.

Ensure all systems appear believable within the civilization’s technological context.

---

### VISUAL EXECUTION

Capture the scene using:

[CAMERA_FRAMEWORK]

Surfaces should display rich texture appropriate to the MATERIAL_SYSTEM.

Illuminate the scene using:

[LIGHTING_FRAMEWORK]

The final image should feel like a cohesive, immersive world fully defined by the chosen layers.

---

### ORNATE PLAQUE LABELING SYSTEM

Include a decorative **ornate plaque positioned at the very bottom of the frame**, integrated naturally into the composition as if it belongs to the world (museum plaque, engraved plate, illuminated panel, carved stone tablet, brass nameplate, holographic label, etc., depending on the PUNK_STYLE).

The plaque must match the **materials, craftsmanship, and technological paradigm of the world**.

Inside the plaque:

LEFT SIDE CONTENT STRUCTURE

• **Heading** — bold, slightly larger lettering
• **Brief Description** — 1–2 sentences describing the scene and explicitly mentioning the **PUNK_STYLE**

Text layout rules:

• Heading on top line in bold, slightly larger type
• Description directly beneath it in smaller text
• Text aligned on the **left side of the plaque**

Placement rules:

• Plaque should appear **at the very bottom of the image whenever possible**
• It should not obscure the main scene but should feel intentionally designed as a descriptive label for the world

Styling rules:

• Plaque materials must match the **MATERIAL_SYSTEM and PUNK_STYLE**
• Engraving, embossing, illumination, carving, or holographic text should reflect the technology level of the world

The plaque should appear as a **natural artifact of the world rather than a modern overlay UI**.

---

**整理：** Yep（[gentpan](https://github.com/gentpan)）  
**来源：** [ImgEdify/awesome-nano-banana-pro-prompts](https://x.com/artingent/status/2031009161975300471)  
**许可：** MIT
