---
marp: true
paginate: true
header: "Session 6: OOP & Debugging"
footer: "Anna Smirnova, October 20, 2025"
style: |
  section {
    font-size: 22px;
  }
  section.lead {
    background: #003aff;
    color: white;
    font-size: 28px;
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
# Key OOP Concepts: The Basics

**Class**: Blueprint for creating objects
- Example: `Student` class

**Object/Instance**: A specific instance of a class
- Example: `alice = Student("Alice", 12345)`

**Attributes**: Data stored in an object
- Example: `name`, `age`, `grades`

**Methods**: Functions that operate on the object's data
- Example: `calculate_average()`

---

# Key OOP Concepts: Core Principles

**Encapsulation**: Bundle data and methods together
- Keep related things in one place

**Inheritance**: Build new classes from existing ones
- `ElectricCar` inherits from `Vehicle`

**Polymorphism**: Same method, different behaviors
- `draw()` works differently for Circle vs. Square

---

# OOP in the Real World

> **Note**: In practice, OOP is much more!
> - Design principles and patterns
> - Architecture and relationships
> - Complex system modeling

**In our class**: We treat OOP as a code organization tool

**In industry**: It's a complete way of thinking about software design

---

# Part 2: Inheritance - Building on Classes

---

# Inheritance: The Concept

**Build new classes based on existing ones**

**Parent Class** (Vehicle):
- Has: brand, model, year, speed
- Can: start(), accelerate()

**Child Class** (ElectricCar):
- **Inherits** everything from Vehicle
- **Plus** adds battery-specific features

---

# Why Use Inheritance?

**Benefits**:
- Don't repeat code - reuse what works!
- Add specific features to specialized classes
- Organize code by relationships

**Example**: All electric cars are vehicles, but not all vehicles are electric!

**Key Tool**: `super()`
- Lets child class use parent class's methods
- Extends behavior without rewriting everything

---

# Part 3: Putting It All Together

---

# Example: Student Grade Tracker

**Design Question**: How should we structure this?

Two classes working together:
- `Student` class: Individual student data
- `GradeBook` class: Collection of students

**Key Design Principle**: Each class has ONE clear responsibility!

---

# Student Grade Tracker: Student Class

**What should Student remember?**
- name
- student_id
- grades (dictionary: subject → list of grades)

**What can Student do?**
- add_grade(subject, grade)
- get_average(subject)

---

# Student Grade Tracker: GradeBook Class

**What should GradeBook remember?**
- Collection of Student objects

**What can GradeBook do?**
- add_student(student)
- find_student(student_id)
- class_average(subject)

**Thinking**: What operations make sense at the class level vs. individual student level?

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

# Common Pitfall #1: Mutable Default Arguments

**DON'T DO THIS**:
```python
class Bad:
    def __init__(self, items=[]):  # Danger!
        self.items = items
```

**Why it's bad**:
```python
a = Bad()
b = Bad()
a.items.append(1)
print(b.items)  # [1] - Surprise! Shared list!
```

**Do this instead**:
```python
class Good:
    def __init__(self, items=None):
        self.items = items or []
```

---

# Common Pitfall #2: Forgetting `self`

**DON'T DO THIS**:
```python
class Calculator:
    def add(x, y):  # Missing self!
        return x + y
```

**Error**: `add() takes 2 positional arguments but 3 were given`

**Do this instead**:
```python
class Calculator:
    def add(self, x, y):  # Always include self!
        return x + y
```

---

# Common Pitfall #3: Infinite Recursion

**DON'T DO THIS**:
```python
class Circle:
    @property
    def area(self):
        return self.area  # Calls itself forever!
```

**Error**: RecursionError: maximum recursion depth exceeded

**Remember**: Accessing an attribute shouldn't call itself!

---



# Homework Assignment

**Build Contact Manager v2.0 with OOP**

Transform your functional Contact Manager to use classes!

---

# Homework: Part 1 - ContactManager Class

**Create a `ContactManager` class with these methods**:
- `__init__()` - initialize empty contact list
- `add_contact(name, phone, email)` - add a contact
- `search(term)` - find contacts
- `delete_contact(name)` - remove a contact
- `save(filename)` and `load(filename)` - persistence

---

# Homework: Part 2 - Error Handling

**Add robust error handling**:
- File not found when loading
- Invalid contact data
- Duplicate contacts
- Empty search results

**Test your error handling** - make sure your code doesn't crash!

---

# Homework: Optional Challenge

**Add a `Contact` class**:
- Separate class for individual contacts
- ContactManager uses Contact objects instead of dictionaries

**Why?** Better encapsulation and cleaner code!

**Deliverable**: Submit Python file or Jupyter notebook

---

# Key Takeaways: OOP Essentials

**Classes** organize code into reusable blueprints

**Objects** are instances with their own data

**Methods** operate on object data using `self`

**Inheritance** lets you build on existing classes

---

# Key Takeaways: Watch Out For...

**Common Pitfalls**:
- ❌ Mutable default arguments in `__init__`
- ❌ Forgetting `self` in methods
- ❌ Shared vs. instance attributes confusion

**Remember**: Test as you build!

---

# Key Takeaways: Practice Strategy

**Start simple**:
1. Convert your functional Contact Manager to OOP
2. Add methods one at a time
3. Test each method before moving on

**Optional**: Try inheritance when it makes sense

**Next Week**: Testing and debugging!

---