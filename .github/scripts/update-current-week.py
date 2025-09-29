#!/usr/bin/env python3
"""
Update the main page with the current week's information based on the current date.
"""

import re
from datetime import datetime
import sys
from pathlib import Path

# Week schedule with start dates (Mondays)
WEEK_SCHEDULE = [
    {"week": "0-1", "start": "2025-09-15", "title": "Course Overview", "topics": "Setup • Unix/Linux • Git"},
    {"week": "2", "start": "2025-09-22", "title": "Advanced Unix", "topics": "Shell Scripting • Automation • Tools"},
    {"week": "3", "start": "2025-09-29", "title": "Git & Python Fundamentals", "topics": "Version Control • Python Basics • Practice"},
    {"week": "4", "start": "2025-10-06", "title": "Functions & Data Structures", "topics": "Functions • Lists • Dictionaries"},
    {"week": "5", "start": "2025-10-13", "title": "AI & Intelligent Agents", "topics": "LLMs • Prompt Engineering • Agents"},
    {"week": "6", "start": "2025-10-20", "title": "OOP & Debugging", "topics": "Classes • Inheritance • Testing"},
    {"week": "7", "start": "2025-10-27", "title": "Linear Regression", "topics": "Data Analysis • ML Basics • sklearn"},
    {"week": "8", "start": "2025-11-03", "title": "Feature Engineering", "topics": "Preprocessing • Selection • Validation"},
    {"week": "9", "start": "2025-11-10", "title": "Advanced Regression", "topics": "Regularization • Cross-validation • Metrics"},
    {"week": "10", "start": "2025-11-17", "title": "Classification", "topics": "Logistic Regression • Trees • Evaluation"},
    {"week": "11", "start": "2025-11-24", "title": "Neural Networks", "topics": "Perceptron • Backpropagation • PyTorch"},
    {"week": "12", "start": "2025-12-01", "title": "Deep Learning", "topics": "CNNs • RNNs • Transfer Learning"},
    {"week": "13", "start": "2025-12-08", "title": "Project Presentations", "topics": "Final Projects • Demos • Peer Review"},
    {"week": "14", "start": "2025-12-15", "title": "Course Wrap-up", "topics": "Review • Exam Prep • Next Steps"}
]

def get_current_week():
    """Determine which week should be displayed based on current date."""
    today = datetime.now().date()

    # Find the appropriate week
    current_week = WEEK_SCHEDULE[0]  # Default to first week

    for week in WEEK_SCHEDULE:
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

    # Get current week
    current_week = get_current_week()
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