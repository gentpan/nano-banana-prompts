#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nano Banana 图像生成脚本

用途：
1. 遍历 prompts/ 目录下的所有 markdown 文件
2. 提取提示词内容
3. 调用 Gemini API 生成图像
4. 保存生成的图像到对应位置

当前状态：存根（TODO）
"""

import os
import re
import yaml
from pathlib import Path
from typing import List, Dict, Optional


class PromptExtractor:
    """提示词提取器"""
    
    @staticmethod
    def extract_from_markdown(md_path: Path) -> Dict:
        """从 markdown 文件提取提示词和元数据"""
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取 YAML frontmatter
        yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not yaml_match:
            return None
        
        metadata = yaml.safe_load(yaml_match.group(1))
        
        # 提取中文提示词
        zh_match = re.search(r'## 中文\n\n```\n(.*?)\n```', content, re.DOTALL)
        prompt_zh = zh_match.group(1).strip() if zh_match else ''
        
        # 提取英文提示词
        en_match = re.search(r'## English\n\n```\n(.*?)\n```', content, re.DOTALL)
        prompt_en = en_match.group(1).strip() if en_match else ''
        
        return {
            'metadata': metadata,
            'prompt_zh': prompt_zh,
            'prompt_en': prompt_en,
            'file_path': md_path
        }


class ImageGenerator:
    """图像生成器（TODO：实现 Gemini API 调用）"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        初始化图像生成器
        
        Args:
            api_key: Google Gemini API 密钥
        """
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            print("警告: 未设置 GEMINI_API_KEY 环境变量")
    
    def generate(self, prompt: str, output_path: Path) -> bool:
        """
        生成图像
        
        Args:
            prompt: 提示词文本
            output_path: 输出图像路径
        
        Returns:
            是否成功生成
        """
        # TODO: 实现 Gemini API 调用
        print(f"[TODO] 生成图像: {output_path}")
        print(f"  提示词: {prompt[:100]}...")
        return False


def walk_prompts(prompts_dir: Path = Path('prompts')) -> List[Dict]:
    """
    遍历所有提示词文件
    
    Args:
        prompts_dir: prompts 目录路径
    
    Returns:
        提示词数据列表
    """
    prompts = []
    extractor = PromptExtractor()
    
    for category_dir in prompts_dir.iterdir():
        if not category_dir.is_dir():
            continue
        
        for md_file in sorted(category_dir.glob('*.md')):
            data = extractor.extract_from_markdown(md_file)
            if data:
                prompts.append(data)
    
    return prompts


def main():
    """主函数"""
    print("Nano Banana 图像生成脚本")
    print("=" * 60)
    
    # 检查当前目录
    if not Path('prompts').exists():
        print("错误: 未找到 prompts 目录")
        print("请在仓库根目录运行此脚本")
        return 1
    
    # 遍历提示词
    print("\n遍历提示词文件...")
    prompts = walk_prompts()
    print(f"找到 {len(prompts)} 个提示词")
    
    # 按分类统计
    categories = {}
    for p in prompts:
        cat = p['metadata'].get('category_zh', '未知')
        categories[cat] = categories.get(cat, 0) + 1
    
    print("\n分类统计:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count} 个")
    
    # TODO: 生成图像
    print("\n" + "=" * 60)
    print("图像生成功能待实现")
    print("\n待办事项:")
    print("  1. 实现 Gemini API 调用")
    print("  2. 处理 API 限速和重试")
    print("  3. 保存生成的图像")
    print("  4. 生成图像索引文件")
    print("\n使用方法:")
    print("  export GEMINI_API_KEY='your-api-key'")
    print("  python scripts/generate_images.py")
    
    return 0


if __name__ == '__main__':
    exit(main())
