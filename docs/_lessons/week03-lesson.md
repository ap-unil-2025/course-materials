---
layout: lesson
title: "Week 3: Git Fundamentals & Python Basics"
week_number: 3
date: 2025-09-29
---

# Week 3: Git Fundamentals & Python Basics

## Learning Objectives

By the end of this week, you will be able to:
- Use essential Git commands for version control
- Understand Git workflow (add, commit, push, pull)
- Write basic Python programs with variables and data types
- Use Python control flow structures (if/else, loops)
- Define and use simple functions

---

## Part 1: Git Fundamentals

### Why Git?

Git is the industry standard for version control. It helps you:
- Track changes to your code over time
- Collaborate with others without conflicts
- Recover from mistakes
- Maintain multiple versions of your project

### Essential Git Commands

#### 1. Setting Up Git

```bash
# Configure your identity (one-time setup)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Check your configuration
git config --list
```

#### 2. Creating a Repository

```bash
# Initialize a new repository
git init

# Clone an existing repository
git clone https://github.com/username/repository.git
```

#### 3. Basic Workflow

```bash
# Check status of your files
git status

# Add files to staging area
git add filename.py        # Add specific file
git add .                   # Add all files

# Commit changes with message
git commit -m "Add feature X"

# Push to remote repository
git push origin main

# Pull latest changes from remote
git pull origin main
```

#### 4. Viewing History

```bash
# View commit history
git log

# View compact history
git log --oneline

# View differences
git diff                    # Unstaged changes
git diff --staged           # Staged changes
```

### Git Best Practices

1. **Commit Often**: Make small, logical commits
2. **Write Clear Messages**: Describe what and why, not how
3. **Pull Before Push**: Always sync before pushing changes
4. **Use .gitignore**: Don't track unnecessary files

Example `.gitignore` for Python:
```
# Python
__pycache__/
*.py[cod]
.env
venv/
*.log

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
```

---

## Part 2: Python Fundamentals

### Variables and Data Types

#### Basic Data Types

```python
# Numbers
integer_num = 42
float_num = 3.14

# Strings
name = "Alice"
message = 'Hello, World!'
multiline = """This is a
multiline string"""

# Booleans
is_student = True
is_finished = False

# None (represents absence of value)
result = None
```

#### Type Checking and Conversion

```python
# Check type
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("hello"))     # <class 'str'>

# Type conversion
str_num = "123"
int_num = int(str_num)   # Convert to integer
float_num = float(str_num) # Convert to float
str_val = str(42)        # Convert to string
```

### Basic Operations

```python
# Arithmetic
a = 10 + 5    # Addition: 15
b = 10 - 5    # Subtraction: 5
c = 10 * 5    # Multiplication: 50
d = 10 / 5    # Division: 2.0
e = 10 // 3   # Floor division: 3
f = 10 % 3    # Modulo: 1
g = 2 ** 3    # Exponentiation: 8

# String operations
greeting = "Hello" + " " + "World"  # Concatenation
repeated = "Ha" * 3                 # "HaHaHa"
length = len("Python")               # 6
```

### Control Flow

#### If/Else Statements

```python
age = 18

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# Ternary operator
status = "adult" if age >= 18 else "minor"
```

#### Loops

```python
# For loop
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# Iterating over a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# While loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Break and continue
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break     # Stop at 7
    print(i)
```

### Functions

#### Defining Functions

```python
# Simple function
def greet():
    print("Hello!")

greet()  # Call the function

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# Function with return value
def add(a, b):
    return a + b

result = add(3, 5)  # result = 8

# Function with default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(3))     # 9 (3^2)
print(power(3, 3))  # 27 (3^3)
```

#### Function Documentation

```python
def calculate_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle

    Returns:
        float: The area of the circle
    """
    import math
    return math.pi * radius ** 2

# Access documentation
help(calculate_area)
```

### Input and Output

```python
# Getting user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert to integer

# Formatted output
print(f"Hello, {name}! You are {age} years old.")

# Writing to a file
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is a test.")

# Reading from a file
with open("output.txt", "r") as f:
    content = f.read()
    print(content)
```

---

## Practice Exercises

### Exercise 1: Git Practice

1. Create a new Git repository
2. Create a Python file called `hello.py`
3. Add and commit the file
4. Make changes to the file
5. View the differences
6. Commit the changes

### Exercise 2: Temperature Converter

Write a function that converts Celsius to Fahrenheit:

```python
def celsius_to_fahrenheit(celsius):
    # Your code here
    pass

# Test cases
print(celsius_to_fahrenheit(0))   # Should print 32
print(celsius_to_fahrenheit(100)) # Should print 212
```

### Exercise 3: Number Guesser

Create a simple guessing game:

```python
import random

secret = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number (1-10): "))
    attempts += 1

    if guess == secret:
        print(f"Correct! It took you {attempts} attempts.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
```

### Exercise 4: List Operations

```python
# Create a function that finds the maximum in a list
def find_max(numbers):
    if not numbers:
        return None

    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Test
test_list = [3, 7, 2, 9, 1, 5]
print(find_max(test_list))  # Should print 9
```

---

## Common Pitfalls and Solutions

### Git Pitfalls

1. **Forgetting to pull before push**
   - Solution: Always run `git pull` before `git push`

2. **Committing sensitive data**
   - Solution: Use `.gitignore` and never commit passwords or API keys

3. **Large commits with unrelated changes**
   - Solution: Make small, focused commits

### Python Pitfalls

1. **Indentation errors**
   - Python uses indentation to define blocks
   - Use consistent spacing (4 spaces recommended)

2. **Type errors**
   ```python
   # Wrong
   age = input("Enter age: ")
   if age > 18:  # Error: comparing string with int

   # Correct
   age = int(input("Enter age: "))
   if age > 18:
   ```

3. **Mutable default arguments**
   ```python
   # Wrong
   def add_item(item, list=[]):
       list.append(item)
       return list

   # Correct
   def add_item(item, list=None):
       if list is None:
           list = []
       list.append(item)
       return list
   ```

---

## Summary

This week you learned:

**Git:**
- Initialize and clone repositories
- Add, commit, and push changes
- Pull updates from remote repositories
- View history and differences

**Python:**
- Work with basic data types
- Use control flow structures
- Define and call functions
- Handle input and output

These fundamentals form the foundation for all your future programming work. Practice these concepts regularly to build muscle memory and confidence.

---

## Next Week Preview

In Week 4, we'll dive deeper into:
- Python data structures (lists, dictionaries, sets)
- Object-oriented programming basics
- More advanced Git features (branches, merging)
- Error handling and debugging

---

## Additional Resources

- [Official Git Documentation](https://git-scm.com/doc)
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [GitHub's Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Python for Everybody](https://www.py4e.com/)