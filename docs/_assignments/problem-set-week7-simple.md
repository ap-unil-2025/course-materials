---
layout: assignment
title: "Problem Set Week 7: Introduction to Linear Regression"
assignment_number: 107
due_date: 2025-11-03 23:59:00
github_classroom_url: "https://classroom.github.com/a/xR7mL9nQ-ps-week7"
topics:
  - "Linear regression with sklearn"
  - "Data preprocessing"
  - "Model evaluation"
  - "Simple gradient descent"
---

# Problem Set 7: Introduction to Linear Regression

## Learning Objectives
- Use sklearn for linear regression
- Understand train/test split
- Evaluate model performance
- Implement simple gradient descent

## Setup
1. Accept the GitHub Classroom assignment
2. Clone your repository
3. Install requirements: `pip install -r requirements.txt`
4. Run tests: `pytest test_assignment.py`

## Exercise 1: Data Preprocessing (20 points)

Create `preprocessing.py`:

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_split_data(X, y, test_size=0.2, random_state=42):
    """
    Split data into training and testing sets
    
    Args:
        X: Feature matrix
        y: Target vector
        test_size: Proportion for test set
        random_state: Random seed
    
    Returns:
        X_train, X_test, y_train, y_test
    """
    # TODO: Use train_test_split from sklearn
    pass

def normalize_features(X_train, X_test):
    """
    Normalize features using StandardScaler
    
    Args:
        X_train: Training features
        X_test: Test features
    
    Returns:
        X_train_scaled, X_test_scaled, scaler object
    """
    # TODO: Fit scaler on training data, transform both
    pass
```

## Exercise 2: Linear Regression with sklearn (25 points)

Create `sklearn_regression.py`:

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def train_linear_regression(X_train, y_train):
    """
    Train a linear regression model
    
    Args:
        X_train: Training features
        y_train: Training targets
    
    Returns:
        Trained LinearRegression model
    """
    # TODO: Create and fit LinearRegression model
    pass

def evaluate_model(model, X_test, y_test):
    """
    Evaluate model performance
    
    Args:
        model: Trained model
        X_test: Test features
        y_test: True test targets
    
    Returns:
        Dictionary with 'mse', 'rmse', and 'r2' scores
    """
    # TODO: Make predictions and calculate metrics
    pass

def get_feature_importance(model, feature_names):
    """
    Get feature importance from linear regression coefficients
    
    Args:
        model: Trained LinearRegression model
        feature_names: List of feature names
    
    Returns:
        List of tuples [(feature_name, coefficient), ...]
        sorted by absolute coefficient value
    """
    # TODO: Pair feature names with coefficients and sort
    pass
```

## Exercise 3: Simple Gradient Descent (30 points)

Create `gradient_descent.py`:

```python
import numpy as np

class SimpleLinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        """
        Simple linear regression using gradient descent
        """
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        self.loss_history = []
    
    def fit(self, X, y):
        """
        Train model using gradient descent
        
        Args:
            X: Training features (n_samples, n_features)
            y: Training targets (n_samples,)
        """
        n_samples, n_features = X.shape
        
        # Initialize parameters
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Gradient descent
        for _ in range(self.n_iterations):
            # TODO: Compute predictions
            y_pred = None  # TODO
            
            # TODO: Compute loss (MSE)
            loss = None  # TODO
            self.loss_history.append(loss)
            
            # TODO: Compute gradients
            dw = None  # TODO: gradient for weights
            db = None  # TODO: gradient for bias
            
            # TODO: Update parameters
            self.weights = None  # TODO
            self.bias = None  # TODO
    
    def predict(self, X):
        """
        Make predictions
        
        Args:
            X: Features (n_samples, n_features)
        
        Returns:
            Predictions (n_samples,)
        """
        # TODO: Compute predictions using weights and bias
        pass
    
    def get_loss_history(self):
        """Return loss history for plotting"""
        return self.loss_history
```

## Exercise 4: Putting It All Together (25 points)

Create `housing_predictor.py`:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

def load_housing_data():
    """
    Load California housing dataset
    
    Returns:
        X (features), y (target prices), feature_names
    """
    # TODO: Use fetch_california_housing
    pass

def compare_models(X, y):
    """
    Compare sklearn LinearRegression with your gradient descent
    
    Args:
        X: Features
        y: Target values
    
    Returns:
        Dictionary with results for both models
    """
    # TODO: Split data
    # TODO: Normalize features
    # TODO: Train both models
    # TODO: Evaluate both models
    # TODO: Return comparison results
    pass

def plot_learning_curve(loss_history):
    """
    Plot gradient descent learning curve
    
    Args:
        loss_history: List of loss values
    """
    # TODO: Create plot showing loss over iterations
    pass

def plot_predictions_vs_actual(y_true, y_pred, title=""):
    """
    Scatter plot of predictions vs actual values
    
    Args:
        y_true: Actual values
        y_pred: Predicted values
        title: Plot title
    """
    # TODO: Create scatter plot with diagonal line
    pass
```

## Testing

Run the automated tests:
```bash
pytest test_assignment.py -v
```

Expected output:
```
test_preprocessing.py::test_data_split PASSED
test_preprocessing.py::test_normalization PASSED
test_sklearn_regression.py::test_training PASSED
test_sklearn_regression.py::test_evaluation PASSED
test_gradient_descent.py::test_simple_regression PASSED
test_housing_predictor.py::test_full_pipeline PASSED
```

## Deliverables

1. All Python files with completed functions
2. A Jupyter notebook `analysis.ipynb` showing:
   - Loading and exploring the data
   - Training both models
   - Comparing performance
   - Visualizing results
3. Brief `README.md` with your observations

## Grading Rubric

- **Automated Tests (70%)**: Code passes all tests
- **Code Quality (15%)**: Clean, readable, follows conventions
- **Analysis (15%)**: Notebook shows understanding of results

## Tips

- Start with sklearn implementation (easier)
- For gradient descent, use vectorized operations
- Remember to normalize features for gradient descent
- Check that loss decreases over iterations
- Use small learning rate if gradient descent diverges

## Common Issues

- **Gradient descent not converging**: Try smaller learning rate
- **Different scales in features**: Always normalize!
- **Shape mismatch errors**: Check dimensions with `.shape`
- **NaN in gradients**: Learning rate might be too large

## Resources

- [sklearn LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- [Gradient Descent Explained](https://ml-cheatsheet.readthedocs.io/en/latest/gradient_descent.html)
- [California Housing Dataset](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset)