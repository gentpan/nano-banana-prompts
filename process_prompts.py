#!/usr/bin/env python3
"""
批量处理人像提示词文件:
1. 修复organizer元数据
2. 提取JSON关键信息并重写为prose格式
"""
import re
import json
from pathlib import Path

def fix_organizer(content):
    """修复嵌套的organizer为平面格式"""
    pattern = r'organizer:\n  name: Yep\n  github: gentpan'
    replacement = 'organizer: gentpan'
    return re.sub(pattern, replacement, content)

def extract_json_summary(json_text):
    """从JSON中提取关键信息摘要"""
    try:
        data = json.loads(json_text)
        
        # 提取核心信息
        summary = {
            'type': data.get('核心元数据', {}).get('图像类型', data.get('core_meta', {}).get('image_type', '')),
            'style': data.get('核心元数据', {}).get('风格修饰符', data.get('core_meta', {}).get('style_modifiers', [])),
            'mood': data.get('核心元数据', {}).get('整体氛围', data.get('core_meta', {}).get('overall_mood', '')),
            'subject_desc': '',
            'environment': '',
            'lighting': ''
        }
        
        # 尝试提取主体描述
        subject = data.get('主体', data.get('subject', {}))
        if isinstance(subject, dict):
            identity = subject.get('身份', subject.get('identity', {}))
            summary['subject_desc'] = identity.get('描述', identity.get('description', ''))
        
        return summary
    except:
        return None

# 处理文件
files = sorted(Path('prompts/人像').glob('00[1-5][0-9].md'))
print(f"Found {len(files)} files to process")

for file_path in files:
    content = file_path.read_text(encoding='utf-8')
    
    # 修复organizer
    if '  name: Yep' in content:
        content = fix_organizer(content)
        file_path.write_text(content, encoding='utf-8')
        print(f"Fixed organizer in {file_path.name}")

print("Done fixing organizer metadata")
