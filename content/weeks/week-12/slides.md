---
marp: true
paginate: true
header: "Session 12: Reports & Documentation"
footer: "Anna Smirnova, December 8, 2025"
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

# Session 12: Creating Professional Reports

**Documentation, Jupyter Notebooks & Reproducibility**

---

# Today's Goals

**Part 1: Why Documentation Matters**
- Code is read more than written
- Types of documentation
- Best practices

**Part 2: Jupyter Notebooks as Reports**
- Structuring analysis narratives
- Markdown formatting
- Code organization

**Part 3: Exporting & Sharing**
- PDF and HTML exports
- Interactive reports
- Reproducibility

---

# Part 1: Why Documentation Matters

---

# The Documentation Problem

**Consider this scenario**:

You open a Jupyter notebook from 6 months ago...

```python
df2 = df.groupby('x')[['y', 'z']].agg(f).reset_index()
result = df2.merge(df3, on='id', how='left')
final = result[result['val'] > threshold]
```

**Questions you'll ask yourself**:
- What is `x`, `y`, `z`?
- What does `f` do?
- Where did `df3` come from?
- What is `threshold` and why this value?
- What business question does this answer?

---

# Code is Read More Than Written

**Reality**:
- You write code once
- You (or others) read it dozens of times
- Your future self is your most important audience

**Good documentation**:
- Explains the "why", not just the "what"
- Makes code maintainable
- Enables collaboration
- Saves time in the long run

**"Programs must be written for people to read, and only incidentally for machines to execute."** — Harold Abelson

---

# Types of Documentation

**1. Code Comments**
```python
# Calculate year-over-year growth rate
growth = (current - previous) / previous * 100
```

**2. Docstrings**
```python
def calculate_roi(investment, return_value):
    """
    Calculate return on investment.

    Args:
        investment (float): Initial investment amount
        return_value (float): Final value

    Returns:
        float: ROI as a percentage
    """
    return (return_value - investment) / investment * 100
```

---

# Types of Documentation (cont.)

**3. README files**
- Project overview
- Installation instructions
- Usage examples
- Dependencies

**4. Analysis narratives** (Jupyter notebooks)
- Problem statement
- Data description
- Methodology
- Results and interpretation

**5. Technical documentation**
- API references
- Architecture diagrams
- Design decisions

---

# Documentation Best Practices

**Do**:
- ✅ Explain *why*, not just *what*
- ✅ Keep it up-to-date
- ✅ Use clear, simple language
- ✅ Provide examples
- ✅ Document assumptions and limitations

**Don't**:
- ❌ State the obvious: `x = x + 1  # increment x`
- ❌ Write novels (be concise)
- ❌ Use jargon unnecessarily
- ❌ Let documentation drift from code

---

# Part 2: Jupyter Notebooks as Reports

---

# Notebooks as Analysis Narratives

A good data analysis notebook tells a story:

1. **Introduction**: What question are we answering?
2. **Data**: What data are we using? Where from?
3. **Exploration**: What do we see in the data?
4. **Analysis**: What methods did we apply?
5. **Results**: What did we find?
6. **Conclusion**: What does it mean? Next steps?

**Think of it as**: A research paper, not a code dump

---

# Notebook Structure Example

```markdown
# Sales Analysis Q4 2025

## Executive Summary
This analysis examines Q4 sales performance across regions...

## Data Sources
- Sales data: `data/sales_q4.csv`
- Date range: Oct 1 - Dec 31, 2025
- 15,234 transactions across 4 regions

## Key Findings
1. North region outperformed by 23%
2. Mobile sales increased 45% YoY
3. December showed highest conversion rate (18.5%)

[Analysis continues...]
```

---

# Markdown in Jupyter Notebooks

**Headers**:
```markdown
# H1 - Main Title
## H2 - Section
### H3 - Subsection
```

**Emphasis**:
```markdown
**bold** or __bold__
*italic* or _italic_
***bold and italic***
```

**Lists**:
```markdown
- Unordered list
  - Nested item

1. Ordered list
2. Second item
```

---

# More Markdown Features

**Links**:
```markdown
[Link text](https://example.com)
[Link to section](#section-name)
```

**Images**:
```markdown
![Alt text](path/to/image.png)
```

**Code**:
```markdown
Inline `code`

```python
# Code block
def hello():
    print("Hello")
```
```

**Tables**:
```markdown
| Product | Sales |
|---------|-------|
| A       | $100K |
| B       | $150K |
```

---

# Mathematical Notation (LaTeX)

Jupyter supports LaTeX for mathematical notation:

**Inline**: `$E = mc^2$` → $E = mc^2$

**Block**:
```markdown
$$
\text{ROI} = \frac{\text{Gain} - \text{Cost}}{\text{Cost}} \times 100\%
$$
```

Renders as:
$$
\text{ROI} = \frac{\text{Gain} - \text{Cost}}{\text{Cost}} \times 100\%
$$

---

# Organizing Code Cells

**Bad**: One giant cell with everything
```python
# DON'T DO THIS
import pandas as pd
import numpy as np
# ... 200 lines of code ...
```

**Good**: Logical, sequential cells
```python
# Cell 1: Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

```python
# Cell 2: Load data
df = pd.read_csv('data/sales.csv')
df.head()
```

```python
# Cell 3: Data cleaning
df = df.dropna()
df['date'] = pd.to_datetime(df['date'])
```

---

# Code Cell Best Practices

**1. One logical step per cell**
- Easier to debug
- Can re-run parts independently
- Clear progression

**2. Display results**
```python
# Show what you did
print(f"Removed {null_count} null values")
print(f"Final dataset: {len(df)} rows")
```

**3. Add markdown between code**
```markdown
## Data Cleaning
We need to handle missing values and convert dates.
```

**4. Use meaningful variable names**
```python
# Good
revenue_by_region = df.groupby('region')['revenue'].sum()

# Bad
x = df.groupby('a')['b'].sum()
```

---

# Visualizations in Notebooks

**Always add context**:

```python
# Create visualization
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['sales'])
plt.title('Daily Sales - Q4 2025', fontsize=14)
plt.xlabel('Date')
plt.ylabel('Sales ($)')
plt.grid(True, alpha=0.3)
plt.show()
```

```markdown
**Figure 1**: Daily sales show clear weekly patterns with
peaks on Fridays and dips on Sundays. Note the spike on
Black Friday (Nov 24).
```

**Explain** what the reader should notice!

---

# Creating a Complete Analysis Template

```markdown
# [Project Title]

**Author**: Your Name
**Date**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD

## 1. Executive Summary
[Brief overview of findings]

## 2. Business Question
[What are we trying to answer?]

## 3. Data Description
[Where data came from, time period, etc.]

## 4. Methodology
[What analysis techniques did you use?]

## 5. Analysis
[The actual code and results]

## 6. Findings
[Key takeaways]

## 7. Recommendations
[What should be done based on findings?]

## 8. Limitations & Next Steps
[What couldn't be answered? What's next?]
```

---

# Part 3: Exporting & Sharing

---

# Exporting Notebooks

**1. HTML** (most common):
```bash
jupyter nbconvert --to html notebook.ipynb
```

**2. PDF** (requires LaTeX):
```bash
jupyter nbconvert --to pdf notebook.ipynb
```

**3. Markdown**:
```bash
jupyter nbconvert --to markdown notebook.ipynb
```

**4. Python script**:
```bash
jupyter nbconvert --to python notebook.ipynb
```

---

# Customizing Exports

**Remove code cells** (show only results):
```bash
jupyter nbconvert --to html notebook.ipynb \
  --no-input
```

**Remove output** (show only code):
```bash
jupyter nbconvert --to html notebook.ipynb \
  --no-output
```

**Hide specific cells**: Add tags in Jupyter
- View → Cell Toolbar → Tags
- Add "remove_cell" tag
- Use `--TagRemovePreprocessor.remove_cell_tags='{"remove_cell"}'`

---

# Creating Shareable Reports

**Best format for different audiences**:

| Audience | Format | Why |
|----------|--------|-----|
| **Non-technical** | HTML (no code) | Easy to view, looks professional |
| **Technical** | HTML (with code) | Can see methodology |
| **Collaborators** | .ipynb file | Can run and modify |
| **Publication** | PDF | Print-ready, formal |
| **Web** | HTML + GitHub Pages | Publicly accessible |

---

# Ensuring Reproducibility

**Problem**: "It works on my machine"

**Solution**: Document environment

**1. List dependencies**:
```bash
# Create requirements file
pip freeze > requirements.txt

# Or with uv
uv pip freeze > requirements.txt
```

**2. Create README**:
```markdown
## Installation

```bash
uv pip install -r requirements.txt
```

## Data
Download from: [URL]
Place in: `data/`

## Running
```bash
jupyter notebook analysis.ipynb
```
```

---

# Reproducibility Checklist

- [ ] All dependencies listed in `requirements.txt`
- [ ] Data sources documented (with download links if possible)
- [ ] Random seeds set (`np.random.seed(42)`)
- [ ] File paths relative, not absolute
- [ ] Clear instructions in README
- [ ] Output cleared before committing to git
- [ ] Notebook runs top-to-bottom without errors

---

# Git + Jupyter Best Practices

**Problem**: Jupyter notebooks have metadata and outputs that change

**Solution**: Clear outputs before committing

```bash
# Clear all outputs
jupyter nbconvert --clear-output --inplace notebook.ipynb

# Or use nbstripout
pip install nbstripout
nbstripout notebook.ipynb
```

**Or**: Configure git to auto-strip outputs
```bash
nbstripout --install
```

---

# Hands-On Exercise: Create a Report

You have sales data for the past year. Create a professional analysis notebook:

**Data**: `sales_2025.csv` (provided)

**Your report should include**:
1. Title and executive summary
2. Data loading and initial exploration
3. At least 3 visualizations with explanations
4. Summary statistics by category
5. Key findings section
6. Recommendations

**Requirements**:
- Proper markdown formatting
- Clear section headers
- Code cells with comments
- Interpretations of results

---

# Exercise: Sample Structure

```markdown
# Annual Sales Analysis 2025

## Executive Summary
[Your findings in 2-3 sentences]

## Data Overview
```

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/sales_2025.csv')
df.head()
```

```markdown
The dataset contains {len(df)} transactions from...

## Sales by Category
```

[Continue building out the analysis...]

---

# Writing Good Interpretations

**Bad interpretation**:
> "The graph shows sales over time."

**Good interpretation**:
> "Sales increased steadily through Q1-Q3, peaking at $2.1M in
> September before declining 15% in Q4. The Q4 decline is
> primarily driven by reduced enterprise sales, which dropped
> 23% compared to Q3."

**What makes it good**:
- Specific numbers
- Identifies patterns
- Explains possible causes
- Actionable insights

---

# Common Report Mistakes

**1. No context**: Jumping straight into code
**2. Too much code**: Showing every exploratory step
**3. No interpretation**: Figures without explanation
**4. Unclear flow**: Random order of analyses
**5. No conclusion**: Analysis without recommendations
**6. Assuming knowledge**: Not defining terms/metrics

**Remember**: Your notebook is a story, not just code!

---

# Creating Templates

Save time by creating reusable templates:

```python
# In your templates/ folder
# data_analysis_template.ipynb

"""
Contains:
- Standard imports
- Data loading section
- Exploratory analysis section
- Visualization section
- Results section
- Conclusion section
"""
```

**Create your own** for:
- Weekly reports
- A/B test analyses
- Financial reports
- Research papers

---

# Key Takeaways

**Documentation matters**:
- Your future self will thank you
- Enables collaboration
- Makes work reproducible

**Jupyter notebooks as reports**:
- Tell a story with your analysis
- Use markdown extensively
- One logical step per cell
- Always interpret your results

**Sharing & reproducibility**:
- Export to HTML/PDF for sharing
- Document dependencies
- Use relative paths
- Clear outputs before git commits

---

# Homework Assignment

**Create a Complete Data Analysis Report**

Choose a dataset (or use one provided) and create a professional analysis:

**Requirements**:
1. **Complete narrative structure** (intro → analysis → conclusion)
2. **At least 5 sections** with markdown headers
3. **3+ visualizations** with interpretations
4. **Code organized** in logical cells
5. **Export to HTML** (without code cells)
6. **Include README** with setup instructions

**Deliverable**:
- `.ipynb` file (original notebook)
- `.html` file (exported report)
- `requirements.txt`
- `README.md`

---

<!-- _class: lead -->

# Questions?

**Next week**: Final project workshop - putting it all together!
