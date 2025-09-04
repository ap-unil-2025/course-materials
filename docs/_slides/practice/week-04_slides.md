---
marp: true
theme: default
paginate: true
header: 'Session 4: Thinking in Objects'
footer: 'Object-Oriented Programming (OOP) Basics'
author: 'Anna Smirnova'
---


# Session 4: Thinking in Objects

**Object-Oriented Programming (OOP) Basics**

---

# First Things First: Today's Goals

*   Understand the **idea** behind OOP.
*   See the difference between **Imperative** and **Object-Oriented** code.
*   Learn the core concepts: **Classes** and **Objects**.
*   Master the `__init__` method and the `self` keyword.
*   Explore the power of **Inheritance** for code reuse.
*   Build a practical, realistic example.

---
<!-- _class: invert -->

# Part 1: A New Way of Thinking

---

# The Story So Far: Imperative Programming

Up to now, we've mostly written **imperative code**. This means we think in terms of:

1.  **Data** (like dictionaries, lists, variables).
2.  **Functions** that operate on that data.

```python
# The DATA
experiment_run = {
    "id": "exp_01",
    "param_A": 0.5,
    "results": [10.2, 10.4, 9.9]
}

# The FUNCTIONS that operate on the data
def calculate_mean(data_dict: dict) -> float | None:
    return sum(data_dict["results"]) / len(data_dict["results"])

def print_summary(data_dict: dict) -> None:
    mean_val = calculate_mean(data_dict)
    print(f"ID: {data_dict['id']}, Mean: {mean_val:.2f}")

print_summary(experiment_run)
```
This works, but the data and the functions are separate.

---

# The Problem with Separate Data and Functions

As our projects grow, this separation becomes a problem:

*   **It gets messy**: Which functions work with which data structures?
*   **No enforced structure**: What if we forget a key in our dictionary, like `"results"`? The `calculate_mean` function will crash.
*   **Hard to manage state**: The data is "dumb." It has no ability to manage itself or ensure its own consistency.

There must be a better way to organize our code...

---

# The OOP Solution: Bundling Data and Functions

**Object-Oriented Programming** is a paradigm based on a simple, powerful idea:

> Let's bundle the data and the functions that work on that data together into a single "thing" called an **Object**.

*   An object **HAS** data (attributes).
*   An object **CAN DO** things (methods).

Think of a car. It's not just a collection of parts (data) and a separate instruction manual (functions). A car is a single object that *has* an engine and wheels, and *can* accelerate and brake.

---
<!-- _class: invert -->

# Part 2: The Building Blocks of OOP

---

# Classes and Objects (Blueprints and Houses)

This is the most important concept in OOP.

*   A **Class** is the **blueprint**. It's the template or recipe that defines the structure and behavior. It doesn't *do* anything on its own.

*   An **Object** (or **Instance**) is the **actual thing** built from the blueprint. You can create many objects from a single class, each with its own unique data.

```python
# The Class (Blueprint)
class Experiment:
    # ... definition goes here ...
    pass

# Creating Objects (Instances) from the blueprint
exp_A = Experiment()  # One house
exp_B = Experiment()  # A second, separate house
```

---

# Building the Object: `__init__`

How do we give an object its initial data when it's created? We use a special "dunder" (double-underscore) method called `__init__`.

*   `__init__` is the **constructor**.
*   It runs **automatically** every time you create a new object from the class.
*   Its job is to set up the initial state of the object.

---

# The `self` Keyword: The Object's "I"

Inside a class's methods, how does an object refer to its *own* data? It uses `self`.

*   `self` is a special variable that represents **the instance of the object itself**.
*   When you write `self.parameter = value`, you are saying: "Store this `value` in *my own* `parameter` attribute."

```python
class Experiment:
    # The constructor method
    def __init__(self, exp_id: str, parameter_A: float):
        print(f"Creating a new experiment with ID: {exp_id}")
        # Storing the initial data ON THE OBJECT ITSELF
        self.id = exp_id
        self.param_A = parameter_A
        self.results: list[float] = [] # Start with an empty list

# When you run this...
exp_1 = Experiment(exp_id="run_01", parameter_A=0.75)
# ...the __init__ method is called automatically.
# `self` inside __init__ refers to the `exp_1` object.
```

---

# Attributes and Methods

An object has two main components:

*   **Attributes**: The variables that belong to an object. They represent what the object **HAS**.
    *   `exp_1.id`
    *   `exp_1.results`

*   **Methods**: The functions that belong to an object. They represent what the object **CAN DO**. Methods always take `self` as their first argument so they can access the object's own attributes.

---

# Putting It All Together: A Full Class

Let's add a method to our `Experiment` class.

```python
class Experiment:
    def __init__(self, exp_id: str, parameter_A: float):
        self.id = exp_id
        self.param_A = parameter_A
        self.results: list[float] = []

    # This is a METHOD
    def add_data_point(self, value: float):
        # It uses `self` to access its own `results` list
        self.results.append(value)

    # Another METHOD
    def calculate_mean(self) -> float | None:
        if not self.results:
            return None
        return sum(self.results) / len(self.results)
```

---

# Using Our New Object

Now our data (`id`, `results`) and the functions that operate on it (`add_data_point`, `calculate_mean`) are bundled together cleanly.

```python
# Create an instance
exp_1 = Experiment(exp_id="run_01", parameter_A=0.75)

# Use its methods to change its internal state
exp_1.add_data_point(12.5)
exp_1.add_data_point(13.1)
exp_1.add_data_point(12.8)

# Access its attributes and methods
print(f"Experiment ID: {exp_1.id}")
print(f"Raw results: {exp_1.results}")
print(f"Mean of results: {exp_1.calculate_mean():.2f}")
```
This is much more organized and less error-prone!

---
<!-- _class: invert -->

# Part 3: The Power-Up - Inheritance

---

# Don't Repeat Yourself (DRY)

What if we have a special kind of experiment, like a computer simulation, that has all the properties of a normal experiment but also some extra ones?

We don't want to copy-paste the `Experiment` class and add to it. Instead, we can use **Inheritance**.

**Inheritance** lets a new class (the "child") inherit all the attributes and methods from an existing class (the "parent"). This is an "is-a" relationship: a `SimulationExperiment` *is a kind of* `Experiment`.

---

# Inheritance in Code

The child class is defined by putting the parent class in parentheses.

```python
# PARENT CLASS
class Experiment:
    # ... (same as before) ...

# CHILD CLASS
class SimulationExperiment(Experiment): # <-- This is inheritance!
    def __init__(self, exp_id: str, parameter_A: float, software_version: str):
        # Ask the parent to do its setup first!
        super().__init__(exp_id, parameter_A)
        # Now add the new attribute specific to this child
        self.version = software_version

    # We can also add new methods
    def run_simulation(self):
        print(f"Running simulation v{self.version} for {self.id}...")
        # ... logic to run simulation and add data points ...
        self.add_data_point(50.1) # We can use methods from the parent!
```
The `super().__init__()` line is crucial: it runs the `__init__` method of the parent class.

---

# A Realistic Example: Data Readers

Let's design a system to read data from different file types.

**The Blueprint (Parent Class):**
We'll create a generic `DataReader` that knows it needs a `filepath`, but doesn't know *how* to read it yet.

```python
class DataReader:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def read(self) -> list[dict]:
        # This is a placeholder. The children MUST implement this.
        raise NotImplementedError("Each subclass must implement its own read method!")
```

---

# The Implementations (Child Classes)

Now we create specialized child classes that inherit from `DataReader` and provide their own concrete implementation of the `read` method.

```python
import csv
import json

class CSVReader(DataReader):
    def read(self) -> list[dict]:
        print(f"Reading CSV from {self.filepath}")
        with open(self.filepath, 'r') as f:
            return list(csv.DictReader(f))

class JSONReader(DataReader):
    def read(self) -> list[dict]:
        print(f"Reading JSON from {self.filepath}")
        with open(self.filepath, 'r') as f:
            return json.load(f)
```
This is a powerful and clean pattern for building extensible software.

---
# Your Assignment
TBA

