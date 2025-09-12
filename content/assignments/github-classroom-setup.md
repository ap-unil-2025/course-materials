---
layout: guide
title: "GitHub Classroom Setup Guide"
description: "Complete guide for setting up GitHub Classroom for AP2025"
author: "Anna Smirnova"
date: 2025-09-01
---

# GitHub Classroom Setup Guide for AP2025

This guide walks through setting up GitHub Classroom for all course assignments, including both regular and advanced (optional grade booster) assignments.

## Table of Contents

1. [Initial Setup](#initial-setup)
2. [Creating Assignments](#creating-assignments)
3. [Starter Code Repositories](#starter-code-repositories)
4. [Autograding Configuration](#autograding-configuration)
5. [Student Workflow](#student-workflow)
6. [Grading Workflow](#grading-workflow)
7. [Troubleshooting](#troubleshooting)

## Initial Setup

### 1. Create GitHub Organization

1. Go to [GitHub Organizations](https://github.com/organizations/new)
2. Create organization: `AP2025-UNIL`
3. Set as Education organization
4. Apply for [GitHub Education benefits](https://education.github.com/teachers)

### 2. Setup GitHub Classroom

1. Visit [GitHub Classroom](https://classroom.github.com)
2. Click "New Classroom"
3. Select the `AP2025-UNIL` organization
4. Configure classroom:
   ```
   Name: AP2025 - Intro to Applied Programming
   Description: UNIL Applied Programming Course 2025
   ```

### 3. Add Teaching Assistants

1. Go to Classroom Settings → TAs & Admins
2. Add TAs with appropriate permissions:
   - **Admin**: Full access to all repositories
   - **Write**: Can view and provide feedback
   - **Read**: Can only view submissions

### 4. Student Roster

Create `students.csv`:
```csv
identifier,github_username,name
as123456,alice-gh,Alice Smith
bj234567,bob-dev,Bob Jones
```

Import via Settings → Roster Management

## Creating Assignments

### Regular Assignments (Weeks 1-6)

For each week's assignment:

```bash
# Example: Week 3 Python Basics
Assignment Title: Week 3 - Python Basics & Control Flow
Repository Prefix: week3-python-basics
Deadline: Sunday 23:59 (one week after session)
Type: Individual
Visibility: Private
```

### Advanced Assignments (Grade Boosters)

```bash
# Example: Advanced HW3
Assignment Title: [BONUS] Advanced HW3 - Text Adventure Game
Repository Prefix: advanced-hw3-adventure
Deadline: Sunday 23:59 (two weeks given)
Type: Individual
Visibility: Private
Template: Include starter with buggy code for debugging
```

## Starter Code Repositories

### Repository Structure

Create starter repositories in the organization:

#### Week 1 Starter
```
ap2025-week1-starter/
├── README.md           # Assignment instructions
├── .gitignore         # Python gitignore
├── requirements.txt   # Empty, for practice
├── tasks/
│   ├── task1.md      # Git basics
│   ├── task2.md      # Collaboration
│   └── task3.md      # Conflict resolution
└── .github/
    └── workflows/
        └── tests.yml  # Autograding
```

#### Week 3 Starter (Python Basics)
```
ap2025-week3-starter/
├── README.md
├── contact_manager.py  # Skeleton with TODOs
├── test_basic.py      # Basic test cases
├── requirements.txt
└── .github/
    └── workflows/
        └── tests.yml
```

#### Week 4 Starter (Functions & Data)
```
ap2025-week4-starter/
├── README.md
├── contact_manager_v2.py  # Week 3 solution + new TODOs
├── test_functions.py
├── data/
│   ├── sample_contacts.csv
│   └── sample_contacts.json
└── .github/
    └── workflows/
        └── tests.yml
```

#### Advanced HW Starters

Each advanced homework needs specialized starters:

```
ap2025-advanced-hw3-starter/
├── README.md
├── haunted_mansion_template.py  # Extensive skeleton
├── test_adventure.py
├── maps/
│   └── mansion_layout.txt
├── story/
│   └── narrative.txt
└── .github/
    └── workflows/
        └── tests.yml
```

## Autograding Configuration

### Basic Test Workflow

`.github/workflows/tests.yml`:
```yaml
name: Autograding Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest pytest-cov
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    
    - name: Run tests
      run: |
        pytest --cov=. --cov-report=xml
    
    - name: Check code style
      run: |
        pip install ruff
        ruff check .
    
    - name: Autograding
      uses: education/autograding@v1
```

### Autograding Configuration

`.github/classroom/autograding.json`:
```json
{
  "tests": [
    {
      "name": "Basic Functionality",
      "setup": "pip install -r requirements.txt",
      "run": "python -m pytest test_basic.py -v",
      "input": "",
      "output": "",
      "comparison": "included",
      "timeout": 10,
      "points": 40
    },
    {
      "name": "Advanced Features",
      "setup": "",
      "run": "python -m pytest test_advanced.py -v",
      "input": "",
      "output": "",
      "comparison": "included",
      "timeout": 10,
      "points": 30
    },
    {
      "name": "Code Style",
      "setup": "pip install ruff",
      "run": "ruff check . --exit-zero",
      "input": "",
      "output": "",
      "comparison": "included",
      "timeout": 5,
      "points": 10
    },
    {
      "name": "Documentation",
      "setup": "",
      "run": "python check_docs.py",
      "input": "",
      "output": "",
      "comparison": "included",
      "timeout": 5,
      "points": 20
    }
  ]
}
```

### Custom Test Scripts

`check_docs.py`:
```python
#!/usr/bin/env python3
"""Check for proper documentation"""

import ast
import sys

def check_docstrings(filename):
    with open(filename, 'r') as f:
        tree = ast.parse(f.read())
    
    missing = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            if not ast.get_docstring(node):
                missing.append(node.name)
    
    if missing:
        print(f"Missing docstrings: {', '.join(missing)}")
        sys.exit(1)
    else:
        print("All functions/classes have docstrings ✓")

if __name__ == "__main__":
    check_docstrings("contact_manager.py")
```

## Student Workflow

### Instructions for Students

Create `STUDENT_GUIDE.md`:

```markdown
# How to Submit Assignments

## 1. Accept Assignment
- Click the GitHub Classroom link in the assignment description
- Accept the assignment (creates your personal repository)
- Clone your repository:
  ```bash
  git clone https://github.com/AP2025-UNIL/week3-python-basics-YOUR_USERNAME.git
  cd week3-python-basics-YOUR_USERNAME
  ```

## 2. Complete the Assignment
- Read README.md for instructions
- Complete all TODOs in the code
- Run tests locally:
  ```bash
  python -m pytest test_basic.py -v
  ```
- Check code style:
  ```bash
  ruff check .
  ```

## 3. Submit Your Work
- Commit your changes:
  ```bash
  git add .
  git commit -m "Complete Week 3 assignment"
  git push origin main
  ```
- Check GitHub Actions tab for test results
- Green checkmark = all tests pass!

## 4. Get Help
- Check test output for hints
- Ask in course Discord/forum
- Office hours: Wednesdays 2-4 PM
```

## Grading Workflow

### Bulk Download Script

`download_submissions.sh`:
```bash
#!/bin/bash
# Download all submissions for grading

ASSIGNMENT="week3-python-basics"
ORG="AP2025-UNIL"
OUTPUT_DIR="submissions/$ASSIGNMENT"

mkdir -p $OUTPUT_DIR

# Get list of repos
gh repo list $ORG --limit 1000 --json name \
  | jq -r '.[] | select(.name | startswith("'$ASSIGNMENT'")) | .name' \
  | while read repo; do
    echo "Cloning $repo..."
    git clone "git@github.com:$ORG/$repo.git" "$OUTPUT_DIR/$repo"
  done

echo "Downloaded $(ls -1 $OUTPUT_DIR | wc -l) submissions"
```

### Grading Rubric Template

`grading_rubric.md`:
```markdown
# Grading Rubric - [Assignment Name]

Student: _______________
GitHub Username: _______________

## Automated Tests (60 points)
- [ ] Basic functionality (30 pts): _____
- [ ] Advanced features (20 pts): _____
- [ ] Code style (10 pts): _____

## Manual Review (40 points)
- [ ] Code organization (10 pts): _____
- [ ] Documentation (10 pts): _____
- [ ] Error handling (10 pts): _____
- [ ] Creativity/extras (10 pts): _____

## Comments:
```
[Space for feedback]
```

## Total: _____ / 100

## Feedback Submitted: [ ]
```

### Batch Feedback Script

`provide_feedback.py`:
```python
#!/usr/bin/env python3
"""Provide feedback via GitHub issues"""

import os
from github import Github

# Setup
g = Github("YOUR_GITHUB_TOKEN")
org = g.get_organization("AP2025-UNIL")

def provide_feedback(repo_name, grade, feedback):
    repo = org.get_repo(repo_name)
    
    # Create issue with feedback
    issue_title = f"Assignment Feedback - Grade: {grade}/100"
    issue_body = f"""
## Grade: {grade}/100

### Automated Tests
{feedback['tests']}

### Code Review
{feedback['review']}

### Suggestions for Improvement
{feedback['suggestions']}

---
*If you have questions about this feedback, please reply to this issue.*
"""
    
    repo.create_issue(title=issue_title, body=issue_body)
    print(f"Feedback provided for {repo_name}")

# Example usage
feedback = {
    'tests': "All tests passed! Great job.",
    'review': "Code is well-organized and documented.",
    'suggestions': "Consider adding more error handling."
}

provide_feedback("week3-python-basics-alice-gh", 95, feedback)
```

## Assignment Schedule

| Week | Regular Assignment | Advanced (Bonus) | Points |
|------|-------------------|------------------|--------|
| 1 | Git Basics | Git Collaboration Challenge | 100 + 150 |
| 2 | (Holiday - Self Study) | - | - |
| 3 | Python Basics | Text Adventure Game | 100 + 150 |
| 4 | Functions & Data | Data Analysis Toolkit | 100 + 150 |
| 5 | AI Tools Practice | AI Engineering Challenge | 100 + 150 |
| 6 | OOP & Debugging | City Simulation Engine | 100 + 150 |

## Troubleshooting

### Common Issues

#### 1. Students Can't Push Code
```bash
# Check repository permissions
Settings → Manage Access → Ensure student has write access

# Common fix:
git remote set-url origin https://github.com/AP2025-UNIL/repo-name.git
```

#### 2. Autograding Not Running
- Check Actions are enabled in repository settings
- Verify workflow file is in `.github/workflows/`
- Check for syntax errors in YAML

#### 3. Tests Pass Locally but Fail on GitHub
- Version mismatch (specify exact Python version)
- Missing dependencies in requirements.txt
- File path issues (use relative paths)

### Support Resources

- [GitHub Classroom Documentation](https://docs.github.com/en/education/manage-coursework-with-github-classroom)
- [GitHub Actions for Testing](https://docs.github.com/en/actions/automating-builds-and-tests)
- [Autograding Guide](https://docs.github.com/en/education/manage-coursework-with-github-classroom/teach-with-github-classroom/use-autograding)

## Best Practices

### For Instructors

1. **Test Everything First**: Complete assignment yourself before releasing
2. **Provide Clear Instructions**: Include examples and expected output
3. **Gradual Complexity**: Start simple, increase difficulty
4. **Fast Feedback**: Use autograding for immediate feedback
5. **Office Hours**: Schedule around deadline times

### For Students

1. **Start Early**: Don't wait until deadline
2. **Commit Often**: Save progress frequently
3. **Read Tests**: Tests show expected behavior
4. **Ask Questions**: Use issues/discussions
5. **Learn from Feedback**: Review comments carefully

## Security Considerations

### Repository Settings
```yaml
Visibility: Private (always for student work)
Branch Protection: Protect main after deadline
Actions: Limit to verified actions
Secrets: Never commit API keys or passwords
```

### Code Review Checklist
- No hardcoded credentials
- No infinite loops in tests
- Resource limits on autograding
- Sanitize student input in scripts

---

## Quick Start Checklist

- [ ] Create GitHub organization
- [ ] Setup GitHub Classroom
- [ ] Add TAs and permissions
- [ ] Create starter repositories
- [ ] Configure autograding
- [ ] Test student workflow
- [ ] Prepare grading tools
- [ ] Write student guide
- [ ] Schedule assignments
- [ ] Monitor and support

---

*Last updated: September 2025*
*Contact: anna.smirnova@unil.ch*