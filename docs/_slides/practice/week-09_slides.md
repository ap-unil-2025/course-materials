---
marp: true
paginate: true
header: "Session 9: Clustering Without Crying"
footer: "Anna Smirnova, November 10, 2025"
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

# Clustering Without Crying

**Practical guide to unsupervised learning**

---

# Today's Plan

**15 min:** Common clustering pitfalls
**30 min:** Hands-on clustering exercise

**Goal:** You can cluster data and know when it's working

---

# Supervised vs Unsupervised

**Supervised:** You have labels
```python
X = [[features]], y = [labels]  # "This is a cat", "This is a dog"
model.fit(X, y)  # Learn from labels
```

**Unsupervised:** NO labels
```python
X = [[features]]  # No y!
model.fit(X)  # Find patterns on its own
```

**Clustering = grouping similar things together without being told what the groups are**

---

# The Clustering Toolkit

**K-Means:** Fast, simple, assumes spherical clusters
```python
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
labels = kmeans.fit_predict(X)
```

**DBSCAN:** Finds arbitrary shapes, handles noise
```python
from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X)
```

**Hierarchical:** Builds tree of clusters
```python
from sklearn.cluster import AgglomerativeClustering
hclust = AgglomerativeClustering(n_clusters=3)
labels = hclust.fit_predict(X)
```

---

# K-Means: The Workhorse

**Algorithm:**
1. Pick k random points as cluster centers
2. Assign each point to nearest center
3. Move centers to mean of assigned points
4. Repeat until centers stop moving

**Pros:**
- Fast and simple
- Works well for spherical clusters

**Cons:**
- Must choose k beforehand
- Fails on non-spherical shapes
- Sensitive to outliers

---

# Common Error #1: Not Scaling Data

```python
# ❌ WRONG - Features on different scales
# [[income, age], [50000, 25], [60000, 30]]
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)  # Income dominates!

# ✅ RIGHT - Scale first
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans.fit(X_scaled)
```

**K-Means uses distance → always scale your features!**

---

# Common Error #2: Wrong Number of Clusters

```python
# ❌ Guessing k randomly
kmeans = KMeans(n_clusters=5)  # Why 5?

# ✅ Use elbow method
inertias = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

plt.plot(range(1, 11), inertias)
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
# Look for the "elbow" - where it stops decreasing sharply
```

**Elbow = sweet spot for k**

---

# Common Error #3: Using K-Means on Non-Spherical Data

```python
# Two half-moon shapes next to each other
from sklearn.datasets import make_moons
X, y = make_moons(n_samples=200, noise=0.05)

# ❌ K-Means fails spectacularly
kmeans = KMeans(n_clusters=2)
labels = kmeans.fit_predict(X)  # Splits each moon in half!

# ✅ DBSCAN works great
dbscan = DBSCAN(eps=0.3)
labels = dbscan.fit_predict(X)  # Finds the moons!
```

**Know your data shape before choosing algorithm**

---

# DBSCAN: For Weird Shapes

**Parameters:**
- `eps`: How close points need to be to join a cluster
- `min_samples`: Minimum points to form a cluster

```python
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X)
```

**Special label: -1 = noise/outliers**

**Pros:**
- Finds arbitrary shapes
- Automatically detects outliers
- Don't need to specify number of clusters

**Cons:**
- Sensitive to eps and min_samples
- Struggles with varying densities

---

# Choosing eps for DBSCAN

```python
from sklearn.neighbors import NearestNeighbors

# Plot k-distance graph
neighbors = NearestNeighbors(n_neighbors=5)
neighbors.fit(X_scaled)
distances, indices = neighbors.kneighbors(X_scaled)

distances = np.sort(distances[:, 4], axis=0)
plt.plot(distances)
plt.ylabel('5th Nearest Neighbor Distance')

# Look for the "knee" - that's your eps!
```

**The knee in the curve = good eps value**

---

# Evaluating Clusters (Without Labels)

**Silhouette Score:**
- Measures how similar points are to their own cluster vs other clusters
- Range: -1 to 1 (higher = better)

```python
from sklearn.metrics import silhouette_score

labels = kmeans.fit_predict(X_scaled)
score = silhouette_score(X_scaled, labels)
print(f"Silhouette Score: {score:.2f}")
# > 0.5 = good clustering
# < 0.2 = poor clustering
```

**Warning:** High score doesn't always mean meaningful clusters!

---

# Evaluating Clusters (With Ground Truth)

If you DO have labels (for testing):

```python
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score

# Adjusted Rand Index (0 to 1, higher = better)
ari = adjusted_rand_score(y_true, labels)

# Normalized Mutual Information (0 to 1, higher = better)
nmi = normalized_mutual_info_score(y_true, labels)
```

**Use these to compare clustering algorithms**

---

# Visualizing Clusters

**2D data:**
```python
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], 
            kmeans.cluster_centers_[:, 1],
            marker='X', s=200, c='red')  # Show centers
```

**High-dimensional data → reduce to 2D first:**
```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_scaled)
plt.scatter(X_2d[:, 0], X_2d[:, 1], c=labels, cmap='viridis')
```

**Always visualize to sanity-check your clusters!**

---

# Hierarchical Clustering

**Builds a tree (dendrogram):**

```python
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Fit clustering
hclust = AgglomerativeClustering(n_clusters=3)
labels = hclust.fit_predict(X_scaled)

# Visualize dendrogram
linkage_matrix = linkage(X_scaled, method='ward')
dendrogram(linkage_matrix)
plt.show()
```

**Pro:** Don't need to pick k beforehand (can cut tree anywhere)
**Con:** Slow on large datasets

---

# Quick Reference: Which Algorithm?

**K-Means:**
- Spherical, well-separated clusters
- Know number of clusters
- Need speed

**DBSCAN:**
- Arbitrary shapes
- Don't know number of clusters
- Have outliers to detect

**Hierarchical:**
- Want to explore different k values
- Small-medium datasets
- Need dendrogram

**Start with K-Means, try DBSCAN if it fails**

---

# Debugging: "My Clusters Make No Sense"

**All points in one cluster:**
- K-Means: k too small
- DBSCAN: eps too large

**Every point is its own cluster:**
- K-Means: k too large
- DBSCAN: eps too small or min_samples too high

**Clusters split obvious groups:**
- Forgot to scale features
- Wrong algorithm (try DBSCAN if K-Means fails)

**Silhouette score is negative:**
- Data might not have natural clusters
- Try different algorithm or k

---

# Pro Tips

**1. Always Scale**
```python
from sklearn.preprocessing import StandardScaler
X_scaled = StandardScaler().fit_transform(X)
```

**2. Try Multiple k Values**
```python
for k in range(2, 10):
    kmeans = KMeans(n_clusters=k)
    score = silhouette_score(X_scaled, kmeans.fit_predict(X_scaled))
    print(f"k={k}: score={score:.2f}")
```

**3. Visualize Everything**
- Plot elbow curve
- Plot silhouette scores
- Plot actual clusters

**4. Not All Data Has Clusters**
- Sometimes data is uniformly distributed
- Clustering will still output labels, but they're meaningless

---

<!-- _class: lead -->

# Let's Cluster Some Data!

**Questions before we start?**
