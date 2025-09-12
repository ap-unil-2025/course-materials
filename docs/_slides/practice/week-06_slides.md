---
marp: true
theme: unil-theme
paginate: true
backgroundColor: #f5f9ff
header: "Session 6: OOP & Debugging"
footer: "Anna Smirnova, October 27, 2025"
---

<!-- _class: lead -->

# Session 6: Contact Manager - Final Form

**Professional OOP & Debugging**

---

# The Journey So Far 🏆

**Week 3**: Basic Contact Manager (v0.1)
- Variables and if/else
- Limited to 3 contacts

**Week 4**: Functional Contact Manager (v1.0)
- Functions and lists
- Unlimited contacts with save/load

**Week 5**: "AI can write this in 30 seconds!"
- But can you debug it?

**Today**: Professional Contact Manager (v2.0)
- Object-oriented design
- Proper error handling
- Production-ready code

---

# Part 1: From Functions to Classes

---

# Refactoring Our Contact Manager

**Week 4 approach** (functions + dictionaries):
```python
# Data and functions are separate
contacts = []  # List of dictionaries

def add_contact(contacts_list, name, phone):
    # Function operates on external data
    pass

def search_contacts(contacts_list, term):
    # Another separate function
    pass
```

**Week 6 approach** (OOP):
```python
class ContactManager:
    def __init__(self):
        self.contacts = []  # Data inside the class
    
    def add_contact(self, name, phone):
        # Method operates on its own data
        pass
    
    def search(self, term):
        # Everything organized together
        pass
```

**The data and the functions that operate on it are now together!**

---
# Key OOP Concepts
> Note: In practice, OOP is an extensive framework and a way of thinking about models and relationships. In our class, we will treat it as a way to organize code, but in the real world, it also includes design principles, patterns, and architecture.
- **Class**: Blueprint for creating objects (e.g., `Student`)
- **Object/Instance**: A specific instance of a class (e.g., `alice`)
- **Attributes**: Data stored in an object (e.g., `name`, `age`, `grades`)
- **Methods**: Functions defined in a class that operate on its data (e.g., `calculate_average`)

---
# Key OOP Concepts (cont.)
- **Encapsulation**: Bundling data and methods in one unit (class)
- **Inheritance**: Creating a new class based on an existing class (e.g., `ElectricCar` inherits from `Vehicle`)
- **Polymorphism**: Methods that can do different things based on the object (e.g., `draw()` method for different shapes)
- **Abstraction**: Hiding complex implementation details and showing only the necessary parts (e.g., using a `Database` class without knowing its internal workings)
- **Patterns**: Reusable solutions to common problems (e.g., Singleton, Factory)
---

# Part 2: Debugging Like a Pro

> "Debugging is twice as hard as writing the code in the first place.
> Therefore, if you write the code as cleverly as possible, you are, by definition,
> not smart enough to debug it." – Brian Kernighan

---

# Types of Bugs

1. **Syntax Errors** - Python can't understand your code
```python
# Missing colon
if x > 5
    print("Big")
```

2. **Runtime Errors (Exceptions)** - Code crashes while running
```python
result = 10 / 0  # ZeroDivisionError
x = y + 1        # NameError if y undefined
'foo' + 6        # TypeError
L = []; x = L[0] # IndexError
```

3. **Logic Errors** - Code runs but gives wrong results
```python
# Should calculate average, but forgets to divide
def average(numbers):
    return sum(numbers)  # Oops, forgot / len(numbers)
```

**Logic errors are the hardest to find!**

---

# Debugging Strategy 1: Print Debugging

```python
def calculate_discount(price, discount_percent):
    print(f"DEBUG: price={price}, discount={discount_percent}")  # Debug line
    
    discount_amount = price * discount_percent
    print(f"DEBUG: discount_amount={discount_amount}")  # Debug line
    
    final_price = price - discount_amount
    print(f"DEBUG: final_price={final_price}")  # Debug line
    
    return final_price

# Test it
result = calculate_discount(100, 0.2)  # Expecting 80
print(f"Result: {result}")
```

**Pro tip**: Use a DEBUG flag
```python
DEBUG = True  # Set to False in production

if DEBUG:
    print(f"Processing user {user_id}")
```

---

# Debugging Strategy 2: Using Debuggers

## Jupyter/IPython: Post-Mortem Debugging

```python
def plot_log():
    fig, ax = plt.subplots(2, 1)  # Bug: should be plt.subplots()
    x = np.linspace(1, 2, 10)
    ax.plot(x, np.log(x))  # Error: ax is array, not axes
    plt.show()

plot_log()  # This will crash
```

After the error, type `%debug` in the next cell:
```python
%debug  # Opens interactive debugger at crash point
# You can inspect variables:
# ipdb> ax
# ipdb> type(ax)
# ipdb> q  # quit debugger
```

---

# Setting Breakpoints

## Method 1: Using pdb
```python
from pdb import set_trace

def plot_log():
    set_trace()  # Execution stops here
    fig, ax = plt.subplots()
    x = np.logspace(1, 2, 10)  # Bug: should be linspace
    ax.plot(x, np.log(x))
    plt.show()

plot_log()  # Enter debugger before the bug
```

## Method 2: Modern Python (3.7+)
```python
def plot_log():
    breakpoint()  # Same as set_trace(), but built-in
    fig, ax = plt.subplots()
    x = np.logspace(1, 2, 10)
    ax.plot(x, np.log(x))
    plt.show()
```

**Debugger commands:**
- `n` - next line
- `s` - step into function
- `c` - continue execution
- `p variable` - print variable
- `h` - help
- `q` - quit

---

# VSCode Debugging (Live Demo)

**Setting Breakpoints:**
1. Click left of line number (red dot appears)
2. Run debugger (F5 or "Debug Cell" in notebooks)
3. Code stops at breakpoint

**Debug Controls:**
- **Continue (F5)**: Run until next breakpoint
- **Step Over (F10)**: Execute current line
- **Step Into (F11)**: Go inside function calls
- **Step Out (Shift+F11)**: Exit current function

**Watch Variables:**
- See all variables in Variables panel
- Add expressions to Watch panel
- Hover over variables to see values

```python
# We'll debug this together
def rev_list_buggy(L):
    for i in range(len(L)):
        j = len(L) - i  # Bug 1: should be len(L) - i - 1
        L[i] = temp      # Bug 2: temp not defined
        L[i] = L[j]      # Bug 3: overwrites L[i] before saving
        L[j] = L[i]      # Bug 4: wrong value (already changed)
```

---

# Part 3: Exception Handling

---

# Handling Errors Gracefully

**Without exception handling** (program crashes):
```python
def divide(a, b):
    return a / b

result = divide(10, 0)  # 💥 Crash!
print("This never prints")
```

**With exception handling** (program continues):
```python
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

result = divide(10, 0)  # Error: Cannot divide by zero!
print("Program continues running")  # This prints!
```

---

# Common Python Exceptions

```python
# ZeroDivisionError
try:
    result = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# ValueError - Wrong type/value
try:
    age = int("twenty")  # Can't convert "twenty" to int
except ValueError:
    print("Please enter a number")

# NameError - Variable not defined
try:
    print(undefined_variable)
except NameError:
    print("Variable doesn't exist")

# TypeError - Wrong type for operation
try:
    result = 'foo' + 6  # Can't add string and int
except TypeError:
    print("Type mismatch")

# IndexError - List index out of range
try:
    L = [1, 2, 3]
    print(L[10])
except IndexError:
    print("Index out of range")
```

---

# Multiple Exception Handling

```python
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print(f"Error: Cannot divide {type(a)} by {type(b)}")
        return None
    except Exception as e:  # Catch any other error
        print(f"Unexpected error: {e}")
        return None
    finally:  # Always runs, even if there's an error
        print("Division operation completed")

# Test different cases
print(safe_divide(10, 2))    # Works: 5.0
print(safe_divide(10, 0))    # ZeroDivisionError
print(safe_divide("10", 2))  # TypeError
```

**Best Practice**: Be specific with exceptions - catch specific errors first, then general ones.

---

# Part 4: Inheritance - Building on Classes

---

# Inheritance: Reusing Code

```python
# Base class (parent)
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    
    def start(self):
        print(f"The {self.brand} {self.model} is starting...")
    
    def accelerate(self, amount):
        self.speed += amount
        print(f"Speed is now {self.speed} km/h")

# Derived class (child)
class ElectricCar(Vehicle):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)  # Call parent constructor
        self.battery_size = battery_size
        self.battery_level = 100
    
    def charge(self):
        self.battery_level = 100
        print(f"Battery charged to {self.battery_level}%")
    
    def accelerate(self, amount):
        super().accelerate(amount)  # Call parent method
        self.battery_level -= amount * 0.1
        print(f"Battery at {self.battery_level:.1f}%")

# Use it
tesla = ElectricCar("Tesla", "Model 3", 2024, 75)
tesla.start()
tesla.accelerate(50)
```

---

# Using Assertions for Early Detection

```python
def calculate_variance(data):
    n = len(data)
    assert n > 1, "Need at least 2 data points for variance"
    
    mean = sum(data) / n
    variance = sum((x - mean)**2 for x in data) / (n - 1)
    return variance

# This will fail early with clear message:
try:
    var = calculate_variance([5])  # Only one data point
except AssertionError as e:
    print(f"Assertion failed: {e}")

# Good for:
# - Checking preconditions
# - Validating inputs
# - Documenting assumptions
# - Failing fast with clear errors
```

**Note**: Assertions can be disabled with `python -O`, so don't use them for actual error handling in production!

---

# Hands-On: Debug This OOP Code

```python
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0
    
    def add_item(self, item, price, quantity):
        self.items.append({
            'item': item,
            'price': price,
            'quantity': quantity
        })
        # BUG: What's wrong here?
        self.total = price * quantity
    
    def remove_item(self, item_name):
        # BUG: This doesn't update the total
        for item in self.items:
            if item['item'] == item_name:
                self.items.remove(item)
    
    def get_total(self):
        # BUG: Why is this wrong?
        return self.total

# Test it
cart = ShoppingCart()
cart.add_item("Apple", 0.5, 10)
cart.add_item("Banana", 0.3, 5)
print(f"Total: ${cart.get_total()}")  # What's wrong?
```

**Your task**: Find and fix the 3 bugs!

---

# Debugging Best Practices

**1. Reproduce the Bug**
- Can you make it happen consistently?
- What are the exact steps?

**2. Isolate the Problem**
- Comment out code sections
- Test individual functions
- Use minimal test cases

**3. Use the Right Tools**
```python
# Built-in debugging help
import pdb
pdb.set_trace()  # Starts interactive debugger

# Better: use VSCode debugger!
```

**4. Read Error Messages**
```python
Traceback (most recent call last):
  File "script.py", line 15, in <module>  # WHERE
    result = divide(10, 0)
  File "script.py", line 3, in divide
    return a / b
ZeroDivisionError: division by zero  # WHAT
```

---

# Part 5: Putting It All Together

---

# Project: Student Grade Tracker

```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}
    
    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)
    
    def get_average(self, subject=None):
        try:
            if subject:
                return sum(self.grades[subject]) / len(self.grades[subject])
            else:
                all_grades = [g for grades in self.grades.values() for g in grades]
                return sum(all_grades) / len(all_grades)
        except (KeyError, ZeroDivisionError):
            return None
    
    def __str__(self):
        return f"Student: {self.name} (ID: {self.student_id})"

class GradeBook:
    def __init__(self):
        self.students = {}
    
    def add_student(self, student):
        self.students[student.student_id] = student
    
    def find_student(self, student_id):
        return self.students.get(student_id, None)
    
    def class_average(self, subject):
        averages = []
        for student in self.students.values():
            avg = student.get_average(subject)
            if avg is not None:
                averages.append(avg)
        return sum(averages) / len(averages) if averages else 0
```

---

# Live Coding Exercise

**Build Together: Library Management System**

Requirements:
1. `Book` class with title, author, ISBN
2. `Library` class that manages books
3. Check out and return books
4. Handle errors (book not found, already checked out)
5. Add debugging to track operations

```python
# We'll build this together from scratch!
class Book:
    # TODO: Constructor
    pass

class Library:
    # TODO: Manage books
    pass

# Test with debugging
DEBUG = True
```

---

# Common OOP + Debugging Pitfalls

**1. Modifying lists in __init__**
```python
class Bad:
    def __init__(self, items=[]):  # DON'T DO THIS!
        self.items = items

# Why it's bad:
a = Bad()
b = Bad()
a.items.append(1)
print(b.items)  # [1] - Surprise! Shared list!

# Do this instead:
class Good:
    def __init__(self, items=None):
        self.items = items or []
```

**2. Forgetting `self`**
```python
class Calculator:
    def add(x, y):  # Forgot self!
        return x + y
```

**3. Infinite recursion**
```python
class Circle:
    @property
    def area(self):
        return self.area  # Calls itself forever!
```

---

# Your Turn: Debug Challenge

```python
class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def divide(self, a, b):
        result = a / b  # Bug 1: No error handling
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        return self.history  # Bug 2: Returns mutable list
    
    def clear_history(self):
        self.history = []  # Is this the best way?

# Test it and find issues:
calc = Calculator()
calc.add(10, 5)
calc.divide(10, 0)  # What happens?
history = calc.get_history()
history.append("HACKED!")  # What happens to calc.history?
```

**Tasks**:
1. Add exception handling to divide()
2. Protect the history list (hint: return a copy)
3. Add debugging with assert statements

---

# Exercise: File Reader with Error Handling

```python
# Create a file with mixed content
with open('numbers.txt', 'w') as f:
    f.write("prices\n3\n8\n\n7\ntwenty\n21")

# Your task: Read and sum the numbers, skip non-numbers
def sum_numbers_from_file(filename):
    total = 0
    with open(filename) as f:
        for line in f:
            # TODO: Add try-except to handle non-numeric lines
            pass  # Your code here
    return total

# Should return 39 (3 + 8 + 7 + 21)
```

---

# Homework Assignment

**Build a Student Grade System with Debugging**

Extend the `Student` and `GradeBook` classes to:

1. **Add robust error handling**:
   - Invalid grades (negative, > 100)
   - Missing students
   - Empty grade lists

2. **Add debugging features**:
   - Debug mode that logs all operations
   - Assertions for data validation
   - Method to verify data integrity

3. **Create test scenarios** with intentional bugs:
   - Division by zero in averages
   - Type errors in grade inputs
   - Index errors in grade access

**Deliverable**: Submit a Jupyter notebook showing:
- Your classes with error handling
- Screenshots of VSCode debugger in action
- Test cases demonstrating exception handling

---

# Key Takeaways

**OOP Essentials**:
- Classes organize code into reusable blueprints
- Objects are instances with their own data
- Inheritance lets you build on existing classes

**Debugging Tools**:
1. Print statements (quick and dirty)
2. `%debug` magic (post-mortem analysis)
3. `breakpoint()` or `pdb.set_trace()` (interactive)
4. VSCode debugger (visual and powerful)
5. Assertions (fail fast with clear messages)

**Error Handling**:
- Use `try-except` for graceful error recovery
- Be specific with exception types
- Use `finally` for cleanup code
- Assertions for documenting assumptions

**Remember**: 
> "The debugger is your friend. Learn to use it well!"