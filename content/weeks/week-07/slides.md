---
marp: true
paginate: true
header: "Session 7: sklearn Survival Guide"
footer: "Anna Smirnova, October 27, 2025"
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

# sklearn Survival Guide
## Regression + Classification

**Practical tips for when theory meets reality**

---

# Today's Plan

**15 min:** Common mistakes & debugging
**30 min:** Hands-on exercise (`ml_regression_classification_starter.py`)

**Goal:** You leave with working code, not confusion

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

This pattern works for EVERYTHING in sklearn.

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

**Quick check:**
```python
print(X.shape)  # (100, 5) ← 100 samples, 5 features ✅
print(y.shape)  # (100,) ← 100 labels ✅
```

---

# Common Error #2: Forgetting to Split

```python
# ❌ DISASTER
model.fit(X, y)
score = model.score(X, y)  # Testing on training data!
print(f"Accuracy: {score}")  # 100% but meaningless

# ✅ CORRECT
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model.fit(X_train, y_train)
score = model.score(X_test, y_test)  # Real performance
```

**Never test on data you trained on!**

---

# Common Error #3: Not Scaling for KNN

```python
# Dataset: [size_sqft, bedrooms]
# [[2000, 3], [1500, 2], [1800, 3]]

# ❌ KNN without scaling
knn = KNeighborsClassifier()
knn.fit(X, y)  # Distance dominated by size!

# ✅ KNN with scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
knn.fit(X_scaled, y)  # All features matter equally
```

**When to scale:** KNN, SVM, neural networks
**When NOT to scale:** Trees, Random Forest

---

# Debugging: "My Model Sucks"

**Training accuracy: 95%, Test accuracy: 60%**
→ **Overfitting**. Model memorized training data.
- Solution: Simpler model, more data, regularization

**Training accuracy: 65%, Test accuracy: 62%**
→ **Underfitting**. Model too simple.
- Solution: More complex model, better features

**Training accuracy: 50%, Test accuracy: 50%** (for binary classification)
→ **Random guessing**. Model learned nothing.
- Solution: Check your data, try different features

---

# Quick Reference: Regression Metrics

```python
from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X_test)

# Mean Squared Error (lower = better)
mse = mean_squared_error(y_test, y_pred)
print(f"MSE: {mse:.2f}")

# R² Score (0 to 1, higher = better)
r2 = r2_score(y_test, y_pred)
print(f"R²: {r2:.2f}")  # 0.85 = explains 85% of variance
```

**Interpretation:**
- R² = 1.0 → Perfect predictions
- R² = 0.0 → Model is useless (same as predicting mean)
- R² < 0.0 → Model worse than predicting mean (!!)

---

# Quick Reference: Classification Metrics

```python
from sklearn.metrics import accuracy_score, confusion_matrix

y_pred = model.predict(X_test)

# Accuracy (higher = better)
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.2%}")

# Confusion Matrix (see where model fails)
cm = confusion_matrix(y_test, y_pred)
print(cm)
#       Predicted
#       0    1
# Act 0 [45]  [5]   ← 5 false positives
#     1 [3]  [47]   ← 3 false negatives
```

**Warning:** Accuracy lies on imbalanced data!

---

# Pro Tips

**1. Start Simple**
- Linear regression before polynomial
- Single decision tree before random forest
- Get something working, THEN optimize

**2. Print Shapes**
```python
print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)
```

**3. Check for NaN/Inf**
```python
print(X.isnull().sum())  # For pandas
print(np.isnan(X).sum())  # For numpy
```

**4. Use random_state for reproducibility**
```python
train_test_split(X, y, random_state=42)
```

---

# Exercise Time!

**File:** `ml_regression_classification_starter.py`

**You'll build:**
1. House price predictor (regression)
2. Iris classifier (classification)
3. Student pass/fail predictor

**Bonus challenges:**
- Feature importance
- Overfitting detection
- SHAP explanations
- Decision boundaries

**Let's code!**

---

<!-- _class: lead -->

# Questions?

Open the file and let's get started!
