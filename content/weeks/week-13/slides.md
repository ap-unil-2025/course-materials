---
marp: true
paginate: true
header: "Session 13: Final Project Workshop"
footer: "Anna Smirnova, December 15, 2025"
style: |
  section.lead {
    background: #003aff;
    color: white;
  }
    section.lead footer {
    color: white;
  }
  section.lead header {
    color: white;
  }
  section.lead h1, section.lead h2, section.lead h3 {
    color: white;
    border-bottom: none;
  }
  section.lead a {
    color: white;
  }
---

<!-- _class: lead -->

# Session 13: Final Project Workshop

**Bringing It All Together**

---

# Today's Goals

**Part 1: Final Project Overview**
- Project requirements
- Dataset selection
- Scope and timeline

**Part 2: Technical Review**
- Recap of course concepts
- Common pitfalls
- Best practices checklist

**Part 3: Working Session**
- Individual consultation
- Peer feedback
- Q&A

---

# Part 1: Final Project Overview

---

# Project Requirements

**Create a complete data analysis project** that demonstrates:

1. **Python fundamentals**: Functions, classes, error handling
2. **Data manipulation**: NumPy and Pandas
3. **Visualization**: Matplotlib/Seaborn
4. **Documentation**: Professional report
5. **Project structure**: Organized code

**Deliverable**: A complete, reproducible analysis

---

# Project Structure

```
final-project/
├── README.md                 # Project overview
├── requirements.txt          # Dependencies
├── data/
│   ├── raw/                 # Original data
│   └── processed/           # Cleaned data
├── notebooks/
│   ├── 01_exploration.ipynb # Initial analysis
│   └── 02_analysis.ipynb    # Main analysis
├── src/                     # Python modules (optional)
│   ├── __init__.py
│   └── utils.py            # Helper functions
└── reports/
    ├── report.html         # Exported report
    └── figures/            # Saved visualizations
```

---

# Choosing a Dataset

**Good sources**:
- [Kaggle](https://kaggle.com/datasets) - Curated datasets
- [Data.gov](https://data.gov) - US government data
- [UCI ML Repository](https://archive.ics.uci.edu/ml) - Classic datasets
- [Our World in Data](https://ourworldindata.org) - Global statistics
- [Eurostat](https://ec.europa.eu/eurostat) - European data
- Your own field's repositories

**Criteria**:
- ✅ Tabular data (CSV, Excel)
- ✅ 1000+ rows (but not millions)
- ✅ Multiple variables
- ✅ Interesting to you!

---

# Dataset Examples by Interest

**Economics/Finance**:
- World Bank economic indicators
- Stock market data
- Income inequality data
- Trade statistics

**Social Sciences**:
- Survey data (happiness, demographics)
- Education statistics
- Crime data
- Health outcomes

**Environmental**:
- Climate data
- Energy consumption
- Air quality
- Biodiversity

**General**:
- Sports statistics
- Movie/book ratings
- Transportation data
- Social media trends

---

# Project Scope

**Too small**:
❌ "Calculate the average of a column"
❌ "Make one scatter plot"

**Too large**:
❌ "Build a machine learning model with 20 features"
❌ "Analyze 10 years of data across 50 countries"

**Just right**:
✅ "Analyze sales trends by region and identify key drivers"
✅ "Explore relationship between education and income across countries"
✅ "Compare COVID-19 response effectiveness across European nations"

**Rule of thumb**: Can be completed in 10-15 hours

---

# Analysis Questions

Your project should answer **2-4 specific questions**, such as:

**Example: Housing Prices**
1. How do house prices vary by neighborhood?
2. What factors (size, bedrooms, age) most influence price?
3. Are prices increasing or decreasing over time?

**Example: Sales Data**
1. Which products are top performers?
2. Are there seasonal patterns in sales?
3. How does customer age affect purchase behavior?

**Example: Health Data**
1. What factors correlate with life expectancy?
2. How has life expectancy changed over time?
3. Are there regional differences in health outcomes?

---

# Timeline

**Week 13 (Today)**:
- [ ] Choose dataset
- [ ] Define 2-4 analysis questions
- [ ] Set up project structure
- [ ] Start exploratory analysis

**Week 14** (if applicable):
- [ ] Complete main analysis
- [ ] Create visualizations
- [ ] Write report
- [ ] Prepare presentation (5-10 minutes)

**Submission**:
- [ ] Complete project on GitHub/submitted
- [ ] Presentation ready

---

# Part 2: Technical Review

---

# Course Concepts Recap

**Weeks 1-4: Python Fundamentals**
- Variables, data types, control flow
- Functions and modules
- Lists, dictionaries
- File I/O

**Weeks 5-8: Advanced Python**
- OOP (classes, inheritance)
- Debugging and error handling
- Project structure and dependencies

**Weeks 9-12: Data Science**
- NumPy for numerical computing
- Pandas for data manipulation
- Matplotlib/Seaborn for visualization
- Documentation and reporting

---

# Essential Python Review

```python
# Functions
def analyze_sales(data, threshold=100):
    """Calculate metrics for sales above threshold."""
    high_sales = data[data['sales'] > threshold]
    return high_sales.describe()

# Classes
class DataAnalyzer:
    def __init__(self, filename):
        self.data = pd.read_csv(filename)

    def summarize(self):
        return self.data.describe()

# Error handling
try:
    df = pd.read_csv('data.csv')
except FileNotFoundError:
    print("File not found! Check the path.")
except pd.errors.EmptyDataError:
    print("File is empty!")
```

---

# Data Manipulation Essentials

```python
import pandas as pd
import numpy as np

# Loading
df = pd.read_csv('data.csv')

# Cleaning
df = df.dropna()
df = df.drop_duplicates()
df['date'] = pd.to_datetime(df['date'])

# Filtering
high_value = df[df['value'] > 100]
recent = df[df['date'] > '2025-01-01']

# Grouping
by_category = df.groupby('category')['sales'].agg(['sum', 'mean', 'count'])

# Merging
combined = df1.merge(df2, on='id', how='left')
```

---

# Visualization Essentials

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Line plot
plt.plot(x, y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()

# Seaborn
sns.set_theme()
sns.scatterplot(data=df, x='x', y='y', hue='category')
plt.show()

# Subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)
plt.tight_layout()
plt.show()

# Save
plt.savefig('figure.png', dpi=300, bbox_inches='tight')
```

---

# Common Pitfalls & Solutions

**Pitfall 1: Not checking data after loading**
```python
# ❌ Don't do this
df = pd.read_csv('data.csv')
# Immediately start analysis

# ✅ Do this
df = pd.read_csv('data.csv')
print(df.shape)
print(df.info())
print(df.head())
print(df.isnull().sum())
```

**Pitfall 2: Ignoring missing values**
```python
# ❌ Don't do this
mean_value = df['column'].mean()  # NaN if any nulls

# ✅ Do this
df = df.dropna(subset=['column'])
# or
df['column'] = df['column'].fillna(df['column'].mean())
```

---

# Common Pitfalls (cont.)

**Pitfall 3: No error handling**
```python
# ❌ Don't do this
df = pd.read_csv(filename)

# ✅ Do this
try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    print(f"Error: {filename} not found")
    # Handle gracefully
```

**Pitfall 4: Hardcoded paths**
```python
# ❌ Don't do this
df = pd.read_csv('/Users/myname/Desktop/data.csv')

# ✅ Do this
from pathlib import Path
data_path = Path('data/raw/data.csv')
df = pd.read_csv(data_path)
```

---

# Best Practices Checklist

**Code Quality**:
- [ ] Functions for repeated operations
- [ ] Clear variable names
- [ ] Comments explaining why, not what
- [ ] Error handling for file operations

**Analysis**:
- [ ] Data cleaning documented
- [ ] Visualizations have labels and titles
- [ ] Results interpreted, not just shown
- [ ] Assumptions stated clearly

**Documentation**:
- [ ] README with setup instructions
- [ ] Markdown cells between code cells
- [ ] Results explained
- [ ] Conclusions and recommendations

---

# README Template

```markdown
# [Project Title]

## Overview
Brief description of the project and research questions.

## Data
- **Source**: [Link or description]
- **Description**: What the data contains
- **Time period**: When the data covers

## Installation
```bash
uv pip install -r requirements.txt
```

## Usage
```bash
jupyter notebook notebooks/analysis.ipynb
```

## Project Structure
Description of folders and key files

## Findings
Brief summary of key findings

## Author
Your name and contact info
```

---

# Part 3: Working Session

---

# Getting Started Today

**During this session**:

1. **Choose your dataset** (~15 min)
   - Browse dataset sources
   - Select one that interests you
   - Download and verify it loads

2. **Define questions** (~10 min)
   - What do you want to know?
   - Write 2-4 specific questions

3. **Set up structure** (~10 min)
   - Create project folders
   - Initialize notebook
   - Load and explore data

4. **Get feedback** (~remaining time)
   - Individual consultation
   - Peer review
   - Q&A

---

# Dataset Selection Workshop

**Task 1**: Find 2-3 potential datasets

**Evaluate each**:
- Is it tabular data?
- Does it have enough rows/columns?
- Is it clean or messy? (Some mess is OK!)
- Does it interest you?
- Can you answer interesting questions?

**Choose one** and verify:
```python
import pandas as pd
df = pd.read_csv('your_data.csv')
print(df.shape)
print(df.head())
print(df.info())
```

---

# Question Formulation Workshop

**Task 2**: Define your analysis questions

**Good questions are**:
- **Specific**: Not "analyze data" but "compare sales by region"
- **Answerable**: With the data you have
- **Interesting**: To you and potential audience
- **Varied**: Use different analysis types

**Example**:
- Descriptive: "What is the distribution of X?"
- Comparative: "How does X differ between groups?"
- Temporal: "How has X changed over time?"
- Relational: "What factors correlate with X?"

---

# Project Structure Workshop

**Task 3**: Set up your project

```bash
# Create structure
mkdir final-project
cd final-project
mkdir data data/raw notebooks reports

# Create files
touch README.md requirements.txt
touch notebooks/01_exploration.ipynb

# Initialize git (optional but recommended)
git init
```

**Add initial content**:
- README with project description
- requirements.txt with dependencies
- First notebook with data loading

---

# Initial Analysis Checklist

In your first notebook, include:

- [ ] Import statements
- [ ] Load data
- [ ] Check shape and types
- [ ] Display first few rows
- [ ] Check for missing values
- [ ] Basic statistics (`.describe()`)
- [ ] Initial observations in markdown

**This should take ~30 minutes**

---

# Common Questions

**Q: My dataset is too large for Pandas**
A: Sample it! `df.sample(n=10000)` or use only recent years

**Q: My data is messy**
A: Perfect! Show your cleaning process in the report

**Q: I don't know what questions to ask**
A: Start with: distributions, trends, comparisons, correlations

**Q: Can I use external libraries?**
A: Stick to: NumPy, Pandas, Matplotlib, Seaborn. Others: ask first!

**Q: How long should my report be?**
A: 5-10 pages (when exported to PDF), quality over quantity

---

# Individual Consultation

**Come talk to me about**:
- Dataset selection and feasibility
- Refining your analysis questions
- Technical challenges
- Project scope

**Bring**:
- Your laptop
- Your dataset (or shortlist)
- Your questions (draft is fine)
- Specific technical questions

---

# Peer Feedback

**Pair up and share**:
1. Your dataset and why you chose it
2. Your analysis questions
3. One thing you're excited about
4. One concern or challenge

**Give feedback**:
- Are the questions clear and specific?
- Is the scope appropriate?
- Any suggestions for additional analysis?

---

# Resources for Your Project

**Documentation**:
- [Pandas docs](https://pandas.pydata.org/docs/)
- [Matplotlib gallery](https://matplotlib.org/stable/gallery/)
- [Seaborn examples](https://seaborn.pydata.org/examples/)

**Inspiration**:
- [Kaggle notebooks](https://www.kaggle.com/code)
- [Towards Data Science](https://towardsdatascience.com)

**Help**:
- Office hours
- Course discussion forum
- Stack Overflow (search before asking)

---

# Grading Criteria

Your project will be evaluated on:

**Technical Skills (40%)**:
- Correct use of Python, Pandas, visualization
- Code quality and organization
- Appropriate analysis methods

**Analysis Quality (30%)**:
- Clear research questions
- Thorough exploration
- Valid conclusions

**Documentation (20%)**:
- Professional report structure
- Clear explanations
- Reproducibility

**Presentation (10%)**:
- Clear communication
- Visual quality
- Time management

---

# Presentation Guidelines

**Format**: 5-10 minute presentation

**Structure**:
1. **Introduction** (1 min): Question and motivation
2. **Data** (1 min): What data, where from
3. **Methods** (2 min): What you did
4. **Results** (3-4 min): Key findings (2-3 visualizations)
5. **Conclusion** (1 min): What it means, next steps

**Tips**:
- Practice timing
- Show visualizations, not code
- Tell a story
- Anticipate questions

---

# Final Tips

**Do**:
- ✅ Start simple, iterate
- ✅ Commit to git regularly
- ✅ Ask for help early
- ✅ Focus on insights, not just code
- ✅ Make it interesting to you

**Don't**:
- ❌ Aim for perfection
- ❌ Try to use every technique
- ❌ Wait until the last minute
- ❌ Ignore data quality issues
- ❌ Forget to interpret results

**Remember**: This is a learning project, not a PhD thesis!

---

# Next Steps

**By end of today**:
- [ ] Dataset selected
- [ ] Questions defined
- [ ] Project structure created
- [ ] Initial exploration done

**By next week** (if applicable):
- [ ] Main analysis complete
- [ ] Visualizations created
- [ ] Report written
- [ ] Presentation prepared

**Need help?** Office hours or ask now!

---

# Key Takeaways

**This course taught you**:
- Python programming fundamentals
- Object-oriented programming
- Data manipulation with Pandas
- Visualization with Matplotlib/Seaborn
- Professional documentation practices

**You can now**:
- Clean and analyze real-world data
- Create insightful visualizations
- Write reproducible analyses
- Communicate findings effectively

**Keep learning**: Data science is a journey, not a destination!

---

<!-- _class: lead -->

# Let's Get Started!

**Work on your projects, ask questions, collaborate!**

Good luck! 🚀

---

<!-- _class: lead -->

# Thank You!

**It's been a great semester. Best of luck with your projects!**

Questions? Let's talk!
