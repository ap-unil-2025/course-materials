---
marp: true
paginate: true
header: "Session 7: Debugging & Error Handling"
footer: "Anna Smirnova, November 3, 2025"
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

# Session 7: Debugging & Error Handling

**Finding Bugs and Handling Errors Gracefully**

---

# What We'll Cover Today

**Part 1: Understanding Bugs**
- Types of bugs (syntax, runtime, logic)
- How to read error messages

**Part 2: Debugging Strategies**
- Print debugging
- Using debuggers (VSCode)

**Part 3: Exception Handling**
- Try/except blocks
- Common Python exceptions
- Best practices

---

# The Debugging Mindset

> "Debugging is twice as hard as writing the code in the first place.
> Therefore, if you write the code as cleverly as possible, you are, by definition,
> not smart enough to debug it." – Brian Kernighan

**Key insight**: Write simple, readable code. Your future self (and debugger) will thank you!

---

# Part 1: Understanding Bugs

---

# Types of Bugs: Overview

There are three main categories of bugs in Python:

1. **Syntax Errors** - Python can't parse your code
   - Detected before the program runs
   - Easiest to fix

2. **Runtime Errors (Exceptions)** - Code crashes during execution
   - Detected when the problematic line runs
   - Can be handled with try-except

3. **Logic Errors** - Code runs but produces wrong results
   - No error messages
   - Hardest to find and fix

Let's explore each type in detail...

---

# Bug Type 1: Syntax Errors

**What they are**: Violations of Python's grammar rules

**When detected**: Before the program runs (at parse time)

**Common examples**:
```python
# Missing colon
if x > 5
    print("Big")

# Mismatched parentheses
result = calculate(5, 10

# Invalid indentation
def greet():
print("Hello")

# Missing quotes
message = Hello World
```

**How to identify**:
- Python shows `SyntaxError` with a caret (^) pointing at the problem
- The error is usually ON or RIGHT BEFORE the line indicated
- Your code won't run at all until fixed

---

# Bug Type 2: Runtime Errors (Exceptions)

**What they are**: Errors that occur during program execution

**When detected**: When the problematic line is executed

**Common examples**:
```python
# ZeroDivisionError - Division by zero
result = 10 / 0

# NameError - Using undefined variable
x = y + 1  # if y doesn't exist

# TypeError - Operation on wrong type
result = 'foo' + 6  # Can't add string and int

# IndexError - Accessing non-existent list index
L = [1, 2, 3]
x = L[10]

# KeyError - Accessing non-existent dictionary key
person = {'name': 'Alice'}
age = person['age']  # 'age' doesn't exist

# FileNotFoundError - Opening non-existent file
f = open('missing.txt', 'r')
```

---

# Bug Type 3: Logic Errors

**What they are**: Code runs successfully but produces incorrect results

**When detected**: Only when you notice wrong output (no error message!)

**Why they're dangerous**: Python can't help you find them

**Common examples**:
```python
# Example 1: Wrong operator
def calculate_discount(price, percent):
    return price + (price * percent)  # Should be minus!

# Example 2: Off-by-one error
def get_last_n_items(items, n):
    return items[-n-1:]  # Should be items[-n:]

# Example 3: Forgetting to return a value
def calculate_average(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    # Oops, forgot to return avg!

# Example 4: Wrong variable scope
total = 0
def add_to_total(amount):
    total = total + amount  # Oops, creates local total
    return total
```

**How to find them**: Testing, debugging, code review, print statements

---

# Reading Error Messages

```python
Traceback (most recent call last):
  File "script.py", line 15, in <module>  # WHERE: line 15
    result = divide(10, 0)
  File "script.py", line 3, in divide     # Inside divide function
    return a / b
ZeroDivisionError: division by zero       # WHAT: the actual error
```

**How to read this**:
1. Start from the bottom - that's the actual error
2. Work up to see the chain of function calls
3. Look for YOUR code (not library code)
4. The line numbers tell you exactly where to look

---

# Part 2: Debugging Strategies

---

# Strategy 1: Print Debugging

**The simplest tool**: Just add `print()` statements!

```python
def calculate_discount(price, discount_percent):
    print(f"DEBUG: price={price}, discount={discount_percent}")

    discount_amount = price * discount_percent
    print(f"DEBUG: discount_amount={discount_amount}")

    final_price = price - discount_amount
    print(f"DEBUG: final_price={final_price}")

    return final_price

# Test it
result = calculate_discount(100, 0.2)  # Expecting 80
print(f"Result: {result}")
```

**Output**:
```
DEBUG: price=100, discount=0.2
DEBUG: discount_amount=20.0
DEBUG: final_price=80.0
Result: 80.0
```

---

# Pro Tip: Use a DEBUG Flag

```python
DEBUG = True  # Set to False in production

def calculate_discount(price, discount_percent):
    if DEBUG:
        print(f"DEBUG: price={price}, discount={discount_percent}")

    discount_amount = price * discount_percent

    if DEBUG:
        print(f"DEBUG: discount_amount={discount_amount}")

    final_price = price - discount_amount
    return final_price
```

**Benefits**:
- Easy to turn off all debug output
- No need to delete debug statements
- Can keep them for future debugging

---

# Strategy 2: Using Debuggers

**Debuggers** let you:
- Pause execution at any line
- Inspect variable values
- Step through code line by line
- See the call stack

We will use **Visual debugging** with VSCode.

---

# VSCode Debugging (Live Demo)

**Visual debugging** is the most powerful approach!

**Setting Breakpoints**:
1. Click left of line number → red dot appears
2. Run debugger (F5 or "Debug Cell" in notebooks)
3. Code pauses at breakpoint

**Debug Controls** (toolbar at top):
- **Continue (F5)**: Run until next breakpoint
- **Step Over (F10)**: Execute current line
- **Step Into (F11)**: Go inside function calls
- **Step Out (Shift+F11)**: Exit current function

**Panels**:
- **Variables**: See all current variables and their values
- **Watch**: Add expressions to monitor (e.g., `len(contacts)`)
- **Call Stack**: See the chain of function calls

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

# The Try-Except-Finally Pattern

```python
try:
    # Code that might raise an exception
    file = open('contacts.json', 'r')
    data = json.load(file)
except FileNotFoundError:
    # Handle specific error
    print("File not found, creating new contacts list")
    data = []
except json.JSONDecodeError:
    # Handle another specific error
    print("Invalid JSON, starting fresh")
    data = []
finally:
    # Always runs, even if there was an error or return
    try:
        file.close()
    except:
        pass  # File wasn't opened
```

**Use `finally` for cleanup**: Closing files, releasing resources, etc.

---

# Raising Your Own Exceptions

Sometimes YOU want to raise an error:

```python
class ContactManager:
    def add_contact(self, name, phone):
        if not name:
            raise ValueError("Name cannot be empty")
        if not phone:
            raise ValueError("Phone cannot be empty")

        contact = {'name': name, 'phone': phone}
        self.contacts.append(contact)

# Usage
manager = ContactManager()
try:
    manager.add_contact("", "123-4567")
except ValueError as e:
    print(f"Error: {e}")  # Error: Name cannot be empty
```

**Why raise exceptions?**
- Communicate errors clearly
- Force calling code to handle errors
- Better than returning `None` or `-1` as error codes

---

# Exercise 1: Debug the Shopping Cart

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

---

# Exercise 1: Solution

**Bug 1**: `add_item` sets total instead of adding to it
```python
# Wrong:
self.total = price * quantity

# Right:
self.total += price * quantity
```

**Bug 2**: `remove_item` doesn't update total
```python
# Add before removing:
self.total -= item['price'] * item['quantity']
self.items.remove(item)
```

**Bug 3**: Better approach - calculate total dynamically
```python
def get_total(self):
    return sum(item['price'] * item['quantity'] for item in self.items)
```

---

# Exercise 2: Add Exception Handling to Contact Manager

```python
class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        # TODO: Add validation
        contact = {'name': name, 'phone': phone}
        self.contacts.append(contact)

    def save(self, filename):
        # TODO: Handle file errors
        with open(filename, 'w') as f:
            json.dump(self.contacts, f)

    def load(self, filename):
        # TODO: Handle file not found, invalid JSON
        with open(filename, 'r') as f:
            self.contacts = json.load(f)
```

**Your task**: Add proper exception handling and validation!

---

# Exercise 2: Solution

```python
class ContactManager:
    def add_contact(self, name, phone):
        if not name or not phone:
            raise ValueError("Name and phone cannot be empty")
        contact = {'name': name, 'phone': phone}
        self.contacts.append(contact)

    def save(self, filename):
        try:
            with open(filename, 'w') as f:
                json.dump(self.contacts, f)
        except (IOError, OSError) as e:
            print(f"Error saving file: {e}")
            raise

    def load(self, filename):
        try:
            with open(filename, 'r') as f:
                self.contacts = json.load(f)
        except FileNotFoundError:
            print(f"File {filename} not found, starting fresh")
            self.contacts = []
        except json.JSONDecodeError:
            print(f"Invalid JSON in {filename}, starting fresh")
            self.contacts = []
```

---

# Debugging Best Practices

**1. Reproduce the Bug**
- Can you make it happen consistently?
- What are the minimal steps?

**2. Isolate the Problem**
- Comment out code sections
- Test individual functions
- Use binary search approach

**3. Read Error Messages Carefully**
- Don't panic and randomly change code
- Understand what the error says
- Look at the line numbers

**4. Use the Right Tools**
- Print debugging for simple issues
- Debugger for complex logic
- VSCode visual debugging for stepping through

---

# Exception Handling Best Practices

**1. Be Specific**
```python
# Bad - catches everything
try:
    result = int(input())
except:
    print("Error")

# Good - catches specific errors
try:
    result = int(input())
except ValueError:
    print("Please enter a number")
```

**2. Don't Silently Ignore Errors**
```python
# Bad
try:
    something()
except:
    pass  # User has no idea what went wrong

# Good
try:
    something()
except Exception as e:
    print(f"Error: {e}")
    # Maybe log it, raise it, or provide fallback
```

---

# Debugging Checklist

Before asking for help, try these steps:

- [ ] Read the error message carefully
- [ ] Check for typos in variable/function names
- [ ] Verify indentation (Python is picky!)
- [ ] Add print statements to see values
- [ ] Use a debugger to step through code
- [ ] Test with simpler inputs
- [ ] Check if variables have expected types
- [ ] Look for off-by-one errors in loops
- [ ] Make sure all functions return values
- [ ] Verify `self` is included in method definitions

---

# Homework Assignment

**Debug and Harden Your Contact Manager**

Take your Contact Manager v2.0 from last week and:

1. **Add comprehensive exception handling**:
   - Validate all inputs (no empty names/phones)
   - Handle file errors gracefully
   - Handle invalid JSON data

2. **Debug a provided buggy version**:
   - I'll give you a Contact Manager with 5 bugs
   - Use debugging techniques to find and fix them
   - Document your debugging process

3. **Test edge cases**:
   - Empty contact list
   - Duplicate contacts
   - Missing files
   - Invalid data types

**Deliverable**: Jupyter notebook showing your debugging process and fixed code

---

# Key Takeaways

**Debugging**:
- Three types of bugs: syntax, runtime, logic
- Read error messages from bottom up
- Use print debugging for simple issues
- Use debuggers (VSCode) for complex problems

**Exception Handling**:
- Use `try-except` to handle errors gracefully
- Be specific with exception types
- Use `finally` for cleanup
- Raise your own exceptions to validate inputs

**Professional Practice**:
- Write code that's easy to debug
- Fail fast with clear error messages
- Test edge cases
- Handle errors, don't ignore them

---

<!-- _class: lead -->

# Questions?

**Next week**: Project structure, dependencies, and modern Python tools!
