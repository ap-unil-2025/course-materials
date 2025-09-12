---
layout: assignment
title: "Advanced HW4: Data Analysis Toolkit"
assignment_number: "HW4"
due_date: 2025-10-20 23:59:00
points: 150
difficulty: "Advanced"
estimated_time: "8-10 hours"
github_classroom_url: "https://classroom.github.com/a/advanced-hw4"
starter_repo: "ap2025-advanced-hw4-starter"
topics:
  - "Advanced functions"
  - "Complex data structures"
  - "File processing"
  - "Data analysis"
  - "Functional programming"
bonus: true
status: "open"
---

## Overview

**This is an OPTIONAL grade booster assignment** worth 150 bonus points. Build a comprehensive data analysis toolkit using advanced Python functions and data structures. Process real-world datasets and create insightful analytics.

## The Challenge: "Student Performance Analytics System"

Create a data analysis toolkit to process student performance data from multiple sources (CSV, JSON, TXT), perform statistical analysis, generate reports, and visualize trends using ASCII charts.

## Project Structure

```
data_analysis_toolkit/
├── data_loader.py       # Functions to load various formats
├── data_processor.py    # Data cleaning and transformation
├── statistics.py        # Statistical analysis functions
├── visualizer.py        # ASCII chart generation
├── report_generator.py  # Report creation functions
├── main.py             # Main program with menu
└── data/
    ├── students.csv    # Student records
    ├── grades.json     # Grade data
    └── attendance.txt  # Attendance logs
```

## Part 1: Data Loading and Parsing (30 points)

### Multi-Format Data Loader

```python
def load_csv(filename, delimiter=',', has_header=True):
    """
    Load CSV file into list of dictionaries
    Handle missing values, different delimiters
    Return: [{col1: val1, col2: val2}, ...]
    """
    pass

def load_json_streaming(filename, chunk_size=100):
    """
    Load large JSON files in chunks
    Yield data in batches for memory efficiency
    """
    pass

def parse_log_file(filename, pattern=None):
    """
    Parse structured log files
    Extract datetime, user, action, details
    Support custom regex patterns
    """
    pass

def merge_datasets(*datasets, key='id', strategy='inner'):
    """
    Merge multiple datasets on common key
    Support inner, outer, left, right joins
    Handle conflicts with merge strategies
    """
    pass
```

### Requirements
- Handle corrupted/incomplete files gracefully
- Support different encodings (UTF-8, Latin-1, etc.)
- Validate data types automatically
- Generate data quality reports

## Part 2: Advanced Data Processing (35 points)

### Functional Programming Techniques

```python
def create_pipeline(*functions):
    """
    Create a data processing pipeline
    Each function transforms data for the next
    Example: pipeline = create_pipeline(clean, transform, aggregate)
    """
    def pipeline_function(data):
        # Your implementation
        pass
    return pipeline_function

def memoize(func):
    """
    Decorator to cache function results
    Improve performance for expensive computations
    """
    cache = {}
    def wrapper(*args, **kwargs):
        # Your implementation
        pass
    return wrapper

def parallel_map(func, data, num_workers=4):
    """
    Apply function to data in parallel
    Simulate parallel processing without imports
    """
    pass
```

### Data Transformation Functions

```python
def normalize_scores(scores, method='z-score'):
    """
    Normalize scores using various methods:
    - z-score: (x - mean) / std
    - min-max: (x - min) / (max - min)
    - percentile: convert to percentile ranks
    """
    pass

def group_by_advanced(data, *keys, aggregations=None):
    """
    Group data by multiple keys with custom aggregations
    Example: group_by_advanced(students, 'grade', 'section',
                               aggregations={'score': ['mean', 'max', 'count']})
    """
    pass

def pivot_table(data, index, columns, values, aggfunc='mean'):
    """
    Create pivot table from data
    Similar to pandas pivot_table but using only base Python
    """
    pass
```

## Part 3: Statistical Analysis Engine (30 points)

### Descriptive Statistics

```python
def calculate_statistics(data, columns=None):
    """
    Calculate comprehensive statistics:
    - Mean, median, mode
    - Standard deviation, variance
    - Quartiles (Q1, Q2, Q3)
    - IQR and outlier detection
    - Skewness and kurtosis
    Return nested dictionary with all stats
    """
    pass

def correlation_matrix(data, variables):
    """
    Calculate Pearson correlation between variables
    Return matrix as nested lists
    """
    pass

def regression_analysis(x, y):
    """
    Simple linear regression
    Return: slope, intercept, r_squared, predictions
    """
    pass
```

### Time Series Analysis

```python
def moving_average(data, window_size, weights=None):
    """
    Calculate moving average with optional weights
    Support simple, weighted, exponential moving averages
    """
    pass

def detect_trends(time_series, method='linear'):
    """
    Detect trends in time series data
    Methods: linear, polynomial, seasonal
    Return trend direction and strength
    """
    pass

def forecast(historical_data, periods=5, method='linear'):
    """
    Simple forecasting based on historical data
    Return predicted values and confidence intervals
    """
    pass
```

## Part 4: ASCII Visualization System (25 points)

### Chart Generation

```python
def create_bar_chart(data, labels, width=50, height=20):
    """
    Create horizontal or vertical bar charts
    Support negative values and stacked bars
    
    Example output:
    Math     |████████████████████| 85%
    Science  |███████████████     | 75%
    English  |██████████████████  | 90%
    """
    pass

def create_line_chart(x, y, width=60, height=20):
    """
    Create ASCII line chart with axis labels
    Support multiple series
    
    Example output:
    100 |    ╱╲
     90 |   ╱  ╲
     80 |  ╱    ╲___
     70 | ╱          ╲
        └──────────────
         Jan Feb Mar Apr
    """
    pass

def create_heatmap(matrix, labels=None):
    """
    Create ASCII heatmap using different characters
    for intensity levels
    
    Example output:
         A  B  C  D
    1  [ ][█][▓][░]
    2  [▓][ ][█][▓]
    3  [█][░][ ][█]
    """
    pass

def create_scatter_plot(x, y, width=40, height=20):
    """
    Create ASCII scatter plot
    Support different markers for categories
    """
    pass
```

## Part 5: Report Generation System (25 points)

### Automated Reports

```python
def generate_student_report(student_id, data):
    """
    Generate comprehensive student report:
    - Personal information
    - Academic performance (with trends)
    - Attendance summary
    - Strengths and weaknesses
    - Recommendations
    Format as formatted text with sections
    """
    pass

def generate_class_report(class_data):
    """
    Generate class-level analytics:
    - Grade distribution
    - Performance comparisons
    - Top performers
    - Areas needing improvement
    - Statistical summary
    Include ASCII charts
    """
    pass

def export_report(report, format='txt', filename=None):
    """
    Export report in various formats:
    - txt: Plain text with formatting
    - md: Markdown with tables
    - html: Basic HTML (without libraries)
    - csv: Data tables only
    """
    pass
```

### Dashboard Creator

```python
def create_dashboard(data, config):
    """
    Create text-based dashboard with multiple widgets
    Config specifies layout and data sources
    
    Example output:
    ╔════════════════════════════════════════╗
    ║     STUDENT PERFORMANCE DASHBOARD      ║
    ╠════════════════════════════════════════╣
    ║ Avg Score: 82.5  | Attendance: 94%     ║
    ║ Trend: ↑ +3.2%   | At Risk: 12 students║
    ╠════════════════════════════════════════╣
    ║ Grade Distribution:                    ║
    ║ A: ████████ 40%                       ║
    ║ B: ██████ 30%                         ║
    ║ C: ████ 20%                           ║
    ╚════════════════════════════════════════╝
    """
    pass
```

## Part 6: Advanced Features (15 points)

### Performance Optimization

```python
def profile_function(func):
    """
    Decorator to profile function performance
    Track execution time, memory usage (approximate)
    Generate performance report
    """
    pass

def lazy_evaluation(generator_func):
    """
    Implement lazy evaluation for large datasets
    Process data only when needed
    """
    pass
```

### Data Validation Framework

```python
def create_validator(rules):
    """
    Create data validator from rules dictionary
    Rules specify type, range, format, required fields
    Return validation function
    """
    pass

def validate_and_clean(data, schema):
    """
    Validate data against schema
    Auto-fix common issues
    Generate validation report
    """
    pass
```

## Sample Data Files

### students.csv
```csv
id,name,grade,section,enrollment_date
001,Alice Johnson,10,A,2023-09-01
002,Bob Smith,10,B,2023-09-01
...
```

### grades.json
```json
{
  "grades": [
    {"student_id": "001", "subject": "Math", "score": 85, "date": "2024-01-15"},
    {"student_id": "001", "subject": "Science", "score": 92, "date": "2024-01-16"}
  ]
}
```

### attendance.txt
```
2024-01-15 08:30:00 | 001 | PRESENT | Math
2024-01-15 09:30:00 | 001 | PRESENT | Science
2024-01-15 08:30:00 | 002 | ABSENT | Math
```

## Main Program Requirements

Create `main.py` with interactive menu:

```python
def main():
    """
    Interactive menu system:
    1. Load Data (choose source)
    2. Process Data (clean, transform)
    3. Analyze Data (statistics, trends)
    4. Generate Visualizations
    5. Create Reports
    6. Export Results
    7. Run Batch Analysis
    8. Settings (configure parameters)
    9. Help
    0. Exit
    """
    pass
```

## Deliverables

1. **Complete toolkit** (all .py files)
2. **Sample data files** (CSV, JSON, TXT)
3. **Generated reports** (at least 3 examples)
4. **Performance benchmarks** (processing times)
5. **User guide** (README.md with examples)
6. **Test suite** (test_toolkit.py with 20+ tests)

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Data Loading | 30 | Multi-format support, error handling |
| Data Processing | 35 | Functional programming, transformations |
| Statistical Analysis | 30 | Comprehensive statistics, trends |
| Visualizations | 25 | ASCII charts, clarity |
| Report Generation | 25 | Automated reports, formatting |
| Advanced Features | 15 | Optimization, validation |
| **Total** | **150** |

## Constraints

You may use:
- All Python basics (variables, control flow)
- Functions (including nested, lambda)
- Lists, dictionaries, tuples, sets
- List/dict comprehensions
- Generators and iterators
- Decorators
- File I/O
- String formatting
- Math operations

You may NOT use:
- External libraries (numpy, pandas, matplotlib)
- Classes (save for Week 6!)
- Import beyond: random, math, json, csv, datetime
- Async/await
- Threading/multiprocessing modules

## Performance Requirements

- Process 10,000 student records in < 5 seconds
- Generate reports for 1,000 students in < 10 seconds
- Charts should render in < 1 second
- Memory usage < 100MB for typical datasets

## Tips for Success

- **Start with data structures**: Design your data schema first
- **Use generators**: For large datasets, use generators to save memory
- **Optimize hotspots**: Profile and optimize slowest functions
- **Test edge cases**: Empty data, missing values, extreme values
- **Document thoroughly**: Each function needs clear docstrings

## Bonus Challenges (Extra 20 points)

1. **Machine Learning** (10 points): Implement k-means clustering without libraries
2. **Real-time Updates** (10 points): Create live-updating dashboard simulation

## Academic Integrity

This is an individual assignment. You may discuss algorithms but must implement all code yourself. Using pandas/numpy or copying implementations will result in zero.

## Submission

1. Ensure all functions have docstrings
2. Include sample outputs in `examples/` folder
3. Test with provided and custom datasets
4. Submit via GitHub Classroom

---

*This optional grade booster demonstrates advanced Python programming skills and data analysis capabilities without relying on external libraries.*