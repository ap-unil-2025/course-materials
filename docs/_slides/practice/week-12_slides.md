---
marp: true
paginate: true
header: "Session 12: Reports & Documentation"
footer: "Anna Smirnova, December 1, 2025"
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

**Part 2: Jupyter Notebooks as Reports**

**Part 3: Exporting & Sharing**

**Part 4: Hyperparameter Tuning**

---

# Part 1: Why Documentation Matters

---

# The Documentation Problem

**Consider this scenario**: You open a Jupyter notebook from 6 months ago...

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
---

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

**3. README files** - we already know!
- Project overview
- Installation instructions
- Usage examples
- Dependencies
---

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
---
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
---

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
---

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
---

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

```

---

# Your Project Report: Required Structure

**8 sections (aligned with professor's requirements):**

1. **Abstract** (~200 words)
2. **Introduction** - research question, motivation
3. **Research Question & Literature** - context, related work
4. **Methodology** - data, algorithms, evaluation approach
5. **Implementation** - key decisions, challenges (can be brief)
6. **Codebase & Reproducibility** - how to run it (2-3 sentences OK)
7. **Results** - tables, figures, interpretation
8. **Conclusion** - summary, limitations, future work

**Appendix**: AI tools used (required if applicable)

---

# Report Tips

**Length**: ~10 pages (min 8, excluding references)

**Where to spend your pages**:
- Methodology + Results = bulk of your report
- Implementation/Codebase can be short if straightforward

**Common mistakes**:
- ❌ Too much code in the report (use appendix)
- ❌ Figures without interpretation
- ❌ Missing research question
- ❌ No discussion of limitations

**Remember**: Explain the "why", not just the "what"

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

# Reproducibility Reminder

**You already know this** — just a quick checklist:

✅ Dependencies in `requirements.txt`, `environment.yml`, or `pyproject.toml`
✅ Random seeds set (`random_state=42`)
✅ Relative file paths (not `/Users/yourname/...`)
✅ Clear README with setup instructions
✅ Notebook runs top-to-bottom without errors

**Any reproducible environment works**: conda, venv, uv, poetry...

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

---

# Writing Good Interpretations

**Bad interpretation**:
> "The graph shows sales over time."

**Good interpretation**:
> "Sales increased steadily through Q1-Q3, peaking at $2.1M in
> September before declining 15% in Q4. The Q4 decline is
> primarily driven by reduced enterprise sales, which dropped
> 23% compared to Q3."


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

---

# Part 4: Hyperparameter Tuning

---

# What Are Hyperparameters?

**Parameters** — learned from data:
- Weights in linear regression
- Split points in decision trees

**Hyperparameters** — set before training:
- Number of trees in Random Forest
- `k` in KNN
- Learning rate
- Max depth

**Goal**: Find the best hyperparameters for your model

---

# GridSearchCV: Exhaustive Search

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
# Define parameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, None],
    'min_samples_split': [2, 5]
}

# Create grid search
grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,              # 5-fold cross-validation
    scoring='accuracy'
)
grid_search.fit(X_train, y_train)
print(f"Best params: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_:.3f}")
```

---

# GridSearchCV Results

```python
# Best model is already fitted
best_model = grid_search.best_estimator_

# Evaluate on test set
test_score = best_model.score(X_test, y_test)
print(f"Test accuracy: {test_score:.3f}")

# See all results
import pandas as pd
results = pd.DataFrame(grid_search.cv_results_)
results[['params', 'mean_test_score', 'rank_test_score']].head()
```

**Note**: GridSearchCV tries all combinations
- 3 × 3 × 2 = 18 combinations
- With 5-fold CV = 90 model fits!

---

# RandomizedSearchCV: Faster Alternative

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform
# Define distributions
param_distributions = {
    'n_estimators': randint(50, 300),
    'max_depth': randint(3, 20),
    'min_samples_split': randint(2, 10),
    'min_samples_leaf': randint(1, 5)
}
random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_distributions,
    n_iter=20,         # Only try 20 random combinations
    cv=5,
    random_state=42
)
random_search.fit(X_train, y_train)
```

---

# Hyperparameter Tuning Best Practices

**1. Start simple**
- First get a baseline with defaults
- Then tune the most impactful parameters

**2. Use cross-validation**
- Never tune on test set!
- CV prevents overfitting to validation data
---
**3. Common parameters to tune**:

| Model | Key Hyperparameters |
|-------|---------------------|
| Random Forest | `n_estimators`, `max_depth`, `min_samples_split` |
| KNN | `n_neighbors`, `weights` |
| Logistic Regression | `C`, `penalty` |
| SVM | `C`, `kernel`, `gamma` |

**4. Document your search**
- Report which parameters you tried
- Include in your methodology section

---

# Deep Learning Hyperparameters (Simple)

If you're using a neural network, key hyperparameters:

| Parameter | What it does | Typical values |
|-----------|--------------|----------------|
| **Learning rate** | Step size for updates | 0.001, 0.01, 0.1 |
| **Batch size** | Samples per update | 16, 32, 64, 128 |
| **Epochs** | Training iterations | 10-100+ |
| **Hidden layers** | Network depth | 1-3 for simple tasks |
| **Neurons per layer** | Network width | 32, 64, 128 |
---
**Simple approach**: Start with defaults, then try 2-3 values for learning rate

```python
# Example with sklearn MLPClassifier
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(64, 32),
                    learning_rate_init=0.001,
                    max_iter=200, random_state=42)
```

---

# Beyond This Course: Real Hyperparameter Tuning

**For info only** — what professionals use:

| Tool | What it does |
|------|--------------|
| **Optuna** | Smart search (Bayesian optimization) |
| **Ray Tune** | Distributed tuning across machines |
| **W&B Sweeps** | Track experiments + automatic tuning |
| **Keras Tuner** | Built-in for TensorFlow/Keras |
**Why they exist**: GridSearch doesn't scale
- 5 hyperparameters × 5 values each = 3,125 combinations
- Bayesian methods find good values faster


---

<!-- _class: lead -->

# Questions?

**Next week**: Final project workshop - putting it all together!
