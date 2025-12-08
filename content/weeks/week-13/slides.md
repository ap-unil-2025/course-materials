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

# Session 13: Multithreading & Parallelization

**Making Python Go Fast**

---

# Today's Goals

**Part 1: Why Parallelism Matters Now**
- The end of the "free lunch"
- CPU-bound vs I/O-bound tasks
- GIL and its implications

**Part 2: Threading**
- ThreadPoolExecutor for I/O-bound tasks

**Part 3: Multiprocessing**
- ProcessPoolExecutor for CPU-bound tasks

**Part 4: Numba**
- JIT compilation for numeric code

**Part 5: Live Demo & Project Time**

---

# Part 1: Why Parallelism Matters Now

---

# The End of the "Free Lunch"

For decades, software got faster automatically:
- **1970s-2005**: Clock speeds doubled every ~18 months
- Your same code ran 2x faster on next year's CPU

**Then it stopped.** Around 2005:
- Heat and power limits hit
- Single-core speed plateaued at ~4 GHz

**The solution?** More cores, not faster cores.

| Year | Typical Desktop | Cores |
|------|-----------------|-------|
| 2005 | Pentium 4       | 1     |
| 2010 | Core i5         | 4     |
| 2024 | Apple M3 / Ryzen| 8-16  |

---

# The New Reality

**Your laptop has 8+ cores.** Most Python code uses **1**.

```
Core 1: [████████████████████] 100%
Core 2: [                    ] 0%
Core 3: [                    ] 0%
Core 4: [                    ] 0%
Core 5: [                    ] 0%
Core 6: [                    ] 0%
Core 7: [                    ] 0%
Core 8: [                    ] 0%
```

**Modern fast software uses parallelism:**
- Web browsers (Chrome uses 1 process per tab)
- Video encoding (FFmpeg parallelizes across cores)
- Machine learning (PyTorch/TensorFlow parallelize training)
- Databases (PostgreSQL parallelizes queries)

---

# The Problem

```python
# This takes 10 seconds
for url in urls:  # 10 URLs
    download(url)  # 1 second each
```

**Sequential execution**: One thing at a time

What if we could do multiple things at once?

```python
# This could take ~1 second
for url in urls:
    start_download(url)  # All start together
wait_for_all()
```

---

# Two Types of Tasks

**I/O-bound** — waiting for external resources:
- Network requests (APIs, web scraping)
- File operations (reading/writing)
- Database queries
- User input

**CPU-bound** — doing calculations:
- Number crunching
- Image processing
- Machine learning training
- Data transformations

**Threading** works great for I/O-bound tasks
**Multiprocessing** needed for CPU-bound tasks

---

# The GIL (Global Interpreter Lock)

Python's "one thread at a time" rule for CPU operations

```python
# Even with 4 threads, only 1 runs Python code at a time
thread1: [===    ===    ===]
thread2: [   ===    ===    ]
thread3: [      ===      ===]
```

**Why?** Memory safety in CPython

**Impact:**
- Threading won't speed up CPU-bound code
- Threading WILL speed up I/O-bound code (waiting doesn't need GIL)
- Use multiprocessing for CPU-bound parallelism

---

# Part 2: Threading

---

# Creating a Simple Thread

```python
import threading
import time

def say_hello(name):
    time.sleep(1)
    print(f"Hello, {name}!")

# Create a thread
thread = threading.Thread(target=say_hello, args=("World",))

# Start the thread
thread.start()

# Wait for it to complete
thread.join()

print("Done!")
```

Output:
```
Hello, World!
Done!
```

---

# Multiple Threads

```python
import threading
import time

def download_file(filename):
    print(f"Starting download: {filename}")
    time.sleep(2)  # Simulate download
    print(f"Finished download: {filename}")

files = ["file1.txt", "file2.txt", "file3.txt"]

# Create threads
threads = []
for f in files:
    t = threading.Thread(target=download_file, args=(f,))
    threads.append(t)
    t.start()

# Wait for all to complete
for t in threads:
    t.join()

print("All downloads complete!")
```

---

# Timing Comparison

```python
import time

# Sequential
start = time.time()
for f in files:
    download_file(f)
print(f"Sequential: {time.time() - start:.1f}s")  # ~6 seconds

# Parallel with threads
start = time.time()
threads = [threading.Thread(target=download_file, args=(f,))
           for f in files]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Threaded: {time.time() - start:.1f}s")  # ~2 seconds
```

**3x speedup** for I/O-bound tasks!

---

# The Problem: Race Conditions

```python
counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1  # NOT atomic!

threads = [threading.Thread(target=increment) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)  # Expected: 400000, Actual: ??? (random!)
```

**Why?** `counter += 1` is actually:
1. Read counter
2. Add 1
3. Write counter

Threads can interleave these steps!

---

# Solution: Locks

```python
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        lock.acquire()
        try:
            counter += 1
        finally:
            lock.release()

# Or using context manager (preferred):
def increment_safe():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1
```

Now `counter` is always 400000!

---

# ThreadPoolExecutor (Recommended)

```python
from concurrent.futures import ThreadPoolExecutor
import time

def fetch_url(url):
    time.sleep(1)  # Simulate network request
    return f"Data from {url}"

urls = ["url1", "url2", "url3", "url4", "url5"]

# Use a pool of 3 workers
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(fetch_url, urls)

for result in results:
    print(result)
```

**Benefits:**
- Manages thread lifecycle automatically
- Limits concurrent threads
- Clean API

---

# ThreadPoolExecutor with submit()

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_item(item):
    time.sleep(item)
    return f"Processed {item}"

items = [3, 1, 2]

with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit returns Future objects
    futures = {executor.submit(process_item, i): i for i in items}

    # Process results as they complete
    for future in as_completed(futures):
        item = futures[future]
        result = future.result()
        print(f"{item}: {result}")
```

Output (in completion order):
```
1: Processed 1
2: Processed 2
3: Processed 3
```

---

# Part 3: Multiprocessing

---

# When Threads Aren't Enough

```python
import time

def cpu_intensive(n):
    """Calculate sum of squares (CPU-bound)"""
    return sum(i*i for i in range(n))

# Threading won't help here!
numbers = [10_000_000] * 4

start = time.time()
results = [cpu_intensive(n) for n in numbers]
print(f"Sequential: {time.time() - start:.1f}s")

# With threads - same time (GIL!)
```

Need **multiprocessing** for CPU-bound tasks.

---

# ProcessPoolExecutor

```python
from concurrent.futures import ProcessPoolExecutor
import time

def cpu_intensive(n):
    return sum(i*i for i in range(n))

numbers = [10_000_000] * 4

# Sequential
start = time.time()
results = [cpu_intensive(n) for n in numbers]
print(f"Sequential: {time.time() - start:.1f}s")  # ~8s

# Parallel with processes
start = time.time()
with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(cpu_intensive, numbers))
print(f"Parallel: {time.time() - start:.1f}s")  # ~2s
```

**4x speedup** on 4 cores!

---

# Threads vs Processes: Summary

| | Threading | Multiprocessing |
|---|-----------|-----------------|
| **Best for** | I/O-bound | CPU-bound |
| **GIL** | Limited by GIL | Bypasses GIL |
| **Memory** | Shared | Separate (copied) |
| **Overhead** | Low | Higher |
| **Communication** | Easy | Needs serialization |

**Rule of thumb:**
- Waiting for something? → Threads
- Crunching numbers? → Processes

---

# Practical Example: Web Scraping

```python
from concurrent.futures import ThreadPoolExecutor
import requests

def fetch_page(url):
    response = requests.get(url, timeout=10)
    return len(response.content)

urls = [
    "https://python.org",
    "https://github.com",
    "https://stackoverflow.com",
]

# Fetch all pages concurrently
with ThreadPoolExecutor(max_workers=5) as executor:
    sizes = list(executor.map(fetch_page, urls))

for url, size in zip(urls, sizes):
    print(f"{url}: {size:,} bytes")
```

---

# Practical Example: Batch Processing

```python
from concurrent.futures import ProcessPoolExecutor
import pandas as pd

def process_chunk(df_chunk):
    # Heavy computation on each chunk
    df_chunk['new_col'] = df_chunk['value'].apply(expensive_calc)
    return df_chunk

# Split large DataFrame into chunks
chunks = np.array_split(df, 4)

# Process chunks in parallel
with ProcessPoolExecutor(max_workers=4) as executor:
    processed = list(executor.map(process_chunk, chunks))

# Combine results
result = pd.concat(processed)
```

---

# Part 4: Numba — JIT Compilation

---

# The Third Option: Make Python Faster

So far we've seen:
- **Threading**: Good for I/O-bound (limited by GIL for CPU)
- **Multiprocessing**: Good for CPU-bound (but has overhead)

**What if we could make Python itself faster?**

Enter **Numba**: Just-In-Time (JIT) compilation

```python
from numba import njit

@njit  # This one decorator changes everything
def fast_function(x):
    ...
```

Numba compiles Python to **native machine code** at runtime.

---

# Numba Example: 50x Speedup

```python
import numpy as np
from numba import njit

def slow_sum_squares(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

@njit
def fast_sum_squares(n):
    total = 0
    for i in range(n):
        total += i * i
    return total
```

```python
%timeit slow_sum_squares(10_000_000)  # ~800ms
%timeit fast_sum_squares(10_000_000)  # ~15ms (first run compiles)
%timeit fast_sum_squares(10_000_000)  # ~15ms (cached)
```

**Same code, 50x faster** — just add `@njit`

---

# How Numba Works

**Just-In-Time Compilation:**

1. First call: Numba infers types from arguments
2. Compiles to optimized machine code via LLVM
3. Caches the compiled code
4. Subsequent calls use cached fast version

```python
@njit
def add(a, b):
    return a + b

add(1, 2)      # Compiles for (int, int) → int
add(1.0, 2.0)  # Compiles again for (float, float) → float
add(1, 2)      # Uses cached (int, int) version
```

**Limitation**: Numba needs to infer types. Works best with:
- NumPy arrays
- Simple numeric types
- Loops (where Python is slowest!)

---

# Numba: What Works and What Doesn't

**Works great:**
```python
@njit
def monte_carlo_pi(n):
    inside = 0
    for _ in range(n):
        x, y = np.random.random(), np.random.random()
        if x*x + y*y < 1:
            inside += 1
    return 4 * inside / n
```

**Doesn't work** (falls back to slow Python):
```python
@njit
def bad_example(data):
    return pandas.DataFrame(data)  # Pandas not supported

@njit
def also_bad(items):
    return [x for x in items if x > 0]  # List comprehensions limited
```

Stick to NumPy and simple loops for best results.

---

# Numba + Parallelism: Best of Both Worlds

```python
from numba import njit, prange

@njit(parallel=True)
def parallel_sum(arr):
    total = 0
    for i in prange(len(arr)):  # prange = parallel range
        total += arr[i]
    return total
```

**`prange`** automatically parallelizes loop iterations across cores!

This combines:
- JIT compilation speed
- Automatic parallelization
- No GIL issues (Numba releases it)

**Result**: Near-C performance with Python syntax.

---

# Part 5: Live Demo

---

# Live Demo: Watch Your Cores Light Up

Let's see parallelism in action with `btop`/`htop`:

**Demo 1: Sequential (1 core busy)**
```python
# All work on one core
for i in range(4):
    cpu_intensive_task()
```

**Demo 2: Multiprocessing (all cores busy)**
```python
# Work spread across cores
with ProcessPoolExecutor(max_workers=4) as ex:
    ex.map(cpu_intensive_task, range(4))
```

Open `btop` or `htop` in another terminal to watch!

---

# Demo Code: cpu_demo.py

```python
"""Run this and watch btop/htop to see cores light up!"""
from concurrent.futures import ProcessPoolExecutor
import time

def cpu_work(n):
    """Burn CPU for a few seconds"""
    total = 0
    for i in range(50_000_000):
        total += i * i % 1000
    return total

if __name__ == "__main__":
    print("Sequential (watch: 1 core at 100%)...")
    start = time.time()
    for _ in range(4):
        cpu_work(0)
    print(f"Sequential: {time.time() - start:.1f}s\n")

    print("Parallel (watch: 4 cores at 100%)...")
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as ex:
        list(ex.map(cpu_work, range(4)))
    print(f"Parallel: {time.time() - start:.1f}s")
```

---

# Part 6: Project Work

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

# Should You Use Parallelism?

**Maybe, if:**
- You're fetching data from multiple sources
- Processing many files
- Training takes a long time

**Probably not if:**
- Your code already runs fast enough
- You're not I/O or CPU bound
- It would complicate your code significantly

**Remember:** Working code > Fast code

---

# Key Takeaways

**Why parallelism now?**
- Single-core speed has plateaued since ~2005
- Modern CPUs have many cores; use them!

**Threading** → I/O-bound (network, files, APIs)
**Multiprocessing** → CPU-bound (number crunching)
**Numba** → Make numeric Python code 50x faster

**For your projects:**
- Focus on correctness first
- Only optimize if needed
- Numba is easiest win for numeric loops

---

<!-- _class: lead -->

# Questions?

**Project deadline: January 11, 2026**

Good luck with your projects!
