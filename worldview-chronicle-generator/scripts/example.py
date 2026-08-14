#!/usr/bin/env python3
"""
WorldView Chronicle Generator — Validation & Statistics Utility
Platform-agnostic helper script for verifying project structure and counting characters/words.
"""

import os
import sys
from pathlib import Path

# Output filenames (without extension - .md is assumed)
OUTPUT_FILES = {
    "world": "world.md",
    "plots": "plots.md",
    "society": "society.md",
    "chronicle": "chronicle.md"
}


def validate_project_structure(project_dir: str = ".") -> dict:
    """
    Verify that all required output files exist in the project directory.
    
    Returns a dict with file presence status and summary.
    """
    project_path = Path(project_dir)
    result = {"valid": True, "files": {}, "missing": []}
    
    for key, filename in OUTPUT_FILES.items():
        file_path = project_path / filename
        exists = file_path.exists()
        result["files"][key] = {"path": str(file_path), "exists": exists}
        if not exists:
            result["missing"].append(filename)
            result["valid"] = False
    
    return result


def count_text_stats(file_path: str) -> dict:
    """
    Count characters and words in a text file.
    Returns stats for both Chinese and English text.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        total_chars = len(content)
        non_space_chars = len([c for c in content if not c.isspace()])
        
        # Rough word count (split by whitespace for English, 
        # each CJK character counts as ~1 word)
        import re
        cjk_chars = len(re.findall(r'[\u4e00-\u9fff\u3400-\u4dbf]', content))
        english_words = len(re.findall(r'[a-zA-Z]+', content))
        estimated_words = cjk_chars + english_words
        
        return {
            "total_chars": total_chars,
            "non_space_chars": non_space_chars,
            "cjk_chars": cjk_chars,
            "english_words": english_words,
            "estimated_words": estimated_words
        }
    except Exception as e:
        return {"error": str(e)}


def print_report(project_dir: str = "."):
    """Print a formatted validation and statistics report."""
    print("=" * 50)
    print("WorldView Chronicle Generator — Project Report")
    print("=" * 50)
    
    # Validate structure
    result = validate_project_structure(project_dir)
    
    print("\n📁 Structure Validation:")
    for key, info in result["files"].items():
        status = "✅" if info["exists"] else "❌"
        print(f"  {status} {info['path']}")
    
    if result["missing"]:
        print(f"\n⚠️  Missing: {', '.join(result['missing'])}")
    
    # Stats for existing files
    print("\n📊 File Statistics:")
    for key, info in result["files"].items():
        if info["exists"]:
            stats = count_text_stats(info["path"])
            if "error" in stats:
                print(f"  ⚠️  {key}: {stats['error']}")
            else:
                print(f"  📄 {key}:")
                print(f"     Characters (no spaces): {stats['non_space_chars']:,}")
                print(f"     Estimated words: {stats['estimated_words']:,}")
    
    print("\n" + "=" * 50)
    return result["valid"]


if __name__ == "__main__":
    project_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    valid = print_report(project_dir)
    sys.exit(0 if valid else 1)
