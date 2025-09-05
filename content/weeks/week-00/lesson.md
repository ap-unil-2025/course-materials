---
layout: lesson
title: "Course Overview & Essential Tools Setup"
week: 0
date: 2025-09-15
type: "introduction"
topics:
  - Introduction to the course
  - Structure, grading, and capstone project
  - Introduction to Nuvolos cloud computing platform
  - Unix/Linux basics and advanced commands
  - Python environment setup
slides: "/slides/practice/week00_slides.html"
code_examples: 
  - environment-setup.sh
summary: "Introduction to Data Science and Advanced Programming course structure, Nuvolos platform, Unix/Linux fundamentals, and Python environment configuration."
---

# Introduction to Data Science and Advanced Programming

HEC Lausanne, Fall Semester 2025

This introductory lesson covers the course structure, learning objectives, and introduces essential tools including the Nuvolos cloud platform and Unix/Linux basics.

## Learning Objectives

By the end of this lesson, you will:

- Understand the course structure, grading, and capstone project requirements
- Access and navigate the Nuvolos cloud computing platform
- Execute basic Unix/Linux commands for file management
- Be familiar with the course website and resources

## Course Overview

This advanced course introduces students to the Python programming language, core concepts of statistical learning, and high-performance computing. It is designed for Master's students in Economics and Finance to build the computational and analytical skills necessary for modern quantitative analysis.

### Course Structure
- Three 45-minute lecture sessions per week
- One 45-minute hands-on session per week  
- Meeting time: Mondays, 12:30–16:00
- Location: Internef 263

### Key Learning Path
**Part I: Python Foundations (Weeks 1–6)**
- Python programming fundamentals
- Scientific computing with NumPy and Pandas
- Data visualization
- Generative AI for programming

**Part II: Statistical Learning (Weeks 7–12)**
- Statistical learning framework
- Regression and classification
- Model validation and regularization
- Tree-based methods and unsupervised learning

**Part III: Advanced Programming & HPC (Weeks 13-14)**
- High-performance computing techniques
- Deep learning primer
- Capstone project presentations

## Grading and Assessment

- **Capstone Project (Primary Assessment)**: Demonstrates understanding of course material
  - 10-page report
  - GitHub repository with code and data
  - 10-minute video presentation
- **Bonus Points**: Available through homework assignments
- **No Exams**: Assessment is project-based

## Nuvolos Cloud Computing Platform

### What is Nuvolos?
- Cloud-based computing environment for data science
- Pre-configured with Python, R, and essential libraries
- Collaborative workspace for academic research
- Access from anywhere with internet connection

### Getting Started with Nuvolos
1. **Enrollment**: Use the [enrollment key](https://app.nuvolos.cloud/enroll/class/RshD654gzU4) 
2. **First Login**: Follow setup instructions
3. **Navigation**: Familiarize yourself with the interface
4. **File Management**: Understand workspace organization

### Nuvolos Features
- **Jupyter Notebooks**: Interactive computing environment
- **Terminal Access**: Command-line interface
- **Collaboration Tools**: Share code and datasets
- **Version Control**: Built-in Git integration
- **Computing Resources**: Scalable computational power

## Unix/Linux Basics

### Why Learn Unix/Linux?
- **Cloud Computing**: Most cloud platforms use Linux
- **Research Computing**: HPC clusters run Unix/Linux
- **Data Science**: Many tools designed for Unix environments
- **Professional Skills**: Essential for modern data scientists

### Essential Commands
```bash
# Navigation
pwd         # Print working directory
ls          # List files and directories
cd          # Change directory

# File Operations
mkdir       # Create directory
cp          # Copy files
mv          # Move/rename files
rm          # Remove files

# Viewing Files
cat         # Display file contents
head        # Show first lines
tail        # Show last lines
less        # Page through files
```

### Hands-on Unix Practice
1. **Navigate the file system**
   ```bash
   pwd                    # Where am I?
   ls -la                 # What's here?
   cd /home/username      # Go to home directory
   ```

2. **Create and organize files**
   ```bash
   mkdir my_project       # Create project directory
   cd my_project          # Enter directory
   touch data.txt         # Create empty file
   ```

3. **File management**
   ```bash
   cp data.txt backup.txt     # Copy file
   mv backup.txt old_data.txt # Rename file
   rm old_data.txt            # Delete file
   ```

## Resources and Support

- **Course Website**: [Course Materials](https://ap-unil-2025.github.io/course-materials/)
- **Nuvolos Platform**: [nuvolos.cloud](https://nuvolos.cloud/)
- **Nuvolos Support**: support@nuvolos.cloud
- **TA Support**: Anna Smirnova (anna.smirnova@unil.ch)
- **QA Sessions**: [Google Doc](https://docs.google.com/spreadsheets/d/1JnbT8enDgKhR6Rfje0CjtCyMwWXdHXim4iZMpn0QE-A/edit#gid=0)

## Getting Started Checklist

1. **Enroll in Nuvolos** using the provided link
2. **Complete Unix/Linux tutorial** on the platform
3. **Explore the course website** and syllabus
4. **Set up your workspace** in Nuvolos
5. **Test basic commands** in the terminal

## Next Steps

Next week we'll continue with essential tools including Git version control, Python environment setup, and research programming workflows.