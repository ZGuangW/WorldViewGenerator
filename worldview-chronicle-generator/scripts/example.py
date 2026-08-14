#!/usr/bin/env python3
# 世界观编年史生成系统 - 辅助脚本
# 此文件为占位示例，可按需添加自动化辅助工具

import os
import sys
from pathlib import Path

def validate_project_structure(project_dir: str) -> bool:
    """
    验证项目目录结构是否完整
    
    必需文件：
    - 世界观框架.md
    - 关键情节.md
    - 社会面貌.md
    - 编年史.md
    """
    required_files = [
        "世界观框架.md",
        "关键情节.md", 
        "社会面貌.md",
        "编年史.md"
    ]
    
    project_path = Path(project_dir)
    missing = []
    
    for f in required_files:
        if not (project_path / f).exists():
            missing.append(f)
    
    if missing:
        print(f"缺少文件: {', '.join(missing)}")
        return False
    
    print("项目结构完整")
    return True


def count_chinese_chars(file_path: str) -> int:
    """统计文件中的中文字符数（粗略估计）"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # 简单统计非空白字符
        count = len([c for c in content if not c.isspace()])
        return count
    except Exception as e:
        print(f"读取文件失败: {e}")
        return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        project_dir = sys.argv[1]
    else:
        project_dir = "."
    
    validate_project_structure(project_dir)
    
    chronicle_file = Path(project_dir) / "编年史.md"
    if chronicle_file.exists():
        char_count = count_chinese_chars(str(chronicle_file))
        print(f"编年史.md 字符数: {char_count}")
