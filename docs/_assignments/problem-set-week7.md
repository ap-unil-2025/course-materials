---
layout: assignment
title: "Problem Set Week 7: Advanced Linear Regression"
assignment_number: 107
due_date: 2025-11-03 23:59:00
difficulty: "Intermediate"
estimated_time: "5-6 hours"
github_classroom_url: "https://classroom.github.com/a/xR7mL9nQ-ps-week7"
topics:
  - "Adaptive learning rates"
  - "Elastic Net regularization"
  - "Robust regression"
  - "Bayesian linear regression"
  - "Online learning"
status: "active"
description: "Extend linear regression beyond basics with advanced optimization and regularization techniques"
---

# Problem Set 7: Advanced Linear Regression Techniques

The lecture covered basic gradient descent, polynomial regression, and Ridge regression. Now let's explore more advanced techniques!

## Exercise 1: Advanced Gradient Descent Optimizers 🚀

The lecture showed basic gradient descent. Now implement advanced optimizers!

### Part A: Adaptive Learning Rate Methods (30 points)
Implement these optimizers from scratch:

```python
class AdaGrad:
    """Adaptive Gradient Algorithm"""
    def __init__(self, learning_rate=0.01, epsilon=1e-8):
        self.lr = learning_rate
        self.epsilon = epsilon
        self.accumulated_gradients = 0
    
    def update(self, params, gradients):
        """
        AdaGrad adapts learning rate based on historical gradients
        Prevents learning rate from being too large for frequently updated parameters
        """
        # TODO: Accumulate squared gradients
        # TODO: Update parameters with adapted learning rate
        pass

class RMSprop:
    """Root Mean Square Propagation"""
    def __init__(self, learning_rate=0.001, decay_rate=0.9, epsilon=1e-8):
        self.lr = learning_rate
        self.decay_rate = decay_rate
        self.epsilon = epsilon
        self.cache = 0
    
    def update(self, params, gradients):
        """
        RMSprop uses exponential moving average of squared gradients
        """
        # TODO: Update cache with exponential moving average
        # TODO: Adapt learning rate based on cache
        pass

class Adam:
    """Adaptive Moment Estimation"""
    def __init__(self, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.lr = learning_rate
        self.beta1 = beta1  # Decay rate for first moment
        self.beta2 = beta2  # Decay rate for second moment
        self.epsilon = epsilon
        self.m = 0  # First moment
        self.v = 0  # Second moment
        self.t = 0  # Time step
    
    def update(self, params, gradients):
        """
        Adam combines momentum with RMSprop
        Includes bias correction
        """
        # TODO: Update biased first moment estimate
        # TODO: Update biased second moment estimate
        # TODO: Compute bias-corrected estimates
        # TODO: Update parameters
        pass
```

### Part B: Learning Rate Scheduling (25 points)
Implement advanced scheduling strategies:

```python
class CosineAnnealingLR:
    """Cosine annealing with warm restarts"""
    def __init__(self, initial_lr, T_max, eta_min=0):
        self.initial_lr = initial_lr
        self.T_max = T_max
        self.eta_min = eta_min
        self.current_step = 0
    
    def get_lr(self):
        """Calculate learning rate using cosine annealing"""
        # TODO: Implement cosine annealing formula
        pass
    
    def step(self):
        """Update internal counter"""
        self.current_step += 1

class CyclicalLR:
    """Cyclical Learning Rates"""
    def __init__(self, base_lr, max_lr, step_size):
        self.base_lr = base_lr
        self.max_lr = max_lr
        self.step_size = step_size
        self.current_step = 0
    
    def get_lr(self):
        """Cycle between base_lr and max_lr"""
        # TODO: Implement triangular cycle
        pass
```

### Part C: Convergence Analysis (20 points)
Compare optimizer performance:

```python
def compare_optimizers(X, y, optimizers_dict):
    """
    Compare convergence speed and final loss
    Plot:
    - Loss curves over iterations
    - Learning rate schedules
    - Parameter trajectories in 2D
    """
    # TODO: Train with each optimizer
    # TODO: Track and visualize metrics
    pass
```

## Exercise 2: Elastic Net and Advanced Regularization 🎯

The lecture covered Ridge (L2) regression. Now implement Elastic Net and more!

### Part A: Elastic Net Regression (30 points)
Combine L1 and L2 regularization:

```python
class ElasticNet:
    def __init__(self, alpha=1.0, l1_ratio=0.5, max_iter=1000):
        """
        Elastic Net: alpha * (l1_ratio * L1 + (1-l1_ratio) * L2)
        """
        self.alpha = alpha
        self.l1_ratio = l1_ratio
        self.max_iter = max_iter
        self.weights = None
        self.bias = None
    
    def soft_threshold(self, x, lambda_):
        """Soft thresholding operator for L1"""
        # TODO: Implement soft thresholding
        pass
    
    def coordinate_descent(self, X, y):
        """
        Use coordinate descent for optimization
        Better than gradient descent for L1 regularization
        """
        # TODO: Implement coordinate descent
        # TODO: Apply soft thresholding for L1 component
        pass
```

### Part B: Group Lasso (25 points)
Regularization for grouped features:

```python
class GroupLasso:
    def __init__(self, groups, alpha=1.0):
        """
        Groups: list of feature indices for each group
        Example: [[0,1,2], [3,4], [5,6,7]] for 3 groups
        """
        self.groups = groups
        self.alpha = alpha
    
    def group_soft_threshold(self, weights_group, lambda_):
        """Apply soft thresholding at group level"""
        # TODO: Compute group norm
        # TODO: Apply group-wise soft thresholding
        pass
    
    def fit(self, X, y):
        """Fit using proximal gradient descent"""
        # TODO: Implement proximal gradient method
        pass
```

### Part C: Adaptive Lasso (20 points)
Weight-adaptive regularization:

```python
class AdaptiveLasso:
    def __init__(self, gamma=1.0):
        """
        Adaptive weights based on initial estimates
        """
        self.gamma = gamma
        self.adaptive_weights = None
    
    def fit(self, X, y):
        """
        Two-stage procedure:
        1. Get initial estimates (OLS or Ridge)
        2. Use adaptive weights for Lasso
        """
        # TODO: Compute initial estimates
        # TODO: Calculate adaptive weights
        # TODO: Solve weighted Lasso
        pass
```

## Exercise 3: Robust Regression Methods 💪

Handle outliers and non-normal errors!

### Part A: Huber Regression (25 points)
Robust to outliers:

```python
class HuberRegressor:
    def __init__(self, epsilon=1.35, max_iter=100):
        """
        Huber loss: quadratic for small errors, linear for large
        """
        self.epsilon = epsilon
        self.max_iter = max_iter
    
    def huber_loss(self, residuals):
        """
        Compute Huber loss
        """
        # TODO: Implement Huber loss function
        pass
    
    def huber_gradient(self, residuals):
        """
        Gradient of Huber loss
        """
        # TODO: Implement gradient
        pass
    
    def fit(self, X, y):
        """
        Iteratively reweighted least squares
        """
        # TODO: Implement IRLS for Huber regression
        pass
```

### Part B: RANSAC Regression (30 points)
Random Sample Consensus for outlier detection:

```python
class RANSACRegressor:
    def __init__(self, min_samples=None, residual_threshold=None, max_trials=100):
        self.min_samples = min_samples
        self.residual_threshold = residual_threshold
        self.max_trials = max_trials
        self.best_model = None
        self.inlier_mask = None
    
    def fit(self, X, y):
        """
        RANSAC algorithm:
        1. Randomly sample minimum points
        2. Fit model to sample
        3. Count inliers
        4. Keep best model
        """
        # TODO: Implement RANSAC
        pass
    
    def compute_inliers(self, X, y, model):
        """Determine which points are inliers"""
        # TODO: Calculate residuals and threshold
        pass
```

### Part C: Quantile Regression (25 points)
Predict quantiles instead of mean:

```python
class QuantileRegressor:
    def __init__(self, quantile=0.5, learning_rate=0.01):
        """
        Predict specified quantile of target distribution
        """
        self.quantile = quantile
        self.lr = learning_rate
    
    def quantile_loss(self, y_true, y_pred):
        """
        Asymmetric loss function for quantiles
        """
        # TODO: Implement pinball loss
        pass
    
    def fit(self, X, y):
        """
        Minimize quantile loss using gradient descent
        """
        # TODO: Implement quantile regression
        pass
```

## Exercise 4: Bayesian Linear Regression 🎲

Go beyond point estimates!

### Part A: Bayesian Linear Regression (35 points)
Implement full Bayesian treatment:

```python
class BayesianLinearRegression:
    def __init__(self, alpha=1.0, beta=1.0):
        """
        alpha: precision of prior (inverse variance)
        beta: precision of noise
        """
        self.alpha = alpha
        self.beta = beta
        self.mean = None
        self.cov = None
    
    def fit(self, X, y):
        """
        Compute posterior distribution over weights
        Posterior is Gaussian with closed-form solution
        """
        # TODO: Compute posterior covariance
        # TODO: Compute posterior mean
        pass
    
    def predict(self, X, return_std=False):
        """
        Predictive distribution is also Gaussian
        """
        # TODO: Compute predictive mean
        # TODO: Compute predictive variance if requested
        pass
    
    def sample_posterior(self, n_samples=10):
        """
        Sample from posterior distribution
        """
        # TODO: Sample weight vectors from posterior
        pass
```

### Part B: Evidence Maximization (30 points)
Automatic relevance determination:

```python
class EvidenceMaximization:
    def __init__(self, max_iter=100):
        """
        Type II Maximum Likelihood for hyperparameters
        """
        self.max_iter = max_iter
        self.alpha = 1.0
        self.beta = 1.0
    
    def log_evidence(self, X, y, alpha, beta):
        """
        Compute log marginal likelihood
        """
        # TODO: Implement evidence calculation
        pass
    
    def update_hyperparameters(self, X, y):
        """
        EM algorithm for alpha and beta
        """
        # TODO: Implement EM updates
        pass
```

## Exercise 5: Online Learning and Streaming Regression 🌊

Handle data that arrives sequentially!

### Part A: Stochastic Gradient Descent with Mini-batches (25 points)
```python
class OnlineSGDRegressor:
    def __init__(self, learning_rate=0.01, batch_size=32):
        self.lr = learning_rate
        self.batch_size = batch_size
        self.weights = None
        self.n_samples_seen = 0
    
    def partial_fit(self, X, y):
        """
        Update model with new batch of data
        """
        # TODO: Update weights incrementally
        # TODO: Implement learning rate decay
        pass
    
    def fit_generator(self, data_generator, steps):
        """
        Train on data generator/stream
        """
        # TODO: Process streaming data
        pass
```

### Part B: Recursive Least Squares (30 points)
Exact online updates:

```python
class RecursiveLeastSquares:
    def __init__(self, forgetting_factor=1.0):
        """
        forgetting_factor < 1 gives more weight to recent data
        """
        self.ff = forgetting_factor
        self.P = None  # Inverse covariance matrix
        self.w = None  # Weights
    
    def update(self, x, y):
        """
        Sherman-Morrison formula for efficient updates
        """
        # TODO: Update P matrix
        # TODO: Update weights
        pass
```

## Real-World Project: Energy Consumption Forecasting ⚡

Apply everything to predict building energy usage!

```python
class EnergyForecaster:
    def __init__(self):
        """
        Combine multiple techniques:
        - Feature engineering (weather, time, holidays)
        - Robust regression for outliers
        - Online learning for real-time updates
        - Bayesian uncertainty quantification
        """
        pass
    
    def engineer_features(self, timestamp, weather_data):
        """
        Create features:
        - Hour of day, day of week, month
        - Temperature, humidity, wind
        - Lagged values
        - Interaction terms
        """
        # TODO: Feature engineering
        pass
    
    def forecast(self, horizon=24):
        """
        Forecast next 24 hours with uncertainty
        """
        # TODO: Multi-step ahead prediction
        pass
```

## Bonus Challenges 🌟

### Challenge 1: Gaussian Process Regression (30 points)
Non-parametric Bayesian regression:
```python
class GaussianProcessRegressor:
    def __init__(self, kernel='rbf'):
        """Implement GP with different kernels"""
        pass
```

### Challenge 2: Neural Network Regression (30 points)
Simple neural net from scratch:
```python
class NeuralRegressor:
    def __init__(self, hidden_sizes=[10, 10]):
        """Two hidden layer network"""
        pass
```

## Submission Requirements

Your submission should include:
1. `optimizers.py` - Advanced optimization algorithms
2. `regularization.py` - Elastic Net and variants
3. `robust_regression.py` - Outlier-resistant methods
4. `bayesian_regression.py` - Probabilistic approaches
5. `online_learning.py` - Streaming algorithms
6. `experiments.ipynb` - Comparative analysis
7. `README.md` - Implementation notes

## Grading Rubric

- **Implementation Quality (40%)**: Correct, efficient algorithms
- **Beyond Lecture Content (30%)**: Successfully implementing advanced techniques
- **Experimental Analysis (20%)**: Thorough comparison and insights
- **Code Quality (10%)**: Clean, documented, tested

## Tips for Success

1. **Start with Validation**: Test on simple synthetic data first
2. **Visualize Everything**: Plot loss curves, weight paths, predictions
3. **Compare Systematically**: Use same data, metrics for fair comparison
4. **Handle Edge Cases**: What if data is singular? All zeros?
5. **Profile Performance**: Which methods scale better?

## Resources

- [Convex Optimization by Boyd](https://web.stanford.edu/~boyd/cvxbook/)
- [Pattern Recognition and ML by Bishop](https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)
- [Elements of Statistical Learning](https://hastie.su.domains/ElemStatLearn/)

Remember: The lecture gave you the foundation - now build the skyscraper! 🏗️