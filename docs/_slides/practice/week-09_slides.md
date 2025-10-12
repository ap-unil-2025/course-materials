---
marp: true
paginate: true
header: "Session 9: NumPy & Data Manipulation"
footer: "Anna Smirnova, November 17, 2025"
style: |
  section.lead {
    background: #003aff;
    color: white;
  }
    section.lead footer {
    color: white;
  }
  section.lead header {
    color: white;
  }
  section.lead h1, section.lead h2, section.lead h3 {
    color: white;
    border-bottom: none;
  }
  section.lead a {
    color: white;
  }
---

<!-- _class: lead -->

# Session 9: Introduction to NumPy

**Efficient Numerical Computing in Python**

---

# Today's Goals

**Part 1: Why NumPy?**
- Limitations of Python lists for numerical data
- What makes NumPy fast
- When to use NumPy vs lists

**Part 2: NumPy Basics**
- Creating arrays
- Array operations
- Indexing and slicing

**Part 3: Data Analysis with NumPy**
- Statistical operations
- Aggregations
- Real-world examples

---

# Part 1: Why NumPy?

---

# The Problem with Python Lists

```python
# Python list approach - slow for large datasets
prices = [100, 105, 102, 108, 112, 109]

# Calculate percentage change
percent_change = []
for i in range(1, len(prices)):
    change = (prices[i] - prices[i-1]) / prices[i-1] * 100
    percent_change.append(change)

print(percent_change)  # [5.0, -2.86, 5.88, 3.70, -2.68]
```

**Issues**:
- Loops are slow for large datasets
- Lists store references, not raw numbers
- No built-in mathematical operations
- Memory inefficient

---

# Enter NumPy

```python
import numpy as np

# NumPy approach - fast and clean
prices = np.array([100, 105, 102, 108, 112, 109])

# Calculate percentage change (no loop needed!)
percent_change = (prices[1:] - prices[:-1]) / prices[:-1] * 100

print(percent_change)  # [5.0  -2.857  5.882  3.704  -2.679]
```

**Benefits**:
- **Vectorized operations** - no explicit loops
- **Memory efficient** - stores raw numbers
- **Fast** - implemented in C
- **Built-in math** - mean, std, sum, etc.

---

# NumPy vs Lists: Speed Comparison

```python
import numpy as np
import time

# Large dataset
size = 1_000_000

# Python list
py_list = list(range(size))
start = time.time()
result = [x * 2 for x in py_list]
print(f"List time: {time.time() - start:.4f}s")

# NumPy array
np_array = np.arange(size)
start = time.time()
result = np_array * 2
print(f"NumPy time: {time.time() - start:.4f}s")
```

**Output**:
```
List time: 0.0850s
NumPy time: 0.0015s  # ~50x faster!
```

---

# When to Use NumPy vs Lists

**Use Python lists when**:
- Mixed data types (strings, numbers, objects)
- Small datasets
- Dynamic size changes (append/remove frequently)
- General-purpose programming

**Use NumPy when**:
- Numerical data only
- Large datasets
- Mathematical operations
- Data analysis/science
- Performance matters

---

# Part 2: NumPy Basics

---

# Installing NumPy

```bash
# Using uv (recommended)
uv pip install numpy

# Or using pip
pip install numpy
```

**Importing**:
```python
import numpy as np  # Standard convention
```

---

# Creating NumPy Arrays

```python
import numpy as np

# From Python list
arr1 = np.array([1, 2, 3, 4, 5])

# Range of values
arr2 = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

# Evenly spaced values
arr3 = np.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1]

# Zeros and ones
zeros = np.zeros(5)       # [0, 0, 0, 0, 0]
ones = np.ones(5)         # [1, 1, 1, 1, 1]

# Random numbers
random = np.random.rand(5)  # Random floats [0, 1)
```

---

# Array Properties

```python
arr = np.array([1, 2, 3, 4, 5])

print(arr.shape)    # (5,) - dimensions
print(arr.dtype)    # dtype('int64') - data type
print(arr.size)     # 5 - number of elements
print(arr.ndim)     # 1 - number of dimensions

# 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d.shape)  # (2, 3) - 2 rows, 3 columns
print(arr2d.ndim)   # 2
```

---

# Array Operations (Vectorized!)

```python
arr = np.array([1, 2, 3, 4, 5])

# Arithmetic operations
print(arr + 10)      # [11, 12, 13, 14, 15]
print(arr * 2)       # [2, 4, 6, 8, 10]
print(arr ** 2)      # [1, 4, 9, 16, 25]

# Array with array
arr2 = np.array([5, 4, 3, 2, 1])
print(arr + arr2)    # [6, 6, 6, 6, 6]
print(arr * arr2)    # [5, 8, 9, 8, 5]

# Comparison operations
print(arr > 3)       # [False, False, False, True, True]
```

**No loops needed!** Operations apply to all elements automatically.

---

# Indexing and Slicing

```python
arr = np.array([10, 20, 30, 40, 50])

# Indexing (same as lists)
print(arr[0])        # 10
print(arr[-1])       # 50

# Slicing (same as lists)
print(arr[1:4])      # [20, 30, 40]
print(arr[:3])       # [10, 20, 30]
print(arr[::2])      # [10, 30, 50]

# Boolean indexing (powerful!)
mask = arr > 25
print(arr[mask])     # [30, 40, 50]

# Or in one line
print(arr[arr > 25]) # [30, 40, 50]
```

---

# 2D Arrays (Matrices)

```python
# Create 2D array
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Indexing: [row, column]
print(data[0, 0])      # 1
print(data[1, 2])      # 6

# Slicing rows and columns
print(data[0, :])      # [1, 2, 3] - first row
print(data[:, 0])      # [1, 4, 7] - first column
print(data[1:, 1:])    # [[5, 6], [8, 9]]

# Row and column operations
print(data.sum(axis=0))  # [12, 15, 18] - sum columns
print(data.sum(axis=1))  # [6, 15, 24] - sum rows
```

---

# Part 3: Data Analysis with NumPy

---

# Statistical Operations

```python
prices = np.array([100, 105, 102, 108, 112, 109, 115])

# Basic statistics
print(f"Mean: {prices.mean()}")           # 107.29
print(f"Median: {np.median(prices)}")     # 108
print(f"Std Dev: {prices.std()}")         # 5.07
print(f"Min: {prices.min()}")             # 100
print(f"Max: {prices.max()}")             # 115

# More statistics
print(f"Range: {prices.ptp()}")           # 15 (peak-to-peak)
print(f"Variance: {prices.var()}")        # 25.73
print(f"25th percentile: {np.percentile(prices, 25)}")  # 102.5
```

---

# Aggregations

```python
sales = np.array([
    [100, 120, 110],  # Product A
    [80, 90, 95],     # Product B
    [150, 140, 160]   # Product C
])

# Total sales
print(f"Total: {sales.sum()}")           # 1145

# Sales per product (sum across columns)
print(f"Per product: {sales.sum(axis=1)}")  # [330, 265, 450]

# Sales per period (sum across rows)
print(f"Per period: {sales.sum(axis=0)}")   # [330, 350, 365]

# Average sales per product
print(f"Avg per product: {sales.mean(axis=1)}")  # [110, 88.33, 150]
```

---

# Real-World Example: Stock Analysis

```python
# Daily closing prices
prices = np.array([100, 102, 98, 105, 110, 108, 112, 115])

# Calculate daily returns
returns = (prices[1:] - prices[:-1]) / prices[:-1]

print(f"Average daily return: {returns.mean():.2%}")
print(f"Volatility (std): {returns.std():.2%}")
print(f"Best day: {returns.max():.2%}")
print(f"Worst day: {returns.min():.2%}")

# Cumulative return
total_return = (prices[-1] - prices[0]) / prices[0]
print(f"Total return: {total_return:.2%}")
```

**Output**:
```
Average daily return: 1.77%
Volatility (std): 3.63%
Best day: 7.14%
Worst day: -3.92%
Total return: 15.00%
```

---

# Hands-On Exercise 1: Temperature Analysis

```python
# Daily temperatures (°C) for a week
temps = np.array([18, 20, 22, 19, 21, 23, 20])

# Your tasks:
# 1. Calculate average temperature
# 2. Find hottest and coldest days
# 3. Calculate temperature range
# 4. Find days above average
# 5. Calculate standard deviation
```

---

# Exercise 1: Solution

```python
temps = np.array([18, 20, 22, 19, 21, 23, 20])

# 1. Average temperature
print(f"Average: {temps.mean():.1f}°C")  # 20.4°C

# 2. Hottest and coldest
print(f"Hottest: {temps.max()}°C")       # 23°C
print(f"Coldest: {temps.min()}°C")       # 18°C

# 3. Temperature range
print(f"Range: {temps.ptp()}°C")         # 5°C

# 4. Days above average
above_avg = temps[temps > temps.mean()]
print(f"Days above avg: {len(above_avg)}")  # 3

# 5. Standard deviation
print(f"Std Dev: {temps.std():.2f}°C")   # 1.60°C
```

---

# Hands-On Exercise 2: Sales Data

```python
# Quarterly sales for 3 products
sales = np.array([
    [1200, 1500, 1300, 1600],  # Product A
    [800, 900, 950, 1000],     # Product B
    [2000, 2200, 2100, 2300]   # Product C
])

# Your tasks:
# 1. Total sales for each product
# 2. Total sales per quarter
# 3. Best performing product
# 4. Strongest quarter
# 5. Average quarterly sales per product
```

---

# Exercise 2: Solution

```python
sales = np.array([
    [1200, 1500, 1300, 1600],
    [800, 900, 950, 1000],
    [2000, 2200, 2100, 2300]
])

# 1. Total sales per product
product_totals = sales.sum(axis=1)
print(f"Product totals: {product_totals}")  # [5600, 3650, 8600]

# 2. Total sales per quarter
quarter_totals = sales.sum(axis=0)
print(f"Quarter totals: {quarter_totals}")  # [4000, 4600, 4350, 4900]

# 3. Best performing product
best_product = product_totals.argmax()
print(f"Best product: {best_product} (Product C)")

# 4. Strongest quarter
best_quarter = quarter_totals.argmax()
print(f"Strongest quarter: {best_quarter} (Q4)")

# 5. Average quarterly sales
avg_sales = sales.mean(axis=1)
print(f"Avg per product: {avg_sales}")  # [1400, 912.5, 2150]
```

---

# Common NumPy Gotchas

**1. Views vs Copies**
```python
arr = np.array([1, 2, 3, 4, 5])
slice_arr = arr[1:4]  # This is a view!
slice_arr[0] = 99
print(arr)  # [1, 99, 3, 4, 5] - Original changed!

# To avoid this, make a copy:
slice_arr = arr[1:4].copy()
```

**2. Integer Division**
```python
arr = np.array([1, 2, 3])
print(arr / 2)        # [0.5, 1, 1.5] - float division
print(arr // 2)       # [0, 1, 1] - integer division
```

---

# Key Takeaways

**NumPy Advantages**:
- **Fast**: 10-100x faster than Python lists
- **Vectorized**: No explicit loops needed
- **Memory efficient**: Stores raw numbers
- **Built-in math**: Statistics, linear algebra, etc.

**Core Concepts**:
- Arrays are homogeneous (one data type)
- Vectorized operations apply to all elements
- Boolean indexing for filtering
- Axis parameter for row/column operations

**Next Week**: We'll learn Pandas, which builds on NumPy to provide even more powerful data analysis tools!

---

# Homework Assignment

**Analyze Your Own Dataset**

Create a Jupyter notebook that:

1. **Load data**: Use `np.array()` or `np.loadtxt()` to load numerical data
   - Stock prices, temperature data, sales data, etc.

2. **Descriptive statistics**: Calculate mean, median, std, min, max

3. **Analysis**: Answer 3 questions about your data using NumPy operations

4. **Visualization**: Create at least one plot (we'll cover this more next week)

**Deliverable**: Jupyter notebook with code, results, and brief explanations

---

<!-- _class: lead -->

# Questions?

**Next week**: Pandas for powerful data analysis!
