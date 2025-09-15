---
layout: assignment
title: "Problem Set Week 8: Advanced Classification Techniques"
assignment_number: 108
due_date: 2025-11-10 23:59:00
difficulty: "Intermediate"
estimated_time: "5-6 hours"
github_classroom_url: "https://classroom.github.com/a/yT8nQ2mR-ps-week8"
topics:
  - "Ensemble methods"
  - "Imbalanced classification"
  - "Multi-class strategies"
  - "Probabilistic classifiers"
  - "Feature selection"
status: "active"
description: "Extend classification beyond basics with advanced ensemble methods and handling real-world challenges"
---

# Problem Set 8: Advanced Classification Techniques

The lecture covered kNN, Decision Trees, and Naive Bayes. Let's explore advanced ensemble methods, imbalanced data handling, and sophisticated classification strategies!

## Exercise 1: Advanced Ensemble Methods 🌲🌲🌲

The lecture showed basic bagging and AdaBoost. Now implement advanced ensembles!

### Part A: Gradient Boosting from Scratch (35 points)
Build a gradient boosting classifier:

```python
import numpy as np

class GradientBoostingClassifier:
    def __init__(self, n_estimators=100, learning_rate=0.1, max_depth=3):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.estimators = []
        self.init_prediction = None
    
    def sigmoid(self, x):
        """Sigmoid function for probability conversion"""
        return 1 / (1 + np.exp(-x))
    
    def log_loss_gradient(self, y_true, y_pred):
        """
        Gradient of log loss with respect to predictions
        """
        # TODO: Compute gradient for binary cross-entropy
        pass
    
    def fit(self, X, y):
        """
        Gradient Boosting algorithm:
        1. Initialize with log-odds
        2. For each iteration:
           - Compute residuals (negative gradient)
           - Fit weak learner to residuals
           - Update predictions
        """
        # TODO: Initialize predictions
        # TODO: Iteratively fit weak learners to gradients
        pass
    
    def predict_proba(self, X):
        """Return probability estimates"""
        # TODO: Aggregate predictions from all estimators
        pass
```

### Part B: XGBoost-style Regularization (30 points)
Add regularization to gradient boosting:

```python
class RegularizedGradientBoosting:
    def __init__(self, n_estimators=100, lambda_=1.0, gamma=0.0):
        """
        lambda_: L2 regularization on leaf weights
        gamma: Minimum loss reduction for split
        """
        self.n_estimators = n_estimators
        self.lambda_ = lambda_
        self.gamma = gamma
    
    def compute_optimal_weight(self, gradient_sum, hessian_sum):
        """
        Optimal weight for leaf with Newton's method
        Including L2 regularization
        """
        # TODO: Implement regularized weight formula
        pass
    
    def compute_gain(self, left_grad, left_hess, right_grad, right_hess):
        """
        Compute gain with regularization and gamma threshold
        """
        # TODO: Implement XGBoost gain formula
        pass
```

### Part C: Stacking Classifier (35 points)
Implement stacking (meta-learning):

```python
class StackingClassifier:
    def __init__(self, base_estimators, meta_estimator, cv_folds=5):
        """
        base_estimators: List of (name, estimator) tuples
        meta_estimator: Final estimator that combines base predictions
        """
        self.base_estimators = base_estimators
        self.meta_estimator = meta_estimator
        self.cv_folds = cv_folds
    
    def generate_base_predictions(self, X, y=None):
        """
        Generate out-of-fold predictions for training
        or simple predictions for testing
        """
        # TODO: K-fold for training, direct prediction for testing
        pass
    
    def fit(self, X, y):
        """
        1. Generate out-of-fold predictions from base models
        2. Train meta-model on these predictions
        """
        # TODO: Implement stacking training
        pass
```

## Exercise 2: Handling Imbalanced Data 📊

Real-world data is rarely balanced. Master these techniques!

### Part A: SMOTE - Synthetic Minority Oversampling (30 points)
```python
class SMOTE:
    def __init__(self, k_neighbors=5, sampling_ratio=1.0):
        """
        Generate synthetic samples for minority class
        """
        self.k_neighbors = k_neighbors
        self.sampling_ratio = sampling_ratio
    
    def generate_synthetic_sample(self, sample, neighbor):
        """
        Create synthetic sample between two points
        """
        # TODO: Linear interpolation between samples
        pass
    
    def fit_resample(self, X, y):
        """
        1. Find k-nearest neighbors for each minority sample
        2. Generate synthetic samples
        3. Return balanced dataset
        """
        # TODO: Implement SMOTE algorithm
        pass
```

### Part B: Cost-Sensitive Learning (25 points)
```python
class CostSensitiveClassifier:
    def __init__(self, base_estimator, class_weights='balanced'):
        """
        Adjust for class imbalance through sample weights
        """
        self.base_estimator = base_estimator
        self.class_weights = class_weights
    
    def compute_sample_weights(self, y):
        """
        Calculate weights inversely proportional to class frequencies
        """
        # TODO: Implement balanced weight calculation
        pass
    
    def fit(self, X, y):
        """
        Train with weighted samples
        """
        # TODO: Apply sample weights during training
        pass
```

### Part C: Threshold Optimization (25 points)
```python
class ThresholdOptimizer:
    def __init__(self, metric='f1'):
        """
        Find optimal decision threshold for specific metric
        """
        self.metric = metric
        self.optimal_threshold = 0.5
    
    def find_optimal_threshold(self, y_true, y_proba):
        """
        Search for threshold that maximizes chosen metric
        """
        # TODO: Grid search over thresholds
        # TODO: Support different metrics (F1, G-mean, etc.)
        pass
```

## Exercise 3: Advanced Multi-class Strategies 🎯

Beyond One-vs-Rest and One-vs-One!

### Part A: Error-Correcting Output Codes (30 points)
```python
class ECOC:
    def __init__(self, code_size=10, base_estimator=None):
        """
        Error-Correcting Output Codes for robust multi-class
        """
        self.code_size = code_size
        self.base_estimator = base_estimator
        self.code_matrix = None
        self.estimators = []
    
    def generate_code_matrix(self, n_classes):
        """
        Generate binary code matrix
        Each column represents a binary classification problem
        """
        # TODO: Create random or deterministic codes
        pass
    
    def fit(self, X, y):
        """
        Train binary classifier for each code column
        """
        # TODO: Transform multi-class to multiple binary problems
        pass
    
    def predict(self, X):
        """
        Decode predictions using Hamming distance
        """
        # TODO: Find closest code word for predictions
        pass
```

### Part B: Hierarchical Classification (35 points)
```python
class HierarchicalClassifier:
    def __init__(self, hierarchy):
        """
        hierarchy: Tree structure of classes
        Example: {'animal': ['cat', 'dog'], 'vehicle': ['car', 'bike']}
        """
        self.hierarchy = hierarchy
        self.node_classifiers = {}
    
    def build_hierarchy_tree(self):
        """
        Build tree of classifiers
        """
        # TODO: Create classifier for each internal node
        pass
    
    def fit(self, X, y):
        """
        Train classifiers hierarchically
        """
        # TODO: Train from root to leaves
        pass
    
    def predict_path(self, X):
        """
        Return full path from root to leaf
        """
        # TODO: Traverse tree making decisions
        pass
```

## Exercise 4: Probabilistic Classification Extensions 🎲

Go beyond basic probability estimates!

### Part A: Calibrated Probabilities (30 points)
```python
class ProbabilityCalibrator:
    def __init__(self, method='platt'):
        """
        Calibrate classifier probabilities
        methods: 'platt' (sigmoid), 'isotonic'
        """
        self.method = method
        self.calibrator = None
    
    def platt_scaling(self, probas, y):
        """
        Fit sigmoid to transform probabilities
        """
        # TODO: Logistic regression on predictions
        pass
    
    def isotonic_regression(self, probas, y):
        """
        Non-parametric isotonic regression
        """
        # TODO: Monotonic function fitting
        pass
    
    def calibrate(self, probas, y):
        """
        Learn calibration mapping
        """
        # TODO: Apply chosen calibration method
        pass
```

### Part B: Conformal Prediction (35 points)
```python
class ConformalPredictor:
    def __init__(self, base_model, significance=0.1):
        """
        Provide prediction sets with confidence guarantees
        """
        self.base_model = base_model
        self.significance = significance
        self.calibration_scores = []
    
    def nonconformity_measure(self, X, y):
        """
        Measure how unusual each example is
        """
        # TODO: Distance to correct class vs others
        pass
    
    def predict_set(self, X):
        """
        Return set of plausible labels with confidence
        """
        # TODO: Include labels within confidence threshold
        pass
```

## Exercise 5: Advanced Feature Selection 🔍

Select the right features for classification!

### Part A: Mutual Information Selection (25 points)
```python
class MutualInformationSelector:
    def __init__(self, n_features=10):
        self.n_features = n_features
        self.selected_features = None
    
    def estimate_mutual_information(self, X, y):
        """
        Estimate MI between each feature and target
        """
        # TODO: Implement MI estimation
        pass
    
    def select_features(self, X, y):
        """
        Select top features by MI
        """
        # TODO: Rank and select features
        pass
```

### Part B: Recursive Feature Elimination with CV (30 points)
```python
class RFECV:
    def __init__(self, estimator, cv=5):
        """
        RFE with cross-validation
        """
        self.estimator = estimator
        self.cv = cv
        self.n_features_ = None
        self.support_ = None
    
    def fit(self, X, y):
        """
        1. Start with all features
        2. Iteratively remove least important
        3. Use CV to find optimal number
        """
        # TODO: Implement RFE with CV
        pass
```

### Part C: L1-based Feature Selection (20 points)
```python
class L1FeatureSelector:
    def __init__(self, C=1.0, threshold=1e-5):
        """
        Use L1 regularization for feature selection
        """
        self.C = C
        self.threshold = threshold
    
    def fit_transform(self, X, y):
        """
        1. Fit L1-regularized model
        2. Select features with non-zero coefficients
        """
        # TODO: Sparse feature selection
        pass
```

## Real-World Project: Credit Card Fraud Detection 💳

Apply everything to detect fraudulent transactions!

```python
class FraudDetector:
    def __init__(self):
        """
        Complete fraud detection pipeline:
        - Handle extreme imbalance (0.1% fraud)
        - Feature engineering
        - Ensemble methods
        - Calibrated probabilities
        - Business metrics optimization
        """
        self.preprocessor = None
        self.feature_selector = None
        self.classifier = None
        self.threshold = 0.5
    
    def engineer_features(self, transactions):
        """
        Create features:
        - Transaction patterns
        - Velocity features
        - Statistical aggregates
        - Anomaly scores
        """
        # TODO: Domain-specific features
        pass
    
    def optimize_for_business(self, y_true, y_proba):
        """
        Optimize for:
        - Precision at fixed recall
        - Cost-sensitive thresholds
        - Alert fatigue management
        """
        # TODO: Business metric optimization
        pass
```

## Bonus Challenges 🌟

### Challenge 1: Online Boosting (30 points)
```python
class OnlineGradientBoosting:
    """Boosting for streaming data"""
    def partial_fit(self, X, y):
        """Update model with new data"""
        pass
```

### Challenge 2: Multi-label Classification (30 points)
```python
class MultiLabelClassifier:
    """Handle multiple labels per instance"""
    def fit(self, X, Y):
        """Y is binary matrix of labels"""
        pass
```

### Challenge 3: Active Learning (30 points)
```python
class ActiveLearner:
    """Query most informative samples"""
    def query_strategy(self, X_pool):
        """Select samples for labeling"""
        pass
```

## Submission Requirements

Your submission should include:
1. `ensemble_methods.py` - Advanced ensemble implementations
2. `imbalanced_learning.py` - Techniques for imbalanced data
3. `multiclass_strategies.py` - Multi-class classification methods
4. `probabilistic_classifiers.py` - Probability calibration and conformal prediction
5. `feature_selection.py` - Advanced feature selection
6. `fraud_detection.py` - Complete fraud detection pipeline
7. `experiments.ipynb` - Comparative analysis
8. `README.md` - Implementation notes and insights

## Grading Rubric

- **Advanced Implementations (40%)**: Correctly implementing complex algorithms
- **Handling Real Challenges (30%)**: Successfully dealing with imbalance, multi-class
- **Experimental Analysis (20%)**: Thorough testing and comparison
- **Code Quality (10%)**: Clean, efficient, documented code

## Tips for Success

1. **Test on Imbalanced Data**: Create synthetic imbalanced datasets
2. **Visualize Decision Boundaries**: Especially for ensemble methods
3. **Monitor Multiple Metrics**: Accuracy isn't enough for imbalanced data
4. **Cross-Validate Carefully**: Stratified folds for imbalanced data
5. **Profile Performance**: Some methods are computationally expensive

## Resources

- [Imbalanced-learn Documentation](https://imbalanced-learn.org/)
- [XGBoost Paper](https://arxiv.org/abs/1603.02754)
- [Ensemble Methods](https://scikit-learn.org/stable/modules/ensemble.html)
- [Learning from Imbalanced Data](https://www.sciencedirect.com/science/article/pii/S0957417408002121)

Remember: Real-world classification is messy - master these techniques to handle it! 💪