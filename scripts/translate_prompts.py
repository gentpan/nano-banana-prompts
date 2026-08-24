#!/usr/bin/env python3
"""
翻译提示词文件的中文部分
将英文 JSON 提示词翻译成中文
"""

import json
import os
import re
from pathlib import Path


def translate_json_prompt(json_obj):
    """
    递归翻译 JSON 对象中的英文文本到中文
    保持 JSON 结构不变
    """
    # 这是一个简化的翻译映射，主要翻译常见的关键词和描述性文本
    translation_map = {
        # 核心元数据
        "core_meta": "核心元数据",
        "image_type": "图像类型",
        "art_medium": "艺术媒介",
        "style_modifiers": "风格修饰符",
        "overall_mood": "整体氛围",
        "vibe": "情绪",
        "quality_boosters": "质量增强",
        
        # 主体信息
        "subject": "主体",
        "subjects": "主体",
        "identity": "身份",
        "subject_type": "主体类型",
        "gender": "性别",
        "age": "年龄",
        "ethnicity": "种族",
        "description": "描述",
        
        # 解剖和身体
        "anatomy_and_body": "解剖与身体",
        "build_and_proportions": "体型与比例",
        "height_estimation_cm": "身高估计(厘米)",
        "skin_texture": "皮肤质感",
        "biological_features": "生物特征",
        "vascularity_and_pigment": "血管与色素",
        "subsurface_scattering": "次表面散射",
        "skin_micro_texture": "皮肤微观质感",
        "eye_complexity": "眼睛复杂度",
        "unique_markings_and_tattoos": "独特标记与纹身",
        
        # 面部和头发
        "face_and_hair": "面部与头发",
        "face_structure": "面部结构",
        "eyes": "眼睛",
        "eyebrows": "眉毛",
        "lips": "嘴唇",
        "makeup": "妆容",
        "expression": "表情",
        "hair": "头发",
        "style": "风格",
        "color": "颜色",
        "interaction_and_physics": "交互与物理",
        
        # 姿势和动作
        "pose_and_action": "姿势与动作",
        "action": "动作",
        "body_position": "身体位置",
        "stance": "站姿",
        "upper_body_and_arms": "上半身与手臂",
        "lower_body_and_legs": "下半身与双腿",
        "hand_gestures": "手势",
        "gaze_direction": "视线方向",
        "accuracy_constraints": "准确性约束",
        
        # 服装和配饰
        "wardrobe_and_inventory": "服装与配饰",
        "clothing": "服装",
        "top": "上装",
        "bottom": "下装",
        "type": "类型",
        "fabric": "面料",
        "details": "细节",
        "outerwear": "外套",
        "footwear": "鞋履",
        "fit_and_physics": "合身度与物理",
        "accessories": "配饰",
        "eyewear": "眼镜",
        "jewelry": "珠宝",
        "headwear": "头饰",
        "held_objects_and_props": "持有物品与道具",
        
        # 环境和场景
        "environment_and_scene": "环境与场景",
        "location": "位置",
        "setting_type": "场景类型",
        "atmosphere": "氛围",
        "time_of_day": "时间",
        "weather_conditions": "天气条件",
        "spatial_elements": "空间元素",
        "foreground_elements": "前景元素",
        "background_elements": "背景元素",
        "texture_details": "纹理细节",
        "environment": "环境",
        "materials": "材质",
        
        # 相机和构图
        "camera_and_composition": "相机与构图",
        "frame": "画幅",
        "aspect_ratio": "宽高比",
        "resolution": "分辨率",
        "orientation": "方向",
        "composition": "构图",
        "shot_type": "镜头类型",
        "camera_angle": "相机角度",
        "framing_guide": "取景指南",
        "perspective": "透视",
        "depth_and_focus": "景深与焦点",
        "symmetry_and_balance": "对称与平衡",
        "hardware_simulation": "硬件模拟",
        "camera_model": "相机型号",
        "lens_type": "镜头类型",
        "focal_length_mm": "焦距(毫米)",
        "phone_visibility": "手机可见度",
        "camera_settings": "相机设置",
        "aperture": "光圈",
        "shutter_speed": "快门速度",
        "iso": "ISO",
        "white_balance": "白平衡",
        "dynamic_range": "动态范围",
        
        # 照明和色彩
        "lighting_and_color": "照明与色彩",
        "lighting": "照明",
        "setup_type": "设置类型",
        "primary_source": "主光源",
        "secondary_source": "辅助光源",
        "direction": "方向",
        "shadow_quality": "阴影质量",
        "highlights": "高光",
        "lighting_interaction": "照明交互",
        "color_grading": "调色",
        "color_mode": "色彩模式",
        "palette": "色板",
        "color_temperature": "色温",
        "contrast_curve": "对比度曲线",
        "lut_application": "LUT应用",
        
        # 后期处理和特效
        "post_processing_and_fx": "后期处理与特效",
        "rendering": "渲染",
        "engine": "引擎",
        "approach": "方法",
        "optical_artifacts": "光学伪影",
        "chromatic_aberration": "色差",
        "vignetting": "晕影",
        "lens_flare": "镜头眩光",
        "bokeh_quality": "散景质量",
        "sensor_atmosphere": "传感器氛围",
        "iso_noise_structure": "ISO噪点结构",
        "sensor_bloom": "传感器泛光",
        "air_particles_and_haze": "空气粒子与雾霾",
        "imperfections_and_realism": "缺陷与真实感",
        
        # 高级控制
        "advanced_controls": "高级控制",
        "controlnet": "控制网络",
        "pose_control": "姿势控制",
        "depth_control": "深度控制",
        "model_type": "模型类型",
        "purpose": "目的",
        "constraints": "约束",
        "recommended_weight": "推荐权重",
        
        # 负面提示
        "negatives": "负面提示",
        "artifact_suppression": "伪影抑制",
        "subject_excludes": "主体排除",
        "forbid": "禁止",
        
        # 最终导演注释
        "final_director_notes": "最终导演注释",
        
        # 性别
        "Female": "女性",
        "Male": "男性",
        
        # 方向
        "Vertical": "竖向",
        "Horizontal": "横向",
    }
    
    if isinstance(json_obj, dict):
        result = {}
        for key, value in json_obj.items():
            # 翻译键名
            translated_key = translation_map.get(key, key)
            # 递归翻译值
            result[translated_key] = translate_json_prompt(value)
        return result
    elif isinstance(json_obj, list):
        return [translate_json_prompt(item) for item in json_obj]
    elif isinstance(json_obj, str):
        # 对于字符串值，可以选择性地翻译一些常见短语
        # 但大部分描述性文本保持原样，因为自动翻译可能不准确
        return json_obj
    else:
        return json_obj


def process_md_file(filepath):
    """
    处理单个 markdown 文件
    读取英文部分，翻译并更新中文部分
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取 YAML frontmatter
    yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not yaml_match:
        print(f"警告：{filepath} 没有找到 YAML frontmatter")
        return False
    
    yaml_section = yaml_match.group(0)
    rest_content = content[len(yaml_section):]
    
    # 提取英文部分的 JSON
    en_match = re.search(r'## English\n\n```\n(\{.*?\})\n```', rest_content, re.DOTALL)
    if not en_match:
        print(f"警告：{filepath} 没有找到英文 JSON")
        return False
    
    en_json_str = en_match.group(1)
    
    try:
        # 解析 JSON
        en_json = json.loads(en_json_str)
        
        # 翻译 JSON 键名
        zh_json = translate_json_prompt(en_json)
        
        # 生成格式化的中文 JSON
        zh_json_str = json.dumps(zh_json, ensure_ascii=False, indent=2)
        
        # 替换中文部分
        new_zh_section = f"## 中文\n\n```\n{zh_json_str}\n```\n"
        
        # 重新组装文件内容
        # 找到 ## 中文 部分的位置
        zh_start = rest_content.find('## 中文')
        if zh_start == -1:
            print(f"警告：{filepath} 没有找到中文部分")
            return False
        
        # 找到 ## English 部分的位置
        en_start = rest_content.find('## English')
        
        # 重建内容
        new_content = yaml_section + rest_content[:zh_start] + new_zh_section + "\n" + rest_content[en_start:]
        
        # 写回文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"错误：{filepath} JSON 解析失败: {e}")
        return False
    except Exception as e:
        print(f"错误：处理 {filepath} 时出错: {e}")
        return False


def main():
    """
    主函数：处理人像分类的所有文件
    """
    portrait_dir = Path(__file__).parent.parent / 'prompts' / '人像'
    
    if not portrait_dir.exists():
        print(f"错误：目录不存在: {portrait_dir}")
        return
    
    md_files = sorted(portrait_dir.glob('*.md'))
    
    print(f"找到 {len(md_files)} 个文件")
    
    success_count = 0
    fail_count = 0
    
    for md_file in md_files:
        print(f"处理: {md_file.name}...", end=' ')
        if process_md_file(md_file):
            print("✓")
            success_count += 1
        else:
            print("✗")
            fail_count += 1
    
    print(f"\n完成！成功: {success_count}, 失败: {fail_count}")


if __name__ == '__main__':
    main()
