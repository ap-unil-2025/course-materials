---
layout: assignment
title: "Problem Set Week 3: Python Control Flow & Functions"
assignment_number: 103
due_date: 2025-10-06 23:59:00
github_classroom_url: "https://classroom.github.com/a/xP3nK7mQ-ps-week3"
topics:
  - "Control flow"
  - "Functions"
  - "Lists and dictionaries"
  - "String manipulation"
---

# Problem Set 3: Python Control Flow & Functions

## GitHub Classroom Setup

1. Accept the assignment via the GitHub Classroom link above
2. Clone your repository: `git clone [your-repo-url]`
3. Install requirements: `pip install -r requirements.txt`
4. Run tests locally: `pytest test_assignment.py`

## Exercise 1: Temperature Converter (20 points)

Create a file `temperature.py` with functions to convert temperatures.

```python
def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit
    Formula: F = C * 9/5 + 32
    
    Args:
        celsius (float): Temperature in Celsius
    Returns:
        float: Temperature in Fahrenheit
    
    Example:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    # TODO: Implement this function
    pass

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius
    Formula: C = (F - 32) * 5/9
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    Returns:
        float: Temperature in Celsius
    """
    # TODO: Implement this function
    pass

def classify_temperature(celsius):
    """
    Classify temperature into categories:
    - "freezing" if below 0°C
    - "cold" if 0-15°C
    - "moderate" if 15-25°C
    - "warm" if 25-35°C
    - "hot" if above 35°C
    
    Args:
        celsius (float): Temperature in Celsius
    Returns:
        str: Temperature category
    """
    # TODO: Implement this function
    pass
```

## Exercise 2: List Operations (25 points)

Create a file `list_operations.py` with these functions:

```python
def find_max_min(numbers):
    """
    Find maximum and minimum in a list without using max()/min()
    
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (maximum, minimum)
    
    Example:
        >>> find_max_min([3, 1, 4, 1, 5, 9])
        (9, 1)
    """
    # TODO: Implement this function
    pass

def remove_duplicates(items):
    """
    Remove duplicates from list while preserving order
    
    Args:
        items (list): List with possible duplicates
    Returns:
        list: List without duplicates
    
    Example:
        >>> remove_duplicates([1, 2, 2, 3, 1, 4])
        [1, 2, 3, 4]
    """
    # TODO: Implement this function
    pass

def calculate_average(numbers):
    """
    Calculate average of numbers in a list
    
    Args:
        numbers (list): List of numbers
    Returns:
        float: Average value, or None if list is empty
    """
    # TODO: Implement this function
    pass
```

## Exercise 3: Word Counter (25 points)

Create a file `word_counter.py`:

```python
def count_words(text):
    """
    Count occurrences of each word (case-insensitive)
    
    Args:
        text (str): Input text
    Returns:
        dict: Word counts {word: count}
    
    Example:
        >>> count_words("Hello world hello Python")
        {'hello': 2, 'world': 1, 'python': 1}
    """
    # TODO: Implement this function
    pass

def most_common_words(text, n=5):
    """
    Find n most common words in text
    
    Args:
        text (str): Input text
        n (int): Number of words to return
    Returns:
        list: List of tuples [(word, count), ...]
    """
    # TODO: Implement this function
    pass
```

## Exercise 4: Simple Calculator (30 points)

Create a file `calculator.py`:

```python
def calculate(expression):
    """
    Evaluate a simple mathematical expression string
    Supports +, -, *, / and parentheses
    
    Args:
        expression (str): Mathematical expression
    Returns:
        float: Result of calculation
    
    Example:
        >>> calculate("2 + 3 * 4")
        14.0
        >>> calculate("(2 + 3) * 4")
        20.0
    """
    # TODO: Implement this function
    # Hint: Consider using eval() for simplicity, but be aware of security
    pass

def is_valid_expression(expression):
    """
    Check if expression contains only valid characters
    Valid: digits, +, -, *, /, (, ), spaces
    
    Args:
        expression (str): Expression to validate
    Returns:
        bool: True if valid, False otherwise
    """
    # TODO: Implement this function
    pass
```

## Testing Your Code

We provide automated tests. Run them with:

```bash
pytest test_assignment.py -v
```

You should see output like:
```
test_temperature.py::test_celsius_to_fahrenheit PASSED
test_temperature.py::test_classify_temperature PASSED
test_list_operations.py::test_find_max_min PASSED
...
```

## Grading Rubric

- **Correctness (70%)**: Code passes all automated tests
- **Code Quality (20%)**: Clean, readable, follows Python conventions
- **Documentation (10%)**: Functions have clear docstrings

## Submission

1. Complete all exercises
2. Ensure all tests pass: `pytest test_assignment.py`
3. Commit and push your code:
   ```bash
   git add .
   git commit -m "Complete Problem Set 3"
   git push
   ```
4. Verify submission on GitHub

## Tips

- Start with the simplest functions first
- Test each function individually before moving on
- Use print statements for debugging
- Remember Python string methods: `.lower()`, `.split()`, etc.
- Lists have useful methods: `.append()`, `.remove()`, etc.

## Getting Help

- Check Python documentation: https://docs.python.org/3/
- Ask on course Discord/Forum
- Office hours: Wednesdays 2-4 PM