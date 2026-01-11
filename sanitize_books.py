#!/usr/bin/env python3
"""
Sanitize Bible book files for public GitHub repository.
- Resets all checkboxes to unchecked
- Replaces all specific dates with placeholder format
"""

import re
from pathlib import Path


def sanitize_file(file_path: Path) -> None:
    """Sanitize a single markdown file."""
    content = file_path.read_text(encoding='utf-8')

    # Reset all checkboxes to unchecked
    content = re.sub(r'- \[x\] Read', '- [ ] Read', content, flags=re.IGNORECASE)

    # Replace specific dates with placeholder
    # Matches formats like: 2026-01-06, 2025-03-15, etc.
    content = re.sub(r'📖\s*\d{4}-\d{2}-\d{2}', '📖 2025-MM-DD', content)

    # Write sanitized content back
    file_path.write_text(content, encoding='utf-8')
    print(f"✓ Sanitized: {file_path.name}")


def main():
    """Sanitize all book files in the directory."""
    base_dir = Path(__file__).parent

    # Find all markdown files in Old Testament and New Testament directories
    book_files = list(base_dir.glob("Old Testament/**/*.md"))
    book_files.extend(base_dir.glob("New Testament/**/*.md"))

    print(f"Found {len(book_files)} book files to sanitize")
    print("-" * 50)

    for book_file in sorted(book_files):
        sanitize_file(book_file)

    print("-" * 50)
    print(f"✅ Sanitized {len(book_files)} files successfully!")


if __name__ == "__main__":
    main()
