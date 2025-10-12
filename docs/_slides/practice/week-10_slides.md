---
marp: true
paginate: true
header: "Session 10: Pandas for Data Analysis"
footer: "Anna Smirnova, November 24, 2025"
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

# Session 10: Pandas for Data Analysis

**Working with Real-World Datasets**

---

# Today's Goals

**Part 1: Introduction to Pandas**
- What is Pandas and why use it?
- Series and DataFrames
- Reading data from files

**Part 2: Data Manipulation**
- Selecting, filtering, sorting
- Adding and removing columns
- Grouping and aggregating

**Part 3: Cleaning Data**
- Handling missing values
- Data type conversions
- Dealing with duplicates

---

# Part 1: Introduction to Pandas

---

# What is Pandas?

**Pandas** is Python's premier data analysis library, built on top of NumPy.

**Think of it as**:
- Excel/Google Sheets in Python
- SQL tables in Python
- A structured way to work with tabular data

**Key structures**:
- **Series**: 1D labeled array (like a column)
- **DataFrame**: 2D labeled table (like a spreadsheet)

---

# NumPy vs Pandas

**NumPy**:
```python
# Homogeneous data, no labels
prices = np.array([100, 105, 102])
```

**Pandas**:
```python
# Mixed data types, labeled columns
data = pd.DataFrame({
    'date': ['2025-01-01', '2025-01-02', '2025-01-03'],
    'price': [100, 105, 102],
    'volume': [1000, 1200, 900]
})
```

**When to use Pandas**:
- Reading CSV/Excel files
- Mixed data types (numbers, dates, strings)
- Need labeled rows/columns
- Data cleaning and transformation

---

# Installing Pandas

```bash
uv pip install pandas
```

**Importing**:
```python
import pandas as pd  # Standard convention
import numpy as np   # Often used together
```

---

# Series: 1D Labeled Data

```python
import pandas as pd

# Create Series from list
prices = pd.Series([100, 105, 102, 108],
                   index=['Mon', 'Tue', 'Wed', 'Thu'])

print(prices)
# Mon    100
# Tue    105
# Wed    102
# Thu    108

# Access by label or position
print(prices['Mon'])    # 100
print(prices[0])        # 100

# Operations work like NumPy
print(prices * 1.1)     # Multiply all by 1.1
print(prices > 103)     # Boolean mask
```

---

# DataFrame: 2D Labeled Data

```python
# Create DataFrame from dictionary
data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000, 60000, 55000]
})

print(data)
#       name  age  salary
# 0    Alice   25   50000
# 1      Bob   30   60000
# 2  Charlie   35   55000

# Access columns
print(data['name'])        # Series of names
print(data[['name', 'age']])  # DataFrame with 2 columns
```

---

# Reading Data from Files

**CSV Files** (most common):
```python
df = pd.read_csv('data.csv')
```

**Excel Files**:
```python
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
```

**From URLs**:
```python
url = 'https://example.com/data.csv'
df = pd.read_csv(url)
```

**Common options**:
```python
df = pd.read_csv('data.csv',
                 sep=';',           # Different delimiter
                 header=0,          # Row for column names
                 index_col='date',  # Column to use as index
                 parse_dates=True)  # Parse dates automatically
```

---

# Exploring DataFrames

```python
df = pd.read_csv('sales.csv')

# First and last rows
print(df.head())      # First 5 rows
print(df.tail(3))     # Last 3 rows

# Shape and info
print(df.shape)       # (rows, columns)
print(df.columns)     # Column names
print(df.dtypes)      # Data types
print(df.info())      # Overview

# Summary statistics
print(df.describe())  # Mean, std, min, max, etc.

# Quick peek
print(df.sample(5))   # Random 5 rows
```

---

# Part 2: Data Manipulation

---

# Selecting Columns

```python
# Single column (returns Series)
names = df['name']

# Multiple columns (returns DataFrame)
subset = df[['name', 'salary']]

# Using dot notation (if column name is valid identifier)
names = df.name  # Same as df['name']
```

---

# Selecting Rows

**By position** (`.iloc`):
```python
# First row
print(df.iloc[0])

# First 3 rows
print(df.iloc[0:3])

# Specific rows and columns
print(df.iloc[0:3, 1:3])  # Rows 0-2, columns 1-2
```

**By label** (`.loc`):
```python
# By index label
print(df.loc[0])

# By boolean mask
high_earners = df.loc[df['salary'] > 55000]

# Specific rows and columns
print(df.loc[0:2, ['name', 'salary']])
```

---

# Filtering Data

```python
# Single condition
high_salary = df[df['salary'] > 55000]

# Multiple conditions (use & and |)
young_high_earners = df[(df['age'] < 30) & (df['salary'] > 50000)]

# Using .query() method (more readable)
result = df.query('age < 30 and salary > 50000')

# String operations
starts_with_a = df[df['name'].str.startswith('A')]

# Check for values in list
subset = df[df['name'].isin(['Alice', 'Bob'])]
```

---

# Sorting Data

```python
# Sort by one column
df_sorted = df.sort_values('salary')

# Sort descending
df_sorted = df.sort_values('salary', ascending=False)

# Sort by multiple columns
df_sorted = df.sort_values(['age', 'salary'],
                           ascending=[True, False])

# Sort by index
df_sorted = df.sort_index()
```

---

# Adding and Modifying Columns

```python
# Add new column
df['bonus'] = df['salary'] * 0.1

# Calculate from multiple columns
df['total_comp'] = df['salary'] + df['bonus']

# Conditional column
df['seniority'] = df['age'].apply(lambda x: 'Senior' if x > 30 else 'Junior')

# Or using np.where
df['seniority'] = np.where(df['age'] > 30, 'Senior', 'Junior')

# Rename columns
df = df.rename(columns={'salary': 'annual_salary'})

# Drop columns
df = df.drop(columns=['bonus'])
# Or
df = df.drop('bonus', axis=1)
```

---

# Grouping and Aggregating

```python
# Group by one column
by_dept = df.groupby('department')

# Calculate statistics
print(by_dept['salary'].mean())
print(by_dept['salary'].sum())

# Multiple aggregations
print(by_dept['salary'].agg(['mean', 'min', 'max', 'count']))

# Different aggregations for different columns
agg_dict = {
    'salary': ['mean', 'sum'],
    'age': 'mean'
}
print(by_dept.agg(agg_dict))

# Group by multiple columns
by_dept_senior = df.groupby(['department', 'seniority'])['salary'].mean()
```

---

# Part 3: Cleaning Data

---

# Handling Missing Values

```python
# Check for missing values
print(df.isnull().sum())    # Count per column
print(df.isnull().any())    # Any missing per column?

# Drop rows with any missing values
df_clean = df.dropna()

# Drop rows where specific column is missing
df_clean = df.dropna(subset=['salary'])

# Fill missing values
df['age'].fillna(df['age'].mean(), inplace=True)  # Fill with mean
df['name'].fillna('Unknown', inplace=True)         # Fill with value

# Forward fill (use previous value)
df['price'].fillna(method='ffill', inplace=True)

# Interpolate (for time series)
df['price'].interpolate(inplace=True)
```

---

# Data Type Conversions

```python
# Check data types
print(df.dtypes)

# Convert to numeric (errors become NaN)
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')

# Convert to datetime
df['date'] = pd.to_datetime(df['date'])

# Convert to string
df['id'] = df['id'].astype(str)

# Change multiple columns
df = df.astype({
    'age': int,
    'salary': float,
    'name': str
})
```

---

# Dealing with Duplicates

```python
# Check for duplicates
print(df.duplicated().sum())

# View duplicate rows
duplicates = df[df.duplicated()]

# Drop duplicates (keep first occurrence)
df_unique = df.drop_duplicates()

# Drop duplicates based on specific columns
df_unique = df.drop_duplicates(subset=['name', 'age'])

# Keep last occurrence instead
df_unique = df.drop_duplicates(keep='last')
```

---

# String Operations

```python
# Common string operations on Series
df['name_upper'] = df['name'].str.upper()
df['name_lower'] = df['name'].str.lower()

# String contains
tech_companies = df[df['company'].str.contains('Tech')]

# String replace
df['name'] = df['name'].str.replace('Dr.', '')

# Split strings
df[['first', 'last']] = df['name'].str.split(' ', expand=True)

# String length
df['name_length'] = df['name'].str.len()

# Strip whitespace
df['name'] = df['name'].str.strip()
```

---

# Real-World Example: Sales Analysis

```python
# Load sales data
sales = pd.read_csv('sales_data.csv')

# Clean data
sales['date'] = pd.to_datetime(sales['date'])
sales = sales.dropna(subset=['revenue'])
sales = sales[sales['revenue'] > 0]

# Add calculated columns
sales['month'] = sales['date'].dt.month
sales['year'] = sales['date'].dt.year

# Analyze by product
by_product = sales.groupby('product').agg({
    'revenue': ['sum', 'mean'],
    'quantity': 'sum'
}).round(2)

print(by_product)
```

---

# Hands-On Exercise 1: Employee Data

```python
# Load employee data
employees = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'department': ['Sales', 'IT', 'Sales', 'IT', 'HR'],
    'salary': [50000, 60000, 55000, 65000, 52000],
    'age': [25, 30, 35, 28, 32]
})

# Your tasks:
# 1. Find average salary by department
# 2. Find employees earning above average
# 3. Add a 'seniority' column (Senior if age > 30)
# 4. Sort by salary (highest first)
# 5. Calculate total payroll per department
```

---

# Exercise 1: Solution

```python
# 1. Average salary by department
avg_by_dept = employees.groupby('department')['salary'].mean()
print(avg_by_dept)

# 2. Above average earners
avg_salary = employees['salary'].mean()
high_earners = employees[employees['salary'] > avg_salary]
print(high_earners)

# 3. Add seniority column
employees['seniority'] = employees['age'].apply(
    lambda x: 'Senior' if x > 30 else 'Junior'
)

# 4. Sort by salary
employees_sorted = employees.sort_values('salary', ascending=False)

# 5. Total payroll per department
payroll = employees.groupby('department')['salary'].sum()
print(payroll)
```

---

# Hands-On Exercise 2: Sales Data Cleaning

```python
# Messy sales data
sales = pd.DataFrame({
    'date': ['2025-01-01', '2025-01-02', None, '2025-01-04'],
    'product': ['Widget', 'Gadget', 'Widget', 'Gadget'],
    'revenue': [100, None, 150, 200],
    'region': ['North', 'South', 'North', 'South']
})

# Your tasks:
# 1. Check for missing values
# 2. Drop rows with missing dates
# 3. Fill missing revenue with the mean
# 4. Calculate total revenue by product
# 5. Find which region has higher average revenue
```

---

# Exercise 2: Solution

```python
# 1. Check missing values
print(sales.isnull().sum())

# 2. Drop rows with missing dates
sales_clean = sales.dropna(subset=['date'])

# 3. Fill missing revenue with mean
sales_clean['revenue'] = sales_clean['revenue'].fillna(
    sales_clean['revenue'].mean()
)

# 4. Total revenue by product
revenue_by_product = sales_clean.groupby('product')['revenue'].sum()
print(revenue_by_product)

# 5. Average revenue by region
avg_by_region = sales_clean.groupby('region')['revenue'].mean()
print(avg_by_region)
best_region = avg_by_region.idxmax()
print(f"Best region: {best_region}")
```

---

# Saving Data

```python
# Save to CSV
df.to_csv('output.csv', index=False)

# Save to Excel
df.to_excel('output.xlsx', sheet_name='Data', index=False)

# Save specific columns
df[['name', 'salary']].to_csv('salaries.csv', index=False)

# Append to existing CSV
df.to_csv('data.csv', mode='a', header=False, index=False)
```

---

# Pandas Cheat Sheet

**Reading**: `pd.read_csv()`, `pd.read_excel()`
**Exploring**: `.head()`, `.info()`, `.describe()`, `.shape`
**Selecting**: `df['col']`, `df[['col1', 'col2']]`, `.loc[]`, `.iloc[]`
**Filtering**: `df[df['col'] > value]`, `.query()`
**Sorting**: `.sort_values()`, `.sort_index()`
**Grouping**: `.groupby().agg()`
**Cleaning**: `.dropna()`, `.fillna()`, `.drop_duplicates()`
**Adding**: `df['new'] = ...`
**Saving**: `.to_csv()`, `.to_excel()`

---

# Key Takeaways

**Pandas is essential for**:
- Loading real-world data (CSV, Excel, etc.)
- Cleaning messy data
- Exploratory data analysis
- Data transformation and aggregation

**Key concepts**:
- DataFrame = labeled 2D table
- `.loc[]` for label-based indexing
- `.iloc[]` for position-based indexing
- `.groupby()` for aggregation
- Always check for and handle missing values

**Next Week**: Data visualization with Matplotlib and Seaborn!

---

# Homework Assignment

**Analyze a Real Dataset**

Find a dataset (e.g., from Kaggle, data.gov, or your field) and:

1. **Load and explore**: Read data, check shape, types, missing values
2. **Clean**: Handle missing values, remove duplicates, fix data types
3. **Analyze**: Use groupby, filtering, sorting to answer 3 questions
4. **Transform**: Create 2 new calculated columns
5. **Export**: Save cleaned data to CSV

**Deliverable**: Jupyter notebook with:
- Dataset description and source
- Code with comments
- Analysis and findings

---

<!-- _class: lead -->

# Questions?

**Next week**: Creating beautiful visualizations!
