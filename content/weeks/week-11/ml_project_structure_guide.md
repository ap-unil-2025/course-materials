# ML Project Structure & Reproducibility Guide
**Advanced Programming 2025 - UNIL**
**Duration: 2 hours**

---

## Session Overview

**Part 1: Environment Management (30 min)**
- Virtual environments (venv)
- Why isolation matters
- Creating and managing environments

**Part 2: Dependency Management (30 min)**
- requirements.txt vs pyproject.toml
- pip vs uv
- Reproducibility best practices

**Part 3: Project Structure (40 min)**
- Standard ML project layout
- File organization
- Documentation

**Part 4: Hands-on Workshop (20 min)**
- Live demo: Setting up a project from scratch
- Common issues and debugging

---

# PART 1: Virtual Environments (30 min)

## What is a Virtual Environment?

A virtual environment is an **isolated Python environment** that has its own:
- Python interpreter
- Installed packages
- Scripts

Think of it like a separate Python installation for each project.

### The Problem Without Virtual Environments

```bash
# Project A needs scikit-learn 1.2
pip install scikit-learn==1.2

# Project B needs scikit-learn 1.5
pip install scikit-learn==1.5  # ⚠️ Overwrites Project A's version!

# Now Project A is broken!
```

**Real-world scenario:**
- Your course project uses TensorFlow 2.15
- Another project uses TensorFlow 2.10
- Installing one breaks the other
- Your system Python gets polluted with hundreds of packages
- "It works on my machine!" syndrome

### The Solution: One Environment Per Project

```
Your Computer
├── System Python (clean!)
├── project-A/
│   └── .venv/  (has scikit-learn 1.2)
├── project-B/
│   └── .venv/  (has scikit-learn 1.5)
└── project-C/
    └── .venv/  (has whatever C needs)
```

## Creating a Virtual Environment

### Method 1: Using `venv` (built-in)

```bash
# Navigate to your project
cd my-ml-project

# Create a virtual environment
python -m venv .venv

# Activate it
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate

# Your prompt changes to show you're in the venv:
(.venv) $
```

### Method 2: Using `uv` (modern, faster)

```bash
# Install uv (once)
pip install uv

# Create and activate environment
uv venv
source .venv/bin/activate  # macOS/Linux
```

**Why `uv`?**
- 10-100x faster than pip
- Better dependency resolution
- Modern tool adopted by industry
- We use it in this course!

## Working with Virtual Environments

### Checking if You're in a venv

```bash
# Your prompt should show (.venv)
(.venv) $ which python
# Output: /path/to/your/project/.venv/bin/python

# NOT: /usr/bin/python (system Python)
```

### Installing Packages

```bash
# Make sure you're activated first!
(.venv) $ pip install pandas scikit-learn

# Check what's installed
(.venv) $ pip list
```

### Deactivating

```bash
(.venv) $ deactivate
# Prompt returns to normal
$
```

### Common Mistakes

❌ **DON'T:**
```bash
# Installing without activating
$ pip install pandas  # Goes to system Python!

# Committing .venv to git
git add .venv/  # NO! Too large, machine-specific
```

✅ **DO:**
```bash
# Always activate first
$ source .venv/bin/activate
(.venv) $ pip install pandas

# Add .venv to .gitignore
echo ".venv/" >> .gitignore
```

## The .gitignore File

**ALWAYS** add this to your `.gitignore`:

```gitignore
# Virtual environments
.venv/
venv/
env/
ENV/

# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# Jupyter
.ipynb_checkpoints/

# Data files (if large)
data/*.csv
data/*.pkl
*.h5

# Model files (if large)
models/*.keras
*.pkl

# Results
results/
```

---

# PART 2: Dependency Management (30 min)

## The Reproducibility Problem

**Scenario:**
```
You: "My project works perfectly!"
TA: "I get errors when I run it..."
You: "But it works on my machine!"
```

**Why?** Different package versions.

## Solution 1: requirements.txt

### Creating requirements.txt

```bash
# Activate your venv
source .venv/bin/activate

# Install packages
pip install pandas scikit-learn matplotlib

# Save EVERYTHING
pip freeze > requirements.txt

# OR: List only what you directly use (better!)
# Create requirements.txt manually:
cat > requirements.txt << EOF
pandas==2.1.0
scikit-learn==1.3.0
matplotlib==3.8.0
numpy==1.24.3
EOF
```

### Using requirements.txt

```bash
# Someone else clones your project
git clone https://github.com/yourname/project.git
cd project

# Create their own venv
python -m venv .venv
source .venv/bin/activate

# Install YOUR exact versions
pip install -r requirements.txt

# Now it works the same way!
```

### requirements.txt Best Practices

**❌ Bad requirements.txt:**
```txt
# Generated with pip freeze - too many dependencies!
pandas==2.1.0
numpy==1.24.3
python-dateutil==2.8.2
pytz==2023.3
six==1.16.0
...
# 50+ packages, most are sub-dependencies
```

**✅ Good requirements.txt:**
```txt
# Only direct dependencies
pandas==2.1.0
scikit-learn==1.3.0
matplotlib==3.8.0

# Or without versions (gets latest compatible):
pandas
scikit-learn
matplotlib
```

**✅ Even better - with comments:**
```txt
# Data processing
pandas==2.1.0
numpy==1.24.3

# Machine learning
scikit-learn==1.3.0
tensorflow==2.15.0

# Visualization
matplotlib==3.8.0
seaborn==0.12.2

# Development tools (optional)
jupyter
ipython
```

## Solution 2: pyproject.toml (Modern)

### What is pyproject.toml?

The **modern Python standard** for project configuration. Replaces:
- `requirements.txt`
- `setup.py`
- `setup.cfg`
- Various config files

### Example pyproject.toml

```toml
[project]
name = "house-price-prediction"
version = "0.1.0"
description = "ML project for predicting house prices"
authors = [
    {name = "Anna Smirnova", email = "anna@unil.ch"}
]
requires-python = ">=3.9"

dependencies = [
    "pandas>=2.0.0",
    "scikit-learn>=1.3.0",
    "matplotlib>=3.7.0",
    "numpy>=1.24.0",
]

[project.optional-dependencies]
dev = [
    "jupyter",
    "pytest",
    "black",
    "ruff",
]

[tool.ruff]
line-length = 100
```

### Using pyproject.toml with uv

```bash
# Install from pyproject.toml
uv pip install -e .

# Install with dev dependencies
uv pip install -e ".[dev]"

# Lock dependencies (like package-lock.json)
uv pip compile pyproject.toml -o requirements.txt
```

## pip vs uv: What's the Difference?

| Feature | pip | uv |
|---------|-----|-----|
| Speed | Slow (minutes) | Fast (seconds) |
| Dependency resolution | Basic | Advanced |
| Lockfiles | Manual | Built-in |
| Industry adoption | Universal | Growing |
| When to use | Always works | When speed matters |

**For this course:** Use `uv` if comfortable, otherwise `pip` is fine.

## Complete Reproducibility Workflow

### Scenario: Starting a New Project

```bash
# 1. Create project directory
mkdir house-price-prediction
cd house-price-prediction

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate

# 3. Install packages
pip install pandas scikit-learn matplotlib

# 4. Create requirements.txt (manual is better)
cat > requirements.txt << EOF
pandas>=2.0
scikit-learn>=1.3
matplotlib>=3.7
EOF

# 5. Create .gitignore
cat > .gitignore << EOF
.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
data/
results/
EOF

# 6. Write code...

# 7. Test reproducibility
deactivate
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py  # Should work!
```

### Scenario: Cloning Someone Else's Project

```bash
# 1. Clone the repository
git clone https://github.com/someone/project.git
cd project

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the project
python main.py
```

---

# PART 3: Project Structure (40 min)

## The Standard ML Project Structure

```
my-ml-project/
├── .venv/                # Virtual environment (DON'T commit)
├── .gitignore           # What NOT to commit
├── README.md            # Project documentation
├── requirements.txt     # Dependencies
├── pyproject.toml       # Modern alternative to requirements.txt
│
├── data/
│   ├── raw/             # Original, immutable data
│   │   └── dataset.csv
│   └── processed/       # Cleaned, preprocessed data
│       └── dataset_clean.csv
│
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py   # Functions to load/clean data
│   ├── features.py      # Feature engineering
│   ├── model.py         # Model training/evaluation
│   ├── visualization.py # Plotting functions
│   └── utils.py         # Helper functions
│
├── results/
│   ├── figures/         # Plots and visualizations
│   │   ├── correlation_matrix.png
│   │   └── model_performance.png
│   ├── metrics.txt      # Model performance metrics
│   └── model.pkl        # Saved model (if not too large)
│
├── tests/               # Unit tests (optional but good!)
│   ├── test_data_loader.py
│   └── test_model.py
│
└── main.py              # Main script to run everything
```

## What Goes Where? (Detailed)

### `/data/`

**`raw/`** - Original datasets, NEVER modified
- Downloaded CSVs, JSON files
- Keep URLs or source in README
- Add to `.gitignore` if large (>10MB)

**`processed/`** - Cleaned data ready for modeling
- Output of preprocessing scripts
- Scaled, encoded, split data
- Also add to `.gitignore` if large

### `/notebooks/`

Jupyter notebooks for **exploration** and **presentation**, NOT production code.

Name them numerically for order:
- `01_exploration.ipynb` - EDA, visualizations
- `02_preprocessing.ipynb` - Data cleaning
- `03_modeling.ipynb` - Model experiments
- `04_results.ipynb` - Final results for presentation

**Best practices:**
- Save with outputs for grading
- Keep them short (<100 cells)
- Extract reusable code to `src/`

### `/src/`

Reusable Python modules (`.py` files).

**`__init__.py`** - Makes `src/` a Python package (can be empty)

**`data_loader.py`** - Data loading and cleaning
```python
def load_housing_data(filepath):
    """Load and basic clean housing data."""
    df = pd.read_csv(filepath)
    df = df.dropna()
    return df
```

**`features.py`** - Feature engineering
```python
def create_features(df):
    """Create new features from raw data."""
    df['price_per_sqft'] = df['price'] / df['sqft']
    return df
```

**`model.py`** - Model training
```python
def train_model(X_train, y_train):
    """Train Random Forest model."""
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    return model
```

**`visualization.py`** - Plotting functions
```python
def plot_confusion_matrix(y_true, y_pred):
    """Plot confusion matrix."""
    # ...
```

**`utils.py`** - Helper functions that don't fit elsewhere

### `/results/`

All outputs from your analysis:
- Plots: `figures/*.png`
- Metrics: `metrics.txt` or `metrics.json`
- Trained models: `model.pkl` (if small)

**Add to `.gitignore` if:**
- Models are >100MB
- Hundreds of plots
- Can be regenerated easily

### `main.py`

The **entry point** to your project. Should be simple and readable.

```python
"""
House Price Prediction - Main Script
Run this to reproduce the full analysis.
"""
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from src.data_loader import load_housing_data
from src.features import create_features
from src.model import train_model, evaluate_model
from src.visualization import plot_predictions

def main():
    print("=" * 60)
    print("House Price Prediction Pipeline")
    print("=" * 60)

    # Load data
    print("\n1. Loading data...")
    df = load_housing_data('data/raw/housing.csv')
    print(f"   Loaded {len(df)} samples")

    # Feature engineering
    print("\n2. Creating features...")
    df = create_features(df)

    # Split features and target
    X = df.drop('price', axis=1)
    y = df['price']

    # Train/test split
    print("\n3. Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    print("\n4. Training model...")
    model = train_model(X_train, y_train)

    # Evaluate
    print("\n5. Evaluating model...")
    metrics = evaluate_model(model, X_test, y_test)
    print(f"   R² Score: {metrics['r2']:.3f}")
    print(f"   RMSE: {metrics['rmse']:.2f}")

    # Visualize
    print("\n6. Creating visualizations...")
    plot_predictions(y_test, model.predict(X_test),
                    save_path='results/figures/predictions.png')

    print("\n" + "=" * 60)
    print("✅ Pipeline complete! Check results/ for outputs.")
    print("=" * 60)

if __name__ == "__main__":
    main()
```

## The Minimal Version (For This Course)

If full structure feels overwhelming:

```
my-ml-project/
├── .venv/               # Virtual environment
├── .gitignore
├── README.md
├── requirements.txt
├── data/
│   └── dataset.csv
├── notebooks/
│   └── analysis.ipynb
├── src/
│   └── model.py
├── results/
│   └── figures/
└── main.py
```

**Must-haves for grading:**
1. ✅ README with setup instructions
2. ✅ requirements.txt
3. ✅ main.py that runs
4. ✅ Notebooks with outputs saved

## The README.md Template

Your README is the **first thing** anyone sees. Make it count!

```markdown
# House Price Prediction

## Overview
Predicts house prices using Random Forest regression on the California Housing dataset.
The model achieves an R² score of 0.81 on the test set.

## Authors
- Anna Smirnova (anna.smirnova@unil.ch)
- Advanced Programming 2025 - UNIL

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourname/house-price-prediction.git
cd house-price-prediction
```

### 2. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Quick start
```bash
python main.py
```

This will:
1. Load the California Housing dataset
2. Preprocess and create features
3. Train a Random Forest model
4. Evaluate and save results to `results/`

### Explore the notebooks
```bash
jupyter notebook
```

Then open:
- `notebooks/01_exploration.ipynb` - Data exploration
- `notebooks/02_modeling.ipynb` - Model experiments

## Results

- **Model:** Random Forest Regressor
- **R² Score:** 0.81
- **RMSE:** $42,500
- **Best features:** Median income, location, average rooms

See `results/figures/` for visualizations.

## Data

- **Source:** sklearn.datasets.fetch_california_housing
- **Samples:** 20,640 houses
- **Features:** 8 (median income, house age, rooms, etc.)
- **Target:** Median house value

## Project Structure

```
├── data/           # Datasets
├── notebooks/      # Jupyter notebooks
├── src/            # Source code modules
├── results/        # Outputs (plots, metrics)
├── main.py         # Main pipeline script
└── README.md       # This file
```

## Dependencies

- Python 3.9+
- pandas 2.0+
- scikit-learn 1.3+
- matplotlib 3.7+

See `requirements.txt` for full list.

## License

MIT License - Feel free to use for learning!
```

---

# PART 4: Hands-on Workshop (20 min)

## Live Demo: Creating a Project from Scratch

Let's create a real ML project together!

### Step-by-step Setup

```bash
# 1. Create project directory
mkdir iris-classifier
cd iris-classifier

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate

# 3. Install packages
pip install pandas scikit-learn matplotlib seaborn jupyter

# 4. Create requirements.txt
cat > requirements.txt << 'EOF'
pandas>=2.0
scikit-learn>=1.3
matplotlib>=3.7
seaborn>=0.12
jupyter
EOF

# 5. Create directory structure
mkdir -p data/{raw,processed}
mkdir -p notebooks
mkdir -p src
mkdir -p results/figures
mkdir -p tests

# 6. Create .gitignore
cat > .gitignore << 'EOF'
.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
data/
results/
*.pkl
EOF

# 7. Create __init__.py
touch src/__init__.py

# 8. Create README
cat > README.md << 'EOF'
# Iris Classifier

Machine learning project to classify iris species.

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```
EOF

# 9. Initialize git
git init
git add .
git commit -m "Initial project structure"
```

### Quick src/ modules

**`src/data_loader.py`:**
```python
from sklearn.datasets import load_iris
import pandas as pd

def load_iris_data():
    """Load iris dataset as pandas DataFrame."""
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names
```

**`src/model.py`:**
```python
from sklearn.ensemble import RandomForestClassifier

def train_classifier(X_train, y_train):
    """Train Random Forest classifier."""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model
```

**`main.py`:**
```python
from sklearn.model_selection import train_test_split
from src.data_loader import load_iris_data
from src.model import train_classifier

def main():
    # Load data
    df, target_names = load_iris_data()
    X = df.drop('species', axis=1)
    y = df['species']

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train
    model = train_classifier(X_train, y_train)

    # Evaluate
    accuracy = model.score(X_test, y_test)
    print(f"Test Accuracy: {accuracy:.3f}")

if __name__ == "__main__":
    main()
```

---

## Common Issues and Solutions

### Issue 1: "Module not found"

```python
# Error: ModuleNotFoundError: No module named 'src'
from src.model import train_model
```

**Solution:** Add project root to Python path in `main.py`:
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from src.model import train_model  # Now works!
```

### Issue 2: "It works in Jupyter but not main.py"

**Cause:** Jupyter uses notebook's directory as working directory.

**Solution:** Use relative paths from project root:
```python
# ❌ In notebook: works
df = pd.read_csv('dataset.csv')

# ✅ In main.py: always works
df = pd.read_csv('data/raw/dataset.csv')
```

### Issue 3: "requirements.txt doesn't work on other machine"

**Cause:** Platform-specific dependencies or missing versions.

**Solution:** Test locally:
```bash
# Simulate fresh install
deactivate
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py  # Should work!
```

### Issue 4: "My .venv is 2GB!"

**Cause:** Installed too many packages, or large models.

**Solution:**
```bash
# See what's taking space
du -sh .venv/

# Start fresh with only what you need
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
pip install pandas scikit-learn matplotlib  # Only essentials!
```

---

## Quick Reference: Common Commands

```bash
# Virtual environments
python -m venv .venv                 # Create venv
source .venv/bin/activate            # Activate (macOS/Linux)
.venv\Scripts\activate               # Activate (Windows)
deactivate                           # Deactivate

# Dependencies
pip install <package>                # Install package
pip install -r requirements.txt      # Install from file
pip freeze > requirements.txt        # Save all packages
pip list                             # Show installed packages

# Project setup
mkdir -p project/{data,src,results}  # Create directories
touch src/__init__.py                # Make Python package
git init                             # Initialize git

# Running
python main.py                       # Run main script
jupyter notebook                     # Start Jupyter
pytest                               # Run tests (if you have them)
```

---

## Submission Checklist

Before submitting your project, verify:

- [ ] **Virtual environment**
  - [ ] `.venv/` exists locally
  - [ ] `.venv/` is in `.gitignore`
  - [ ] Can recreate environment from `requirements.txt`

- [ ] **Dependencies**
  - [ ] `requirements.txt` exists
  - [ ] Lists all necessary packages
  - [ ] Tested: fresh install → run → works

- [ ] **Code**
  - [ ] `main.py` runs without errors
  - [ ] No hardcoded absolute paths
  - [ ] Imports work correctly
  - [ ] Code has comments

- [ ] **Documentation**
  - [ ] `README.md` exists and is complete
  - [ ] Includes setup instructions
  - [ ] Includes usage examples
  - [ ] Describes results

- [ ] **Notebooks**
  - [ ] Saved with outputs visible
  - [ ] Cells run in order
  - [ ] Markdown explanations included

- [ ] **Results**
  - [ ] Outputs saved in `results/`
  - [ ] Plots are clear and labeled
  - [ ] Metrics are documented

- [ ] **Git** (if applicable)
  - [ ] `.gitignore` includes `.venv/`, `__pycache__/`, etc.
  - [ ] No large files committed
  - [ ] Meaningful commit messages

---

## For Grading: What We Look For

| Category | Weight | Criteria |
|----------|--------|----------|
| **Reproducibility** | 40% | Can we run it? Does `pip install -r requirements.txt && python main.py` work? |
| **Organization** | 20% | Logical structure, proper file locations, clean code |
| **Documentation** | 20% | Clear README, code comments, notebook explanations |
| **Correctness** | 20% | Model works, proper ML workflow, reasonable results |

---

## Additional Resources

### Tools
- **cookiecutter-data-science**: Project template generator
- **uv**: Fast Python package installer
- **ruff**: Fast Python linter
- **black**: Code formatter

### Learn More
- [Python Packaging User Guide](https://packaging.python.org/)
- [Real Python: Virtual Environments](https://realpython.com/python-virtual-environments/)
- [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)

---

**Remember:**
- Good project structure takes 30 minutes to set up
- Saves hours of debugging later
- Makes collaboration possible
- Impresses graders (and future employers!)

**When in doubt:**
1. Create a venv
2. Make a requirements.txt
3. Write a README
4. Organize your code
