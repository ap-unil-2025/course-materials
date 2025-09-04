---
marp: true
theme: gradient
paginate: true
header: "Finding and Preventing Bugs"
footer: "Anna Smirnova, June 24, 2025"
style: |
  section {
    font-size: 29px;
  }
  h1 {
    font-size: 40px;
  }
  h2 {
    font-size: 10px;
  }
  h3 {
    font-size: 20px;
    }
---

# Session 4: Finding and Preventing Bugs

**An Introduction to Debugging and Type Hints**

---

# Today's Goals

*   Move beyond `print()` for finding bugs.
*   Learn to use a real **Debugger** in VS Code.
*   Understand what **Type Hints** are.
*   Use type hints to write clearer, safer, and self-documenting code.

---


# Part 1: The Art of Finding Bugs (Debugging)

---

# The Old-Fashioned Way: `print()`

We've all done this. Your code isn't working, so you add `print()` statements everywhere to see the values of variables.

```python
def calculate_mean(numbers):
    total = 0
    print(f"Starting total: {total}")
    for n in numbers:
        total += n
        print(f"  - Added {n}, new total is {total}")
    mean = total / len(numbers)
    print(f"Final mean: {mean}")
    return mean

calculate_mean([10, 20, 30])
```

**It works, but it's messy, slow, and you have to remove the prints later.**

---

# Level Up: Using a Debugger

A **debugger** is a tool that lets you run your code line by line, pausing it at any point to inspect its state.

Think of it as **pausing time inside your program** to look around.

### Why is it better than `print()`?
*   **Interactive**: You can explore variables without re-running your code.
*   **Controlled**: You decide exactly how and when the code proceeds.
*   **Clean**: No need to add and remove temporary `print()` statements.

---

# The VS Code Debugger

![bg left:30% contain](https://code.visualstudio.com/assets/docs/debugtest/debugging/debugging_hero.png)
The VS Code Debugger is a powerful built-in tool that allows you to debug Python code (and many other languages) directly within Visual Studio Code.

The VS Code Debugger is built into Visual Studio Code, making it easy to use without any extra setup.

[Learn more in the official documentation &rarr;](https://code.visualstudio.com/docs/debugtest/debugging)

---
# Debugging: Key Concepts
1.  **Breakpoints**: A "stop sign" you place on a line of code.
2.  **Debug Controls**: Buttons to control the flow of time (step, continue).
3.  **Variable Inspector**: A panel showing the real-time values of all variables.

---

# Key Concept: Breakpoints

A **breakpoint** is a red dot you place next to a line number in VS Code by clicking in the margin.

When you run your code in debug mode, it will **execute normally until it hits a breakpoint, then it will pause.**

This is the most fundamental feature of any debugger.

---

# Controlling Time: The Debug Toolbar

Once paused at a breakpoint, this toolbar appears. It lets you control how the code proceeds.

*   ▶️ **Continue (F5)**: Unpause and run until the next breakpoint.
*   ↪️ **Step Over (F10)**: Execute the current line and pause on the *next* one. (If the line is a function call, it runs the whole function without going inside).
*   🔽 **Step Into (F11)**: If the line is a function call, "step into" that function and pause on its first line.
*   🔼 **Step Out (Shift+F11)**: Finish running the current function and pause on the line where it was called from.

---

# The Superpower: Inspecting Variables

While your code is paused, the **Variables** panel on the left is your best friend.

*   It shows you the **current value of every variable** in scope.
*   You can see how values change as you "step" through the code line by line.
*   This is infinitely more powerful than adding `print()` statements!

---

# A Quick Detour: Handling Expected Errors (Exceptions)

---

# What if an Error is *Expected*?

Sometimes, errors are a normal part of a program's operation.
*   What if a file you want to read doesn't exist?
*   What if a user enters text when you expect a number?
*   What if you try to divide by zero?

Crashing is not a good user experience. Python gives us a way to "catch" these errors and handle them gracefully using a `try...except` block.

---

# The `try...except` Block

The basic idea:
1.  **`try`**: You put the code that *might* cause an error in this block.
2.  **`except`**: If an error of a specific type occurs in the `try` block, the code inside `except` is executed. The program does **not** crash.
---
# Example: Handling Division by Zero
```python
try:
    # This will cause a ZeroDivisionError
    result = 10 / 0
    print("This line will never be reached.")
except ZeroDivisionError:
    print("Oops! You can't divide by zero. Setting result to 0.")
    result = 0

print(f"The final result is: {result}")
```
This is a clean way to handle predictable problems without stopping your entire script.

---

# Part 2: Preventing Bugs with Type Hints

---

# From Fixing Bugs to Preventing Them

Debugging is a great skill for fixing bugs that already exist.

**Type Hints** help us prevent a whole class of bugs from being written in the first place.

---

# What Are Type Hints?

Type hints are optional "labels" you add to your Python code to indicate the expected data type of variables, function arguments, and return values.

**Before:**
```python
def add(a, b):
    return a + b
```

**After:**
```python
def add(a: int, b: int) -> int:
    return a + b
```

The `-> int` indicates that this function is expected to return an integer.

---

# Type Hint Syntax

```python
# For variables
name: str = "Anna"
age: int = 29
is_researcher: bool = True

# For collections 
scores: list[int] = [95, 88, 100]
headers: dict[str, int, bool] = {
    "name": "Anna",
    "age": 29,
    "is_researcher": True
}

# For function return values
def get_name() -> str:
    return "Anna"
```

---

# Important: Python Itself Ignores Type Hints!

This is a critical point. At runtime, the Python interpreter **does nothing** with these hints. Your code doesn't run slower or faster.

`"hello" + "world"` works, and so does `2 + 3`. A function `add(a, b)` will work with both strings and integers, even if you hint it for `int`.

So... *why bother?*

---

# Why Use Them? Three Huge Benefits

Type hints are for **humans** and for **tools**.

1.  **Readability & Documentation**: Your code becomes self-documenting. You immediately know what kind of data a function expects and returns.

2.  **Editor Superpowers**: Your code editor (like VS Code) understands the types, giving you much better autocompletion and suggestions.

3.  **Automatic Error Checking**: This is the big one. Tools can read your type hints and find bugs for you *before you even run the code*.
    
---

# Catching Bugs Before You Run

Remember `ruff` from last session? It's not just a formatter; it's also a linter that understands type hints.

Consider this code:
```python
def calculate_mean(scores: list[float]) -> float:
    return sum(scores) / len(scores)

# This will cause a TypeError at runtime!
# We are passing a string instead of a number.
calculate_mean([90.5, 88.1, "75.3"])
```

When you run `uv run ruff check .`, `ruff` will immediately flag this as an error, saving you from a runtime crash!

---

# Part 3: Advanced Type Hinting

**Describing more complex data structures.**

---

# Multiple Possible Types: The `Union`

**Problem:** What if a variable could be one of several different types? For example, an ID could be an `int` or a `str`.

**Solution:** Use `Union` to specify all possible types.

```python
from typing import Union

def get_user_by_id(user_id: Union[int, str]) -> dict:
    # ... logic to fetch user ...
    pass

# Modern Python (3.10+) allows a cleaner syntax with `|`
def get_user_by_id_modern(user_id: int | str) -> dict:
    pass
```

This tells the type checker that `user_id` is allowed to be *either* an `int` *or* a `str`.

---

# Handling `None`: The `Optional` Type

**Problem:** What if a function might return a value, but it could also return `None`? This is extremely common when searching for something that might not exist.

**Solution:** Use `Optional`. It is a shortcut for `Union[YourType, None]`.

```python
from typing import Optional

def find_user(name: str) -> Optional[dict]:
    # Returns a user dict if found in names dict, otherwise returns None
    if name in all_users:
        return all_users[name]
    return None
```
`mypy` and `ruff` will now force you to check if the result is `None` before you try to use it as a dictionary, preventing `NoneType` errors!

---

# The Escape Hatch: `Any`

**Problem:** You're working with a library that has no type hints, or you have a piece of code that is so dynamic it's nearly impossible to type.

**Solution:** Use `Any` to tell the type checker: **"Trust me. Stop checking here."**

```python
from typing import Any

def process_legacy_data(raw_data: Any) -> int:
    # We don't know the type of 'raw_data',
    # so we use Any and hope for the best.
    # The type checker will not complain about the next line.
    return int(raw_data['user']['id'])
```
**⚠️ Caution:** `Any` is powerful but dangerous. It silences the type checker. Use it as a last resort when you cannot be more specific. Overusing it defeats the purpose of type hinting.

---

# Typing Functions Themselves: `Callable`

**Problem:** How do you specify the type of an argument that is itself a function (like a callback or a transformation function)?

**Solution:** Use `Callable`. The syntax is `Callable[[arg1_type, arg2_type], return_type]`.

---
# Example
```python
from typing import Callable

# This function takes a list of numbers and a function
# that transforms one float into another.
def apply_transform(
    data: list[float],
    transform_func: Callable[[float], float]
) -> list[float]:
    return [transform_func(x) for x in data]

# Example usage:
import math
result = apply_transform([1.0, 4.0, 9.0], math.sqrt)
```

---

# Creating Your Own Type Names: `TypeAlias`

**Problem:** Your type hints are getting long and repetitive, making function signatures hard to read.

**Solution:** Use `TypeAlias` to create a shorter, more meaningful name for a complex type.

```python
from typing import TypeAlias

# This is a complex and repetitive type for a user dict
UserDict: TypeAlias = dict[str, Union[int, str, bool]]

def process_user(user: UserDict) -> None:
    # The signature is now much cleaner!
    pass
```

---

# Special Case for Researchers: `numpy` Arrays

A NumPy array is not a `list`. So how do we type it? The `numpy` library provides its own special types that you should use.

```python
import numpy as np
from numpy.typing import NDArray

# NDArray is a generic type for any numpy array
def get_magnitude(vector: NDArray) -> np.float64:
    return np.linalg.norm(vector)

# You can even specify the data type inside the array!
def process_image(image: NDArray[np.uint8]) -> NDArray[np.float64]:
    # This function expects an array of unsigned 8-bit integers
    # and returns an array of 64-bit floats.
    return image.astype(np.float64) / 255.0
```

---

# Putting It All Together: A Complex Example
```python
from typing import Callable, Optional, TypeAlias
import numpy as np
from numpy.typing import NDArray

ProcessingFunc: TypeAlias = Callable[[NDArray], NDArray]

def analyze_data(
    data: NDArray[np.float64],
    preprocessor: Optional[ProcessingFunc] = None
) -> dict[str, float]:
    """Analyzes a dataset, optionally preprocessing it first."""

    if preprocessor:
        data = preprocessor(data)

    return {"mean": np.mean(data), "std": np.std(data)}
```
---

# `mypy`: The Original Type Checker

While `ruff`'s linter is fantastic and catches many type errors, the most powerful and dedicated tool for type checking is **`mypy`**.

*   `mypy` is the gold standard for static type analysis in Python.
*   It performs a deeper, more comprehensive analysis of your type hints than most linters.
*   If you are serious about type safety, `mypy` is the tool to use.

---

# Using `mypy`

1.  **Install it as a dev dependency:**
    Just like `ruff`, it's a tool for developers.
    ```bash
    uv pip install --dev mypy
    ```

2.  **Run it from the command line:**
    `mypy` will check your entire codebase, following imports to ensure types are consistent across all your files.
    ```bash
    uv run mypy src/
    ```
    If it finds no issues, it will output nothing. If it finds a type inconsistency, it will give you a clear error message pointing to the exact line.

---

# `ruff` vs. `mypy`

*   **`ruff`**: An all-in-one, blazing-fast tool. Its type checking is very good for most day-to-day use and catches the most common errors.
*   **`mypy`**: A specialized, highly-configurable, and more thorough type checker. It is the definitive authority on whether your type hints are correct.

**Recommendation:** Use `ruff` for instant feedback as you code. Use `mypy` as a final, comprehensive check before you commit your code.

---

# Final Project: Automated Checks with GitHub Actions

---

# Bringing It All Together

For your final project, we will use an automated system called **GitHub Actions** to ensure code quality.

GitHub Actions allows you to run specific scripts automatically whenever you push code to your repository. This way, you don't have to worry about forgetting to run checks or format your code.

---
# What does this mean?
Every time you `git push` your code to your project's `main` branch on GitHub, a process that **I have outlined** will automatically run on GitHub's servers.This process will:
1.  Set up a clean Python environment.
2.  Install all your dependencies from `pyproject.toml`.
2.  Run `uv run ruff check .` to find linting errors *without fixing them*.
3.  Run `ruff format --check .` to ensure your code is formatted correctly (without actually changing it).
4.  Run `uv run mypy src/` to perform a strict type check.

**If any of these checks fail, you will see a red ❌ next to your commit on GitHub.** You will need to fix the issues and push again to get a green ✅.

