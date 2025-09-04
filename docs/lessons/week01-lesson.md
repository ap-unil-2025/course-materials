---
layout: lesson
title: "Essential Tools Setup & Unix/Linux Continuation"
week: 1
date: 2025-09-15
type: "hands-on"
topics:
  - Advanced Unix/Linux commands
  - Git version control fundamentals
  - Python environment setup
  - Nuvolos platform workflows
slides: "/slides/practice/week01_slides.html"
code_examples: 
  - git-basics.py
  - environment-setup.sh
summary: "Continuation of course setup with advanced Unix/Linux, Git fundamentals, and Python environment configuration on Nuvolos platform."
---

# Essential Tools Setup & Unix/Linux Continuation

This lesson builds on Week 0's introduction by diving deeper into Unix/Linux commands, introducing Git version control, and setting up Python development environments on the Nuvolos platform.

## Learning Objectives

By the end of this lesson, you will:

- Master advanced Unix/Linux commands for file manipulation and system navigation
- Use Git for version control of your research code
- Set up Python development environments on Nuvolos
- Create reproducible research workflows using cloud tools
- Integrate Unix/Linux, Git, and Python for efficient data science workflows

## Advanced Unix/Linux Commands

Building on Week 0's basics, let's explore more powerful Unix/Linux commands essential for data science work.

### Advanced File Operations
```bash
# Find files and directories
find . -name "*.csv"           # Find all CSV files
find . -type f -size +1M       # Find files larger than 1MB
locate filename                # Quick file location

# Text processing
grep "pattern" file.txt        # Search for patterns in files
grep -r "function" .           # Recursively search in directories  
sed 's/old/new/g' file.txt     # Replace text in files
awk '{print $1}' data.txt      # Extract columns from data

# File compression and archives
tar -czf archive.tar.gz dir/   # Create compressed archive
tar -xzf archive.tar.gz        # Extract archive
zip -r backup.zip project/     # Create zip archive
```

### Process and System Management
```bash
# Process management
ps aux                         # List all running processes
top                           # Monitor system resources
htop                          # Enhanced process monitor
kill PID                      # Terminate process by ID

# Disk usage and system info
df -h                         # Disk space usage
du -sh *                      # Directory sizes
free -h                       # Memory usage
uname -a                      # System information
```

### Advanced Navigation and Shortcuts
```bash
# Command history
history                       # View command history
!!                           # Repeat last command
!n                           # Repeat command number n
Ctrl+R                       # Search command history

# File permissions
chmod 755 script.py          # Set executable permissions
chmod +x script.py           # Make file executable
chown user:group file.txt    # Change ownership

# Pipes and redirection
ls -la | grep ".py"          # Filter output
python script.py > output.txt    # Redirect output to file
python script.py 2>&1 | tee log.txt    # Log both output and errors
```

### 2. Git Version Control
Git tracks changes in your code and enables collaboration.

**Basic Workflow:**
```bash
# Initialize repository
git init

# Track changes
git add .
git commit -m "Descriptive message"

# Sync with remote
git push origin main
git pull origin main
```

### 3. Python Environment Management
Professional Python development requires proper environment management.

**Using UV (recommended):**
```bash
# Create virtual environment
uv venv .venv

# Activate environment
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows

# Install packages
uv pip install package-name
```

## Hands-on Activities

### Activity 1: Command Line Navigation
1. Open your terminal
2. Navigate to your Documents folder
3. Create a new directory called `research-projects`
4. List the contents to verify creation

### Activity 2: First Git Repository
1. Initialize a Git repository in your project folder
2. Create a simple Python file
3. Add and commit your changes
4. Check the commit history

### Activity 3: Nuvolos Workspace Setup
1. Create a project workspace in Nuvolos
2. Set up Python environment with required packages
3. Test Git integration within Nuvolos
4. Create your first Jupyter notebook

## Integrated Nuvolos Workflow

### Working with Nuvolos Platform
1. **Project Organization**: Use Nuvolos workspace structure
2. **Version Control**: Integrate Git within Nuvolos environment  
3. **Environment Management**: Leverage pre-configured Python environments
4. **Collaboration**: Share workspaces with team members
5. **Resource Scaling**: Use cloud computing resources as needed

### Research Programming Workflow
1. **Project Setup**: Create organized directory structure in Nuvolos
2. **Version Control**: Initialize Git repository (local and remote)
3. **Environment**: Configure Python packages for your project
4. **Development**: Write code with proper documentation using Jupyter
5. **Testing**: Validate your code works correctly
6. **Collaboration**: Share via Nuvolos and push to GitHub

## Code Examples

See the accompanying code examples for practical implementations:
- `git-basics.py`: Common Git operations in Python
- `environment-setup.sh`: Automated environment setup script

## Resources

- **Slides**: [Session 1 Slides]({{ page.slides }})
- **Git Documentation**: [git-scm.com](https://git-scm.com/doc)
- **UV Documentation**: [astral.sh/uv](https://docs.astral.sh/uv/)
- **Command Line Cheat Sheet**: Available in course materials

## Troubleshooting

**Common Issues:**
- Git permission errors: Check SSH key setup
- Python environment conflicts: Use virtual environments
- Command not found: Verify software installation

## Assessment

This lesson contributes to:
- Assignment 1: Git Basics
- Final project setup and version control

## Next Steps

Continue with the next lesson to build on these foundational tools.