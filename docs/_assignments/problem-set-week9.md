---
layout: assignment
title: "Problem Set Week 9: Unsupervised Learning"
assignment_number: 109
due_date: 2025-11-17 23:59:00
difficulty: "Intermediate-Advanced"
estimated_time: "5-6 hours"
github_classroom_url: "https://classroom.github.com/a/pQ9mK3nT-ps-week9"
topics:
  - "k-means clustering"
  - "Hierarchical clustering"
  - "DBSCAN"
  - "Gaussian Mixture Models"
  - "Dimensionality reduction"
status: "active"
description: "Discover hidden patterns in data without labels using clustering and dimensionality reduction"
---

# Problem Set 9: Unsupervised Learning - Finding Hidden Patterns

Welcome to the world of unsupervised learning! This week you'll implement algorithms that find structure in unlabeled data.

## Exercise 1: Customer Segmentation System 🛍️

Build a complete customer segmentation pipeline for an e-commerce company!

### Part A: k-Means Clustering (30 points)
Implement k-means from scratch:

```python
class KMeansClustering:
    def __init__(self, n_clusters=3, max_iters=100, random_state=42):
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.random_state = random_state
        self.centroids = None
        self.labels = None
        self.inertia_ = None
    
    def fit(self, X):
        """
        Implement k-means algorithm:
        1. Initialize centroids (k-means++)
        2. Assign points to nearest centroid
        3. Update centroids
        4. Repeat until convergence
        """
        # TODO: Implement k-means++  initialization
        # TODO: Implement Lloyd's algorithm
        # TODO: Calculate inertia (sum of squared distances)
        pass
    
    def predict(self, X):
        """Assign new points to nearest centroid"""
        # TODO: Find nearest centroid for each point
        pass
    
    def elbow_method(self, X, k_range):
        """Find optimal number of clusters"""
        # TODO: Test different k values
        # TODO: Plot inertia vs k
        # TODO: Identify elbow point
        pass
```

### Part B: Hierarchical Clustering (35 points)
Build dendrograms and hierarchical clusters:

```python
class HierarchicalClustering:
    def __init__(self, n_clusters=None, linkage='single'):
        self.n_clusters = n_clusters
        self.linkage = linkage  # single, complete, average
        self.dendrogram = None
    
    def fit(self, X):
        """
        Build hierarchy bottom-up:
        1. Start with each point as cluster
        2. Merge closest clusters
        3. Update distance matrix
        4. Repeat until desired clusters
        """
        # TODO: Implement agglomerative clustering
        # TODO: Store merge history for dendrogram
        pass
    
    def compute_distance_matrix(self, X):
        """Calculate pairwise distances"""
        # TODO: Compute distance matrix
        pass
    
    def plot_dendrogram(self):
        """Visualize clustering hierarchy"""
        # TODO: Create dendrogram visualization
        pass
```

### Part C: Customer Profiling (35 points)
Analyze and interpret clusters:

```python
def profile_customer_segments(X, labels, feature_names):
    """
    For each cluster:
    - Calculate centroid (typical customer)
    - Find most important features
    - Generate business insights
    - Name the segment (e.g., "Budget Conscious", "Premium Shoppers")
    """
    profiles = {}
    # TODO: Analyze each cluster
    # TODO: Create interpretable descriptions
    return profiles
```

## Exercise 2: Anomaly Detection System 🚨

Detect fraudulent transactions and outliers!

### Part A: DBSCAN Implementation (35 points)
Density-based clustering for anomaly detection:

```python
class DBSCAN:
    def __init__(self, eps=0.5, min_samples=5):
        self.eps = eps  # Neighborhood radius
        self.min_samples = min_samples  # Min points for core point
        self.labels = None
        self.core_points = set()
        self.noise_points = set()
    
    def fit(self, X):
        """
        DBSCAN algorithm:
        1. Find core points (dense regions)
        2. Form clusters from core points
        3. Assign border points
        4. Mark noise points as outliers
        """
        # TODO: Find neighbors for each point
        # TODO: Identify core, border, and noise points
        # TODO: Form clusters using density connectivity
        pass
    
    def find_neighbors(self, X, point_idx):
        """Find all points within eps distance"""
        # TODO: Efficient neighbor search
        pass
```

### Part B: Isolation Forest (35 points)
Implement tree-based anomaly detection:

```python
class IsolationTree:
    def __init__(self, max_depth=10):
        self.max_depth = max_depth
        self.root = None
    
    def fit(self, X):
        """Build isolation tree with random splits"""
        # TODO: Randomly split data
        # TODO: Isolate anomalies quickly
        pass
    
    def path_length(self, x):
        """Calculate path length to isolate point"""
        # TODO: Shorter path = more anomalous
        pass

class IsolationForest:
    def __init__(self, n_trees=100):
        self.n_trees = n_trees
        self.trees = []
    
    def anomaly_score(self, X):
        """
        Calculate anomaly scores:
        - Average path length across trees
        - Normalize to [0, 1]
        """
        # TODO: Ensemble of isolation trees
        pass
```

### Part C: Visualization & Interpretation (30 points)
```python
def visualize_anomalies(X, anomaly_scores, threshold=0.9):
    """
    Create comprehensive anomaly visualization:
    - 2D/3D scatter plot with anomalies highlighted
    - Distribution of anomaly scores
    - Feature analysis for anomalous points
    """
    # TODO: Create interpretable visualizations
    pass
```

## Exercise 3: Gaussian Mixture Models 🔔

Implement soft clustering with probability distributions!

### Part A: GMM with EM Algorithm (40 points)
```python
class GaussianMixtureModel:
    def __init__(self, n_components=3, max_iters=100):
        self.n_components = n_components
        self.max_iters = max_iters
        self.means = None
        self.covariances = None
        self.weights = None  # Mixing coefficients
    
    def fit(self, X):
        """
        Expectation-Maximization algorithm:
        1. E-step: Calculate responsibilities
        2. M-step: Update parameters
        3. Calculate log-likelihood
        4. Repeat until convergence
        """
        # TODO: Initialize parameters
        # TODO: Implement EM algorithm
        pass
    
    def e_step(self, X):
        """Calculate posterior probabilities (responsibilities)"""
        # TODO: Use Bayes' rule
        pass
    
    def m_step(self, X, responsibilities):
        """Update means, covariances, and weights"""
        # TODO: Maximum likelihood estimates
        pass
    
    def multivariate_gaussian(self, X, mean, cov):
        """Calculate multivariate Gaussian probability"""
        # TODO: Implement PDF
        pass
```

### Part B: Model Selection (30 points)
Choose optimal number of components:

```python
def select_gmm_components(X, max_components=10):
    """
    Use information criteria:
    - BIC (Bayesian Information Criterion)
    - AIC (Akaike Information Criterion)
    - Cross-validation likelihood
    """
    # TODO: Test different component numbers
    # TODO: Calculate and compare criteria
    pass
```

### Part C: Sampling & Generation (30 points)
```python
def generate_samples(gmm, n_samples=1000):
    """
    Generate new data points from fitted GMM:
    1. Sample component from mixing weights
    2. Sample point from chosen Gaussian
    """
    # TODO: Implement generative sampling
    pass
```

## Exercise 4: Dimensionality Reduction 📊

Visualize high-dimensional data!

### Part A: PCA from Scratch (35 points)
```python
class PCA:
    def __init__(self, n_components=2):
        self.n_components = n_components
        self.components = None  # Principal components
        self.explained_variance = None
        self.mean = None
    
    def fit(self, X):
        """
        PCA algorithm:
        1. Center the data
        2. Calculate covariance matrix
        3. Find eigenvalues and eigenvectors
        4. Select top components
        """
        # TODO: Implement PCA
        pass
    
    def transform(self, X):
        """Project data onto principal components"""
        # TODO: Linear transformation
        pass
    
    def inverse_transform(self, X_transformed):
        """Reconstruct original data (approximately)"""
        # TODO: Reverse transformation
        pass
```

### Part B: t-SNE Visualization (35 points)
Implement t-SNE for non-linear dimensionality reduction:

```python
class TSNE:
    def __init__(self, n_components=2, perplexity=30.0):
        self.n_components = n_components
        self.perplexity = perplexity
    
    def fit_transform(self, X):
        """
        t-SNE algorithm:
        1. Calculate pairwise similarities in high-D
        2. Initialize low-D representation
        3. Optimize using gradient descent
        """
        # TODO: Implement simplified t-SNE
        pass
    
    def compute_joint_probabilities(self, X):
        """Calculate similarity matrix with Gaussian kernel"""
        # TODO: Handle perplexity parameter
        pass
```

### Part C: Autoencoder (30 points)
Simple neural network for dimensionality reduction:

```python
class Autoencoder:
    def __init__(self, input_dim, encoding_dim):
        self.input_dim = input_dim
        self.encoding_dim = encoding_dim
        self.encoder_weights = None
        self.decoder_weights = None
    
    def encode(self, X):
        """Compress to lower dimension"""
        # TODO: Forward pass through encoder
        pass
    
    def decode(self, encoded):
        """Reconstruct from encoding"""
        # TODO: Forward pass through decoder
        pass
    
    def fit(self, X, learning_rate=0.01, epochs=100):
        """Train using reconstruction loss"""
        # TODO: Implement training loop
        pass
```

## Real-World Projects 🌍

### Project A: Music Recommendation System
```python
def build_music_recommender(song_features, user_history):
    """
    1. Cluster songs by audio features
    2. Find user's preferred clusters
    3. Recommend songs from those clusters
    4. Use collaborative filtering
    """
    # TODO: Complete recommendation system
    pass
```

### Project B: Image Compression
```python
def compress_image(image, compression_ratio=0.1):
    """
    Use k-means for color quantization:
    1. Treat pixels as 3D points (RGB)
    2. Cluster to reduce colors
    3. Replace pixels with cluster centers
    """
    # TODO: Implement compression
    pass
```

### Project C: Document Clustering
```python
def cluster_documents(documents):
    """
    1. Convert documents to TF-IDF vectors
    2. Reduce dimensionality with PCA
    3. Cluster similar documents
    4. Extract topics per cluster
    """
    # TODO: NLP clustering pipeline
    pass
```

## Bonus Challenges 🌟

### Challenge 1: Spectral Clustering (25 points)
Graph-based clustering using eigenvalues:
```python
class SpectralClustering:
    def fit(self, X):
        """
        1. Build similarity graph
        2. Calculate graph Laplacian
        3. Find eigenvectors
        4. Cluster in eigenspace
        """
        # TODO: Implement spectral clustering
        pass
```

### Challenge 2: Mean Shift Clustering (25 points)
Mode-seeking algorithm:
```python
class MeanShift:
    def fit(self, X, bandwidth=1.0):
        """
        Iteratively shift points toward density modes
        """
        # TODO: Implement mean shift
        pass
```

### Challenge 3: Variational Autoencoder (25 points)
Probabilistic dimensionality reduction:
```python
class VAE:
    def __init__(self, latent_dim):
        """
        Add probabilistic layer to autoencoder
        """
        # TODO: Implement VAE basics
        pass
```

## Submission Requirements

Your submission should include:
1. `clustering.py` - All clustering implementations
2. `dimensionality_reduction.py` - PCA, t-SNE, autoencoder
3. `anomaly_detection.py` - DBSCAN, Isolation Forest
4. `experiments.ipynb` - Comprehensive experiments
5. `visualizations/` - All generated plots
6. `README.md` - Analysis and insights

## Grading Rubric

- **Algorithm Implementation (40%)**: Correct, efficient algorithms
- **Experimental Analysis (25%)**: Thorough testing and comparison
- **Visualization Quality (20%)**: Clear, informative plots
- **Code Quality (15%)**: Clean, documented, modular code

## Tips for Success

1. **Normalize Features**: Clustering is sensitive to scale
2. **Visualize Clusters**: Always plot results to verify
3. **Try Multiple Algorithms**: No single best clustering method
4. **Validate Results**: Use silhouette score, Davies-Bouldin index
5. **Handle High Dimensions**: Curse of dimensionality is real

## Common Pitfalls

- Not standardizing features before clustering
- Assuming spherical clusters (k-means limitation)
- Ignoring outliers' effect on centroids
- Using too many clusters (overfitting)
- Not checking cluster stability

## Resources

- [Clustering Visualization](https://www.naftaliharris.com/blog/visualizing-k-means-clustering/)
- [t-SNE Explained](https://distill.pub/2016/misread-tsne/)
- [EM Algorithm Tutorial](https://www.cs.utah.edu/~piyush/teaching/EM_algorithm.pdf)

## Fun Facts 🤓

- k-means was invented in 1957 for pulse-code modulation
- DBSCAN stands for "Density-Based Spatial Clustering of Applications with Noise"
- t-SNE can create beautiful visualizations but can also be misleading
- Gaussian mixtures can approximate any continuous distribution
- PCA was invented by Karl Pearson in 1901

Remember: Unsupervised learning is like being a detective - you're looking for clues and patterns without knowing what you'll find! 🔍