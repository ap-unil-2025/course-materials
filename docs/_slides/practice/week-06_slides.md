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

# Part 2: Inheritance - Building on Classes

---

# Inheritance: Reusing Code

**Concept**: Build new classes based on existing ones

**Parent Class** (Vehicle):
- Has: brand, model, year, speed
- Can: start(), accelerate()

**Child Class** (ElectricCar):
- **Inherits** everything from Vehicle
- **Adds**: battery_size, battery_level
- **Adds** new method: charge()
- **Extends** accelerate() to also use battery

**Why is this useful?**
- Don't repeat code - reuse what works!
- Add specific features to specialized classes
- All electric cars are vehicles, but not all vehicles are electric!

**Key Tool**: `super()` - lets you use the parent class's methods

---

# Part 3: Putting It All Together

---

# Example: Student Grade Tracker

**Design Question**: How should we structure this?

**Option 1**: Two classes working together
- `Student` class: Manages individual student data
- `GradeBook` class: Manages collection of students

**Student Class** should:
- Store: name, student_id, grades (dictionary of subjects → list of grades)
- Methods: add_grade(), get_average()

**GradeBook Class** should:
- Store: collection of Student objects
- Methods: add_student(), find_student(), class_average()

**Key Design Principle**: Each class has a clear responsibility!

**Thinking Process**:
1. What data does each class need to remember?
2. What operations make sense for each class?
3. How do they interact with each other?

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

# Common OOP Pitfalls

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



# Homework Assignment

**Build a Contact Manager v2.0 with OOP**

Extend your Contact Manager to use classes:

1. **Create a `ContactManager` class** with:
   - `__init__` method to initialize empty contact list
   - `add_contact(name, phone, email)` method
   - `search(term)` method to find contacts
   - `delete_contact(name)` method
   - `save(filename)` and `load(filename)` methods

2. **Add robust error handling**:
   - Handle file not found errors
   - Handle invalid contact data
   - Handle duplicate contacts

3. **Optional: Add a `Contact` class**:
   - Separate class for individual contacts
   - ContactManager uses Contact objects

**Deliverable**: Submit a Python file or Jupyter notebook with your class implementation

---

# Key Takeaways

**OOP Essentials**:
- Classes organize code into reusable blueprints
- Objects are instances with their own data
- Methods operate on object data using `self`
- Inheritance lets you build on existing classes

**Common Pitfalls**:
- Don't use mutable default arguments in `__init__`
- Always include `self` as first parameter in methods
- Be careful with shared vs. instance attributes

**Practice**:
- Start by converting your functional Contact Manager to OOP
- Add methods one at a time and test as you go
- Use inheritance when it makes sense (optional)

**Next Week**: We'll learn about testing and debugging!