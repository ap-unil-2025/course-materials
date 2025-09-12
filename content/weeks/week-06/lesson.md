---
layout: lesson
title: "Scientific Computing in Python"
week: 6
date: 2025-10-20
type: "programming"
topics:
  - NumPy arrays and vectorization
  - Pandas data cleaning, transformation, grouping
  - Jupyter notebooks
  - Scientific computing workflow
slides: "/slides/practice/week06_slides.html"
summary: "Introduction to scientific computing with NumPy for numerical operations and Pandas for data manipulation, plus effective use of Jupyter notebooks."
---

# Scientific Computing in Python

This lesson introduces the core scientific computing libraries that form the foundation of data science in Python: NumPy for numerical computations and Pandas for data manipulation.

## Learning Objectives

By the end of this lesson, you will:

- Create and manipulate NumPy arrays for efficient numerical computing
- Apply vectorization techniques for performance optimization
- Use Pandas for data cleaning, transformation, and analysis
- Perform grouping and aggregation operations on datasets
- Work effectively with Jupyter notebooks for exploratory data analysis
- Understand the scientific computing workflow for research

## NumPy: Numerical Computing Foundation

### Why NumPy?
- **Performance**: Operations are implemented in C, much faster than pure Python
- **Vectorization**: Operate on entire arrays without explicit loops
- **Memory Efficient**: Homogeneous data types, compact storage
- **Foundation**: Base for other scientific libraries (Pandas, SciPy, scikit-learn)

### NumPy Arrays Basics
```python
import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Array properties
print(arr1.shape)      # (5,)
print(arr2.shape)      # (2, 3)
print(arr1.dtype)      # int64
print(arr2.ndim)       # 2

# Creating special arrays
zeros = np.zeros((3, 4))
ones = np.ones((2, 5))
identity = np.eye(3)
random_data = np.random.random((100, 5))
```

### Array Operations and Vectorization
```python
# Mathematical operations (vectorized)
prices = np.array([100, 105, 98, 110, 103])
returns = (prices[1:] - prices[:-1]) / prices[:-1]

# Broadcasting
portfolio_weights = np.array([0.3, 0.2, 0.5])
asset_returns = np.array([[0.05, 0.02, 0.08],
                         [0.03, 0.04, 0.06],
                         [-0.01, 0.03, 0.04]])
portfolio_returns = np.sum(asset_returns * portfolio_weights, axis=1)

# Statistical operations
mean_return = np.mean(portfolio_returns)
volatility = np.std(portfolio_returns)
correlation_matrix = np.corrcoef(asset_returns.T)
```

### Advanced NumPy Features
```python
# Boolean indexing
high_returns = portfolio_returns[portfolio_returns > 0.04]

# Fancy indexing
top_performers = asset_returns[:, [0, 2]]  # Select columns 0 and 2

# Linear algebra
covariance_matrix = np.cov(asset_returns.T)
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

# Financial calculations
def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
    excess_returns = returns - risk_free_rate
    return np.mean(excess_returns) / np.std(excess_returns)
```

## Pandas: Data Manipulation and Analysis

### Core Data Structures
```python
import pandas as pd

# Series: 1-dimensional labeled array
stock_prices = pd.Series([100, 105, 98, 110, 103], 
                        index=['2025-01-01', '2025-01-02', '2025-01-03', 
                               '2025-01-04', '2025-01-05'])

# DataFrame: 2-dimensional labeled data structure
portfolio_data = pd.DataFrame({
    'Symbol': ['AAPL', 'GOOGL', 'MSFT', 'AMZN'],
    'Price': [150.25, 2800.50, 310.75, 3400.25],
    'Shares': [100, 10, 50, 5],
    'Sector': ['Technology', 'Technology', 'Technology', 'Consumer']
})
```

### Data Loading and Inspection
```python
# Reading data from various sources
df = pd.read_csv('financial_data.csv')
df = pd.read_excel('portfolio.xlsx')
df = pd.read_json('market_data.json')

# Basic inspection
print(df.head())           # First 5 rows
print(df.tail(3))          # Last 3 rows
print(df.info())           # Data types and memory usage
print(df.describe())       # Statistical summary
print(df.shape)            # (rows, columns)
print(df.columns.tolist()) # Column names
```

### Data Cleaning and Transformation
```python
# Handling missing data
df_clean = df.dropna()                    # Remove rows with any NaN
df_filled = df.fillna(method='ffill')     # Forward fill
df_interpolated = df.interpolate()        # Linear interpolation

# Data type conversion
df['Date'] = pd.to_datetime(df['Date'])
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# String operations
df['Symbol'] = df['Symbol'].str.upper()
df['Company'] = df['Company'].str.replace('Inc.', 'Inc')

# Creating new columns
df['Market_Value'] = df['Price'] * df['Shares']
df['Weight'] = df['Market_Value'] / df['Market_Value'].sum()

# Date/time operations
df.set_index('Date', inplace=True)
df['Year'] = df.index.year
df['Month'] = df.index.month
df['Quarter'] = df.index.quarter
```

### Data Selection and Filtering
```python
# Column selection
prices = df['Price']
subset = df[['Symbol', 'Price', 'Shares']]

# Row selection
first_10 = df.head(10)
last_month = df.loc['2025-01-01':'2025-01-31']

# Boolean filtering
high_value = df[df['Market_Value'] > 10000]
tech_stocks = df[df['Sector'] == 'Technology']
recent_data = df[df.index > '2025-01-01']

# Complex filtering
large_tech = df[(df['Sector'] == 'Technology') & 
                (df['Market_Value'] > 5000)]
```

### Grouping and Aggregation
```python
# Group by single column
sector_analysis = df.groupby('Sector').agg({
    'Market_Value': ['sum', 'mean', 'count'],
    'Price': ['min', 'max'],
    'Shares': 'sum'
})

# Group by multiple columns
monthly_sector = df.groupby([df.index.to_period('M'), 'Sector']).agg({
    'Price': 'mean',
    'Volume': 'sum'
})

# Custom aggregation functions
def portfolio_metrics(group):
    return pd.Series({
        'total_value': group['Market_Value'].sum(),
        'avg_price': group['Price'].mean(),
        'price_volatility': group['Price'].std(),
        'stock_count': len(group)
    })

sector_metrics = df.groupby('Sector').apply(portfolio_metrics)
```

### Time Series Operations
```python
# Resampling time series data
daily_data = df.resample('D').mean()      # Daily averages
monthly_data = df.resample('M').last()    # Month-end values
quarterly_data = df.resample('Q').agg({   # Quarterly aggregation
    'Price': 'last',
    'Volume': 'sum'
})

# Rolling calculations
df['MA_20'] = df['Price'].rolling(window=20).mean()
df['Volatility_30'] = df['Returns'].rolling(window=30).std()
df['Cumulative_Return'] = (1 + df['Returns']).cumprod()

# Lag and lead operations
df['Price_Lag1'] = df['Price'].shift(1)
df['Price_Lead1'] = df['Price'].shift(-1)
df['Price_Change'] = df['Price'] - df['Price_Lag1']
```

## Jupyter Notebooks: Interactive Computing

### Why Jupyter Notebooks?
- **Interactive Development**: Test code incrementally
- **Rich Output**: Display plots, tables, and formatted text
- **Documentation**: Combine code, explanations, and results
- **Reproducibility**: Share complete analysis workflows

### Best Practices for Jupyter
```python
# Cell organization
# 1. Import all libraries at the top
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 2. Define functions in separate cells
def calculate_portfolio_return(weights, returns):
    return np.sum(weights * returns)

# 3. Load and explore data
df = pd.read_csv('data.csv')
df.head()

# 4. Analysis in logical steps
# Data cleaning
# Exploratory analysis  
# Visualization
# Statistical analysis
# Conclusions
```

### Jupyter Magic Commands
```python
# Timing code execution
%time result = expensive_function()
%%time
# Time entire cell
for i in range(1000000):
    pass

# Load external Python files
%load financial_functions.py

# Display matplotlib plots inline
%matplotlib inline

# Get help
?pd.DataFrame
??np.array  # Show source code
```

## Scientific Computing Workflow

### Typical Research Workflow
1. **Data Acquisition**: Load from files, APIs, databases
2. **Data Exploration**: Understand structure, quality, patterns
3. **Data Cleaning**: Handle missing values, outliers, inconsistencies
4. **Feature Engineering**: Create new variables, transformations
5. **Analysis**: Statistical tests, modeling, machine learning
6. **Visualization**: Create plots and charts for insights
7. **Reporting**: Document findings and methodology

### Performance Considerations
```python
# Vectorization vs. loops
# Slow: explicit loop
total = 0
for value in large_array:
    total += value ** 2

# Fast: vectorized operation
total = np.sum(large_array ** 2)

# Memory efficiency with chunks
def process_large_dataset(filename):
    chunk_size = 10000
    results = []
    for chunk in pd.read_csv(filename, chunksize=chunk_size):
        processed_chunk = process_chunk(chunk)
        results.append(processed_chunk)
    return pd.concat(results, ignore_index=True)
```

## Hands-on Activities

### Activity 1: Portfolio Analysis with NumPy
1. Create a multi-asset portfolio simulation
2. Calculate returns, volatility, and correlations
3. Implement portfolio optimization functions

### Activity 2: Financial Data Analysis with Pandas
1. Load historical stock price data
2. Clean and transform the data
3. Calculate technical indicators
4. Perform sector-based analysis

### Activity 3: Jupyter Notebook Report
1. Create a complete analysis notebook
2. Include data loading, cleaning, analysis, and visualization
3. Add markdown explanations and conclusions
4. Ensure reproducibility

## Integration with Previous Concepts

### Object-Oriented Design with NumPy/Pandas
```python
class PortfolioAnalyzer:
    def __init__(self, data):
        self.data = data
        self.returns = None
        self.weights = None
    
    def calculate_returns(self):
        self.returns = self.data.pct_change().dropna()
        return self.returns
    
    def set_weights(self, weights):
        self.weights = np.array(weights)
    
    def portfolio_return(self):
        return np.sum(self.returns.mean() * self.weights)
    
    def portfolio_volatility(self):
        cov_matrix = self.returns.cov()
        return np.sqrt(np.dot(self.weights.T, 
                             np.dot(cov_matrix, self.weights)))
```

### Using AI for Scientific Computing
- Ask AI to explain complex NumPy operations
- Generate Pandas code for specific data transformations
- Get help with debugging vectorization issues
- Create test datasets for experimentation

## Assessment

This lesson contributes to:
- Proficiency in NumPy for numerical computing
- Skills in Pandas for data manipulation
- Effective use of Jupyter notebooks
- Foundation for advanced data science techniques

## Next Steps

With Python fundamentals and scientific computing skills established, we'll move into Statistical Learning concepts, starting with visualization and the statistical learning framework.