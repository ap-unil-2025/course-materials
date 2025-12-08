#!/usr/bin/env python3
"""
Numba JIT Compilation Demo - See the speedup!

This script demonstrates how adding @njit can make Python code
run 50x faster (or more) with zero algorithmic changes.

Usage:
    pip install numba  # if not installed
    python numba_demo.py
"""

import time
import numpy as np

try:
    from numba import njit, prange
    NUMBA_AVAILABLE = True
except ImportError:
    NUMBA_AVAILABLE = False
    print("Numba not installed. Run: pip install numba")
    print("Showing pure Python version only.\n")


# =============================================================================
# Example 1: Simple loop - sum of squares
# =============================================================================

def sum_squares_python(n):
    """Pure Python version"""
    total = 0
    for i in range(n):
        total += i * i
    return total


if NUMBA_AVAILABLE:
    @njit
    def sum_squares_numba(n):
        """Numba JIT version - same code, just decorated"""
        total = 0
        for i in range(n):
            total += i * i
        return total


# =============================================================================
# Example 2: Monte Carlo Pi estimation
# =============================================================================

def monte_carlo_pi_python(n):
    """Estimate Pi using random points - Pure Python"""
    inside = 0
    for _ in range(n):
        x = np.random.random()
        y = np.random.random()
        if x*x + y*y < 1:
            inside += 1
    return 4 * inside / n


if NUMBA_AVAILABLE:
    @njit
    def monte_carlo_pi_numba(n):
        """Estimate Pi using random points - Numba version"""
        inside = 0
        for _ in range(n):
            x = np.random.random()
            y = np.random.random()
            if x*x + y*y < 1:
                inside += 1
        return 4 * inside / n


# =============================================================================
# Example 3: Numba with automatic parallelization
# =============================================================================

if NUMBA_AVAILABLE:
    @njit(parallel=True)
    def monte_carlo_pi_parallel(n):
        """Estimate Pi - Numba with automatic parallelization"""
        inside = 0
        for _ in prange(n):  # prange = parallel range
            x = np.random.random()
            y = np.random.random()
            if x*x + y*y < 1:
                inside += 1
        return 4 * inside / n


def time_function(func, arg, warmup=True):
    """Time a function call, with optional warmup for JIT"""
    if warmup:
        func(1000)  # Warmup call to trigger compilation

    start = time.time()
    result = func(arg)
    elapsed = time.time() - start
    return elapsed, result


def main():
    print("="*60)
    print(" NUMBA JIT COMPILATION DEMO")
    print("="*60)

    # Example 1: Sum of squares
    print("\n[Example 1: Sum of Squares]")
    print("-" * 40)
    n = 10_000_000

    t_python, _ = time_function(sum_squares_python, n, warmup=False)
    print(f"Pure Python:  {t_python*1000:.1f} ms")

    if NUMBA_AVAILABLE:
        t_numba, _ = time_function(sum_squares_numba, n)
        print(f"Numba @njit:  {t_numba*1000:.1f} ms")
        print(f"Speedup:      {t_python/t_numba:.0f}x faster!")

    # Example 2: Monte Carlo Pi
    print("\n[Example 2: Monte Carlo Pi Estimation]")
    print("-" * 40)
    n = 5_000_000

    t_python, pi_python = time_function(monte_carlo_pi_python, n, warmup=False)
    print(f"Pure Python:  {t_python:.2f}s  (π ≈ {pi_python:.6f})")

    if NUMBA_AVAILABLE:
        t_numba, pi_numba = time_function(monte_carlo_pi_numba, n)
        print(f"Numba @njit:  {t_numba:.2f}s  (π ≈ {pi_numba:.6f})")
        print(f"Speedup:      {t_python/t_numba:.0f}x faster!")

    # Example 3: Parallel Numba
    if NUMBA_AVAILABLE:
        print("\n[Example 3: Numba + Automatic Parallelization]")
        print("-" * 40)
        n = 50_000_000

        t_numba, pi = time_function(monte_carlo_pi_numba, n)
        print(f"Numba @njit:           {t_numba:.2f}s  (π ≈ {pi:.6f})")

        t_parallel, pi = time_function(monte_carlo_pi_parallel, n)
        print(f"Numba parallel=True:   {t_parallel:.2f}s  (π ≈ {pi:.6f})")
        print(f"Parallel speedup:      {t_numba/t_parallel:.1f}x faster!")

    # Summary
    print("\n" + "="*60)
    print(" KEY TAKEAWAYS")
    print("="*60)
    print("""
1. @njit decorator: Same Python code, 50-100x faster
2. Works best with: loops, NumPy arrays, numeric code
3. First call compiles (slow), subsequent calls are fast
4. parallel=True + prange: automatic multi-core execution
5. Limitation: doesn't work with pandas, complex objects
""")


if __name__ == "__main__":
    main()
