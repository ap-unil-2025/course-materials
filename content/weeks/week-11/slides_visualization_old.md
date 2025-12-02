---
marp: true
paginate: true
header: "Session 11: Data Visualization"
footer: "Anna Smirnova, December 1, 2025"
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

# Session 11: Data Visualization

**Creating Publication-Ready Figures**

---

# Today's Goals

**Part 1: Visualization Principles**
- Why visualize data?
- Choosing the right chart type
- Design principles

**Part 2: Matplotlib Basics**
- Line plots, scatter plots, bar charts
- Customizing figures
- Subplots

**Part 3: Seaborn for Statistical Plots**
- Distribution plots
- Relationship plots
- Categorical plots

---

# Part 1: Visualization Principles

---

# Why Visualize Data?

**Numbers tell, but pictures sell**:

```python
# Raw numbers
data = [23, 45, 67, 89, 12, 34, 56, 78]
print(f"Mean: {np.mean(data):.1f}")
```

vs.

**A quick plot** reveals patterns, outliers, trends instantly!

**Key benefits**:
- Spot patterns and trends
- Identify outliers and anomalies
- Communicate findings effectively
- Make data-driven decisions

---

# Choosing the Right Chart Type

| Data Type | Chart Type | Use Case |
|-----------|-----------|----------|
| **Trends over time** | Line plot | Stock prices, temperature |
| **Comparisons** | Bar chart | Sales by region |
| **Distributions** | Histogram | Age distribution |
| **Relationships** | Scatter plot | Height vs weight |
| **Proportions** | Pie chart | Market share |
| **Correlations** | Heatmap | Feature correlations |

**Rule of thumb**: Choose the chart that makes your point clearest!

---

# Design Principles

**Good visualizations are**:
1. **Clear**: Easy to understand at a glance
2. **Accurate**: Don't distort or mislead
3. **Accessible**: Readable colors, fonts, labels
4. **Focused**: One main message per chart

**Avoid**:
- 3D charts (unless truly 3D data)
- Too many colors
- Chartjunk (unnecessary decorations)
- Missing axis labels
- Unclear titles

---

# Part 2: Matplotlib Basics

---

# Installing Matplotlib

```bash
uv pip install matplotlib
```

**Importing**:
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# For Jupyter notebooks
%matplotlib inline
```

---

# Basic Line Plot

```python
# Data
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave')
plt.grid(True)
plt.show()
```

**Key functions**:
- `plt.figure()`: Create new figure
- `plt.plot()`: Draw line
- `plt.xlabel/ylabel()`: Axis labels
- `plt.title()`: Title
- `plt.show()`: Display plot

---

# Customizing Line Plots

```python
plt.figure(figsize=(10, 6))

# Multiple lines with customization
plt.plot(x, np.sin(x), label='sin(x)', color='blue',
         linestyle='-', linewidth=2)
plt.plot(x, np.cos(x), label='cos(x)', color='red',
         linestyle='--', linewidth=2)

plt.xlabel('X-axis', fontsize=12)
plt.ylabel('Y-axis', fontsize=12)
plt.title('Trigonometric Functions', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

**Line styles**: `-`, `--`, `-.`, `:`
**Markers**: `o`, `s`, `^`, `*`, `+`

---

# Scatter Plot

```python
# Random data
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.5, s=50, c='steelblue')
plt.xlabel('X variable')
plt.ylabel('Y variable')
plt.title('Scatter Plot Example')
plt.grid(True, alpha=0.3)
plt.show()
```

**Parameters**:
- `alpha`: Transparency (0-1)
- `s`: Size
- `c`: Color (can be array for color mapping)

---

# Bar Chart

```python
# Data
categories = ['Q1', 'Q2', 'Q3', 'Q4']
sales = [120, 150, 180, 210]

plt.figure(figsize=(8, 6))
plt.bar(categories, sales, color='steelblue', edgecolor='black')
plt.xlabel('Quarter')
plt.ylabel('Sales ($1000s)')
plt.title('Quarterly Sales')
plt.grid(axis='y', alpha=0.3)
plt.show()
```

**Horizontal bar chart**:
```python
plt.barh(categories, sales)  # Use barh instead
```

---

# Grouped Bar Chart

```python
# Data
products = ['Product A', 'Product B', 'Product C']
q1 = [120, 150, 100]
q2 = [140, 160, 110]

x = np.arange(len(products))
width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(x - width/2, q1, width, label='Q1', color='steelblue')
plt.bar(x + width/2, q2, width, label='Q2', color='coral')

plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales Comparison')
plt.xticks(x, products)
plt.legend()
plt.show()
```

---

# Histogram

```python
# Generate random data
data = np.random.normal(100, 15, 1000)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='steelblue', edgecolor='black', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Distribution of Values')
plt.grid(axis='y', alpha=0.3)
plt.show()
```

**Key parameter**: `bins` controls number of bars

---

# Subplots

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Top-left: Line plot
axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('Line Plot')

# Top-right: Scatter
axes[0, 1].scatter(x, y)
axes[0, 1].set_title('Scatter Plot')

# Bottom-left: Bar
axes[1, 0].bar(categories, sales)
axes[1, 0].set_title('Bar Chart')

# Bottom-right: Histogram
axes[1, 1].hist(data, bins=20)
axes[1, 1].set_title('Histogram')

plt.tight_layout()
plt.show()
```

---

# Saving Figures

```python
# Create plot
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('My Plot')

# Save in different formats
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.savefig('plot.pdf', bbox_inches='tight')
plt.savefig('plot.svg', bbox_inches='tight')

plt.show()
```

**Parameters**:
- `dpi`: Resolution (300 for publications)
- `bbox_inches='tight'`: Remove whitespace
- `transparent=True`: Transparent background

---

# Part 3: Seaborn for Statistical Plots

---

# Why Seaborn?

**Seaborn** builds on Matplotlib to provide:
- Beautiful default styles
- Statistical visualizations
- Easier syntax for complex plots
- Better integration with Pandas

```bash
uv pip install seaborn
```

```python
import seaborn as sns
sns.set_theme()  # Apply Seaborn style
```

---

# Seaborn Styles

```python
# Available styles: darkgrid, whitegrid, dark, white, ticks
sns.set_style('whitegrid')

# Available color palettes
sns.set_palette('deep')  # deep, muted, pastel, bright, dark, colorblind

# Reset to default
sns.reset_defaults()
```

---

# Distribution Plot

```python
# Sample data
data = np.random.normal(100, 15, 1000)

plt.figure(figsize=(10, 6))

# Histogram with KDE (kernel density estimate)
sns.histplot(data, kde=True, bins=30)

plt.xlabel('Value')
plt.ylabel('Count')
plt.title('Distribution with KDE')
plt.show()
```

---

# Box Plot

```python
# Sample data
df = pd.DataFrame({
    'category': ['A']*100 + ['B']*100 + ['C']*100,
    'value': np.concatenate([
        np.random.normal(100, 10, 100),
        np.random.normal(110, 15, 100),
        np.random.normal(95, 12, 100)
    ])
})

plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='category', y='value')
plt.title('Value Distribution by Category')
plt.show()
```

**Shows**: Median, quartiles, outliers

---

# Violin Plot

```python
plt.figure(figsize=(8, 6))
sns.violinplot(data=df, x='category', y='value')
plt.title('Value Distribution by Category (Violin)')
plt.show()
```

**Combines**: Box plot + KDE
**Shows**: Distribution shape more clearly

---

# Scatter Plot with Regression

```python
# Generate correlated data
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5

df = pd.DataFrame({'x': x, 'y': y})

plt.figure(figsize=(8, 6))
sns.regplot(data=df, x='x', y='y')
plt.title('Scatter Plot with Regression Line')
plt.show()
```

**Automatically**: Fits and plots regression line with confidence interval

---

# Pair Plot

```python
# Multi-dimensional data
iris = sns.load_dataset('iris')

# Create pair plot
sns.pairplot(iris, hue='species')
plt.show()
```

**Shows**: All pairwise relationships in dataset
**Great for**: Exploratory data analysis

---

# Heatmap (Correlation Matrix)

```python
# Load data
df = pd.DataFrame({
    'A': np.random.randn(100),
    'B': np.random.randn(100),
    'C': np.random.randn(100)
})

# Create B correlated with A
df['B'] = df['A'] * 0.8 + df['B'] * 0.2

# Calculate correlations
corr = df.corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0,
            square=True, linewidths=1)
plt.title('Correlation Matrix')
plt.show()
```

---

# Count Plot (Categorical)

```python
# Sample data
df = pd.DataFrame({
    'product': ['A', 'B', 'C'] * 20,
    'region': ['North', 'South'] * 30
})

plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='product', hue='region')
plt.title('Sales Count by Product and Region')
plt.show()
```

**Shows**: Frequency of categories

---

# Time Series Plot

```python
# Generate time series data
dates = pd.date_range('2025-01-01', periods=100)
values = np.cumsum(np.random.randn(100)) + 100

df = pd.DataFrame({'date': dates, 'value': values})

plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['value'], linewidth=2)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time Series Plot')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

# Hands-On Exercise: Sales Dashboard

```python
# Create sales data
np.random.seed(42)
sales_data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'] * 3,
    'product': ['A']*6 + ['B']*6 + ['C']*6,
    'sales': np.random.randint(50, 200, 18)
})

# Your tasks:
# 1. Create a line plot showing sales trends by product
# 2. Create a bar chart comparing total sales by product
# 3. Create a box plot showing sales distribution by product
# 4. Create a 2x2 subplot combining different visualizations
```

---

# Exercise Solution (Part 1)

```python
# 1. Line plot - Sales trends
pivot_data = sales_data.pivot(index='month', columns='product',
                               values='sales')

plt.figure(figsize=(10, 6))
for product in pivot_data.columns:
    plt.plot(pivot_data.index, pivot_data[product],
             marker='o', label=product, linewidth=2)

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales by Product')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---

# Exercise Solution (Part 2)

```python
# 2. Bar chart - Total sales by product
total_sales = sales_data.groupby('product')['sales'].sum()

plt.figure(figsize=(8, 6))
plt.bar(total_sales.index, total_sales.values,
        color=['steelblue', 'coral', 'lightgreen'],
        edgecolor='black')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.title('Total Sales by Product')
plt.grid(axis='y', alpha=0.3)
plt.show()

# 3. Box plot - Distribution
plt.figure(figsize=(8, 6))
sns.boxplot(data=sales_data, x='product', y='sales')
plt.title('Sales Distribution by Product')
plt.show()
```

---

# Exercise Solution (Part 3)

```python
# 4. Combined dashboard
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Line plot
for product in pivot_data.columns:
    axes[0, 0].plot(pivot_data.index, pivot_data[product],
                    marker='o', label=product)
axes[0, 0].set_title('Monthly Trends')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Bar chart
axes[0, 1].bar(total_sales.index, total_sales.values)
axes[0, 1].set_title('Total Sales')

# Box plot
sns.boxplot(data=sales_data, x='product', y='sales', ax=axes[1, 0])
axes[1, 0].set_title('Distribution')

# Count plot
sns.countplot(data=sales_data, x='product', ax=axes[1, 1])
axes[1, 1].set_title('Sample Count')

plt.tight_layout()
plt.show()
```

---

# Visualization Best Practices

**Do**:
- Always label axes and add titles
- Use appropriate chart types
- Keep it simple and focused
- Use colorblind-friendly palettes
- Save high-resolution (300 dpi) for publications

**Don't**:
- Overload with information
- Use too many colors
- Forget to add legends
- Truncate axes misleadingly
- Use 3D effects unnecessarily

---

# Key Takeaways

**Matplotlib**:
- Core plotting library
- Fine-grained control
- Good for basic plots

**Seaborn**:
- Built on Matplotlib
- Beautiful defaults
- Great for statistical plots
- Better Pandas integration

**Remember**:
- Choose the right chart for your data
- Label everything clearly
- Less is often more
- Test on different screens/printouts

**Next week**: Creating complete reports with Jupyter notebooks!

---

# Homework Assignment

**Create a Data Analysis Dashboard**

Choose a dataset and create a comprehensive visualization:

1. **4-6 different plot types** showing different aspects of the data
2. **At least one Seaborn plot** with statistical information
3. **A multi-panel figure** (subplots) combining visualizations
4. **Publication-ready quality**: Proper labels, titles, legends

**Deliverable**: Jupyter notebook with:
- Code and visualizations
- Brief interpretation of each plot
- One high-resolution PNG of your best figure

**Bonus**: Try different Seaborn styles and color palettes!

---

<!-- _class: lead -->

# Questions?

**Next week**: Creating complete analysis reports!
