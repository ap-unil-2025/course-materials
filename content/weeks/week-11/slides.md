---
marp: true
paginate: true
theme: unil
header: "Week 11: Final Project Workshop"
footer: "Anna Smirnova · Advanced Programming 2025"
style: |
  section {
    font-size: 24px;
  }
  code {
    font-size: 16px;
  }
---

<!-- _class: lead -->

# Week 11: Final Project Workshop

**From Research Question to Submission**

---

# Today's Journey

**Part 1: Research Question → Full Repository** (30 min)
- Start with a research question
- Build proper project structure
- Set up environments

**Part 2: Debug Your ML Project** (25 min)
- Common ML bugs and fixes
- Reproducibility and overfitting

**Part 3: Write Your Report** (20 min)
- Document your methodology
- Present results clearly

**Part 4: Submission Checklist** (15 min)
- Make it work everywhere
- Final polish

---

# Why This Matters

**3 weeks until project deadline (Dec 21)**

The #1 grading criterion:
> **Does `python main.py` work on our machines?**

If we can't run it, we can't grade it.

---

<!-- _class: lead -->

# Part 1: Research Question → Full Repository

**Building a proper ML project**

---

# Example Research Question

> "Which classification model performs best for Iris species:
> Random Forest, K-Nearest Neighbors, or Logistic Regression?"

**Let's build a complete project to answer this.**

This is the journey we'll follow today.

---

# What Files Do We Need?

```
my-iris-comparison/
├── README.md              # What, why, how
├── environment.yml        # Dependencies (conda)
├── main.py               # Entry point
├── src/
│   ├── data_loader.py    # Load and preprocess
│   ├── models.py         # Model definitions
│   └── evaluation.py     # Metrics and plots
├── data/
│   └── raw/              # Original data
├── results/              # Outputs
└── notebooks/            # Exploration
```

We'll build this step by step.

---

# Step 1: Set Up Environment (Conda on Nuvolos)

**Conda is what you use on Nuvolos** (the platform you have access to).

```bash
# Create new environment
conda create -n iris-project python=3.11

# Activate it
conda activate iris-project

# Install packages
conda install pandas scikit-learn matplotlib seaborn

# Save dependencies
conda env export > environment.yml
```

**This creates a reproducible environment.**

---

# Your environment.yml File

```yaml
name: iris-project
channels:
  - defaults
dependencies:
  - python=3.11
  - pandas
  - scikit-learn
  - matplotlib
  - seaborn
  - jupyter
```

**Anyone can recreate your exact environment:**
```bash
conda env create -f environment.yml
conda activate iris-project
```

---

# Optional: Local Python (venv/uv)

If you're working locally (not on Nuvolos):

**Using venv (built-in):**
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

**Using uv (modern/fast):**
```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

---

# Step 2: Create Project Structure

```bash
# Create directories
mkdir -p my-iris-comparison/{src,data/raw,results,notebooks}
cd my-iris-comparison

# Create __init__.py for src/ package
touch src/__init__.py

# Create main files
touch main.py README.md environment.yml
touch src/data_loader.py src/models.py src/evaluation.py
```

**Structure before code.**

---

# Step 3: Write src/data_loader.py

```python
"""Data loading and preprocessing."""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_split(test_size=0.2, random_state=42):
    """Load Iris dataset and split into train/test."""
    iris = load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Scale features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test
```

---

# Step 4: Write src/models.py (1/2)

```python
"""Model definitions and training."""
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

def train_random_forest(X_train, y_train, random_state=42):
    """Train Random Forest model."""
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=random_state
    )
    model.fit(X_train, y_train)
    return model
```

---

# Step 4: Write src/models.py (2/2)

```python
def train_knn(X_train, y_train, n_neighbors=5):
    """Train K-Nearest Neighbors model."""
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(X_train, y_train)
    return model

def train_logistic_regression(X_train, y_train, random_state=42):
    """Train Logistic Regression model."""
    model = LogisticRegression(
        max_iter=200,
        random_state=random_state
    )
    model.fit(X_train, y_train)
    return model
```

---

# Step 5: Write src/evaluation.py

```python
"""Model evaluation and visualization."""
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

def evaluate_model(model, X_test, y_test, model_name):
    """Evaluate model and print results."""
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"\n{model_name} Results:")
    print(f"Accuracy: {accuracy:.3f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    return accuracy
```

---

# Step 6: Write main.py (1/2)

```python
"""
Main script to compare ML models on Iris dataset.
"""
from src.data_loader import load_and_split
from src.models import (
    train_random_forest,
    train_knn,
    train_logistic_regression
)
from src.evaluation import evaluate_model

def main():
    print("=" * 60)
    print("Iris Classification: Model Comparison")
    print("=" * 60)

    # Load data
    print("\n1. Loading and preprocessing data...")
    X_train, X_test, y_train, y_test = load_and_split()
    print(f"   Train size: {X_train.shape}")
    print(f"   Test size: {X_test.shape}")
```

---

# Step 6: Write main.py (2/2)

```python
    # Train models
    print("\n2. Training models...")
    rf_model = train_random_forest(X_train, y_train)
    knn_model = train_knn(X_train, y_train)
    lr_model = train_logistic_regression(X_train, y_train)
    print("   ✓ All models trained")

    # Evaluate
    print("\n3. Evaluating models...")
    rf_acc = evaluate_model(rf_model, X_test, y_test, "Random Forest")
    knn_acc = evaluate_model(knn_model, X_test, y_test, "KNN")
    lr_acc = evaluate_model(lr_model, X_test, y_test, "Logistic Regression")

    # Conclusion
    results = {"Random Forest": rf_acc, "KNN": knn_acc, "Logistic Regression": lr_acc}
    winner = max(results, key=results.get)
    print("\n" + "=" * 60)
    print(f"Winner: {winner} ({results[winner]:.3f} accuracy)")
    print("=" * 60)

if __name__ == "__main__":
    main()
```

---

# Step 7: Write README.md

```markdown
# Iris Classification: Model Comparison

## Research Question
Which classification model performs best for Iris species:
Random Forest, K-Nearest Neighbors, or Logistic Regression?

## Setup
```bash
# Create environment
conda env create -f environment.yml
conda activate iris-project
```

## Usage
```bash
python main.py
```

Expected output: Accuracy comparison between three models.
```

---

# README.md (continued)

```markdown
## Project Structure
```
my-iris-comparison/
├── main.py              # Main entry point
├── src/                 # Source code
│   ├── data_loader.py   # Data loading/preprocessing
│   ├── models.py        # Model training
│   └── evaluation.py    # Evaluation metrics
├── results/             # Output plots and metrics
└── environment.yml      # Dependencies
```

## Results
- Random Forest: 0.967 accuracy
- KNN: 0.933 accuracy
- Logistic Regression: 0.967 accuracy
- Winner: Tie between Random Forest and Logistic Regression

## Requirements
- Python 3.11
- scikit-learn, pandas, matplotlib, seaborn
```

---

# Test It!

```bash
# Activate environment
conda activate iris-project

# Run the project
python main.py
```

**Expected output:**
```
============================================================
Iris Classification: Model Comparison
============================================================

1. Loading and preprocessing data...
   Train size: (120, 4)
   Test size: (30, 4)

2. Training models...
   ✓ All models trained

3. Evaluating models...
...
============================================================
Winner: Random Forest (0.967 accuracy)
============================================================
```

---

# Checkpoint: What We Built

✅ **Proper project structure**
✅ **Environment management** (conda)
✅ **Modular code** (src/ directory)
✅ **Entry point** (main.py)
✅ **Documentation** (README.md)
✅ **Reproducibility** (environment.yml)

**This is the foundation of a good research project.**

---

<!-- _class: lead -->

# Part 2: Debug Your ML Project

**Common bugs and how to fix them**

---

# Common ML Bug 1: Shape Mismatches

**The Problem:**
```python
X_train = scaler.fit_transform(X_train)  # Shape: (120, 4)
X_test = X_test[:10]  # Accidentally subset - Shape: (10, 4)

# Later...
model.fit(X_train, y_train)  # y_train has 120 samples
model.predict(X_test)  # Works, but...

# But what if:
X_test = X_test[:, :2]  # Only 2 features now!
model.predict(X_test)  # ❌ ValueError!
```

**The Fix:** Always check shapes
```python
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
```

---

# Common ML Bug 2: Wrong Data Types

**The Problem:**
```python
# CSV with numeric columns
df = pd.read_csv('data.csv')
X = df[['age', 'income', 'score']]

# Oops, 'income' was read as string!
print(df['income'].dtype)  # object (string)

model.fit(X, y)  # ❌ ValueError: could not convert string to float
```

**The Fix:** Always check dtypes
```python
print(df.dtypes)
df['income'] = pd.to_numeric(df['income'], errors='coerce')
```

---

# Common ML Bug 3: Missing Values (NaN)

**The Problem:**
```python
df = pd.read_csv('data.csv')
X = df[['age', 'income', 'score']]

# Some values are missing!
print(X.isnull().sum())  # age: 5, income: 3, score: 0

model.fit(X, y)  # ❌ ValueError: Input contains NaN
```

**The Fix:** Handle missing values
```python
# Option 1: Drop rows
X = X.dropna()

# Option 2: Fill with mean
X = X.fillna(X.mean())

# Option 3: Use imputer
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)
```

---

# Common ML Bug 4: Not Scaling Features

**The Problem:**
```python
# Features with very different scales
df['age']     # Range: 20-80
df['income']  # Range: 20,000-200,000

# Train without scaling
model = KNeighborsClassifier()
model.fit(X_train, y_train)  # Works but...
# Model is dominated by 'income' (larger values)!
```

**The Fix:** Scale your features
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model.fit(X_train_scaled, y_train)
```

---

# Common ML Bug 5: Data Leakage

**The Problem:**
```python
# ❌ WRONG: Scale before split
X_scaled = scaler.fit_transform(X)  # Leak test info into train!
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)
```

**Why it's wrong:** The scaler "saw" the test data during fit!

**The Fix:** Split first, then scale
```python
# ✅ RIGHT: Split first, then scale
X_train, X_test, y_train, y_test = train_test_split(X, y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Fit on train only
X_test_scaled = scaler.transform(X_test)        # Transform test only
```

---

# Common sklearn Error Messages (1/3)

**Error 1:** `ValueError: Found input variables with inconsistent numbers of samples`

```python
X = [[1, 2], [3, 4], [5, 6]]  # 3 samples
y = [0, 1]                     # 2 samples - MISMATCH!

model.fit(X, y)  # ❌ Error!
```

**Fix:** Make sure X and y have same number of samples
```python
print(f"X samples: {len(X)}, y samples: {len(y)}")
```

---

# Common sklearn Error Messages (2/3)

**Error 2:** `ValueError: X has 5 features, but SVC is expecting 8 features`

```python
# Training
X_train = df[['age', 'income', 'score', 'rating', 'years']]  # 5 features
model.fit(X_train, y_train)

# Testing with different features
X_test = df_test[['age', 'income', 'score']]  # Only 3 features
model.predict(X_test)  # ❌ Error!
```

**Fix:** Use same features for train and test
```python
FEATURES = ['age', 'income', 'score', 'rating', 'years']
X_train = df_train[FEATURES]
X_test = df_test[FEATURES]
```

---

# Common sklearn Error Messages (3/3)

**Error 3:** `ValueError: could not convert string to float: 'Male'`

```python
df = pd.DataFrame({
    'gender': ['Male', 'Female', 'Male'],
    'age': [25, 30, 35]
})

X = df[['gender', 'age']]
model.fit(X, y)  # ❌ Error: can't use strings directly
```

**Fix:** Encode categorical variables
```python
# Option 1: One-hot encoding
X = pd.get_dummies(df, columns=['gender'])

# Option 2: Label encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])
```

---

# Reproducibility Problem

**The Problem:**
```python
# Run 1
model = RandomForestClassifier()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))  # 0.867

# Run 2 (same code!)
model = RandomForestClassifier()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))  # 0.833 - Different!
```

**Why:** Many algorithms use randomness (initialization, sampling, etc.)

---

# Reproducibility Fix: random_state

**Use `random_state` everywhere:**

```python
# Data splitting
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model training
model = RandomForestClassifier(random_state=42)
model = KNeighborsClassifier()  # No random_state needed for KNN

# Cross-validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5, random_state=42)

# DataFrame sampling
df.sample(frac=0.8, random_state=42)
```

**Use the same number (e.g., 42) everywhere.**

---

# Overfitting: What It Looks Like

**Symptoms:**
```python
# Train your model
model.fit(X_train, y_train)

# Check accuracy
train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)

print(f"Training accuracy: {train_acc:.3f}")   # 0.997
print(f"Test accuracy: {test_acc:.3f}")        # 0.650

# Gap is huge!
gap = train_acc - test_acc  # 0.347 - BAD!
```

**The model memorized the training data instead of learning patterns.**

---

# Overfitting: How to Fix

**1. Simplify the model:**
```python
# Too complex
rf = RandomForestClassifier(max_depth=50, n_estimators=500)

# Simpler
rf = RandomForestClassifier(max_depth=10, n_estimators=100)
```

**2. Use cross-validation:**
```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
print(f"Mean: {scores.mean():.3f} (+/- {scores.std():.3f})")
```

**3. Get more training data** (most effective, but not always possible)

---

# ML Debugging Checklist

**Your model has low accuracy. Check:**

1. **Data quality:** Missing values? Wrong dtypes? Duplicates?
2. **Feature scaling:** Did you scale? KNN/SVM need it!
3. **Train/test split:** Too small test set? Unbalanced classes?
4. **Model choice:** Is the model appropriate for your data?
5. **Hyperparameters:** Did you tune them? Try GridSearchCV
6. **Data leakage:** Did you split before scaling?
7. **Overfitting:** Large train/test gap?
8. **Reproducibility:** Set random_state everywhere

**Systematic debugging beats random changes.**

---

<!-- _class: lead -->

# Part 3: Write Your Report

**Documenting your methodology and results**

---

# Why Write a Report?

**Your code works. Now explain:**
- What you did (methodology)
- Why you did it (justification)
- What you found (results)
- What it means (interpretation)

**A good report makes your project reusable and citable.**

Think: mini research paper, not just code documentation.

---

# Report Structure

Your report should include:

1. **Introduction** - Research question and motivation
2. **Methodology** - Data, models, evaluation approach
3. **Results** - What you found
4. **Discussion** - What it means
5. **Conclusion** - Summary and future work
6. **References** - Citations (if applicable)

Save as `REPORT.md` in your project root.

---

# Section 1: Introduction

**What and Why**

```markdown
# Introduction

## Research Question
Which classification model performs best for predicting Iris species:
Random Forest, K-Nearest Neighbors, or Logistic Regression?

## Motivation
The Iris dataset is a classic benchmark for classification algorithms.
Understanding which models perform best on this task helps us choose
appropriate algorithms for similar multi-class classification problems
in botany and ecology.

## Objectives
- Compare three classification algorithms on Iris dataset
- Evaluate using accuracy and per-class metrics
- Identify strengths and weaknesses of each approach
```

---

# Section 2: Methodology (1/2)

**Data and Preprocessing**

```markdown
# Methodology

## Dataset
- **Source**: sklearn.datasets.load_iris()
- **Samples**: 150 (120 train, 30 test)
- **Features**: 4 (sepal length/width, petal length/width)
- **Classes**: 3 species (setosa, versicolor, virginica)
- **Split**: 80% train, 20% test (random_state=42)

## Preprocessing
All features were standardized using StandardScaler:
- Fit on training data only (to avoid data leakage)
- Applied same transformation to test data
- Scaling is critical for KNN (distance-based algorithm)
```

---

# Section 2: Methodology (2/2)

**Models and Evaluation**

```markdown
## Models
1. **Random Forest** (n_estimators=100, random_state=42)
   - Ensemble of decision trees
   - Handles non-linear relationships

2. **K-Nearest Neighbors** (n_neighbors=5)
   - Instance-based learning
   - Requires feature scaling

3. **Logistic Regression** (max_iter=200, random_state=42)
   - Linear classifier with softmax for multi-class
   - Baseline model

## Evaluation Metrics
- Accuracy: Overall correct predictions
- Per-class precision, recall, F1-score
- All experiments use random_state=42 for reproducibility
```

---

# Section 3: Results

**Present Your Findings**

```markdown
# Results

## Model Performance

| Model                | Accuracy | Notes                        |
|---------------------|----------|------------------------------|
| Random Forest       | 0.967    | Best overall, robust         |
| Logistic Regression | 0.967    | Tied for best, simpler model |
| K-Nearest Neighbors | 0.933    | Good, but slightly behind    |

## Per-Class Performance (Random Forest)

| Class      | Precision | Recall | F1-Score |
|-----------|-----------|--------|----------|
| Setosa    | 1.00      | 1.00   | 1.00     |
| Versicolor| 0.94      | 0.94   | 0.94     |
| Virginica | 0.94      | 0.94   | 0.94     |

All models achieve >93% accuracy, indicating Iris is well-separated.
```

---

# Section 4: Discussion

**Interpret Your Results**

```markdown
# Discussion

## Key Findings
1. **Random Forest and Logistic Regression tied for best accuracy (96.7%)**
   - Surprising: Linear model matches ensemble method
   - Suggests Iris classes are linearly separable

2. **KNN performed well but slightly lower (93.3%)**
   - May be sensitive to distance metric choice
   - Could improve with hyperparameter tuning

3. **All models perfect on Setosa class**
   - Setosa is well-separated from other classes
   - Main confusion between Versicolor and Virginica

## Limitations
- Small dataset (150 samples)
- No hyperparameter tuning performed
- Single train/test split (should use cross-validation)
```

---

# Section 5: Conclusion

**Wrap It Up**

```markdown
# Conclusion

## Summary
We compared three classification algorithms on the Iris dataset.
Random Forest and Logistic Regression both achieved 96.7% accuracy,
while KNN achieved 93.3%. All models performed well, with perfect
classification of the Setosa species.

## Recommendations
For this dataset:
- **Use Logistic Regression** - Simplest, tied for best performance
- **Use Random Forest** - If interpretability is less important

## Future Work
- Perform hyperparameter tuning (GridSearchCV)
- Use k-fold cross-validation for more robust evaluation
- Add confusion matrix visualization
- Test on additional multi-class datasets
```

---

# Report Tips

**Do:**
✅ Be concise - 2-4 pages is fine
✅ Use tables and figures to present results
✅ Explain *why* you made each choice
✅ Discuss limitations honestly
✅ Use proper markdown formatting

**Don't:**
❌ Just paste code (that's what src/ is for)
❌ Say "the results are good" without specifics
❌ Ignore unexpected findings
❌ Forget to cite datasets/methods if from papers

---

# Where Does the Report Go?

```
my-iris-comparison/
├── README.md              # Setup and usage instructions
├── REPORT.md             # ← Your research report here
├── environment.yml
├── main.py
├── src/
├── data/
├── results/
└── notebooks/
```

**README = How to run it**
**REPORT = What you did and found**

They serve different purposes!

---

# Report Example: File Structure

Your `REPORT.md` should look like:

```markdown
# Iris Classification: Model Comparison Report

## 1. Introduction
[Research question, motivation, objectives]

## 2. Methodology
[Data, preprocessing, models, evaluation]

## 3. Results
[Tables, metrics, findings]

## 4. Discussion
[Interpretation, limitations]

## 5. Conclusion
[Summary, recommendations, future work]

## 6. References (if applicable)
```

**Total: 3-5 pages** (not including code)

---

<!-- _class: lead -->

# Part 4: Submission Checklist

**Making sure it works everywhere**

---

# The #1 Grading Criterion

> **Does `python main.py` work on our machines?**

**This means:**
- We can create your environment
- We can install your dependencies
- We can run your code
- We get meaningful output

**If any of these fail, we can't grade your project.**

---

# Submission Checklist

**Before you submit, verify:**

✅ **1. Code runs:** `python main.py` works without errors
✅ **2. Dependencies listed:** `environment.yml` or `requirements.txt`
✅ **3. README complete:** Setup, usage, expected output
✅ **4. Report written:** `REPORT.md` with methodology and results
✅ **5. Reproducible:** Same results every run (random_state=42)
✅ **6. No hardcoded paths:** Use relative paths only
✅ **7. Data included:** Or clear instructions to download
✅ **8. Clean structure:** No junk files (`.DS_Store`, `__pycache__/`)
✅ **9. Git history clean:** Meaningful commit messages
✅ **10. Tested fresh:** Works on clean environment

---

# Test on Fresh Environment

**The ultimate test:** Can someone else run it?

```bash
# 1. Deactivate current environment
conda deactivate

# 2. Delete and recreate environment
conda env remove -n iris-project
conda env create -f environment.yml

# 3. Activate and test
conda activate iris-project
python main.py
```

**If this works, you're good to submit!**

---

# Common Submission Mistakes

**❌ Hardcoded paths:**
```python
df = pd.read_csv('/Users/yourname/Desktop/data.csv')  # Won't work!
```

**✅ Relative paths:**
```python
df = pd.read_csv('data/raw/data.csv')  # Works anywhere
```

**❌ Missing dependencies:**
```bash
python main.py
# ModuleNotFoundError: No module named 'seaborn'
```

**✅ Complete environment.yml:**
```yaml
dependencies:
  - seaborn  # Now it's listed!
```

---

# Common Mistakes (Continued)

**❌ No clear entry point:**
```
# Which file do we run?
analysis.py
test.py
final_version_v2_FINAL.py
```

**✅ Clear main.py:**
```python
# main.py - Always run this
if __name__ == "__main__":
    main()
```

**❌ No report:**
```
# Only code, no documentation of findings
```

**✅ Complete report:**
```markdown
# REPORT.md with methodology, results, discussion
```

---

# Final Project Structure

```
my-project/
├── README.md              # Setup and usage
├── REPORT.md             # Research findings
├── environment.yml        # Conda dependencies
├── main.py               # Entry point
├── src/                  # Source code
│   ├── __init__.py
│   ├── data_loader.py
│   ├── models.py
│   └── evaluation.py
├── data/
│   └── raw/              # Original data
├── results/              # Outputs (plots, metrics)
└── notebooks/            # Exploration (optional)
```

**Everything a grader needs.**

---

# Quick Reference: Conda Commands

```bash
# Create environment
conda create -n project-name python=3.11

# Activate
conda activate project-name

# Install packages
conda install pandas scikit-learn matplotlib

# Save dependencies
conda env export > environment.yml

# Recreate from file
conda env create -f environment.yml

# Remove environment
conda env remove -n project-name
```

---

# Quick Reference: Common sklearn Fixes

```python
# Check shapes
print(X_train.shape, y_train.shape)

# Check dtypes
print(df.dtypes)

# Check missing values
print(df.isnull().sum())

# Scale features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Set random_state
train_test_split(X, y, random_state=42)
RandomForestClassifier(random_state=42)

# Check for overfitting
train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)
print(f"Gap: {train_acc - test_acc:.3f}")
```

---

# Resources

**Course Materials:**
- Week 11 project structure guide (detailed examples)
- Example projects in course repository
- Professor's slides on advanced ML

**Documentation:**
- [scikit-learn](https://scikit-learn.org/)
- [pandas](https://pandas.pydata.org/)
- [Conda user guide](https://docs.conda.io/projects/conda/en/latest/user-guide/)

**Getting Help:**
- Office hours
- Course discussion forum
- Check previous weeks' materials

---

<!-- _class: lead -->

# Summary

**Research Question → Full Repo → Debug → Report → Submit**

1. Build proper project structure
2. Debug common ML bugs
3. Write clear report documenting findings
4. Make it reproducible
5. Test on fresh environment
6. Submit with confidence

**You have 3 weeks. Start now!**

---

<!-- _class: lead -->

# Questions?

**Dec 21 deadline - Let's make your projects great!**
