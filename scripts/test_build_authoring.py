#!/usr/bin/env python3
"""
Smoke test for build_authoring.py script.
Run this to verify the script works correctly.
"""

import sys
import subprocess
from pathlib import Path


def test_script_runs():
    """Test that the script runs without errors."""
    print("Testing script execution...")
    result = subprocess.run(
        ["python3", "scripts/build_authoring.py"],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"❌ Script failed with exit code {result.returncode}")
        print(f"STDERR: {result.stderr}")
        return False
    
    if "✓ Build authoring completed successfully" not in result.stdout:
        print("❌ Script didn't report success")
        print(f"STDOUT: {result.stdout}")
        return False
    
    print("✅ Script executed successfully")
    return True


def test_critical_files_exist():
    """Test that critical index.md files were created."""
    print("\nTesting critical files...")
    critical_paths = [
        "docs/authoring/index.md",
        "docs/reposzablony/index.md",
        "docs/reposzablony/01_core/index.md",
        "docs/reposzablony/01_core/api/index.md",
    ]
    
    all_exist = True
    for path in critical_paths:
        if not Path(path).exists():
            print(f"❌ Missing: {path}")
            all_exist = False
    
    if all_exist:
        print(f"✅ All {len(critical_paths)} critical files exist")
    
    return all_exist


def test_content_embedded():
    """Test that CSV and Mermaid content is embedded."""
    print("\nTesting embedded content...")
    
    # Check CSV
    datasets_index = Path("docs/reposzablony/01_core/datasets/index.md")
    if datasets_index.exists():
        content = datasets_index.read_text()
        if "{csv-table}" not in content:
            print("❌ CSV tables not embedded in datasets/index.md")
            return False
        print("✅ CSV tables embedded")
    
    # Check Mermaid
    diagrams_index = Path("docs/reposzablony/01_core/diagrams/index.md")
    if diagrams_index.exists():
        content = diagrams_index.read_text()
        if "{mermaid}" not in content:
            print("❌ Mermaid diagrams not embedded in diagrams/index.md")
            return False
        print("✅ Mermaid diagrams embedded")
    
    return True


def test_internal_links():
    """Test that authoring/index.md uses internal links."""
    print("\nTesting internal links...")
    authoring = Path("docs/authoring/index.md")
    
    if not authoring.exists():
        print("❌ authoring/index.md doesn't exist")
        return False
    
    content = authoring.read_text()
    
    if "github.com" in content:
        print("⚠️  GitHub links still present in authoring/index.md")
        return False
    
    if "../reposzablony/" not in content:
        print("❌ Internal links to reposzablony not found")
        return False
    
    print("✅ Internal links are correct")
    return True


def main():
    """Run all tests."""
    print("=" * 60)
    print("Build Authoring Script - Smoke Test")
    print("=" * 60)
    
    tests = [
        test_script_runs,
        test_critical_files_exist,
        test_content_embedded,
        test_internal_links,
    ]
    
    results = [test() for test in tests]
    
    print("\n" + "=" * 60)
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"✅ All {total} tests passed!")
        print("=" * 60)
        return 0
    else:
        print(f"❌ {total - passed} of {total} tests failed")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
