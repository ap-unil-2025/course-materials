---
layout: lesson
title: "Python Fundamentals II"
week: 4
date: 2025-10-06
type: "programming"
topics:
  - Functions and recursion
  - Object-Oriented Programming (OOP) basics
  - Classes and inheritance
  - Code organization and modularity
slides: "/slides/practice/week04_slides.html"
summary: "Advanced Python programming concepts including functions, recursion, and introduction to object-oriented programming with classes and inheritance."
---

# Python Fundamentals II

This lesson builds on Python basics to cover more advanced programming concepts that are essential for writing organized, reusable, and maintainable code.

## Learning Objectives

By the end of this lesson, you will:

- Write and use functions effectively for code organization
- Understand and apply recursion for problem-solving
- Create and use classes in object-oriented programming
- Implement inheritance to create related classes
- Organize code into modular, reusable components

## Functions: Building Blocks of Programs

### Function Definition and Usage
```python
def calculate_compound_interest(principal, rate, time):
    """
    Calculate compound interest.
    
    Args:
        principal (float): Initial amount
        rate (float): Interest rate (as decimal)
        time (int): Time period in years
    
    Returns:
        float: Final amount after compound interest
    """
    return principal * (1 + rate) ** time

# Usage
final_amount = calculate_compound_interest(1000, 0.05, 10)
print(f"Final amount: ${final_amount:.2f}")
```

### Function Features
- **Parameters and Arguments**: Pass data to functions
- **Return Values**: Get results back from functions
- **Docstrings**: Document what your functions do
- **Default Parameters**: Set default values for flexibility

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))                    # Uses default
print(greet("Bob", "Good morning"))      # Custom greeting
```

## Recursion: Functions That Call Themselves

Recursion is powerful for problems that can be broken down into similar subproblems.

```python
def factorial(n):
    """Calculate factorial using recursion."""
    if n <= 1:          # Base case
        return 1
    else:               # Recursive case
        return n * factorial(n - 1)

def fibonacci(n):
    """Calculate Fibonacci number using recursion."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

### When to Use Recursion
- Tree-like data structures
- Mathematical sequences
- Divide-and-conquer algorithms
- Problems with recursive definitions

## Object-Oriented Programming (OOP) Basics

### Classes: Blueprints for Objects
```python
class BankAccount:
    """A simple bank account class."""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        """Deposit money to the account."""
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        """Return current balance."""
        return self.balance
    
    def __str__(self):
        return f"Account({self.account_holder}): ${self.balance:.2f}"
```

### Using Classes
```python
# Create objects (instances)
alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob")

# Use methods
alice_account.deposit(500)
alice_account.withdraw(200)
print(alice_account)  # Account(Alice): $1300.00
```

## Inheritance: Building on Existing Classes

```python
class SavingsAccount(BankAccount):
    """A savings account with interest."""
    
    def __init__(self, account_holder, initial_balance=0, interest_rate=0.02):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        """Add interest to the account."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest
    
    def __str__(self):
        return f"SavingsAccount({self.account_holder}): ${self.balance:.2f} @ {self.interest_rate*100}%"

class CheckingAccount(BankAccount):
    """A checking account with overdraft protection."""
    
    def __init__(self, account_holder, initial_balance=0, overdraft_limit=100):
        super().__init__(account_holder, initial_balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        """Withdraw with overdraft protection."""
        if amount > 0 and (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            return True
        return False
```

## Code Organization and Modularity

### Why Organize Code?
- **Maintainability**: Easier to update and fix
- **Reusability**: Functions and classes can be used multiple times
- **Readability**: Clear structure helps others understand your code
- **Testing**: Modular code is easier to test

### Best Practices
```python
# Good: Clear, focused functions
def calculate_tax(income, tax_rate):
    return income * tax_rate

def calculate_net_income(gross_income, tax_rate):
    tax = calculate_tax(gross_income, tax_rate)
    return gross_income - tax

# Good: Classes with single responsibility
class Portfolio:
    def __init__(self):
        self.stocks = {}
    
    def add_stock(self, symbol, shares, price):
        self.stocks[symbol] = {"shares": shares, "price": price}
    
    def get_total_value(self):
        return sum(stock["shares"] * stock["price"] 
                  for stock in self.stocks.values())
```

## Hands-on Activities

### Activity 1: Function Design
Create functions for common economic calculations:
1. Present value calculation
2. Loan payment calculator
3. Investment growth projector

### Activity 2: Recursion Practice
Implement recursive solutions for:
1. Calculating compound interest recursively
2. Tree-traversal problems
3. Economic modeling scenarios

### Activity 3: OOP Design
Design and implement:
1. A `Student` class with grades and GPA calculation
2. A `Portfolio` class for investment tracking
3. Inheritance hierarchy for different account types

## Key OOP Concepts

### Encapsulation
- Keep related data and methods together
- Control access to internal data
- Use private attributes when appropriate

### Inheritance
- Reuse code from parent classes
- Extend functionality in child classes
- Override methods when needed

### Polymorphism
- Different objects can respond to the same method call
- Enables flexible, extensible code design

## Assessment

This lesson contributes to:
- Advanced Python programming skills
- Object-oriented design thinking
- Code organization and modularity
- Problem-solving with recursion

## Next Steps

Next week we'll explore Generative AI and how it can assist in programming, followed by scientific computing with NumPy and Pandas.