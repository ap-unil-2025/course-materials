---
marp: true
paginate: true
header: "Session 8: sklearn in Practice"
footer: "Anna Smirnova, November 3, 2025"
style: |
  section {
    font-size: 22px;
  }
  section.lead {
    font-size: 28px;
    background: #003aff;
    color: white;
  }
  section.lead footer, section.lead header, section.lead h1, section.lead h2, section.lead h3 {
    color: white;
  }
---

<!-- _class: lead -->

# sklearn in Practice
## Combined Regression + Classification Session

**Because you missed Week 7 due to midterms**

---

# Today's Combined Session

We're covering **both** regression (Week 7) and classification (Week 8) today!

**15 min:** Common mistakes & debugging
**30 min:** Hands-on exercise

**File:** `ml_regression_classification_starter.py`
- Part 1: Regression (house prices)
- Part 2: Classification (iris, students)
- Part 3: Mini project
- Bonus: Advanced challenges

---

# The sklearn Recipe (Always the Same)

```python
from sklearn.whatever import TheModel
from sklearn.model_selection import train_test_split

# 1. Split your data FIRST
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 2. Create model
model = TheModel()

# 3. Train (fit)
model.fit(X_train, y_train)

# 4. Predict
y_pred = model.predict(X_test)

# 5. Evaluate
score = model.score(X_test, y_test)
```

**This works for Linear Regression, KNN, Decision Trees, everything.**

---

# Common Error #1: Shape Mismatches

```python
# ❌ WRONG - X must be 2D
X = [1, 2, 3, 4, 5]
model.fit(X, y)  # ValueError: Expected 2D array

# ✅ RIGHT - Reshape to 2D
X = [[1], [2], [3], [4], [5]]
# Or: X = np.array([1,2,3,4,5]).reshape(-1, 1)
model.fit(X, y)
```

**Rule:** X is always 2D (samples × features), y is always 1D

**Always print shapes when debugging:**
```python
print(f"X: {X.shape}, y: {y.shape}")
# X: (100, 5), y: (100,) ✅
```

---

# Common Error #2: Testing on Training Data

```python
# ❌ DISASTER - 100% accuracy that means nothing
model.fit(X, y)
score = model.score(X, y)

# ✅ CORRECT - Real test performance
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
```

**The #1 beginner mistake:** Never test on data you trained on!

---

# Common Error #3: Forgetting to Scale for KNN

```python
# Dataset: [house_size_sqft, bedrooms]
# [[2000, 3], [1500, 2], [1800, 3]]

# ❌ KNN without scaling - size dominates everything!
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# ✅ KNN with scaling - features balanced
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
knn.fit(X_scaled, y)
```

**When to scale:** KNN, SVM, Neural Networks
**When NOT to scale:** Decision Trees, Random Forest

---

# Regression vs Classification

**Regression:** Predict a number
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
price = model.predict([[1800, 3, 10]])  # $245,000
```

**Classification:** Predict a category
```python
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
species = model.predict([[5.1, 3.5, 1.4, 0.2]])  # "Setosa"
```

**Same workflow, different outputs!**

---

# Debugging: "My Model Sucks"

**Train: 95%, Test: 60%** → **Overfitting** (memorized data)
- Fix: Simpler model, more data, regularization

**Train: 65%, Test: 62%** → **Underfitting** (too simple)
- Fix: More complex model, better features

**Train: 50%, Test: 50%** (binary) → **Random guessing** (learned nothing)
- Fix: Check data quality, try different features

**Train: 50%, Test: 85%** → **You got lucky** (probably data leakage)
- Fix: Check your train/test split!

---

# Quick Reference: Evaluation Metrics

**Regression:**
```python
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, y_pred)   # Lower = better
r2 = r2_score(y_test, y_pred)              # 0 to 1, higher = better
```

**Classification:**
```python
from sklearn.metrics import accuracy_score, confusion_matrix

acc = accuracy_score(y_test, y_pred)      # Higher = better
cm = confusion_matrix(y_test, y_pred)     # Shows mistakes
```

---

# Confusion Matrix: Where Your Model Fails

```python
cm = confusion_matrix(y_test, y_pred)
print(cm)

#           Predicted
#           Cat  Dog
# Actual Cat [45] [5]   ← 5 cats wrongly called dogs
#        Dog [3]  [47]  ← 3 dogs wrongly called cats
```

**Diagonal = correct**
**Off-diagonal = mistakes**

Use this to see WHAT your model confuses!

---

# Pro Tips

**1. Start Simple, Then Optimize**
```python
# ✅ Start here
model = LinearRegression()

# ❌ Don't start here
model = GradientBoostingRegressor(
    n_estimators=500,
    learning_rate=0.001,
    max_depth=10,
    subsample=0.8
)
```

**2. Always Print Shapes**
```python
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
```

**3. Use random_state=42** (or any number) for reproducibility

---

# Exercise Structure

**Part 1: Regression**
- Predict house prices
- Multiple features
- Evaluate with MSE and R²

**Part 2: Classification**
- Iris species (KNN vs Decision Tree)
- Student pass/fail predictor
- Confusion matrices

**Part 3: Bonus Challenges**
- Level 1: Feature importance, residual analysis, scaling experiments
- Level 2: SHAP, decision boundaries, overfitting detection, Yellowbrick

---

<!-- _class: lead -->

# Let's Code!

Open: `ml_regression_classification_starter.py`

**Questions before we start?**
