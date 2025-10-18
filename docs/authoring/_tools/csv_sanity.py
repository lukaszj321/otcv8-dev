#!/usr/bin/env python3
"""
CSV Sanity Checker for OTClient v8 Documentation

Validates CSV datasets:
1. Checks for consistent headers
2. Validates no empty columns (except notes/note)
3. Checks relative paths are valid
4. Ensures idempotency

Generates: docs/authoring/qa/dataset_sanity.csv
"""

import csv
import sys
from pathlib import Path
from typing import List, Tuple, Dict

def check_csv_file(csv_path: Path, base_path: Path) -> List[Tuple[str, str]]:
    """Check a single CSV file for sanity."""
    issues = []
    
    try:
        with open(csv_path, 'r', encoding='utf-8', newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
            
            if not rows:
                issues.append(('WARN', 'File is empty'))
                return issues
            
            headers = rows[0]
            data_rows = rows[1:]
            
            # Check for empty file (only headers)
            if not data_rows:
                issues.append(('INFO', 'No data rows (only headers)'))
                return issues
            
            # Check each column for emptiness
            for col_idx, header in enumerate(headers):
                # Skip notes/note columns
                if header.lower() in ['note', 'notes']:
                    continue
                
                # Check if all values in this column are empty
                all_empty = all(
                    col_idx >= len(row) or not row[col_idx].strip()
                    for row in data_rows
                )
                
                if all_empty:
                    issues.append(('WARN', f'Column "{header}" is empty in all rows'))
            
            # Check for path columns and validate
            path_columns = [i for i, h in enumerate(headers) if 'path' in h.lower()]
            for col_idx in path_columns:
                for row_idx, row in enumerate(data_rows):
                    if col_idx < len(row) and row[col_idx].strip():
                        path_val = row[col_idx].strip()
                        # Check if it's a relative path
                        if not path_val.startswith(('http://', 'https://', '/')):
                            # Try to resolve relative to base
                            check_path = base_path / path_val
                            if not check_path.exists():
                                issues.append((
                                    'INFO',
                                    f'Row {row_idx+2}, col "{headers[col_idx]}": path not found: {path_val}'
                                ))
            
            # Check for consistent row length
            expected_cols = len(headers)
            for row_idx, row in enumerate(data_rows):
                if len(row) != expected_cols:
                    issues.append((
                        'WARN',
                        f'Row {row_idx+2}: has {len(row)} columns, expected {expected_cols}'
                    ))
            
    except Exception as e:
        issues.append(('ERROR', f'Failed to process: {str(e)}'))
    
    return issues

def main():
    """Main entry point."""
    import argparse
    parser = argparse.ArgumentParser(description='Check CSV sanity')
    parser.add_argument('--in', dest='input_dir', required=True, help='Input directory with CSVs')
    parser.add_argument('--out', dest='output', required=True, help='Output CSV report')
    args = parser.parse_args()
    
    input_path = Path(args.input_dir)
    output_path = Path(args.output)
    
    if not input_path.exists():
        print(f"Error: Input directory does not exist: {input_path}")
        return 1
    
    # Find all CSV files
    csv_files = list(input_path.rglob('*.csv'))
    if not csv_files:
        print(f"Warning: No CSV files found in {input_path}")
    
    print(f"Checking {len(csv_files)} CSV files...")
    
    results = []
    base_path = Path('.')
    
    for csv_file in csv_files:
        rel_path = csv_file.relative_to(input_path)
        issues = check_csv_file(csv_file, base_path)
        
        if not issues:
            results.append([str(rel_path), 'PASS', 'No issues found'])
        else:
            for severity, issue in issues:
                results.append([str(rel_path), severity, issue])
                if severity in ['ERROR', 'WARN']:
                    print(f"  {severity}: {rel_path} - {issue}")
    
    # Write report
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['file', 'status', 'issue'])
        writer.writerows(results)
    
    print(f"\nReport written to: {output_path}")
    print(f"Total files checked: {len(csv_files)}")
    print(f"Files with issues: {len(set(r[0] for r in results if r[1] in ['ERROR', 'WARN']))}")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
