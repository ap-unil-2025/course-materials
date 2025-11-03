#!/usr/bin/env python3
"""
Update the main page with the current week's information based on the current date.
Reads week information from content/week-definitions/ files.
"""

import re
from datetime import datetime
import sys
from pathlib import Path

def parse_week_definition(file_path):
    """Parse a week definition file using regex (no YAML dependency needed)."""
    with open(file_path, 'r') as f:
        content = f.read()

    # Extract values using regex
    title_match = re.search(r'^title:\s*["\']?([^"\'\n]+)["\']?', content, re.MULTILINE)
    date_match = re.search(r'^date:\s*(\d{4}-\d{2}-\d{2})', content, re.MULTILINE)
    desc_match = re.search(r'^description:\s*["\']?([^"\'\n]+)["\']?', content, re.MULTILINE)

    if not all([title_match, date_match, desc_match]):
        return None

    return {
        'title': title_match.group(1),
        'date': date_match.group(1),
        'description': desc_match.group(1)
    }

def get_week_schedule(repo_root):
    """Build week schedule from week definition files."""
    week_defs_dir = repo_root / "content" / "week-definitions"

    schedule = []

    # Process week00 through week14
    for i in range(15):
        week_file = week_defs_dir / f"week{i:02d}.md"
        if not week_file.exists():
            continue

        data = parse_week_definition(week_file)
        if not data:
            continue

        # Extract week number from title (e.g., "Week 7: Linear Regression" -> "7")
        title = data.get('title', '')

        # Handle special cases like "Week 0-1"
        if i == 0:
            week_num = "0-1"
        else:
            # Extract number from title
            match = re.search(r'Week (\d+)', title)
            week_num = match.group(1) if match else str(i)

        # Remove "Week X: " prefix from title
        clean_title = re.sub(r'^Week \d+:\s*', '', title)

        # Get description for topics
        topics = data.get('description', '')

        schedule.append({
            "week": week_num,
            "start": str(data.get('date', '')),
            "title": clean_title,
            "topics": topics
        })

    return sorted(schedule, key=lambda x: x['start'])

def get_current_week(schedule):
    """Determine which week should be displayed based on current date."""
    today = datetime.now().date()

    # Find the appropriate week
    current_week = schedule[0]  # Default to first week

    for week in schedule:
        week_start = datetime.strptime(week["start"], "%Y-%m-%d").date()
        if today >= week_start:
            current_week = week
        else:
            break

    return current_week

def update_index_file(file_path, current_week):
    """Update the index.html file with current week information."""

    with open(file_path, 'r') as f:
        content = f.read()

    # Pattern to match the current week banner section
    pattern = r'(<div class="current-info">[\s\S]*?<h2>)(Week [^<]+)(<\/h2>[\s\S]*?<p>)([^<]+)(<\/p>)'

    # Build replacement string
    replacement = (
        r'\1Week {}: {}\3{}\5'.format(
            current_week["week"],
            current_week["title"],
            current_week["topics"]
        )
    )

    # Perform replacement
    updated_content = re.sub(pattern, replacement, content)

    # Check if replacement was made
    if updated_content == content:
        print("⚠️  Warning: No changes made. Pattern might not match.")
        return False

    # Write updated content
    with open(file_path, 'w') as f:
        f.write(updated_content)

    return True

def main():
    # Get repository root (assuming script is in .github/scripts/)
    repo_root = Path(__file__).parent.parent.parent
    index_path = repo_root / "docs" / "index.html"

    if not index_path.exists():
        print(f"❌ Error: {index_path} not found")
        sys.exit(1)

    # Build schedule from week definition files
    print("📖 Reading week definitions...")
    schedule = get_week_schedule(repo_root)

    if not schedule:
        print("❌ Error: No week definitions found")
        sys.exit(1)

    print(f"✅ Loaded {len(schedule)} weeks")

    # Get current week
    current_week = get_current_week(schedule)
    print(f"📅 Current week: Week {current_week['week']} - {current_week['title']}")
    print(f"   Topics: {current_week['topics']}")

    # Update index file
    if update_index_file(index_path, current_week):
        print(f"✅ Successfully updated index.html")
    else:
        print(f"❌ Failed to update index.html")
        sys.exit(1)

if __name__ == "__main__":
    main()
