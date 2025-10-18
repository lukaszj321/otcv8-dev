#!/usr/bin/env python3
"""
YAML Front-matter Fixer
Normalizes YAML front-matter to proper multiline format:
- Converts single-line to multiline
- Converts tags to YAML list format
- Ensures single --- delimiter blocks
- Preserves all fields
"""

import re
import sys
from pathlib import Path
from typing import Tuple, Dict


def parse_single_line_frontmatter(line: str) -> Dict[str, str]:
    """Parse single-line frontmatter into dict."""
    fields = {}
    # Match key: value pairs, handling commas in values
    pattern = r'(\w+):\s*([^,]+?)(?:,\s*(?=\w+:)|$)'
    for match in re.finditer(pattern, line):
        key = match.group(1)
        value = match.group(2).strip()
        fields[key] = value
    return fields


def format_multiline_frontmatter(fields: Dict[str, str]) -> str:
    """Format fields as multiline YAML."""
    lines = ['---']
    
    # Order: doc_id, source_path, source_sha, last_sync_iso, doc_class, language, title, summary, tags
    key_order = ['doc_id', 'source_path', 'source_sha', 'last_sync_iso', 
                 'doc_class', 'language', 'title', 'summary', 'tags']
    
    for key in key_order:
        if key in fields:
            value = fields[key]
            
            # Remove extra quotes from value if present
            if value.startswith('""') and value.endswith('""'):
                value = value[1:-1]  # Remove outer quotes, keep inner quotes
            
            # Special handling for tags
            if key == 'tags':
                # Convert comma-separated to YAML list
                if ',' in value and not value.startswith('['):
                    tags = [tag.strip() for tag in value.split(',')]
                    lines.append('tags:')
                    for tag in tags:
                        lines.append(f'  - {tag}')
                elif value.startswith('['):
                    # Already a list, keep as-is
                    lines.append(f'{key}: {value}')
                else:
                    # Single tag
                    lines.append('tags:')
                    lines.append(f'  - {value}')
            # Special handling for ISO timestamps
            elif key == 'last_sync_iso':
                # Ensure timestamp is quoted
                if not (value.startswith('"') and value.endswith('"')):
                    value = f'"{value}"'
                lines.append(f'{key}: {value}')
            else:
                # Quote values that contain commas, colons, or special chars
                # But don't double-quote
                if ':' in value or ',' in value:
                    if not (value.startswith('"') and value.endswith('"')):
                        value = f'"{value}"'
                lines.append(f'{key}: {value}')
    
    # Add any remaining fields not in key_order
    for key, value in fields.items():
        if key not in key_order:
            # Remove extra quotes
            if value.startswith('""') and value.endswith('""'):
                value = value[1:-1]
            if ',' in value or ':' in value:
                if not (value.startswith('"') and value.endswith('"')):
                    value = f'"{value}"'
            lines.append(f'{key}: {value}')
    
    lines.append('---')
    return '\n'.join(lines)


def fix_frontmatter(filepath: Path) -> Tuple[bool, str]:
    """
    Fix frontmatter in a markdown file.
    
    Returns:
        (modified, reason)
    """
    try:
        content = filepath.read_text(encoding='utf-8')
        lines = content.splitlines(keepends=False)
        
        if not lines or not lines[0].startswith('---'):
            # No frontmatter
            return False, "no_frontmatter"
        
        # Find end of frontmatter
        end_idx = -1
        for i in range(1, min(len(lines), 50)):
            if lines[i].startswith('---'):
                end_idx = i
                break
        
        if end_idx == -1:
            return False, "unclosed_frontmatter"
        
        # Get frontmatter content
        fm_lines = lines[1:end_idx]
        
        # Check if it's single-line
        if len(fm_lines) == 1:
            # Parse single-line frontmatter
            fields = parse_single_line_frontmatter(fm_lines[0])
            if not fields:
                return False, "parse_error"
            
            # Generate multiline YAML
            new_frontmatter = format_multiline_frontmatter(fields)
            
            # Reconstruct file
            rest_of_file = lines[end_idx + 1:]
            new_content = new_frontmatter + '\n\n' + '\n'.join(rest_of_file)
            
            filepath.write_text(new_content, encoding='utf-8')
            return True, "single_line_fixed"
        
        # Check if tags needs fixing (multiline but wrong format)
        needs_tag_fix = False
        for line in fm_lines:
            if line.startswith('tags:'):
                value = line.split(':', 1)[1].strip()
                if ',' in value and not value.startswith('['):
                    needs_tag_fix = True
                    break
        
        if needs_tag_fix:
            # Parse existing multiline frontmatter
            fields = {}
            i = 0
            while i < len(fm_lines):
                line = fm_lines[i]
                if ':' in line and not line.startswith(' '):
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # Check if next lines are list items
                    if i + 1 < len(fm_lines) and fm_lines[i + 1].startswith('  - '):
                        # Already a list, collect items
                        items = []
                        i += 1
                        while i < len(fm_lines) and fm_lines[i].startswith('  - '):
                            items.append(fm_lines[i][4:].strip())
                            i += 1
                        fields[key] = items
                        continue
                    else:
                        fields[key] = value
                i += 1
            
            # Regenerate frontmatter with proper formatting
            new_frontmatter = format_multiline_frontmatter(fields)
            
            # Reconstruct file
            rest_of_file = lines[end_idx + 1:]
            new_content = new_frontmatter + '\n\n' + '\n'.join(rest_of_file)
            
            filepath.write_text(new_content, encoding='utf-8')
            return True, "tags_fixed"
        
        return False, "no_issues"
        
    except Exception as e:
        return False, f"error: {e}"


def main():
    """Main entry point."""
    base_path = Path('docs/authoring')
    
    if not base_path.exists():
        print(f"Error: {base_path} does not exist", file=sys.stderr)
        sys.exit(1)
    
    total_files = 0
    fixes = {'single_line_fixed': 0, 'tags_fixed': 0}
    modified_files = []
    
    # Process all markdown files in docs/authoring
    for md_file in base_path.rglob('*.md'):
        # Skip _instructions and _tools
        if any(part.startswith('_') for part in md_file.parts):
            continue
        
        # Skip certain doc files
        if md_file.name in ['README.md', 'MERMAID_FIX_COMPLETE.md', 'facets.md']:
            continue
        
        was_modified, reason = fix_frontmatter(md_file)
        if was_modified:
            total_files += 1
            if reason in fixes:
                fixes[reason] += 1
            rel_path = md_file.relative_to(base_path)
            modified_files.append((str(rel_path), reason))
    
    # Print summary
    print(f"Front-matter Fix Complete")
    print(f"  Files modified: {total_files}")
    for fix_type, count in fixes.items():
        if count > 0:
            print(f"  {fix_type}: {count}")
    
    if modified_files:
        print("\nModified files:")
        for filepath, reason in modified_files[:20]:  # Show first 20
            print(f"  - {filepath}: {reason}")
        if len(modified_files) > 20:
            print(f"  ... and {len(modified_files) - 20} more")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
