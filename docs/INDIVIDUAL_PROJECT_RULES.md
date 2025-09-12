---
layout: page
title: "Individual Project Guidelines"
subtitle: "Final project requirements for Advanced Programming Spring 2025"
---

# INDIVIDUAL PROJECT GUIDELINES
Advanced Programming · Fall 2025 HEC Lausanne

> **Important:** These guidelines outline the requirements for your individual programming project.
> The project demonstrates your ability to apply programming concepts learned throughout the course.

---

## Quick Overview
1. [Project Scope & Options](#1--project-scope--options)
2. [Deliverables](#2--deliverables)
3. [Technical Requirements](#3--technical-requirements)
4. [Timeline & Milestones](#4--timeline--milestones)
5. [Grading Criteria](#5--grading-criteria)
6. [AI Tool Usage](#6--ai-tool-usage)
7. [Academic Integrity](#7--academic-integrity)
8. [Support & Help](#8--support--help)

---

## 1 · Project Scope & Options

### Choose One Project Type:

#### Option A: Data Analysis Project
* Analyze a real-world dataset using Python
* Apply pandas, NumPy, and visualization techniques
* Examples: Economic indicators analysis, stock market trends, climate data patterns

#### Option B: Interactive Application
* Create a command-line tool or simple GUI application
* Examples: Personal finance calculator, text-based game, task manager, data converter

#### Option C: Statistical/Scientific Computing
* Implement statistical methods or scientific algorithms
* Examples: Monte Carlo simulation, optimization solver, statistical test suite

#### Option D: Web Scraping & API Project
* Collect and process data from web sources
* Examples: News aggregator, price tracker, social media analyzer

### Project Scope Requirements:
* **Individual work only** - no teams
* **Manageable scope** - should be completable in 4-6 weeks of part-time work
* **Original code** - while you can use libraries, the core logic should be yours
* **Practical application** - solve a real problem or provide useful functionality

---

## 2 · Deliverables

### Required Components:

1. **GitHub Repository**
   - Well-organized code with clear file structure
   - README with installation and usage instructions
   - At least 10 meaningful commits showing project evolution

2. **Working Software**
   - Executable Python program
   - Handles basic error cases
   - Provides user documentation (--help or README)

3. **Project Report** (10 pages)
   - Project description and objectives
   - Technical approach and design decisions
   - Key challenges and how you solved them
   - Testing approach and results
   - Reflection on what you learned

4. **Video Recording** (max 10 minutes)
   - Present your project and findings
   - Demonstrate key functionality
   - Explain technical decisions

4. **Code Documentation**
   - Docstrings for all major functions
   - Comments for complex logic
   - Type hints where appropriate

---

## 3 · Technical Requirements

### Minimum Requirements:

| Component | Requirement |
|-----------|-------------|
| **Python Version** | Python 3.8+ |
| **Code Organization** | Logical file structure with separate modules |
| **External Libraries** | Appropriate use of course-covered libraries (pandas, NumPy, etc.) |
| **Error Handling** | Basic try/except blocks for user inputs and file operations |
| **Testing** | At least 5 test cases using pytest or unittest |
| **Code Style** | Consistent formatting (PEP 8 recommended) |
| **Version Control** | Regular commits with descriptive messages |

### Recommended Project Structure:
```
project-name/
├── README.md           # Project description and usage
├── requirements.txt    # Python dependencies
├── main.py            # Main entry point
├── src/               # Source code modules
│   ├── __init__.py
│   └── ...
├── tests/             # Test files
│   └── test_*.py
├── data/              # Sample data (if applicable)
└── docs/              # Additional documentation
```

### Good Practices (Bonus Points):

* **Clean Code**
  - Meaningful variable names
  - Functions under 30 lines
  - DRY principle (Don't Repeat Yourself)

* **Documentation**
  - Clear README with examples
  - Inline comments for complex logic
  - Docstrings following NumPy/Google style

* **Testing**
  - Unit tests for core functions
  - Edge case handling
  - Test coverage > 60%

* **Advanced Features** (optional)
  - Command-line arguments (argparse)
  - Configuration files
  - Logging instead of print statements
  - Type hints
  - Basic CI/CD with GitHub Actions

---

## 4 · Timeline & Milestones

| Week | Date | Milestone | Description |
|------|------|-----------|-------------|
| **Week 8** | Nov 3 | Project Proposal | Submit 1-paragraph project description |
| **Week 9** | Nov 10 | Initial Implementation | Core functionality working |
| **Week 10** | Nov 17 | Feature Complete | All planned features implemented |
| **Week 11** | Nov 24 | Testing & Documentation | Tests written, documentation complete |
| **Week 13** | Dec 8 | Final Submission | Repository finalized, report submitted |
| **Week 14** | Dec 15 | Presentations | Project presentations (voluntary) |

---

## 5 · Grading Criteria

### Grade Distribution (100 points total):

| Category | Points | Description |
|----------|--------|-------------|
| **Functionality** | 30 | Program works as intended, handles errors gracefully |
| **Code Quality** | 25 | Clean, readable, well-organized code |
| **Documentation** | 15 | Clear README, docstrings, and comments |
| **Testing** | 15 | Appropriate test cases that verify functionality |
| **Project Report** | 10 | Clear explanation of project and technical decisions |
| **Version Control** | 5 | Regular commits with meaningful messages |

### Grade Boundaries:
- **90-100**: Excellent (5.5-6.0)
- **75-89**: Good (4.5-5.4)
- **60-74**: Satisfactory (4.0-4.4)
- **< 60**: Needs Improvement

---

## 6 · AI Tool Usage

### Encouraged Use:
- **Learning aid**: Use AI to understand concepts and debug
- **Code assistance**: Get help with syntax and library usage
- **Documentation**: Generate docstrings and comments

### Required Disclosure:
- Create an `AI_USAGE.md` file listing significant AI contributions
- Include brief description of what AI helped with
- Be prepared to explain any AI-assisted code

### Not Allowed:
- Submitting entirely AI-generated projects
- Using AI to complete assignments without understanding
- Copying AI code without comprehension

Remember: You must understand and be able to explain all code in your project!

---

## 7 · Academic Integrity

### Expected:
- **Original work**: Your project should be primarily your own code
- **Proper attribution**: Credit all external sources and libraries
- **Understanding**: Be able to explain every line of your code

### Forbidden:
- Submitting others' work as your own
- Copying projects from online sources
- Sharing code with other students (discussion is OK, copying is not)

### Consequences:
- Plagiarism will result in project failure
- University academic integrity policies apply

---

## 8 · Support & Help

### Available Resources:

1. **Weekly TA Sessions**
   - Project help during practice sessions
   - Code review and debugging assistance

2. **Online Resources**
   - Course website with examples
   - Recommended tutorials and documentation

3. **Communication**
   - Course forum for questions
   - Email TAs for specific issues

4. **Office Hours**
   - Schedule via email with 48h notice
   - Bring specific questions or code issues

### Submission Guidelines:

1. **GitHub Repository**: Share repository link via course submission system
2. **Project Report**: Submit PDF (10 pages) separately
3. **Video Recording**: Submit video file (max 10 minutes)
4. **Deadline**: December 8, 2025 (Week 13)

### Late Policy:
- Up to 24 hours late: -10% penalty
- Up to 48 hours late: -20% penalty
- Beyond 48 hours: Not accepted without valid excuse

---

## Tips for Success

1. **Start Early**: Don't wait until the last week
2. **Plan First**: Outline your project before coding
3. **Iterate**: Start simple, then add features
4. **Test Often**: Write tests as you develop
5. **Commit Regularly**: Use version control throughout
6. **Ask for Help**: Don't struggle alone - use available resources
7. **Document as You Go**: Don't leave documentation for the end

---

## Example Project Ideas

### Data Analysis
- **Economic Dashboard**: Analyze and visualize economic indicators
- **Portfolio Analyzer**: Track and analyze investment performance
- **Weather Pattern Analysis**: Study climate data trends
- **Sports Statistics**: Analyze team or player performance

### Applications
- **Budget Tracker**: Personal finance management tool
- **Study Timer**: Pomodoro technique implementation
- **Password Manager**: Simple encrypted password storage
- **File Organizer**: Automated file sorting system

### Scientific Computing
- **Option Pricing Calculator**: Implement Black-Scholes model
- **Population Simulation**: Model population dynamics
- **Optimization Solver**: Implement linear programming
- **Statistical Calculator**: Various statistical tests

### Web & API Projects
- **News Summarizer**: Aggregate and summarize news articles
- **Currency Converter**: Real-time exchange rates
- **GitHub Stats**: Analyze repository statistics
- **Weather App**: Fetch and display weather data

---

> **Note:** These guidelines align with the capstone project requirements.
> Students who volunteer may present their projects in Week 14 (December 15, 2025).
> There are no exams - your grade is based entirely on the capstone project.