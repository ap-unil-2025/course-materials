---
marp: true
paginate: true
theme: unil
header: "Week 11: Project Workshop"
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

# Week 11: Project Workshop

**Debugging · Environments · Project Structure**

---

# Today's Session

**Part 1: Debugging**
- Common bugs and how to find them
- Reading error messages
- Exception handling

**Part 2: Environment Management**
- Conda on Nuvolos (main platform)
- Local Python: venv/uv (optional)

**Part 3: Project Structure**
- Standard ML project layout
- README and reproducibility: `requirements.txt` / `environment.yml`

---

# Why This Matters

**3 weeks until project deadline (Dec 21)**

Your project needs to:
- ✅ Run on our machines 
- ✅ Have clear structure
- ✅ Be well-documented
- ✅ Handle errors gracefully


---

# Types of Bugs

**1. Syntax Errors** - Python can't parse your code
```python
if x > 5  # Missing colon
```

**2. Runtime Errors** - Crashes during execution
```python
result = 10 / 0  # ZeroDivisionError
```

**3. Logic Errors** - Code runs but produces wrong results
```python
def calculate_discount(price, percent):
    return price + (price * percent)  # Should be minus!
```

---

# Reading Error Messages

```python
Traceback (most recent call last):
  File "script.py", line 15, in <module>
    result = divide(10, 0)
  File "script.py", line 3, in divide
    return a / b
ZeroDivisionError: division by zero
```

**How to read:**
1. Start from **bottom** - that's the actual error
2. Work **up** to see the call chain
3. Look for **your code** (not library code)
4. **Line numbers** tell you exactly where

---

# Debugging Strategy 1: Print Debugging

**The simplest tool:** Add `print()` statements!

```python
def calculate_discount(price, discount_percent):
    print(f"DEBUG: price={price}, discount={discount_percent}")

    discount_amount = price * discount_percent
    print(f"DEBUG: discount_amount={discount_amount}")

    final_price = price - discount_amount
    print(f"DEBUG: final_price={final_price}")

    return final_price
```

**Pro tip:** Use a DEBUG flag to turn off in production

---

# Debugging Strategy 2: Debugger

**VSCode/Jupyter visual debugging:**
- Click left of line number → breakpoint
- Run in debug mode
- Step through code line by line
- Inspect variables

**Controls:**
- **Continue (F5):** Run until next breakpoint
- **Step Over (F10):** Execute current line
- **Step Into (F11):** Go inside function calls

---

# Exception Handling

**Without handling** (program crashes):
```python
def divide(a, b):
    return a / b

result = divide(10, 0)  # 💥 Crash!
```
---
# Exception Handling

**With handling** (program continues):
```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

result = divide(10, 0)  # Handles gracefully
print("Program continues")
```

---

# Common Python Exceptions (1/2)

```python
# ValueError - Wrong value
age = int("twenty")

# TypeError - Wrong type
result = 'foo' + 6

# IndexError - List index out of range
L = [1, 2, 3]
print(L[10])
```

---

# Common Python Exceptions (2/2)

```python
# KeyError - Dictionary key doesn't exist
person = {'name': 'Alice'}
age = person['age']

# FileNotFoundError - File doesn't exist
f = open('missing.txt', 'r')
```

**Add try-except for file I/O in your projects!**

---

# Multiple Exception Handling

```python
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print(f"Error: Cannot divide {type(a)} by {type(b)}")
        return None
    finally:
        print("Division operation completed")  # Always runs
```

**Best Practice:** Catch specific exceptions, not all!

---

# ML-Specific Debugging

**Now let's talk about what actually breaks in ML projects...**

---

# Common ML Bug 1: Shape Mismatches

```python
# Your error:
ValueError: X has 2 features, but RandomForest expects 5

# What happened?
X_train = df[['age', 'income', 'score', 'years', 'rating']]
model.fit(X_train, y_train)

# Later, you forgot columns:
X_test = df[['age', 'income']]  # Only 2 features!
predictions = model.predict(X_test)  # 💥 Crash!
```

**Debug it:**
```python
print(f"Train shape: {X_train.shape}")  # (1000, 5)
print(f"Test shape: {X_test.shape}")    # (200, 2) <- AHA!
print(f"Train columns: {list(X_train.columns)}")
print(f"Test columns: {list(X_test.columns)}")
```

---

# Common ML Bug 2: Wrong Data Types

```python
# Your error:
ValueError: could not convert string to float: 'yes'

# What happened?
df = pd.read_csv('data.csv')
X = df.drop('target', axis=1)
model.fit(X, y)  # 💥 Crash!

# Your data has strings!
```
---
# Common ML Bug 2: Wrong Data Types
**Debug it:**
```python
print(df.dtypes)  # Check data types
print(df.head())  # Look at actual values

# Found the problem:
# category    object  <- This should be numeric!
# age         int64
# income      float64
```

**Fix it:**
```python
# Encode categorical variables
X = pd.get_dummies(df.drop('target', axis=1))
```

---

# Common ML Bug 3: Missing Values

```python
# Your error:
ValueError: Input contains NaN

# What happened?
df = pd.read_csv('data.csv')
X = df.drop('target', axis=1)
model.fit(X, y)  # 💥 Crash!
```

**Debug it:**
```python
print(df.isnull().sum())  # Count NaNs per column
# age        0
# income     45  <- 45 missing values!
# score      12
```
---
# Common ML Bug 3: Missing Values

**Fix it:**
```python
# Option 1: Drop rows with NaN
df = df.dropna()

# Option 2: Fill with mean/median
df['income'].fillna(df['income'].mean(), inplace=True)

# Option 3: Use a model that handles NaN
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)
```

---

# Common ML Bug 4: Not Scaling

```python
# Your model performs terribly
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
print(f"Accuracy: {knn.score(X_test, y_test)}")  # 0.52 😢

# Your data:
print(X_train.head())
#    age  income   score
# 0   25  150000     0.8
# 1   45   80000     0.6
```

**The problem:** Income dominates! (150000 vs 0.8)

---
# Common ML Bug 4: Not Scaling

**Fix it:**
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn.fit(X_train_scaled, y_train)
print(f"Accuracy: {knn.score(X_test_scaled, y_test)}")  # 0.87 ✅
```

---

# Common ML Bug 5: Data Leakage

```python
# Your training accuracy: 99%
# Your test accuracy: 60%
# What went wrong?

# ❌ WRONG: Scaled before split
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Leak! Used test info
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)

# ✅ RIGHT: Split first, then scale
X_train, X_test, y_train, y_test = train_test_split(X, y)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Fit on train only
X_test_scaled = scaler.transform(X_test)        # Transform test
```

---

# Debugging ML Performance

**Your model accuracy is terrible. Now what?**

```python
# Step 1: Check your baseline
print(f"Majority class: {y.value_counts()}")
# 0    700
# 1    300
# Baseline accuracy: 70% (always predict 0)

# Your model: 52% <- WORSE than baseline!
```

**Possible issues:**
- Data not shuffled
- Features not scaled
- Wrong model for the problem
- Bugs in preprocessing

---

# Debugging Strategy for ML

**1. Print shapes everywhere**
```python
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
```

**2. Check data types**
```python
print(X_train.dtypes)
print(X_train.isnull().sum())
```
---
# Debugging Strategy for ML
**3. Look at the data**
```python
print(X_train.head())
print(X_train.describe())
```

**4. Check intermediate outputs**
```python
predictions = model.predict(X_test[:5])
print(f"First 5 predictions: {predictions}")
print(f"First 5 actual: {y_test[:5]}")
```

---

# ML Debugging Checklist

Before asking for help, check:

- [ ] Shape matches: `X_train.shape[1] == X_test.shape[1]`
- [ ] No NaN values: `X.isnull().sum()`
- [ ] Correct data types: `X.dtypes`
- [ ] Train/test split done: not using same data
- [ ] Features scaled (for KNN, SVM, neural nets)
- [ ] Categories encoded: no strings in X
- [ ] Correct target format: 1D for classification
- [ ] Model matches problem: classifier for classification

---

# Debugging with Visualizations
```python
import matplotlib.pyplot as plt

# 1. Plot predictions vs actual
plt.scatter(y_test, predictions)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()], 'r--')
plt.show()

# 2. Plot confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, predictions)
print(cm)

# 3. Plot feature distributions
X_train.hist(figsize=(12, 8))
plt.show()
```

---

# Common sklearn Error Messages (1/3)

**Error:** `ValueError: Found input variables with inconsistent numbers of samples`

**What it means:** X and y have different lengths

```python
X = [[1, 2], [3, 4], [5, 6]]  # 3 samples
y = [0, 1]                     # 2 samples - MISMATCH!
model.fit(X, y)  # 💥
```

**Fix:**
```python
print(f"X length: {len(X)}")  # 3
print(f"y length: {len(y)}")  # 2
# Check your data loading!
```

---

# Common sklearn Error Messages (2/3)

**Error:** `ValueError: X has 5 features, but this RandomForestClassifier is expecting 8`

**What it means:** Train and predict use different features

```python
# Training
X_train = df[['age', 'income', 'score', 'rating', 'years']]
model.fit(X_train, y_train)  # 5 features

# Prediction - oops, added more columns!
X_test = df[['age', 'income', 'score', 'rating', 'years',
             'new_col', 'another', 'yet_another']]
model.predict(X_test)  # 💥 Expects 5, got 8!
```

**Fix:** Keep features consistent!
```python
feature_columns = ['age', 'income', 'score', 'rating', 'years']
X_train = df_train[feature_columns]
X_test = df_test[feature_columns]  # Same columns!
```

---

# Common sklearn Error Messages (3/3)

**Error:** `ValueError: could not convert string to float: 'Male'`

**What it means:** Non-numeric data in your features

```python
df = pd.read_csv('data.csv')
print(df.dtypes)
# age        int64
# income     float64
# gender     object  <- Problem!

X = df.drop('target', axis=1)
model.fit(X, y)  # 💥
```
---
# Common sklearn Error Messages (3/3)

**Fix:** Encode categorical variables
```python
# Option 1: One-hot encoding
X = pd.get_dummies(df.drop('target', axis=1))

# Option 2: Label encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])
```

---

# Common ML Bug 6: Reproducibility

**The problem:** Results change every time!

```python
# Run 1
model = RandomForestClassifier()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))  # 0.87

# Run 2 - different result!
model = RandomForestClassifier()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))  # 0.84  <- Different!
```

**Why?** Random initialization in many ML algorithms

---

# Reproducibility: The Fix

**Use random_state everywhere!**

```python
# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42  # ✅
)

# Models
rf = RandomForestClassifier(random_state=42)  # ✅
knn = KNeighborsClassifier()  # ✅ No random state needed
nn = MLPClassifier(random_state=42)  # ✅

# Data shuffling
df = df.sample(frac=1, random_state=42)  # ✅
```

**Pro tip:** Pick one number (42, 0, 123) and use it everywhere

---

# Reproducibility Checklist

For reproducible results, set random_state in:

- [ ] `train_test_split(random_state=42)`
- [ ] `RandomForestClassifier(random_state=42)`
- [ ] `DecisionTreeClassifier(random_state=42)`
- [ ] `KMeans(random_state=42)`
- [ ] `df.sample(random_state=42)`
- [ ] Neural networks: `MLPClassifier(random_state=42)`
- [ ] Deep learning: `np.random.seed(42)`, `tf.random.set_seed(42)`

**Document it in your README!**

---

# Common ML Bug 7: Overfitting

**The symptoms:**
```python
train_score = model.score(X_train, y_train)  # 0.99
test_score = model.score(X_test, y_test)     # 0.65

print(f"Train: {train_score:.2f}")  # 99%
print(f"Test: {test_score:.2f}")    # 65%
```

**Big gap = Overfitting!** Model memorized training data

---

# Detecting Overfitting

**Compare train vs test performance:**

```python
from sklearn.model_selection import train_test_split

# Split your data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier(max_depth=50)  # Very deep!
model.fit(X_train, y_train)

# Compare
train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)

print(f"Train: {train_acc:.2f}")  # 0.99
print(f"Test: {test_acc:.2f}")    # 0.67
print(f"Gap: {train_acc - test_acc:.2f}")  # 0.32 <- Too big!
```

**Rule of thumb:** Gap > 0.1 = probably overfitting

---

# Fixing Overfitting (1/2)

**Strategy 1: Simplify your model**
```python
# ❌ Too complex
rf = RandomForestClassifier(n_estimators=1000, max_depth=50)

# ✅ Simpler
rf = RandomForestClassifier(n_estimators=100, max_depth=10)
```

**Strategy 2: Get more data**
```python
# More training data → harder to memorize
```

**Strategy 3: Use regularization**
```python
from sklearn.linear_model import LogisticRegression

# C parameter: smaller = more regularization
model = LogisticRegression(C=0.1)  # Strong regularization
```

---

# Fixing Overfitting (2/2)

**Strategy 4: Cross-validation**
```python
from sklearn.model_selection import cross_val_score

# Test on multiple splits
scores = cross_val_score(model, X, y, cv=5)
print(f"CV scores: {scores}")
print(f"Mean: {scores.mean():.3f}")
print(f"Std: {scores.std():.3f}")

# High std = unstable model (might be overfitting)
```

**Strategy 5: Feature selection**
```python
# Remove features that might cause overfitting
from sklearn.feature_selection import SelectKBest

selector = SelectKBest(k=10)  # Keep only 10 best features
X_selected = selector.fit_transform(X, y)
```

---

<!-- _class: lead -->

# PART 2
## Environment Management

---

# Two Options for Python Environments

**Option 1: Conda on Nuvolos** (recommended for course)
- Pre-installed on Nuvolos
- Easy to share environments
- Works with Jupyter notebooks

**Option 2: Local Python with venv/uv** (optional)
- For working on your own laptop
- More control
- Industry standard

**Most of you: Use Nuvolos!**

---

# Option 1: Conda on Nuvolos

**What is conda?**
- Package and environment manager
- Pre-installed on Nuvolos
- Creates isolated environments

**Why use it?**
- Different projects need different packages
- Avoids version conflicts
- Makes your project reproducible

---

# Creating Conda Environment on Nuvolos

```bash
# Create environment
conda create -n myproject python=3.11

# Activate it
conda activate myproject

# Install packages
conda install pandas scikit-learn matplotlib
```

---

# Using Conda Environment

```bash
# Already activated your environment
conda activate myproject

# Or use pip within conda (totally fine!)
pip install seaborn

# Deactivate when done
conda deactivate
```

---

# Saving Conda Environment

**Export your environment:**
```bash
# Activate your environment
conda activate myproject

# Export to file
conda env export > environment.yml
```

**Your `environment.yml` looks like:**
```yaml
name: myproject
channels:
  - defaults
dependencies:
  - python=3.11
  - pandas=2.1.0
  - scikit-learn=1.3.0
  - matplotlib=3.8.0
```

---

# Recreating Conda Environment

**Someone else (or TA) can recreate:**
```bash
# From your environment.yml
conda env create -f environment.yml

# Activate
conda activate myproject

# Now has exact same packages!
```

**This is how we'll grade your projects on Nuvolos!**

---

# Conda Best Practices

✅ **DO:**
- One environment per project
- Export environment.yml before submission
- Test: create fresh env → run code

---

# Conda Common Mistakes

❌ **DON'T:**
- Use base environment for projects
- Forget to activate before installing
- Mix conda and pip unnecessarily (but pip is OK in conda env)

---

# Option 2: Local Python with venv

**If working on your laptop (not Nuvolos):**

```bash
# Create virtual environment
cd my-project
python -m venv .venv

# Activate
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Install packages
pip install pandas scikit-learn matplotlib

# Save dependencies
pip freeze > requirements.txt
```

---

# Option 2: Modern Alternative - uv
```bash
# Install uv (once)
pip install uv

# Create environment
cd my-project
uv venv

# Activate
source .venv/bin/activate

# Install packages (much faster!)
uv pip install pandas scikit-learn matplotlib

# Save dependencies
uv pip freeze > requirements.txt
```

**10-100x faster than regular pip!**

---

# Conda vs venv/uv

| Feature | Conda (Nuvolos) | venv + pip | venv + uv |
|---------|-----------------|------------|-----------|
| **Use case** | Course projects | Local Python | Local Python |
| **Speed** | Medium | Slow | Very fast |
| **File** | environment.yml | requirements.txt | requirements.txt |
| **Recreate** | `conda env create -f` | `pip install -r` | `uv pip install -r` |

**For this course: Use conda on Nuvolos**
**For personal projects: venv or uv**

---

# Why Project Structure Matters

**Unorganized:**
```
my_project/
├── final_FINAL_v3.py
├── test.py
├── data.csv
├── output.png
```

**Organized:**
```
my-ml-project/
├── README.md
├── environment.yml
├── main.py
├── data/
├── src/
└── results/
```

---

# Standard ML Project Structure 

```
my-ml-project/
├── environment.yml       # Conda env (or requirements.txt)
├── .gitignore
├── README.md             # REQUIRED
├── main.py               # REQUIRED - runs everything
│
├── data/
│   ├── raw/              # Original data (never modify!)
│   └── processed/        # Cleaned data (optional)
│
├── notebooks/
│   └── analysis.ipynb    # Exploration & results
│
├── src/                  # REQUIRED - your code here
│   ├── __init__.py
│   ├── data_loader.py    # Load/clean data
│   ├── model.py          # ML models
│   └── visualization.py  # Plotting functions
│
├── results/              # REQUIRED - outputs
│   ├── figures/          # Plots
│   └── metrics.txt       # Performance metrics
│
└── tests/                # OPTIONAL (but recommended)
    └── test_model.py
```

---

# What Goes Where?

| Directory | What to put here | Required? |
|-----------|------------------|-----------|
| `data/raw/` | Original datasets (**never modify**) | ✅ Yes |
| `data/processed/` | Cleaned data | Optional |
| `notebooks/` | Jupyter notebooks with outputs | ✅ Yes |
| `src/` | Reusable Python code | ✅ Yes |
| `results/` | Plots, metrics, model performance | ✅ Yes |
| `tests/` | Unit tests | Nice to have |

**Key:** Anyone should be able to run `python main.py` and reproduce your results

---

# Required Files

**✅ REQUIRED (will lose points if missing):**
- README.md with setup instructions
- environment.yml (or requirements.txt)
- main.py that runs
- src/ with organized code
- results/ with outputs
- Notebooks with cell outputs saved

---

# environment.yml vs requirements.txt

**If using conda (Nuvolos):**
```yaml
# environment.yml
name: myproject
dependencies:
  - python=3.11
  - pandas>=2.0
  - scikit-learn>=1.3
  - matplotlib>=3.7
```

**If using venv/uv (local):**
```txt
# requirements.txt
pandas>=2.0
scikit-learn>=1.3
matplotlib>=3.7
```

**Include whichever you're using!**

---

# The Sacred Rule: README.md

```markdown
# House Price Prediction

## Setup (Nuvolos)

conda env create -f environment.yml
conda activate myproject

## Setup (Local Python)

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Usage
python main.py

## Results
- Model: Random Forest
- R² Score: 0.81
```

---

# Good main.py Pattern

```python
"""
House Price Prediction. Main entry point - run this to reproduce results.
"""
from src.model import train_model
from src.data_loader import load_data

def main():
    print("Loading data...")
    X, y = load_data('data/raw/housing.csv')

    print("Training model...")
    model = train_model(X, y)

    print("Evaluating...")
    score = model.score(X_test, y_test)
    print(f"R² Score: {score:.3f}")

if __name__ == "__main__":
    main()
```

---

# The src/ Directory - What Goes Here?

**Split your code into logical modules:**

**`src/data_loader.py`** - Data loading and cleaning
```python
import pandas as pd

def load_housing_data(filepath):
    """Load and clean housing data."""
    df = pd.read_csv(filepath)
    df = df.dropna()
    return df
```
---

**`src/model.py`** - ML model training and evaluation
```python
from sklearn.ensemble import RandomForestRegressor

def train_model(X, y):
    """Train Random Forest model."""
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X, y)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate model performance."""
    score = model.score(X_test, y_test)
    return {'r2': score}
```

---

# The src/ Directory - More Examples

**`src/visualization.py`** - Plotting functions
```python
import matplotlib.pyplot as plt

def plot_predictions(y_true, y_pred, save_path):
    """Plot predictions vs actual."""
    plt.scatter(y_true, y_pred, alpha=0.5)
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.savefig(save_path)
    plt.close()
```
---

**`src/utils.py`** - Helper functions
```python
def save_metrics(metrics, filepath):
    """Save metrics to file."""
    with open(filepath, 'w') as f:
        for key, value in metrics.items():
            f.write(f"{key}: {value}\n")
```

**Why split?** Easier to test, reuse, and debug!

---

# The .gitignore File

```gitignore
# Environments
.venv/
venv/
env/

# Python
__pycache__/
*.pyc

# Jupyter
.ipynb_checkpoints/

# Data (if large)
data/*.csv
*.pkl

# Results
results/

# Note: DO commit environment.yml or requirements.txt!
```

---

# Common Mistakes (1/2)

❌ **DON'T:**
1. Hardcode paths: `pd.read_csv('/Users/anna/Desktop/data.csv')`
2. Forget environment file (environment.yml or requirements.txt)
3. No README
4. Notebooks without outputs
5. One giant 2000-line file

---

# Common Mistakes (2/2)

✅ **DO:**
1. Relative paths: `pd.read_csv('data/raw/data.csv')`
2. Include environment.yml (conda) or requirements.txt (venv)
3. Clear README with setup + usage
4. Save notebook outputs
5. Split into modules (src/)


---

# Let's Build a Complete Project

**Task:** Iris classifier with proper structure

**Time:** 15 minutes

**What we'll create:**
- Project structure
- Environment file
- Exception handling
- README
- Working code

---

# Demo Part 1: Setup (Conda)

```bash
# Create project
mkdir iris-classifier && cd iris-classifier

# Create conda environment
conda create -n iris python=3.11 -y
conda activate iris

# Install packages
conda install pandas scikit-learn matplotlib -y

# Export environment
conda env export > environment.yml
```

---

# Demo Part 2: Project Structure

```bash
# Create directories
mkdir -p data/{raw,processed}
mkdir -p notebooks
mkdir -p src
mkdir -p results/figures

# Create files
touch src/__init__.py
touch src/model.py
touch src/data_loader.py
touch main.py

# Create .gitignore
cat > .gitignore <<EOF
__pycache__/
*.pyc
.ipynb_checkpoints/
data/
results/
EOF
```

---

# Demo Part 3: Write Code with Error Handling

**`src/data_loader.py`:**
```python
from sklearn.datasets import load_iris
import pandas as pd

def load_iris_data():
    """Load iris dataset."""
    try:
        iris = load_iris()
        df = pd.DataFrame(iris.data, columns=iris.feature_names)
        df['species'] = iris.target
        return df, iris.target_names
    except Exception as e:
        print(f"Error loading data: {e}")
        raise
```

---

# Demo Part 4: Model with Error Handling

**`src/model.py`:**
```python
from sklearn.ensemble import RandomForestClassifier

def train_classifier(X_train, y_train):
    """Train Random Forest classifier."""
    try:
        if X_train.empty or len(y_train) == 0:
            raise ValueError("Training data cannot be empty")

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        print(f"Error training model: {e}")
        raise
```

---

# Demo Part 5: main.py

```python
from sklearn.model_selection import train_test_split
from src.data_loader import load_iris_data
from src.model import train_classifier

def main():
    try:
        print("Loading data...")
        df, target_names = load_iris_data()
        X = df.drop('species', axis=1)
        y = df['species']

        print("Splitting data...")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        print("Training model...")
        model = train_classifier(X_train, y_train)

        accuracy = model.score(X_test, y_test)
        print(f"✅ Test Accuracy: {accuracy:.3f}")

    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())
```

---

# Demo Part 6: README

```markdown
# Iris Classifier

Classifies iris species using Random Forest.

## Setup (Nuvolos/Conda)
conda env create -f environment.yml
conda activate iris
python main.py
## Setup (Local Python)

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py

## Results
- Model: Random Forest
- Test Accuracy: 0.97

## Project Structure
- `src/`: Source code modules
- `data/`: Datasets
- `results/`: Output plots and metrics
- `main.py`: Run this!
```

---

# Demo Part 7: Test It!

```bash
# Run it
(iris) $ python main.py
Loading data...
Splitting data...
Training model...
✅ Test Accuracy: 0.967

# Test reproducibility (conda)
$ conda deactivate
$ conda env remove -n iris
$ conda env create -f environment.yml
$ conda activate iris
$ python main.py
✅ Works!
```

---

# Submission Checklist
- [ ] environment.yml (conda) OR requirements.txt (venv)
- [ ] Tested: fresh environment → install → run
- [ ] main.py runs without errors
- [ ] No hardcoded absolute paths
- [ ] Code split into modules (src/)
- [ ] README.md with setup instructions
- [ ] Notebooks saved with outputs
- [ ] Comments explaining complex logic

---

# For Grading: What We Look For

**Reproducibility:**
- Can we run it? `conda env create -f environment.yml && python main.py`
- Fresh environment works

**Organization:**
- Proper structure: src/, data/, results/, README
- Files in logical locations

**Documentation:**
- Clear README with setup instructions
- Code comments
- Notebook explanations

---
# **Most important: Does `python main.py` work?**

---

# Your Projects: Q&A Time

**Common questions:**
- Environment issues on Nuvolos?
- Import errors?
- File path problems?
- How to structure my specific project?

**Bring your questions!**

---

# Common Issues: Solutions

**Issue 1: "Module not found"**
```python
# Add to main.py if needed:
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
```

**Issue 2: "Works in notebook but not main.py"**
- Use paths relative to project root: `data/raw/file.csv`

**Issue 3: "Environment doesn't work on TA's machine"**
- Test: delete env → recreate from file → run

---

# Quick Reference: Conda Commands (1/2)

```bash
# Create environment
conda create -n myproject python=3.11

# Activate/deactivate
conda activate myproject
conda deactivate

# Install packages
conda install pandas scikit-learn
pip install some-package  # pip works in conda!
```

---

# Quick Reference: Conda Commands (2/2)

```bash
# Export/recreate
conda env export > environment.yml
conda env create -f environment.yml

# List/remove
conda env list
conda env remove -n myproject
```

---

# Quick Reference: venv Commands (1/2)

```bash
# Create environment
python -m venv .venv

# Activate/deactivate
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
deactivate
```

---

# Quick Reference: venv Commands (2/2)

```bash
# Install packages
pip install pandas scikit-learn

# Save/restore
pip freeze > requirements.txt
pip install -r requirements.txt
```

---

# Key Takeaways (1/2)

**Debugging:**
- Read error messages bottom-up
- Use try-except for file I/O
- Add print debugging when stuck

**Environments:**
- Use conda on Nuvolos (main platform)
- venv/uv for local Python (optional)
- Export environment.yml or requirements.txt

---

# Key Takeaways (2/2)

**Structure:**
- Standard layout makes grading easier
- main.py as entry point
- src/ for reusable code
- README explains setup

**Most important:**
- Does `python main.py` work?
- Can we reproduce your results?

---

# Next Steps

**This week:**
1. ✅ Set up your project structure
2. ✅ Create conda environment (or venv locally)
3. ✅ Export environment file
4. ✅ Add exception handling
5. ✅ Write README

**Dec 21:** Project deadline

**Use today's demo as template!**

---

# Additional Resources

**Course materials:**
- Full guide: `ml_project_structure_guide.md`
- Example projects on course repo

**Nuvolos:**
- Conda documentation in Nuvolos docs
- Ask in #nuvolos-help channel

**Online:**
- [Conda cheat sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
- [Real Python: Virtual Environments](https://realpython.com/python-virtual-environments/)

---

<!-- _class: lead -->

# Questions?


---

<!-- _class: lead -->

# Good luck with your projects!

**Remember:**
1. Debug with try-except
2. Use conda on Nuvolos
3. Export environment.yml
4. Write clear README
5. Organize your code

**We're here to help!**
