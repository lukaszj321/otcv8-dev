#!/usr/bin/env python3
"""
fix_sphinx_and_cleanup.py

Orchestrator script that runs all helper scripts in order.
Supports --apply to apply changes and --report to generate a summary report.

Usage:
    python3 docs/scripts/fix_sphinx_and_cleanup.py                # dry-run all scripts
    python3 docs/scripts/fix_sphinx_and_cleanup.py --apply        # apply all changes
    python3 docs/scripts/fix_sphinx_and_cleanup.py --report       # generate summary report
    python3 docs/scripts/fix_sphinx_and_cleanup.py --apply --report  # both
"""

import sys
import subprocess
from pathlib import Path
from datetime import datetime
from typing import List, Dict


def find_script_dir() -> Path:
    """Find the docs/scripts directory."""
    return Path(__file__).parent


def run_script(script_name: str, args: List[str] = None) -> Dict:
    """
    Run a helper script and capture its output.
    
    Returns:
        dict with 'returncode', 'stdout', 'stderr', 'success'
    """
    script_dir = find_script_dir()
    script_path = script_dir / script_name
    
    if not script_path.exists():
        return {
            'returncode': -1,
            'stdout': '',
            'stderr': f'Script not found: {script_path}',
            'success': False
        }
    
    cmd = [sys.executable, str(script_path)]
    if args:
        cmd.extend(args)
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        return {
            'returncode': result.returncode,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'success': result.returncode == 0
        }
    except subprocess.TimeoutExpired:
        return {
            'returncode': -1,
            'stdout': '',
            'stderr': f'Script timed out after 5 minutes',
            'success': False
        }
    except Exception as e:
        return {
            'returncode': -1,
            'stdout': '',
            'stderr': str(e),
            'success': False
        }


def print_section(title: str):
    """Print a formatted section header."""
    print("\n" + "="*70)
    print(title)
    print("="*70 + "\n")


def main():
    apply = '--apply' in sys.argv
    report = '--report' in sys.argv
    
    mode = "APPLY MODE" if apply else "DRY-RUN MODE"
    print_section(f"Sphinx Docs Fix & Cleanup - {mode}")
    
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Apply changes: {apply}")
    print(f"Generate report: {report}")
    
    # Define scripts to run in order
    scripts = [
        {
            'name': 'detect_duplicate_anchors.py',
            'description': 'Detect duplicate anchors',
            'args': []
        },
        {
            'name': 'dedupe_anchors.py',
            'description': 'Deduplicate anchors',
            'args': ['--apply'] if apply else []
        },
        {
            'name': 'find_and_stub_missing_docs.py',
            'description': 'Find missing doc references and create placeholders',
            'args': ['--apply'] if apply else []
        },
        {
            'name': 'cleanup_scripts_tools.py',
            'description': 'Clean up old and unreferenced scripts',
            'args': ['--apply'] if apply else []
        }
    ]
    
    results = []
    
    # Run each script
    for script_info in scripts:
        print_section(f"Running: {script_info['name']}")
        print(f"Description: {script_info['description']}")
        print(f"Args: {' '.join(script_info['args']) if script_info['args'] else '(none)'}\n")
        
        result = run_script(script_info['name'], script_info['args'])
        results.append({
            'script': script_info['name'],
            'description': script_info['description'],
            'result': result
        })
        
        # Print output
        if result['stdout']:
            print(result['stdout'])
        
        if result['stderr']:
            print("STDERR:", file=sys.stderr)
            print(result['stderr'], file=sys.stderr)
        
        if not result['success']:
            print(f"\n⚠️  Warning: {script_info['name']} had issues (exit code: {result['returncode']})")
        else:
            print(f"\n✓ {script_info['name']} completed successfully")
    
    # Print summary
    print_section("SUMMARY")
    
    success_count = sum(1 for r in results if r['result']['success'])
    total_count = len(results)
    
    print(f"Completed: {success_count}/{total_count} scripts ran successfully\n")
    
    for r in results:
        status = "✓" if r['result']['success'] else "✗"
        print(f"  {status} {r['script']}")
    
    # Generate report if requested
    if report:
        print_section("GENERATING REPORT")
        report_path = find_script_dir().parent / "_data" / "fix_sphinx_report.txt"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(f"Sphinx Docs Fix & Cleanup Report\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Mode: {mode}\n")
                f.write(f"\n{'='*70}\n\n")
                
                for r in results:
                    f.write(f"Script: {r['script']}\n")
                    f.write(f"Description: {r['description']}\n")
                    f.write(f"Success: {r['result']['success']}\n")
                    f.write(f"Exit code: {r['result']['returncode']}\n")
                    f.write(f"\nOutput:\n{r['result']['stdout']}\n")
                    if r['result']['stderr']:
                        f.write(f"\nErrors:\n{r['result']['stderr']}\n")
                    f.write(f"\n{'-'*70}\n\n")
                
                f.write(f"\nSummary: {success_count}/{total_count} scripts completed successfully\n")
            
            print(f"Report written to: {report_path}")
        except Exception as e:
            print(f"Error writing report: {e}", file=sys.stderr)
    
    print(f"\nFinished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    
    # Exit with error if any script failed
    if success_count < total_count:
        sys.exit(1)


if __name__ == '__main__':
    main()
