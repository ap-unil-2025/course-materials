"""
Machine Learning Practice: Regression & Classification - SOLUTION
Session 8: November 3, 2025
Anna Smirnova

Complete solutions with bonus challenges implemented!
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# ============================================================================
# PART 1: LINEAR REGRESSION - Predicting House Prices
# ============================================================================

print("="*60)
print("PART 1: LINEAR REGRESSION - House Price Prediction")
print("="*60)

# Sample housing data (size in sq ft, bedrooms, age in years, price in $1000s)
housing_data = {
    'size': [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700],
    'bedrooms': [3, 3, 2, 4, 2, 3, 4, 4, 3, 3],
    'age': [10, 8, 15, 5, 20, 7, 3, 2, 12, 9],
    'price': [245, 312, 279, 308, 199, 219, 405, 324, 319, 255]
}

df_housing = pd.DataFrame(housing_data)

# SOLUTION 1.1: Create features (X) and target (y)
X_housing = df_housing[['size', 'bedrooms', 'age']]
y_housing = df_housing['price']

print(f"Features shape: {X_housing.shape}")
print(f"Target shape: {y_housing.shape}")

# SOLUTION 1.2: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_housing, y_housing, test_size=0.2, random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# SOLUTION 1.3: Create and train a Linear Regression model
model_regression = LinearRegression()
model_regression.fit(X_train, y_train)

print("\nModel coefficients:")
for feature, coef in zip(X_housing.columns, model_regression.coef_):
    print(f"  {feature}: {coef:.2f}")
print(f"Intercept: {model_regression.intercept_:.2f}")

# SOLUTION 1.4: Make predictions on the test set
y_pred = model_regression.predict(X_test)

# SOLUTION 1.5: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nRegression Results:")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")
print(f"RMSE: {np.sqrt(mse):.2f} (average error in $1000s)")

# SOLUTION 1.6: Test your model with a new house
new_house = [[1800, 3, 6]]
predicted_price = model_regression.predict(new_house)[0]
print(f"\nPredicted price for new house (1800 sqft, 3 bed, 6 years): ${predicted_price:.2f}k")


# ============================================================================
# PART 2: CLASSIFICATION - Iris Flower Species
# ============================================================================

print("\n" + "="*60)
print("PART 2: CLASSIFICATION - Iris Species Recognition")
print("="*60)

# Sample Iris data (sepal_length, sepal_width, petal_length, petal_width, species)
# Species: 0=Setosa, 1=Versicolor, 2=Virginica
iris_data = {
    'sepal_length': [5.1, 4.9, 4.7, 7.0, 6.4, 6.9, 6.3, 5.8, 6.7, 5.7],
    'sepal_width': [3.5, 3.0, 3.2, 3.2, 3.2, 3.1, 2.3, 2.7, 3.3, 2.8],
    'petal_length': [1.4, 1.4, 1.3, 4.7, 4.5, 4.9, 4.4, 3.9, 5.7, 4.1],
    'petal_width': [0.2, 0.2, 0.2, 1.4, 1.5, 1.5, 1.3, 1.2, 2.5, 1.3],
    'species': [0, 0, 0, 1, 1, 1, 1, 1, 2, 1]
}

df_iris = pd.DataFrame(iris_data)

species_names = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}

# SOLUTION 2.1: Create features (X) and target (y)
X_iris = df_iris.drop('species', axis=1)
y_iris = df_iris['species']

# SOLUTION 2.2: Split data into training and testing sets
X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(
    X_iris, y_iris, test_size=0.3, random_state=42
)

# SOLUTION 2.3: Create and train a K-Nearest Neighbors classifier
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train_iris, y_train_iris)

# SOLUTION 2.4: Make predictions
y_pred_knn = knn_model.predict(X_test_iris)

# SOLUTION 2.5: Evaluate the KNN model
accuracy_knn = accuracy_score(y_test_iris, y_pred_knn)
print(f"\nK-NN Accuracy: {accuracy_knn:.2%}")

# SOLUTION 2.6: Create and train a Decision Tree classifier
tree_model = DecisionTreeClassifier(random_state=42, max_depth=3)
tree_model.fit(X_train_iris, y_train_iris)

# SOLUTION 2.7: Make predictions with Decision Tree
y_pred_tree = tree_model.predict(X_test_iris)

# SOLUTION 2.8: Evaluate the Decision Tree model
accuracy_tree = accuracy_score(y_test_iris, y_pred_tree)
print(f"Decision Tree Accuracy: {accuracy_tree:.2%}")

# SOLUTION 2.9: Compare models
print("\nModel Comparison:")
print(f"K-NN: {accuracy_knn:.2%}")
print(f"Decision Tree: {accuracy_tree:.2%}")

better_model = "K-NN" if accuracy_knn > accuracy_tree else "Decision Tree"
better_pred = y_pred_knn if accuracy_knn > accuracy_tree else y_pred_tree
print(f"Winner: {better_model}")

# SOLUTION 2.10: Create a confusion matrix for the better model
cm = confusion_matrix(y_test_iris, better_pred)
print("\nConfusion Matrix:")
print(cm)
print("\nInterpretation:")
print("  Rows = Actual, Columns = Predicted")
print(f"  Correctly classified: {np.trace(cm)} out of {len(y_test_iris)}")


# ============================================================================
# PART 3: MINI PROJECT - Student Grade Prediction
# ============================================================================

print("\n" + "="*60)
print("PART 3: MINI PROJECT - Predict Student Pass/Fail")
print("="*60)

# Student data (study_hours, previous_score, attendance%, passed)
student_data = {
    'study_hours': [2, 4, 1, 5, 3, 6, 2, 7, 4, 1],
    'previous_score': [55, 67, 45, 88, 62, 91, 58, 95, 70, 40],
    'attendance': [60, 75, 55, 90, 70, 95, 65, 98, 80, 50],
    'passed': [0, 1, 0, 1, 1, 1, 0, 1, 1, 0]
}

df_students = pd.DataFrame(student_data)

# SOLUTION 3.1: Split features and target
X_students = df_students[['study_hours', 'previous_score', 'attendance']]
y_students = df_students['passed']

# SOLUTION 3.2: Split into train/test sets
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_students, y_students, test_size=0.3, random_state=42
)

# SOLUTION 3.3: Try BOTH K-NN and Decision Tree
print("\nTesting both models on student data:")

# K-NN Model
knn_student = KNeighborsClassifier(n_neighbors=3)
knn_student.fit(X_train_s, y_train_s)
y_pred_knn_s = knn_student.predict(X_test_s)
acc_knn_s = accuracy_score(y_test_s, y_pred_knn_s)
print(f"K-NN Accuracy: {acc_knn_s:.2%}")

# Decision Tree Model
tree_student = DecisionTreeClassifier(random_state=42, max_depth=3)
tree_student.fit(X_train_s, y_train_s)
y_pred_tree_s = tree_student.predict(X_test_s)
acc_tree_s = accuracy_score(y_test_s, y_pred_tree_s)
print(f"Decision Tree Accuracy: {acc_tree_s:.2%}")

# SOLUTION 3.4: Predict for a new student
new_student = [[5, 75, 85]]  # 5 hours study, 75 previous score, 85% attendance
pred_knn = knn_student.predict(new_student)[0]
pred_tree = tree_student.predict(new_student)[0]

print(f"\nNew student prediction (5 hrs, 75 score, 85% attendance):")
print(f"  K-NN predicts: {'PASS' if pred_knn == 1 else 'FAIL'}")
print(f"  Decision Tree predicts: {'PASS' if pred_tree == 1 else 'FAIL'}")

# Get probability scores
prob_knn = knn_student.predict_proba(new_student)[0]
prob_tree = tree_student.predict_proba(new_student)[0]
print(f"  K-NN confidence: Fail={prob_knn[0]:.1%}, Pass={prob_knn[1]:.1%}")
print(f"  Tree confidence: Fail={prob_tree[0]:.1%}, Pass={prob_tree[1]:.1%}")


# ============================================================================
# BONUS CHALLENGES - Level 1 (Implemented Examples)
# ============================================================================

print("\n" + "="*60)
print("BONUS CHALLENGES - LEVEL 1 EXAMPLES")
print("="*60)

# BONUS 1: Feature Importance
print("\n--- BONUS 1: Feature Importance ---")
importances = tree_model.feature_importances_
feature_names = X_iris.columns

print("Feature importances for Iris classification:")
for name, importance in zip(feature_names, importances):
    print(f"  {name}: {importance:.3f}")

# Plot feature importance
plt.figure(figsize=(8, 5))
plt.bar(feature_names, importances)
plt.title('Feature Importance - Decision Tree (Iris)')
plt.xlabel('Feature')
plt.ylabel('Importance')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('feature_importance.png', dpi=150, bbox_inches='tight')
print("Saved: feature_importance.png")
plt.close()

# BONUS 2: Residual Analysis
print("\n--- BONUS 2: Residual Analysis ---")
residuals = y_test - y_pred

plt.figure(figsize=(8, 5))
plt.scatter(y_pred, residuals, alpha=0.7)
plt.axhline(y=0, color='r', linestyle='--', linewidth=2)
plt.xlabel('Predicted Price ($1000s)')
plt.ylabel('Residuals (Actual - Predicted)')
plt.title('Residual Plot - Housing Price Regression')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('residuals.png', dpi=150, bbox_inches='tight')
print("Saved: residuals.png")
print(f"Mean residual: {np.mean(residuals):.2f} (should be close to 0)")
print(f"Std of residuals: {np.std(residuals):.2f}")
plt.close()

# BONUS 3: The KNN Scaling Mystery
print("\n--- BONUS 3: KNN Scaling Mystery ---")

# Without scaling
knn_no_scale = KNeighborsClassifier(n_neighbors=3)
knn_no_scale.fit(X_train_iris, y_train_iris)
acc_no_scale = knn_no_scale.score(X_test_iris, y_test_iris)

# With scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_iris)
X_test_scaled = scaler.transform(X_test_iris)

knn_scaled = KNeighborsClassifier(n_neighbors=3)
knn_scaled.fit(X_train_scaled, y_train_iris)
acc_scaled = knn_scaled.score(X_test_scaled, y_test_iris)

print(f"KNN without scaling: {acc_no_scale:.2%}")
print(f"KNN with scaling: {acc_scaled:.2%}")
print(f"Improvement: {(acc_scaled - acc_no_scale):.2%}")
print("\nWhy? KNN uses distance. Features on different scales dominate!")
print("Example: 1000 sqft difference >> 1 bedroom difference in raw values")

# BONUS 4: Learning Curves
print("\n--- BONUS 4: Learning Curves ---")
train_sizes = [0.2, 0.4, 0.6, 0.8, 1.0]
train_scores = []
test_scores = []

for size in train_sizes:
    # Use subset of training data
    X_subset = X_train_iris[:int(len(X_train_iris) * size)]
    y_subset = y_train_iris[:int(len(y_train_iris) * size)]

    # Train and evaluate
    temp_model = DecisionTreeClassifier(random_state=42, max_depth=3)
    temp_model.fit(X_subset, y_subset)

    train_scores.append(temp_model.score(X_subset, y_subset))
    test_scores.append(temp_model.score(X_test_iris, y_test_iris))

plt.figure(figsize=(8, 5))
plt.plot([s*100 for s in train_sizes], train_scores, 'o-', label='Training Accuracy', linewidth=2)
plt.plot([s*100 for s in train_sizes], test_scores, 's-', label='Test Accuracy', linewidth=2)
plt.xlabel('Training Data Size (%)')
plt.ylabel('Accuracy')
plt.title('Learning Curve - Decision Tree (Iris)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('learning_curve.png', dpi=150, bbox_inches='tight')
print("Saved: learning_curve.png")
print("Insight: After ~60% of data, more data doesn't help much (plateau)")
plt.close()


# ============================================================================
# BONUS CHALLENGES - Level 2 (Advanced Examples)
# ============================================================================

print("\n" + "="*60)
print("BONUS CHALLENGES - LEVEL 2 EXAMPLES")
print("="*60)

# ADVANCED 1: SHAP Values (if shap is installed)
print("\n--- ADVANCED 1: SHAP Values ---")
try:
    import shap

    explainer = shap.TreeExplainer(tree_model)
    shap_values = explainer.shap_values(X_test_iris)

    # For multi-class, shap_values is a list of arrays (one per class)
    # Let's explain the first test sample
    sample_idx = 0
    print(f"\nExplaining prediction for test sample {sample_idx}:")
    print(f"Features: {X_test_iris.iloc[sample_idx].to_dict()}")
    print(f"Actual class: {species_names[y_test_iris.iloc[sample_idx]]}")
    print(f"Predicted class: {species_names[y_pred_tree[sample_idx]]}")

    shap.summary_plot(shap_values, X_test_iris, plot_type="bar", show=False)
    plt.tight_layout()
    plt.savefig('shap_summary.png', dpi=150, bbox_inches='tight')
    print("Saved: shap_summary.png")
    plt.close()

except ImportError:
    print("SHAP not installed. Run: pip install shap")

# ADVANCED 2: Decision Boundaries
print("\n--- ADVANCED 2: Decision Boundaries ---")
# Use only 2 features for 2D visualization
X_2d = X_iris[['petal_length', 'petal_width']]
y_2d = y_iris

X_train_2d, X_test_2d, y_train_2d, y_test_2d = train_test_split(
    X_2d, y_2d, test_size=0.3, random_state=42
)

# Train both models on 2D data
knn_2d = KNeighborsClassifier(n_neighbors=3)
knn_2d.fit(X_train_2d, y_train_2d)

tree_2d = DecisionTreeClassifier(max_depth=3, random_state=42)
tree_2d.fit(X_train_2d, y_train_2d)

# Create mesh grid
h = 0.02
x_min, x_max = X_2d.iloc[:, 0].min() - 0.5, X_2d.iloc[:, 0].max() + 0.5
y_min, y_max = X_2d.iloc[:, 1].min() - 0.5, X_2d.iloc[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Plot decision boundaries
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for ax, model, title in zip(axes, [knn_2d, tree_2d], ['K-NN', 'Decision Tree']):
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    ax.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.RdYlBu)
    scatter = ax.scatter(X_2d.iloc[:, 0], X_2d.iloc[:, 1], c=y_2d,
                        cmap=plt.cm.RdYlBu, edgecolor='black', s=50)
    ax.set_xlabel('Petal Length')
    ax.set_ylabel('Petal Width')
    ax.set_title(f'{title} Decision Boundary')

plt.tight_layout()
plt.savefig('decision_boundaries.png', dpi=150, bbox_inches='tight')
print("Saved: decision_boundaries.png")
print("Notice: KNN has smooth boundaries, Tree has sharp axis-aligned cuts")
plt.close()

# ADVANCED 5: The Overfitting Detective
print("\n--- ADVANCED 5: Overfitting Detective ---")
depths = [1, 3, 5, 10, 20]
train_accs = []
test_accs = []

for depth in depths:
    dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt.fit(X_train_iris, y_train_iris)

    train_accs.append(dt.score(X_train_iris, y_train_iris))
    test_accs.append(dt.score(X_test_iris, y_test_iris))

plt.figure(figsize=(8, 5))
plt.plot(depths, train_accs, 'o-', label='Training Accuracy', linewidth=2)
plt.plot(depths, test_accs, 's-', label='Test Accuracy', linewidth=2)
plt.xlabel('Tree Depth (Complexity)')
plt.ylabel('Accuracy')
plt.title('Overfitting: Training vs Test Accuracy')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axvline(x=3, color='g', linestyle='--', alpha=0.5, label='Sweet Spot')
plt.tight_layout()
plt.savefig('overfitting.png', dpi=150, bbox_inches='tight')
print("Saved: overfitting.png")
print("\nThe Goldilocks Problem:")
for i, depth in enumerate(depths):
    gap = train_accs[i] - test_accs[i]
    print(f"  Depth={depth}: Train={train_accs[i]:.2%}, Test={test_accs[i]:.2%}, Gap={gap:.2%}")
print("Sweet spot: Good test accuracy, small train-test gap")
plt.close()

# ADVANCED 6: Ensemble Power
print("\n--- ADVANCED 6: Random Forest vs Single Tree ---")
from sklearn.ensemble import RandomForestClassifier

single_tree = DecisionTreeClassifier(random_state=42)
single_tree.fit(X_train_iris, y_train_iris)
acc_single = single_tree.score(X_test_iris, y_test_iris)

random_forest = RandomForestClassifier(n_estimators=100, random_state=42)
random_forest.fit(X_train_iris, y_train_iris)
acc_forest = random_forest.score(X_test_iris, y_test_iris)

print(f"Single Decision Tree: {acc_single:.2%}")
print(f"Random Forest (100 trees): {acc_forest:.2%}")
print(f"Improvement: {(acc_forest - acc_single):.2%}")
print("\nWhy? Averaging 100 trees reduces overfitting and variance!")


print("\n" + "="*60)
print("Exercise Complete!")
print("="*60)
print("\nKey Takeaways:")
print("1. Regression predicts continuous values (prices, scores)")
print("2. Classification predicts categories (species, pass/fail)")
print("3. Always split data into train/test sets")
print("4. Feature scaling matters for distance-based models (KNN)")
print("5. Overfitting = high training accuracy, low test accuracy")
print("6. Ensemble methods (Random Forest) often beat single models")
print("7. SHAP and visualizations help explain 'black box' models")
