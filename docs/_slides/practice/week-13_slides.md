---
marp: true
paginate: true
header: "Session 13: Multithreading & Parallelization"
footer: "Anna Smirnova, December 8, 2025"
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

# Session 13: Practice Session

**Parallelism in Python**

---

# Today: Hands-On Practice

**Part 1: Quick Recap** (5 min)
- Threading vs Multiprocessing — when to use which

**Part 2: Numba** (15 min)
- New content: JIT compilation for numeric code

**Part 3: Live Demos** (25 min)
- Run code together, watch cores light up

**Part 4: Project Work** (rest of session)
- Work on your projects, ask questions

---

# Part 1: Quick Recap

*You saw this in the lecture — let's just summarize*

---

# The One Slide Summary

<div style="display: flex; gap: 2em;">
<div style="flex: 1;">

**I/O-bound** (waiting for stuff)

```python
# Downloading, API calls, file I/O
with ThreadPoolExecutor() as pool:
    pool.map(download, urls)
```

Threads wait simultaneously.
GIL doesn't matter — you're waiting anyway.

</div>
<div style="flex: 1;">

**CPU-bound** (crunching numbers)

```python
# Simulations, ML, heavy math
with ProcessPoolExecutor() as pool:
    pool.map(calculate, data)
```

Each process has its own Python.
Bypasses GIL completely.

</div>
</div>

---

# Quick Reference

| | ThreadPoolExecutor | ProcessPoolExecutor |
|---|---|---|
| **Use for** | I/O-bound | CPU-bound |
| **Example** | Download 500 stock prices | 1M Monte Carlo sims |
| **GIL** | Blocked (but doesn't matter) | Bypassed |
| **Overhead** | Low | Higher |
| **Sharing data** | Easy | Needs pickle |

**That's it.** Now let's look at something new.

---

# Part 2: Numba

*The professor didn't cover this — it's a nice trick for numeric code*

---

# The Problem with Python Loops

```python
def calculate_var(n_sims, weights, mu, sigma):
    returns = np.empty(n_sims)
    for i in range(n_sims):  # ← Python loops are SLOW
        asset_returns = np.random.randn(len(weights)) * sigma + mu
        returns[i] = np.dot(weights, asset_returns)
    returns.sort()
    return returns[int(n_sims * 0.05)]
```

With 10 million simulations, this takes ~60 seconds.

---

# The Numba Solution

```python
from numba import njit

@njit  # ← Add this one line
def calculate_var(n_sims, weights, mu, sigma):
    returns = np.empty(n_sims)
    for i in range(n_sims):
        asset_returns = np.random.randn(len(weights)) * sigma + mu
        returns[i] = np.dot(weights, asset_returns)
    returns.sort()
    return returns[int(n_sims * 0.05)]
```

Same code. Now takes **~0.5 seconds**. That's **120x faster**.

---

# How Numba Works

1. First call → Numba compiles your function to machine code
2. Subsequent calls → uses cached compiled version

```python
@njit
def add(a, b):
    return a + b

add(1, 2)      # Compiles (slow first time)
add(1, 2)      # Uses cache (fast)
add(1.0, 2.0)  # Different types → recompiles
```

**Works with:** NumPy, loops, basic math
**Doesn't work with:** Pandas, most libraries

---

# Numba + Parallelism

```python
from numba import njit, prange

@njit(parallel=True)  # ← Add parallel=True
def calculate_var(n_sims, weights, mu, sigma):
    returns = np.empty(n_sims)
    for i in prange(n_sims):  # ← Change range to prange
        ...
```

| | Time |
|---|------|
| Pure Python | ~60 sec |
| `@njit` | ~0.5 sec |
| `@njit(parallel=True)` | ~0.15 sec |

---

# When to Use Numba

**Good fit:**
- Monte Carlo simulations
- Option pricing loops
- Any numeric loop that's too slow

**Bad fit:**
- Pandas operations (use vectorized pandas instead)
- Code that's already fast enough
- Complex objects, strings, I/O

**Rule:** Use Numba for the math-heavy inner loop, not the whole program.

---

# Part 3: Live Demos

*Let's run some code together*

---

# Demo Setup

Open two terminal windows side by side:

**Terminal 1:** Run `btop` or `htop`
```bash
btop
```

**Terminal 2:** Run our demos
```bash
cd demos/week13
python cpu_demo.py
```

Watch the CPU cores light up!

---

# Demo 1: cpu_demo.py

```bash
python cpu_demo.py
```

What to watch:
- **Sequential**: Only 1 core at 100%
- **Parallel**: All cores at 100%

This is multiprocessing in action.

---

# Demo 2: finance_demo.py

```bash
python finance_demo.py
```

Monte Carlo VaR calculation:
- $1M portfolio, 10 assets
- 5 million simulations
- Sequential vs parallel

*"This is how banks calculate risk for Basel III requirements"*

---

# Demo 3: numba_demo.py

```bash
python numba_demo.py
```

Two examples:
1. **Option pricing** — Black-Scholes Monte Carlo
2. **Portfolio VaR** — with `parallel=True`

Watch the speedup numbers!

---

# Let's Try It Together

If you have Python + NumPy:

```python
from numba import njit
import numpy as np

@njit
def pi_monte_carlo(n):
    inside = 0
    for _ in range(n):
        x, y = np.random.random(), np.random.random()
        if x*x + y*y < 1:
            inside += 1
    return 4 * inside / n

# Try it!
print(pi_monte_carlo(10_000_000))
```

---

# Part 4: Project Work

---

# Project Deadline: January 11, 2026

**What to submit:**
- GitHub repository (`python main.py` must work!)
- ~10 page report (PDF)
- 10-15 minute video OR live presentation

**Live Presentation Option:**
- Present December 15 → no video needed
- Sign up by December 8

**Email to all TAs:**
- anna.smirnova@unil.ch
- francesco.brunamonti@unil.ch
- zhongshan.chen@unil.ch

---

# Should You Use Parallelism in Your Project?

**Maybe, if:**
- Downloading data from multiple sources
- Running many simulations
- Training is slow

**Probably not, if:**
- Code already runs fast enough
- Would add complexity for little gain

**Numba is the easiest win** — just add `@njit` to slow loops.

---

# Questions?

Now is a good time to:
- Ask about parallelism
- Ask about your project
- Work on your code

**I'm here to help!**

---

<!-- _class: lead -->

# Work Time

**Project deadline: January 11, 2026**

Ask questions as you work!
