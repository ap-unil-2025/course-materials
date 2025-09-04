---
layout: lesson
title: "Python Fundamentals I"
week: 3
date: 2025-09-29
type: "programming"
topics:
  - Python basics (variables, types)
  - Control flow (loops, branching)
  - Strings and data structures (lists, tuples, dictionaries)
  - Git version control productivity
slides: "/slides/practice/week03_slides.html"
summary: "Introduction to core Python programming concepts including variables, data types, control flow, and essential data structures."
---

# Python Fundamentals I

This lesson introduces the core concepts of Python programming that form the foundation for all data science and advanced programming work.

## Learning Objectives

By the end of this lesson, you will:

- Work confidently with Python variables and basic data types
- Use control flow structures (if/else, loops) effectively
- Manipulate strings and understand string methods
- Work with Python's essential data structures: lists, tuples, and dictionaries
- Apply Git version control for productivity in your programming workflow

## Python Basics: Variables and Types

### Variables and Assignment
Python uses dynamic typing - you don't need to declare variable types explicitly.

```python
# Basic variable assignment
name = "Data Science"
age = 25
height = 5.9
is_student = True
```

### Basic Data Types
- **int**: Whole numbers
- **float**: Decimal numbers  
- **str**: Text/strings
- **bool**: True/False values

## Control Flow

### Conditional Statements
```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

### Loops
```python
# For loops
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# While loops
count = 0
while count < 5:
    print(count)
    count += 1
```

## Strings and String Methods

Strings are sequences of characters with powerful built-in methods:

```python
text = "Introduction to Data Science"
print(text.lower())           # lowercase
print(text.upper())           # uppercase
print(text.split())           # split into words
print(text.replace("Data", "Computer"))  # replace text
```

## Data Structures

### Lists (Ordered, Mutable)
```python
courses = ["Economics", "Statistics", "Programming"]
courses.append("Machine Learning")
courses[0] = "Advanced Economics"
```

### Tuples (Ordered, Immutable)
```python
coordinates = (10.5, 20.3)
# coordinates[0] = 15  # This would cause an error
```

### Dictionaries (Key-Value Pairs)
```python
student = {
    "name": "Alice",
    "major": "Economics",
    "gpa": 3.8
}
student["graduation_year"] = 2025
```

## Productivity with Git

### Essential Git Workflow for Programming
```bash
# Check status frequently
git status

# Add specific files (not everything)
git add specific_file.py

# Commit with meaningful messages
git commit -m "Add data validation function"

# Push to remote
git push origin main
```

### Best Practices
- Commit early and often
- Write descriptive commit messages
- Use .gitignore for temporary files
- Review changes before committing

## Hands-on Activities

### Activity 1: Variable Practice
Create a program that:
1. Stores personal information in variables
2. Calculates and displays derived values
3. Uses different data types appropriately

### Activity 2: Control Flow Challenge
Write a program that:
1. Takes user input
2. Uses conditional logic to make decisions
3. Implements loops for repetitive tasks

### Activity 3: Data Structure Manipulation
Create a program that:
1. Uses lists to store course information
2. Uses dictionaries to represent student data
3. Combines different data structures effectively

## Assessment

This lesson contributes to:
- Understanding of Python fundamentals
- Programming problem-solving skills
- Git workflow for code management

## Next Steps

Next week we'll build on these fundamentals with functions, recursion, and object-oriented programming basics.