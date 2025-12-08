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

# Part 3: Live Coding

*Open your laptops — we're coding together*

---

# Setup

Open a Python file or Jupyter notebook.

```python
import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
```

If you have Numba:
```python
from numba import njit
```

---

# Exercise 1: Simulate Slow Downloads

Let's pretend we're downloading stock data:

```python
import time

def download_stock(ticker):
    """Simulate downloading — takes 1 second"""
    time.sleep(1)
    return f"{ticker}: ${np.random.uniform(100, 500):.2f}"

tickers = ["AAPL", "GOOGL", "MSFT", "AMZN", "META", "NVDA"]
```

Try downloading sequentially. How long does it take?

```python
start = time.time()
for t in tickers:
    print(download_stock(t))
print(f"Time: {time.time() - start:.1f}s")
```

---

# Exercise 1: Now Parallelize It

```python
from concurrent.futures import ThreadPoolExecutor

start = time.time()
with ThreadPoolExecutor(max_workers=6) as pool:
    results = list(pool.map(download_stock, tickers))
for r in results:
    print(r)
print(f"Time: {time.time() - start:.1f}s")
```

How much faster? Why does this work even with the GIL?

---

# Exercise 2: CPU-Bound Work

Now let's try something CPU-intensive:

```python
def slow_sum(n):
    """Sum of squares — pure CPU work"""
    total = 0
    for i in range(n):
        total += i * i
    return total

# Try it
start = time.time()
results = [slow_sum(5_000_000) for _ in range(4)]
print(f"Sequential: {time.time() - start:.1f}s")
```

---

# Exercise 2: Try Threading

```python
start = time.time()
with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(lambda _: slow_sum(5_000_000), range(4)))
print(f"Threaded: {time.time() - start:.1f}s")
```

Is it faster? (Spoiler: no — GIL blocks CPU work)

---

# Exercise 2: Use Multiprocessing

```python
from concurrent.futures import ProcessPoolExecutor

def slow_sum_wrapper(n):
    return slow_sum(n)

start = time.time()
with ProcessPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(slow_sum_wrapper, [5_000_000]*4))
print(f"Parallel: {time.time() - start:.1f}s")
```

Now it's ~4x faster!

---

# Exercise 3: Numba

Same slow function, but with `@njit`:

```python
from numba import njit

@njit
def fast_sum(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

# First call compiles
fast_sum(100)

# Now time it
start = time.time()
result = fast_sum(50_000_000)  # 10x more iterations!
print(f"Numba: {time.time() - start:.3f}s")
```

---

# Exercise 4: Monte Carlo Pi

Classic example — estimate π by throwing darts:

```python
def pi_slow(n):
    inside = 0
    for _ in range(n):
        x = np.random.random()
        y = np.random.random()
        if x*x + y*y < 1:
            inside += 1
    return 4 * inside / n

start = time.time()
print(f"π ≈ {pi_slow(1_000_000)}")
print(f"Time: {time.time() - start:.2f}s")
```

---

# Exercise 4: Speed It Up

```python
@njit
def pi_fast(n):
    inside = 0
    for _ in range(n):
        x = np.random.random()
        y = np.random.random()
        if x*x + y*y < 1:
            inside += 1
    return 4 * inside / n

pi_fast(1000)  # Compile

start = time.time()
print(f"π ≈ {pi_fast(10_000_000)}")  # 10x more!
print(f"Time: {time.time() - start:.2f}s")
```

---

# Bonus: Watch btop

If you have time, open `btop` or Activity Monitor.

Run this and watch the cores:

```python
from concurrent.futures import ProcessPoolExecutor
import time

def burn_cpu(n):
    total = 0
    for i in range(50_000_000):
        total += i * i % 1000
    return total

with ProcessPoolExecutor(max_workers=4) as pool:
    list(pool.map(burn_cpu, range(4)))
```

All 4 cores should hit 100%!

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
