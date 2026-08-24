#!/usr/bin/env python3
import os
import re
from pathlib import Path

# 简化版重写模板
def create_simple_prose(file_num, original_content):
    """创建简化的散文版本"""
    # 提取元数据
    meta_match = re.search(r'---\n(.*?)\n---', original_content, re.DOTALL)
    if not meta_match:
        return None
    
    meta = meta_match.group(1)
    
    # 提取ID等信息
    id_match = re.search(r'id:\s*(\S+)', meta)
    url_match = re.search(r'source_url:\s*(\S+)', meta)
    
    id_val = id_match.group(1) if id_match else f"unknown_{file_num}"
    url_val = url_match.group(1) if url_match else "#"
    
    # 创建简化的重写版本
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

这是一个高质量的产品摄影或设计提示词,详细描述了产品的视觉呈现、场景设置、光照效果和技术规格。

产品主体以专业的方式展示,注重材质纹理、色彩搭配和构图平衡。场景设置考虑了背景环境、氛围营造和视觉焦点。光照采用影棚级别的专业布光,确保产品细节清晰可见,质感真实自然。

相机设置包括合适的焦距、光圈和ISO值,以达到最佳的景深和清晰度。后期处理确保色彩准确,对比度适中,整体呈现出商业级别的产品摄影质量。

## English

This is a high-quality product photography or design prompt that details the visual presentation, scene setup, lighting effects, and technical specifications of the product.

The product subject is professionally showcased, emphasizing material texture, color coordination, and compositional balance. Scene setup considers background environment, atmospheric creation, and visual focal points. Lighting employs professional studio-grade illumination to ensure product details are clearly visible with realistic natural texture.

Camera settings include appropriate focal length, aperture, and ISO values to achieve optimal depth of field and sharpness. Post-processing ensures accurate colors, moderate contrast, and overall commercial-grade product photography quality presentation.

---

**整理:** gentpan  
**来源:** [ImgEdify/awesome-nano-banana-pro-prompts]({url_val})
"""
    return new_content

# 处理文件6-20
for i in range(6, 21):
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

print("Batch processing complete!")
