---
layout: assignment
title: "Week 7: Linear Regression & Gradient Descent"
assignment_number: 7
due_date: 2025-11-03 23:59:00
points: 120
difficulty: "Intermediate"
estimated_time: "6-7 hours"
topics:
  - "Linear Regression"
  - "Gradient Descent"
  - "Polynomial Regression"
  - "Model Evaluation"
  - "Stock Market Prediction"
status: "open"
---

## Overview

Implement linear regression from scratch, understand gradient descent optimization, and apply these techniques to real-world problems including stock market prediction. This assignment bridges mathematical theory with practical implementation.

## Learning Objectives

By completing this assignment, you will:

- Implement linear regression from scratch using NumPy
- Understand and implement gradient descent optimization
- Apply polynomial regression and regularization techniques
- Evaluate models using appropriate metrics
- Work with real financial data for stock prediction

## Part 1: Linear Regression from Scratch (30 points)

Create `linear_regression.py` implementing:

### 1.1 Simple Linear Regression (10 points)

```python
import numpy as np

class SimpleLinearRegression:
    """
    Implement simple linear regression (one feature):
    - Analytical solution using normal equation
    - Gradient descent solution
    - Visualization of fit
    """
    def __init__(self):
        self.w = None
        self.b = None
        self.loss_history = []
    
    def fit_normal_equation(self, X, y):
        """Solve using closed-form solution"""
        # Your implementation here
    
    def fit_gradient_descent(self, X, y, learning_rate=0.01, epochs=1000):
        """Solve using gradient descent"""
        # Your implementation here
    
    def predict(self, X):
        """Make predictions"""
        # Your implementation here
    
    def compute_loss(self, X, y):
        """Calculate mean squared error"""
        # Your implementation here
```

### 1.2 Multiple Linear Regression (10 points)

```python
class MultipleLinearRegression:
    """
    Implement multiple linear regression:
    - Handle multiple features
    - Feature scaling/normalization
    - Batch vs. stochastic gradient descent
    """
    def __init__(self, normalize=True):
        self.weights = None
        self.normalize = normalize
        self.mean = None
        self.std = None
    
    def fit(self, X, y, method='gradient_descent', **kwargs):
        """
        Fit model using specified method:
        - 'normal': Normal equation
        - 'gradient_descent': Batch gradient descent
        - 'sgd': Stochastic gradient descent
        - 'mini_batch': Mini-batch gradient descent
        """
        # Your implementation here
    
    def predict(self, X):
        """Make predictions with feature normalization"""
        # Your implementation here
```

### 1.3 Regularized Regression (10 points)

```python
class RegularizedRegression:
    """
    Implement Ridge and Lasso regression:
    - L2 regularization (Ridge)
    - L1 regularization (Lasso)
    - Elastic Net (combination)
    """
    def __init__(self, alpha=1.0, l1_ratio=0.5):
        self.alpha = alpha  # Regularization strength
        self.l1_ratio = l1_ratio  # Balance between L1 and L2
    
    def fit_ridge(self, X, y):
        """Ridge regression with L2 penalty"""
        # Your implementation here
    
    def fit_lasso(self, X, y, learning_rate=0.01, epochs=1000):
        """Lasso regression with L1 penalty (use gradient descent)"""
        # Your implementation here
    
    def fit_elastic_net(self, X, y):
        """Elastic Net with combined penalties"""
        # Your implementation here
```

## Part 2: Gradient Descent Optimization (25 points)

Create `gradient_optimization.py` with:

### 2.1 Gradient Descent Variants (15 points)

```python
class GradientOptimizer:
    """
    Implement various gradient descent algorithms:
    """
    def batch_gradient_descent(self, X, y, learning_rate=0.01, epochs=1000):
        """Standard batch gradient descent"""
        # Your implementation here
    
    def stochastic_gradient_descent(self, X, y, learning_rate=0.01, epochs=1000):
        """SGD with single sample updates"""
        # Your implementation here
    
    def mini_batch_gradient_descent(self, X, y, batch_size=32, learning_rate=0.01, epochs=1000):
        """Mini-batch gradient descent"""
        # Your implementation here
    
    def adaptive_gradient_descent(self, X, y, initial_lr=0.1, epochs=1000):
        """Implement learning rate scheduling"""
        # Your implementation here
```

### 2.2 Advanced Optimizers (10 points)

```python
class AdvancedOptimizers:
    """
    Implement modern optimization algorithms:
    """
    def momentum_sgd(self, X, y, learning_rate=0.01, momentum=0.9, epochs=1000):
        """SGD with momentum"""
        # Your implementation here
    
    def adam_optimizer(self, X, y, learning_rate=0.001, beta1=0.9, beta2=0.999, epochs=1000):
        """Simplified Adam optimizer"""
        # Your implementation here
    
    def visualize_convergence(self, optimizers_results):
        """Plot convergence rates of different optimizers"""
        # Your implementation here
```

## Part 3: Polynomial Regression & Model Selection (25 points)

Create `polynomial_regression.py`:

### 3.1 Polynomial Features (10 points)

```python
class PolynomialRegression:
    """
    Polynomial regression with degree selection:
    """
    def __init__(self, degree=2):
        self.degree = degree
        self.linear_regression = None
    
    def create_polynomial_features(self, X):
        """
        Generate polynomial features up to specified degree
        Handle single and multiple input features
        """
        # Your implementation here
    
    def fit(self, X, y):
        """Fit polynomial regression model"""
        # Your implementation here
    
    def predict(self, X):
        """Make predictions"""
        # Your implementation here
```

### 3.2 Model Complexity & Overfitting (15 points)

```python
class ModelSelector:
    """
    Tools for model selection and validation:
    """
    def train_validation_split(self, X, y, val_size=0.2):
        """Split data into training and validation sets"""
        # Your implementation here
    
    def cross_validation(self, X, y, model, k=5):
        """
        Implement k-fold cross-validation
        Return mean and std of scores
        """
        # Your implementation here
    
    def learning_curves(self, X, y, model, train_sizes):
        """
        Plot learning curves to diagnose bias/variance
        """
        # Your implementation here
    
    def select_polynomial_degree(self, X, y, max_degree=10):
        """
        Use cross-validation to select optimal polynomial degree
        Plot validation curves
        """
        # Your implementation here
```

## Part 4: Stock Market Prediction (40 points)

Create `stock_prediction.py` for a complete ML pipeline:

### 4.1 Data Preparation (10 points)

```python
class StockDataProcessor:
    """
    Prepare stock data for prediction:
    """
    def load_stock_data(self, symbol, start_date, end_date):
        """
        Load stock data (use yfinance or provided CSV)
        """
        # Your implementation here
    
    def create_features(self, df):
        """
        Engineer features:
        - Moving averages (5, 10, 20, 50 days)
        - RSI (Relative Strength Index)
        - MACD indicators
        - Volume indicators
        - Lag features
        """
        # Your implementation here
    
    def prepare_sequences(self, data, lookback=30):
        """
        Create sequences for time series prediction
        """
        # Your implementation here
```

### 4.2 Prediction Models (20 points)

```python
class StockPredictor:
    """
    Build and evaluate stock prediction models:
    """
    def __init__(self):
        self.models = {}
        self.results = {}
    
    def train_linear_model(self, X_train, y_train):
        """Train linear regression model"""
        # Your implementation here
    
    def train_polynomial_model(self, X_train, y_train, degree=3):
        """Train polynomial regression model"""
        # Your implementation here
    
    def train_regularized_model(self, X_train, y_train, alpha=1.0):
        """Train Ridge regression model"""
        # Your implementation here
    
    def ensemble_prediction(self, models, X_test, weights=None):
        """Combine predictions from multiple models"""
        # Your implementation here
```

### 4.3 Evaluation & Visualization (10 points)

```python
class ModelEvaluator:
    """
    Evaluate and visualize predictions:
    """
    def calculate_metrics(self, y_true, y_pred):
        """
        Calculate:
        - MSE, RMSE, MAE
        - R-squared
        - Direction accuracy (for trading)
        """
        # Your implementation here
    
    def plot_predictions(self, dates, y_true, y_pred, title="Stock Price Prediction"):
        """Visualize actual vs predicted prices"""
        # Your implementation here
    
    def backtest_strategy(self, predictions, actual_prices, initial_capital=10000):
        """
        Simple backtesting:
        - Buy when predicted price > current price
        - Sell when predicted price < current price
        - Calculate returns
        """
        # Your implementation here
```

## Deliverables

Create a Jupyter notebook `stock_analysis.ipynb` that:

1. **Data Analysis** (10 points)
   - Load and explore stock data
   - Visualize price trends and indicators
   - Analyze feature correlations

2. **Model Comparison** (15 points)
   - Train multiple models
   - Compare performance metrics
   - Select best model with justification

3. **Trading Strategy** (10 points)
   - Implement simple trading strategy
   - Backtest on historical data
   - Report returns and risk metrics

4. **Insights** (5 points)
   - Discuss model limitations
   - Suggest improvements
   - Ethical considerations in financial ML

## Submission Requirements

```
week7-assignment/
├── linear_regression.py
├── gradient_optimization.py
├── polynomial_regression.py
├── stock_prediction.py
├── stock_analysis.ipynb
├── data/
│   └── stock_data.csv  # Your collected data
├── results/
│   ├── predictions.png
│   ├── learning_curves.png
│   └── backtest_results.txt
├── tests/
│   └── test_regression.py
└── README.md
```

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Implementation | 60 | Correct algorithm implementation |
| Mathematical Understanding | 20 | Proper gradient calculations |
| Code Quality | 15 | Clean, documented, efficient |
| Analysis | 15 | Insightful interpretation |
| Visualization | 10 | Clear, informative plots |

## Tips

- Start with simple linear regression before moving to complex models
- Verify gradient calculations with numerical gradient checking
- Normalize features for better convergence
- Use vectorized operations with NumPy for efficiency
- Don't overfit to training data - use validation sets

## Resources

- [Understanding Linear Regression](https://www.stat.cmu.edu/~cshalizi/mreg/)
- [Gradient Descent Tutorial](https://www.youtube.com/watch?v=sDv4f4s2SB8)
- [Introduction to Statistical Learning - Chapter 3](https://www.statlearning.com/)
- [yfinance Documentation](https://pypi.org/project/yfinance/)

---

*Due: {{ page.due_date | date: "%B %d, %Y at %I:%M %p" }} • Points: {{ page.points }} • Difficulty: {{ page.difficulty }}*