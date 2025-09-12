---
layout: assignment
title: "Week 0-1: Environment Setup & Unix/Git Fundamentals"
assignment_number: 1
due_date: 2025-09-22 23:59:00
points: 50
difficulty: "Beginner"
estimated_time: "3-4 hours"
topics:
  - "Development Environment"
  - "Unix/Linux Commands"
  - "Git Version Control"
  - "Python Installation"
status: "open"
---

## Overview

Set up your development environment and master fundamental tools for the course. This assignment ensures everyone has a working setup and understands basic Unix/Git operations essential for all future work.

## Learning Objectives

By completing this assignment, you will:

- Configure a complete Python development environment
- Master essential Unix/Linux commands
- Understand Git version control basics
- Set up VS Code or preferred IDE
- Create and manage a GitHub repository

## Part 1: Environment Setup (15 points)

### 1.1 Python Installation (5 points)

Install Python 3.11 or later and verify:

```bash
python3 --version  # Should show 3.11.x or higher
pip3 --version     # Package manager
```

Create a test script `hello_world.py`:
```python
import sys
import platform

print(f"Python version: {sys.version}")
print(f"Platform: {platform.platform()}")
print(f"Machine: {platform.machine()}")
print("Hello, Advanced Programming 2025!")
```

### 1.2 Development Tools (5 points)

Install and configure:
- **VS Code** (or your preferred IDE)
- **Git** (version 2.30+)
- **Python extensions** for your IDE
- **pytest** for testing: `pip install pytest`

### 1.3 Virtual Environment (5 points)

Create and activate a virtual environment:

```bash
# Create virtual environment
python3 -m venv ap2025_env

# Activate (Unix/Mac)
source ap2025_env/bin/activate

# Activate (Windows)
ap2025_env\Scripts\activate

# Install required packages
pip install pytest numpy pandas matplotlib jupyter
```

Create `requirements.txt` with your installed packages:
```bash
pip freeze > requirements.txt
```

## Part 2: Unix/Linux Commands (15 points)

### 2.1 Basic Navigation (5 points)

Create a script `unix_practice.sh` that demonstrates:

```bash
#!/bin/bash

# Your name and date
echo "Name: [Your Name]"
echo "Date: $(date)"

# Create directory structure
mkdir -p ap2025/projects ap2025/assignments ap2025/notes

# Navigate and list contents
cd ap2025
ls -la

# Create sample files
touch projects/README.md
echo "Advanced Programming 2025" > notes/course_info.txt

# Display file contents
cat notes/course_info.txt

# Show current path
pwd
```

### 2.2 File Operations (5 points)

Extend your script to:
- Copy files between directories
- Move and rename files
- Search for files using `find`
- Search within files using `grep`
- Display file permissions
- Change file permissions with `chmod`

### 2.3 Process Management (5 points)

Add commands to:
- List running processes (`ps aux`)
- Check system resources (`top` or `htop`)
- Check disk usage (`df -h`)
- Find your username (`whoami`)
- Display system information (`uname -a`)

## Part 3: Git Fundamentals (20 points)

### 3.1 Repository Setup (7 points)

Create a new Git repository:

```bash
mkdir ap2025-assignment1
cd ap2025-assignment1
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

Create `.gitignore`:
```
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

### 3.2 Basic Git Workflow (8 points)

Demonstrate Git operations in a script `git_practice.py`:

```python
import subprocess
import os

def run_command(cmd):
    """Run shell command and return output"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

# Initialize repository (if not already done)
print("Initializing Git repository...")
print(run_command("git init"))

# Create files
with open("README.md", "w") as f:
    f.write("# AP2025 Assignment 1\n\nEnvironment setup and Git practice\n")

with open("main.py", "w") as f:
    f.write('print("Hello from main.py")\n')

# Stage and commit
print("\nStaging files...")
print(run_command("git add ."))
print(run_command('git commit -m "Initial commit"'))

# Show status and log
print("\nGit status:")
print(run_command("git status"))
print("\nGit log:")
print(run_command("git log --oneline"))
```

### 3.3 GitHub Integration (5 points)

1. Create a GitHub repository named `ap2025-[your-username]`
2. Add remote origin:
   ```bash
   git remote add origin https://github.com/[username]/ap2025-[username].git
   ```
3. Push your code:
   ```bash
   git push -u origin main
   ```
4. Create a `workflow_log.txt` documenting all Git commands used

## Part 4: Integration Project (Bonus: 10 points)

Create a Python script `system_info.py` that:

```python
#!/usr/bin/env python3
"""
System Information Reporter
Combines Unix commands with Python to generate a system report
"""

import subprocess
import platform
import os
import json
from datetime import datetime

class SystemInfo:
    def __init__(self):
        self.info = {}
        
    def get_python_info(self):
        """Gather Python environment information"""
        # Add implementation
        
    def get_git_info(self):
        """Get Git configuration and repository status"""
        # Add implementation
        
    def get_system_info(self):
        """Gather system information using Unix commands"""
        # Add implementation
        
    def generate_report(self, format='json'):
        """Generate report in specified format"""
        # Add implementation

if __name__ == "__main__":
    reporter = SystemInfo()
    # Generate and save report
```

## Submission Requirements

Submit a ZIP file containing:

```
assignment1/
├── hello_world.py          # Python test script
├── requirements.txt        # Package list
├── unix_practice.sh        # Unix commands script
├── git_practice.py         # Git demonstration
├── workflow_log.txt        # Git commands used
├── system_info.py          # Bonus: Integration project
├── .gitignore             # Git ignore file
├── README.md              # Project description
└── screenshots/           # Screenshots of:
    ├── terminal_setup.png # Terminal showing Python version
    ├── vscode_setup.png   # IDE configuration
    └── github_repo.png    # Your GitHub repository
```

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| **Environment Setup** | 15 | Python, IDE, virtual environment working |
| **Unix Commands** | 15 | All scripts execute correctly |
| **Git Operations** | 20 | Repository created, commits made, GitHub integration |
| **Bonus Project** | +10 | System info script works |
| **Total** | 50 (+10) | |

### Deductions
- Missing screenshots: -3 points
- Scripts don't execute: -5 points
- No GitHub repository: -5 points

## Verification Checklist

Before submitting, ensure:

- [ ] Python 3.11+ is installed
- [ ] Virtual environment activates correctly
- [ ] All required packages are installed
- [ ] Unix script runs without errors
- [ ] Git repository has at least 3 commits
- [ ] Code is pushed to GitHub
- [ ] All files are included in submission

## Troubleshooting

### Common Issues:

**Python not found:**
- Check PATH environment variable
- Try `python` instead of `python3`

**Permission denied for scripts:**
```bash
chmod +x unix_practice.sh
```

**Git push fails:**
- Check remote URL: `git remote -v`
- Ensure you're logged into GitHub
- Try HTTPS instead of SSH

**Virtual environment issues:**
- Deactivate and reactivate
- Delete and recreate if corrupted

## Resources

- [Python Installation Guide](https://www.python.org/downloads/)
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Unix Command Reference](https://ss64.com/bash/)
- [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)

## Questions?

Post on the course forum with the tag `#setup-help` or attend office hours. Don't hesitate to ask for help with environment setup - it's crucial for the rest of the course!