---
marp: true
theme: unil-theme
paginate: true
backgroundColor: #f5f9ff
size: 16:9
title: "Scientific Computing in Python"
description: "NumPy, Pandas, and Jupyter Notebooks for Data Science"
author: "Data Science Course"
date: "2025-10-20"
header: "Session 6: Scientific Computing in Python"
footer: "NumPy, Pandas, and Jupyter Notebooks"
---

<!-- _class: lead -->

# Session 6: Scientific Computing in Python

**NumPy Arrays, Pandas DataFrames, and Jupyter Notebooks**

---

# Today's Goals

- Master **NumPy arrays** for efficient numerical computing
- Use **Pandas** for data manipulation and analysis  
- Work effectively with **Jupyter notebooks** for exploration
- Understand **vectorization** and performance optimization
- Build the foundation for **statistical learning**

---
<!-- _class: invert -->

# Part 1: NumPy - The Foundation of Scientific Python

---

# Why NumPy?

**The Problem with Pure Python:**
```python
# Slow: Python lists with loops
data = [1, 2, 3, 4, 5] * 100000
result = []
for x in data:
    result.append(x ** 2)
```

**The NumPy Solution:**
```python
# Fast: NumPy arrays with vectorization
import numpy as np
data = np.array([1, 2, 3, 4, 5] * 100000)
result = data ** 2  # 100x faster!
```

---

# NumPy Arrays: The Basics

```python
import numpy as np

# Creating arrays
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# Array properties
print(arr2d.shape)    # (2, 3)
print(arr2d.dtype)    # int64
print(arr2d.ndim)     # 2
print(arr2d.size)     # 6

# Special arrays
zeros = np.zeros((3, 4))
ones = np.ones((2, 5))
identity = np.eye(3)
random_data = np.random.random((100, 3))
```

---

# Financial Data with NumPy

```python
# Stock price analysis
prices = np.array([100, 105, 98, 110, 103, 108])

# Calculate returns
returns = (prices[1:] - prices[:-1]) / prices[:-1]
print(f"Returns: {returns}")

# Portfolio calculations
weights = np.array([0.4, 0.3, 0.3])
asset_returns = np.array([[0.05, 0.02, 0.08],
                         [0.03, 0.04, 0.06],
                         [-0.01, 0.03, 0.04]])

# Portfolio return for each period
portfolio_returns = np.sum(asset_returns * weights, axis=1)
```

---

# Vectorization: The NumPy Superpower

```python
# Instead of loops...
result = []
for i in range(len(prices)):
    result.append(prices[i] * 1.02)  # 2% increase

# Use vectorization!
result = prices * 1.02

# Complex operations vectorized
risk_adjusted = (returns - 0.02) / np.std(returns)

# Boolean indexing
high_return_days = returns[returns > 0.05]
```

**Key Point**: Vectorization is not just faster, it's more readable!

---

# NumPy for Linear Algebra

```python
# Covariance matrix calculation
returns_matrix = np.array([[0.05, 0.02, 0.08],
                          [0.03, 0.04, 0.06], 
                          [-0.01, 0.03, 0.04]])

cov_matrix = np.cov(returns_matrix.T)
print("Covariance Matrix:")
print(cov_matrix)

# Portfolio risk calculation
portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
print(f"Portfolio Risk: {portfolio_risk:.4f}")
```

---
<!-- _class: invert -->

# Part 2: Pandas - Data Manipulation Made Easy

---

# Why Pandas?

**NumPy** is great for numerical arrays, but real data is messy:
- Missing values
- Different data types  
- Row and column labels
- Time series data
- Grouping and aggregation

**Pandas** provides labeled, heterogeneous data structures built on NumPy.

---

# Pandas Data Structures

```python
import pandas as pd

# Series: 1-dimensional labeled array
stock_prices = pd.Series([100, 105, 98, 110], 
                        index=['AAPL', 'GOOGL', 'MSFT', 'AMZN'])

# DataFrame: 2-dimensional labeled data
portfolio = pd.DataFrame({
    'Symbol': ['AAPL', 'GOOGL', 'MSFT', 'AMZN'],
    'Price': [150.25, 2800.50, 310.75, 3400.25],
    'Shares': [100, 10, 50, 5],
    'Sector': ['Tech', 'Tech', 'Tech', 'Consumer']
})

print(portfolio)
```

---

# Loading Real Data

```python
# Reading from various sources
df = pd.read_csv('financial_data.csv')
df = pd.read_excel('portfolio.xlsx', sheet_name='holdings')
df = pd.read_json('market_data.json')

# Quick data inspection
print(df.head())        # First 5 rows
print(df.info())        # Data types and missing values
print(df.describe())    # Statistical summary
print(df.shape)         # (rows, columns)
```

---

# Data Cleaning and Transformation

```python
# Handling missing data
df_clean = df.dropna()                    # Remove rows with NaN
df_filled = df.fillna(method='ffill')     # Forward fill
df_interpolated = df.interpolate()        # Linear interpolation

# Data type conversion
df['Date'] = pd.to_datetime(df['Date'])
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Creating new columns
df['Market_Value'] = df['Price'] * df['Shares']
df['Weight'] = df['Market_Value'] / df['Market_Value'].sum()
df['Return'] = df['Price'].pct_change()
```

---

# Data Selection and Filtering

```python
# Column selection
prices = df['Price']
subset = df[['Symbol', 'Price', 'Market_Value']]

# Boolean filtering
high_value = df[df['Market_Value'] > 10000]
tech_stocks = df[df['Sector'] == 'Tech']

# Multiple conditions
large_tech = df[(df['Sector'] == 'Tech') & 
                (df['Market_Value'] > 5000)]

# Date-based filtering (if Date is index)
recent = df.loc['2025-01-01':'2025-01-31']
```

---

# Grouping and Aggregation

```python
# Group by sector analysis
sector_analysis = df.groupby('Sector').agg({
    'Market_Value': ['sum', 'mean', 'count'],
    'Price': ['min', 'max'],
    'Return': 'std'
})

# Custom aggregation
def portfolio_metrics(group):
    return pd.Series({
        'total_value': group['Market_Value'].sum(),
        'avg_return': group['Return'].mean(),
        'volatility': group['Return'].std(),
        'sharpe_ratio': group['Return'].mean() / group['Return'].std()
    })

metrics_by_sector = df.groupby('Sector').apply(portfolio_metrics)
```

---

# Time Series with Pandas

```python
# Set date as index
df.set_index('Date', inplace=True)

# Resampling time series
daily_prices = df.resample('D')['Price'].last()      # Daily
monthly_avg = df.resample('M')['Price'].mean()       # Monthly averages

# Rolling calculations
df['MA_20'] = df['Price'].rolling(20).mean()         # 20-day moving average
df['Volatility'] = df['Return'].rolling(30).std()    # 30-day volatility

# Lag operations
df['Price_Lag1'] = df['Price'].shift(1)
df['Return'] = (df['Price'] - df['Price_Lag1']) / df['Price_Lag1']
```

---
<!-- _class: invert -->

# Part 3: Jupyter Notebooks - Interactive Data Science

---

# Why Jupyter Notebooks?

**Traditional Scripts** → Run all at once, hard to experiment

**Jupyter Notebooks** → Interactive cells, perfect for:
- Data exploration
- Iterative analysis  
- Visualization
- Documentation
- Sharing results

**Best for**: Prototyping, analysis, teaching
**Not best for**: Production code, large applications

---

# Jupyter Best Practices

```python
# 1. Organize imports at the top
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# 2. Define functions in separate cells
def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
    excess_returns = returns - risk_free_rate
    return np.mean(excess_returns) / np.std(excess_returns)

# 3. Load and explore data step by step
df = pd.read_csv('data.csv')
df.head()
```

---

# Jupyter Magic Commands

```python
# Timing code execution
%time result = expensive_calculation()

%%time  
# Time entire cell
for i in range(1000):
    complex_operation()

# Other useful magics
%matplotlib inline    # Display plots in notebook
%load script.py       # Load external Python file
?pd.DataFrame         # Get help
??np.array           # Show source code
%who                 # List variables
```

---

# Example: Complete Portfolio Analysis

```python
# Step 1: Load and clean data
portfolio_data = pd.read_csv('portfolio.csv')
portfolio_data['Date'] = pd.to_datetime(portfolio_data['Date'])
portfolio_data.set_index('Date', inplace=True)

# Step 2: Calculate returns
for stock in ['AAPL', 'GOOGL', 'MSFT']:
    portfolio_data[f'{stock}_Return'] = portfolio_data[stock].pct_change()

# Step 3: Portfolio metrics
returns_cols = [col for col in portfolio_data.columns if 'Return' in col]
returns_matrix = portfolio_data[returns_cols].dropna()

weights = np.array([0.4, 0.3, 0.3])
portfolio_returns = np.dot(returns_matrix, weights)
sharpe_ratio = calculate_sharpe_ratio(portfolio_returns)

print(f"Portfolio Sharpe Ratio: {sharpe_ratio:.3f}")
```

---

# Integration: NumPy + Pandas + Jupyter

```python
# NumPy for mathematical operations
correlation_matrix = np.corrcoef(returns_matrix.T)

# Pandas for data structure and manipulation
corr_df = pd.DataFrame(correlation_matrix, 
                      index=['AAPL', 'GOOGL', 'MSFT'],
                      columns=['AAPL', 'GOOGL', 'MSFT'])

# Jupyter for interactive exploration and visualization
import seaborn as sns
plt.figure(figsize=(8, 6))
sns.heatmap(corr_df, annot=True, cmap='coolwarm', center=0)
plt.title('Stock Correlation Matrix')
plt.show()
```

---

# Performance Tips

```python
# Do: Vectorize with NumPy/Pandas
df['normalized'] = (df['value'] - df['value'].mean()) / df['value'].std()

# Don't: Use Python loops
normalized = []
mean_val = df['value'].mean()
std_val = df['value'].std()
for val in df['value']:
    normalized.append((val - mean_val) / std_val)

# Do: Use built-in methods
df.groupby('category')['value'].mean()

# Don't: Manual grouping
categories = df['category'].unique()
means = {}
for cat in categories:
    means[cat] = df[df['category'] == cat]['value'].mean()
```

---

# Next Steps: Statistical Learning Foundation

With NumPy, Pandas, and Jupyter, you now have the tools for:

- **Data Loading**: Read from CSV, Excel, databases
- **Data Cleaning**: Handle missing values, outliers
- **Feature Engineering**: Create new variables
- **Exploratory Analysis**: Understand your data
- **Statistical Computing**: Efficient numerical operations

**Next week**: We'll use these tools for statistical learning, starting with visualization and the statistical learning framework!

---

# Resources

- **NumPy Documentation**: [numpy.org](https://numpy.org/doc/)
- **Pandas Documentation**: [pandas.pydata.org](https://pandas.pydata.org/docs/)  
- **Jupyter Documentation**: [jupyter.org](https://jupyter.org/documentation)
- **Python for Data Analysis** by Wes McKinney
- **Course Examples**: Available in Nuvolos workspace

---

# Hands-on Lab

**Lab Activity**: Complete portfolio analysis
1. Load sample financial dataset
2. Clean and prepare the data
3. Calculate portfolio metrics using NumPy
4. Create summary statistics with Pandas
5. Document your analysis in Jupyter notebook

**Goal**: Create a reproducible analysis that demonstrates scientific computing workflow!