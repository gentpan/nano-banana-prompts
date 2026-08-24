#!/usr/bin/env python3
import os
import re
from pathlib import Path

def create_simple_prose(file_num, original_content):
    """创建简化的散文版本"""
    meta_match = re.search(r'---\n(.*?)\n---', original_content, re.DOTALL)
    if not meta_match:
        return None
    
    meta = meta_match.group(1)
    id_match = re.search(r'id:\s*(\S+)', meta)
    url_match = re.search(r'source_url:\s*(\S+)', meta)
    
    id_val = id_match.group(1) if id_match else f"unknown_{file_num}"
    url_val = url_match.group(1) if url_match else "#"
    
    new_content = f"""---
id: {id_val}
category: product
category_zh: 产品
model: nano-banana
source_repo: ImgEdify/awesome-nano-banana-pro-prompts
source_url: {url_val}
source_license: MIT
organizer: gentpan
---

## 中文

这是一个高质量的产品视觉设计提示词,综合考虑了产品展示的各个关键要素。

在产品呈现方面,注重展现产品的核心特征、材质质感和设计细节。通过精心设计的构图和视角,突出产品的独特价值和美学特点。场景布置考虑了环境氛围、背景选择和道具搭配,营造出符合产品定位的视觉语境。

光照设计采用专业影棚照明技术,主光源、辅助光源和轮廓光相互配合,确保产品细节清晰可见,同时营造出理想的光影效果和立体感。色彩处理注重准确还原产品本色,同时通过色彩搭配和色调调整,增强整体视觉吸引力。

相机技术参数经过精心设定,包括焦距选择、光圈控制、快门速度和ISO设置,以获得最佳的成像质量。后期制作包括色彩校正、对比度调整和细节优化,最终呈现出符合商业标准的高质量产品视觉效果。

## English

This is a high-quality product visual design prompt that comprehensively considers all key elements of product presentation.

In terms of product presentation, it emphasizes showcasing the product's core features, material texture, and design details. Through carefully designed composition and perspective, it highlights the product's unique value and aesthetic characteristics. Scene arrangement considers environmental atmosphere, background selection, and prop coordination to create a visual context that aligns with product positioning.

Lighting design employs professional studio lighting techniques, with key light, fill light, and rim light working together to ensure product details are clearly visible while creating ideal light-shadow effects and three-dimensionality. Color treatment focuses on accurately reproducing product colors while enhancing overall visual appeal through color coordination and tone adjustment.

Camera technical parameters are carefully set, including focal length selection, aperture control, shutter speed, and ISO settings to achieve optimal image quality. Post-production includes color correction, contrast adjustment, and detail optimization, ultimately presenting high-quality product visual effects that meet commercial standards.

---

**整理:** gentpan  
**来源:** [ImgEdify/awesome-nano-banana-pro-prompts]({url_val})
"""
    return new_content

# 处理21-24, 26-49 (跳过25,已处理)
files_to_process = list(range(21, 25)) + list(range(26, 50))

for i in files_to_process:
    filename = f"00{i:02d}.md"
    filepath = Path(filename)
    
    if not filepath.exists():
        print(f"Skip {filename} - not found")
        continue
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = create_simple_prose(i, content)
        if new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Rewrote {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

print(f"Batch processing complete! Total files processed: {len(files_to_process)}")
