---
layout: assignment
title: "Week 4: Functions, Data Structures & Recursion"
assignment_number: 4
due_date: 2025-10-13 23:59:00
points: 120
difficulty: "Intermediate"
estimated_time: "5-6 hours"
topics:
  - "Functions and scope"
  - "Lists, tuples, dictionaries"
  - "Recursion"
  - "Jupyter Notebooks"
status: "open"
---

## Overview

Deepen your Python knowledge by mastering functions, data structures, and recursive algorithms. This assignment includes both traditional Python scripts and Jupyter notebook exercises.

## Learning Objectives

By completing this assignment, you will:

- Write reusable functions with proper parameter handling
- Master Python's built-in data structures
- Implement recursive solutions to problems
- Work effectively with Jupyter notebooks
- Understand time and space complexity basics

## Part 1: Advanced Functions (25 points)

Create `functions_advanced.py` with:

### 1.1 Function Decorators (10 points)

```python
def timer_decorator(func):
    """Decorator that times function execution"""
    # Your implementation here

def memoize(func):
    """Decorator that caches function results"""
    # Your implementation here

@timer_decorator
@memoize
def fibonacci(n):
    """Calculate nth Fibonacci number"""
    # Your implementation here
```

### 1.2 Higher-Order Functions (8 points)

```python
def create_multiplier(factor):
    """Return a function that multiplies by factor"""
    # Your implementation here

def apply_operation(data, operation):
    """Apply operation to all elements in data"""
    # Your implementation here

def compose(*functions):
    """Compose multiple functions into one"""
    # Your implementation here
```

### 1.3 Variable Arguments (7 points)

```python
def smart_calculator(*args, **kwargs):
    """
    Flexible calculator supporting:
    - Variable number of operands
    - Named operations (add, multiply, etc.)
    - Statistical operations (mean, median, std)
    """
    # Your implementation here
```

## Part 2: Data Structure Mastery (30 points)

Create `data_structures.py` with:

### 2.1 List Comprehensions & Generators (10 points)

```python
def matrix_operations():
    """
    Implement:
    1. Matrix transpose using list comprehension
    2. Matrix multiplication
    3. Generator for prime numbers up to n
    4. Generator for Fibonacci sequence
    """
    # Your implementation here
```

### 2.2 Dictionary Operations (10 points)

```python
class StudentDatabase:
    """
    Implement a student database with:
    - Add/remove students
    - Update grades
    - Calculate GPA
    - Find top performers
    - Generate transcript
    """
    def __init__(self):
        self.students = {}
    
    # Your implementation here
```

### 2.3 Set Operations & Applications (10 points)

```python
def analyze_text_similarity(text1, text2):
    """
    Use sets to:
    - Find common words
    - Calculate Jaccard similarity
    - Identify unique words in each text
    """
    # Your implementation here

def find_duplicates_efficient(data):
    """Find duplicates in O(n) time using sets"""
    # Your implementation here
```

## Part 3: Recursion Challenges (30 points)

Create `recursion_problems.py` with:

### 3.1 Classic Recursion (10 points)

```python
def tower_of_hanoi(n, source, destination, auxiliary):
    """Solve Tower of Hanoi puzzle"""
    # Your implementation here

def binary_search_recursive(arr, target, left=0, right=None):
    """Recursive binary search"""
    # Your implementation here
```

### 3.2 Tree Recursion (10 points)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_height(root):
    """Calculate height of binary tree"""
    # Your implementation here

def tree_sum(root):
    """Sum all values in binary tree"""
    # Your implementation here

def is_balanced(root):
    """Check if binary tree is balanced"""
    # Your implementation here
```

### 3.3 Backtracking (10 points)

```python
def solve_n_queens(n):
    """
    Solve N-Queens problem
    Return all possible solutions
    """
    # Your implementation here

def generate_permutations(items):
    """Generate all permutations recursively"""
    # Your implementation here
```

## Part 4: Jupyter Notebook Analysis (35 points)

Create `data_analysis.ipynb` with the following sections:

### 4.1 Data Loading and Exploration (10 points)
- Load the provided CSV dataset
- Display basic statistics
- Identify missing values
- Create visualizations using matplotlib

### 4.2 Data Manipulation (15 points)
- Filter and sort data
- Group and aggregate operations
- Create pivot tables
- Handle missing data appropriately

### 4.3 Analysis and Insights (10 points)
- Perform statistical analysis
- Create at least 3 meaningful visualizations
- Write markdown cells explaining your findings
- Draw conclusions from the data

## Bonus Challenges (+15 points)

### Dynamic Programming (7 points)
Convert recursive solutions to dynamic programming:
```python
def longest_common_subsequence(str1, str2):
    """Find LCS using dynamic programming"""
    # Your implementation here
```

### Custom Data Structure (8 points)
Implement a Trie (prefix tree):
```python
class Trie:
    """
    Implement:
    - insert(word)
    - search(word)
    - starts_with(prefix)
    """
    # Your implementation here
```

## Submission Requirements

```
week4-assignment/
├── functions_advanced.py
├── data_structures.py
├── recursion_problems.py
├── data_analysis.ipynb
├── data/
│   └── sample_data.csv  # We provide this
├── tests/
│   ├── test_functions.py
│   ├── test_data_structures.py
│   └── test_recursion.py
└── README.md
```

## Testing

Run the provided test suite:
```bash
pytest tests/ -v
```

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Correctness | 70 | All functions work as specified |
| Efficiency | 20 | Optimal time/space complexity |
| Code Quality | 15 | Clean, readable, well-documented |
| Notebook | 15 | Clear analysis and visualization |

## Performance Requirements

- Recursive functions should handle reasonable input sizes
- Use memoization where appropriate
- Document time complexity for each function

## Resources

- [Python Functions Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Recursion Tutorial](https://realpython.com/python-recursion/)
- [Jupyter Notebook Basics](https://jupyter-notebook.readthedocs.io/)

---

*Due: {{ page.due_date | date: "%B %d, %Y at %I:%M %p" }} • Points: {{ page.points }} • Difficulty: {{ page.difficulty }}*