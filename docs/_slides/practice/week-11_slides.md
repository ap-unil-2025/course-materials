---
marp: true
theme: unil-theme
paginate: true
backgroundColor: #f5f9ff
header: "session 3: Modern Python Projects"
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

<!-- _class: lead -->

# Session 11: Modern Python Projects

**Building organized, reproducible, and professional code.**

---

# First Things First: Today's Goals

* Welcome to Session 11! Today, we will:
*  Learn a standard **Project Structure** for Python.
*   Understand what **Dependencies** are and why they matter.
*   Manage projects with **`uv`**, a modern, all-in-one tool.
*   Keep code clean and consistent with **`ruff`**.

---

# Part 1: Project Structure & Dependencies

---

# Why Not Just One `.py` File?

As projects grow, a single file becomes messy. Good structure makes your project:

*   **Understandable**: Newcomers can find things easily.
*   **Maintainable**: Fixing bugs and adding features is simpler.
*   **Importable**: Allows you to create reusable code modules.

---

# A Standard Project Structure

A great starting point for most research projects:

```
my-research-project/
├── .gitignore
├── README.md
├── pyproject.toml      # <-- The new control center
├── src/                # <-- Your source code lives here
│   ├── __init__.py     # <-- Makes this a package
│   ├── main.py
│   └── calculations/   # <-- A submodule for related code
│       ├── __init__.py
│       └── math_utils.py
│
└── tests/              # (Optional but good practice)
    └── test_calculations.py
```
---

# Modules and Packages: The `__init__.py` File

*   A Python file (`.py`) is a **module**.
*   A directory containing an `__init__.py` file is a **package**.

The `__init__.py` file tells Python:
> "Treat this folder as a group of modules you can **import** from."

This allows you to import code from your own project, just like you import libraries!

---
# Importing from Packages
To import code from a module placed in a subfolder, you can use the dot notation:
```python
from src.calculations import math_utils
```

This works because `src/` and `src/calculations/` both contain an `__init__.py`.
It can be completely empty; its presence is what matters. This allows you to organize your code into sub-folders and still import it.
> Caution! TODO paths

---
# Absolute vs. Relative Imports

How you import depends on where you are.

**1. Absolute Imports (Recommended)**
*   Start the import path from the project's source root (`src`).
*   They are clear, explicit, and work from anywhere.
*   **Example**: `from src.calculations import math_utils`

**2. Relative Imports (Use with caution)**
*   Use `.` for the current package and `..` for the parent package.
*   **Example**: Inside `src/main.py`, you could write `from .calculations import math_utils`
*   Can be fragile if you move files around. **Stick to absolute imports.**

---

# What Are Dependencies?

> Recall: A **dependency** is an external software package at a specific version your project needs to function.

When you write `import numpy`, your code has a **dependency** on NumPy.

### Why does managing them matter?
1.  **Functionality**: Your code will crash without them.
2.  **Versions**: A new version of a library could break your existing code. You need to "lock" the versions that you know work.
3.  **Reproducibility**: For research to be reproducible, others must be able to recreate your *exact* software environment.

---
<!-- _class: invert -->

# Part 2: Modern Tooling with `uv`

---

# Introducing `uv`

Forget juggling `venv` and `pip` separately.

**`uv`** is an extremely fast, all-in-one tool that is both a:
*   **Package Installer** (like `pip`)
*   **Virtual Environment Manager** (like `venv`)

It simplifies the entire project management workflow.

---

# Project Setup with `uv`

In a new, empty project folder, this one command does it all:

```bash
uv init
```

This will automatically:
1.  Create a virtual environment in a `.venv` folder.
2.  Create a `pyproject.toml` file to configure your project.

---

# The `pyproject.toml` Control Center

This file is the modern standard for configuring Python projects. It replaces multiple older files (`setup.py`, `requirements.txt`).

Let's look inside...

---

### `pyproject.toml`: The `[project]` Section

This section holds general information about your project.

```toml
[project]
name = "my-research-project"
version = "0.1.0"
description = "A short description of the project."
```

---

### `pyproject.toml`: The `[project.dependencies]` Section

This is where you list the packages your code needs to **run**. It's the "source of truth" for your project's needs.

```toml
[project.dependencies]
# We will add packages like "numpy" here
```

---

# Adding Dependencies with `uv`

This single command is all you need:

```bash
uv pip install numpy pandas
```

This will:
1.  Add `numpy` and `pandas` to your `pyproject.toml`.
2.  Install them into your `.venv` virtual environment.
3.  Create/update a `uv.lock` file, which freezes the exact versions of *all* dependencies for perfect reproducibility.

---

# Running Code with `uv`

No more typing `source .venv/bin/activate`!

`uv` can run any command directly within your project's environment.

```bash
# Run a python script
uv run python src/main.py

# Run any other command
uv run <command>
```

---

# The Power of `uv sync`

You've cloned a project from GitHub. How do you install everything?

```bash
# Don't do this: uv pip install -r requirements.txt
# Do this instead:
uv sync
```

`uv sync` reads the `uv.lock` file and installs the **exact** versions of all packages, guaranteeing a perfectly replicated environment.

**This is the key to reproducibility.**

---
# Advanced `uv` Features

<img src="image.png" alt="alt text" width="650"/>

---
<!-- _class: invert -->

# Part 3: Code Quality with `ruff`

---

# Linters and Formatters

*   **Linter**: A tool that analyzes your code to find potential bugs, style errors, and bad practices.
*   **Formatter**: A tool that automatically rewrites your code to follow a strict, consistent style guide.

**`ruff`** is a next-generation tool that is an extremely fast **linter AND formatter** in one.

---

# Using `ruff` in Your Project

1.  **Install `ruff` as a "dev" dependency:**
    It's a tool for you, the developer, not for running the code.
    ```bash
    uv pip install --dev ruff
    ```
    This adds `ruff` to a special `[tool.uv.dev-dependencies]` section in your `pyproject.toml`.

2.  **Lint your code:**
    Find potential problems in all files in the current directory (`.`).
    ```bash
    uv run ruff check .
    ```

3.  **Format your code:**
    Automatically clean up your code's style.
    ```bash
    uv run ruff format .
    ```

---

<!-- _class: lead -->

# Recap

You can now create a modern, structured, and reproducible Python project!

| Task | `uv` Command | `ruff` Command |
| :--- | :--- | :--- |
| Start a new project | `uv init` | |
| Add a runtime package | `uv add <package>` | |
| Recreate environment | `uv sync` | |
| Run a script in env | `uv run python script.py` | |
| Find code errors | | `uv run ruff check .` |
| Auto-format code | | `uv run ruff format .` |
---
# Your Assignment
* Unify your project structure using today's standard layout.
* Add and manage dependencies with `uv`.
* Use `ruff` to lint and format your code.
* Submit your updated project by the next session.
* If you have any questions or need help, feel free to reach out during office hours or via email.
---