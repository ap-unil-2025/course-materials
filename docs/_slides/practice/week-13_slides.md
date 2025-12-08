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

**Part 1: Why Parallelism?**
- CPU-bound vs I/O-bound tasks
- GIL and its implications

**Part 2: Threading**
- Creating threads
- Synchronization with locks
- ThreadPoolExecutor

**Part 3: Multiprocessing**
- When to use processes vs threads
- ProcessPoolExecutor

**Part 4: Project Work Time**

---

# Part 1: Why Parallelism?

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

**Threading:**
- Great for I/O-bound tasks
- Use `ThreadPoolExecutor` for clean code
- Watch out for race conditions → use locks

**Multiprocessing:**
- Required for CPU-bound speedups
- Use `ProcessPoolExecutor`
- Higher overhead than threading

**Project advice:**
- Focus on correctness first
- Only optimize if needed
- Document any parallelism used

---

<!-- _class: lead -->

# Questions?

**Project deadline: January 11, 2026**

Good luck with your projects!
