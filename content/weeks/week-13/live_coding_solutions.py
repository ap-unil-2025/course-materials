"""
Session 13: Live Coding SOLUTIONS
Keep this open on your second monitor.
"""

import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# =============================================================================
# EXERCISE 1: Slow Downloads (I/O-bound)
# =============================================================================

def download_stock(ticker):
    """Simulate downloading — takes 1 second"""
    time.sleep(1)
    return f"{ticker}: ${np.random.uniform(100, 500):.2f}"


# =============================================================================
# EXERCISE 2: CPU-Bound Work
# =============================================================================

def slow_sum(n):
    """Sum of squares — pure CPU work"""
    total = 0
    for i in range(n):
        total += i * i
    return total


# =============================================================================
# EXERCISE 5: Option Pricing (finance example)
# =============================================================================

def price_option(args):
    """Monte Carlo option pricing"""
    S, K, T, r, sigma, n_sims = args
    total = 0.0
    for _ in range(n_sims):
        Z = np.random.randn()
        ST = S * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)
        total += max(ST - K, 0)
    return np.exp(-r * T) * total / n_sims


# =============================================================================
# BONUS: Max out all cores
# =============================================================================

def burn_cpu(x):
    total = 0
    for i in range(50_000_000):
        total += i * i % 1000
    return total


# =============================================================================
# MAIN - Required for ProcessPoolExecutor on macOS/Windows
# =============================================================================

if __name__ == '__main__':
    tickers = ["AAPL", "GOOGL", "MSFT", "AMZN", "META", "NVDA"]

    # Sequential version
    print("=== Exercise 1: Sequential ===")
    start = time.time()
    for t in tickers:
        print(download_stock(t))
    print(f"Time: {time.time() - start:.1f}s")  # ~6 seconds

    # SOLUTION: ThreadPoolExecutor
    print("\n=== Exercise 1: Parallel ===")
    start = time.time()
    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(download_stock, tickers))
    for r in results:
        print(r)
    print(f"Time: {time.time() - start:.1f}s")  # ~1 second

    # Sequential version
    print("\n=== Exercise 2: Sequential ===")
    start = time.time()
    results = [slow_sum(5_000_000) for _ in range(4)]
    print(f"Time: {time.time() - start:.1f}s")  # ~X seconds

    # SOLUTION 1: ThreadPoolExecutor (doesn't help!)
    print("\n=== Exercise 2: Threaded ===")
    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(slow_sum, [5_000_000]*4))
    print(f"Time: {time.time() - start:.1f}s")  # Same time! GIL blocks it.

    # SOLUTION 2: ProcessPoolExecutor (works!)
    print("\n=== Exercise 2: Multiprocessing ===")
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(slow_sum, [5_000_000]*4))
    print(f"Time: {time.time() - start:.1f}s")  # ~4x faster

    # =============================================================================
    # EXERCISE 3: Numba
    # =============================================================================

    from numba import njit

    @njit
    def fast_sum(n):
        total = 0.0  # Use float to avoid integer overflow
        for i in range(n):
            total += i * i
        return total

    print("\n=== Exercise 3: Numba ===")
    fast_sum(100)  # Warmup / compile
    start = time.time()
    result = fast_sum(50_000_000)  # 10x more iterations!
    print(f"Result: {result}")
    print(f"Time: {time.time() - start:.3f}s")  # ~0.02s

    # =============================================================================
    # EXERCISE 4: Monte Carlo Pi
    # =============================================================================

    def estimate_pi_slow(n):
        inside = 0
        for _ in range(n):
            x = np.random.random()
            y = np.random.random()
            if x*x + y*y < 1:
                inside += 1
        return 4 * inside / n

    print("\n=== Exercise 4: Slow Pi ===")
    start = time.time()
    pi = estimate_pi_slow(1_000_000)
    print(f"π ≈ {pi:.6f}")
    print(f"Time: {time.time() - start:.2f}s")

    # SOLUTION: with @njit
    @njit
    def estimate_pi_fast(n):
        inside = 0
        for _ in range(n):
            x = np.random.random()
            y = np.random.random()
            if x*x + y*y < 1:
                inside += 1
        return 4 * inside / n

    print("\n=== Exercise 4: Fast Pi ===")
    estimate_pi_fast(1000)  # Warmup
    start = time.time()
    pi = estimate_pi_fast(10_000_000)  # 10x more!
    print(f"π ≈ {pi:.6f}")
    print(f"Time: {time.time() - start:.2f}s")

    # Price one option
    print("\n=== Exercise 5: Single Option ===")
    start = time.time()
    price = price_option((100, 100, 1.0, 0.05, 0.2, 1_000_000))
    print(f"Option price: ${price:.2f}")
    print(f"Time: {time.time() - start:.2f}s")

    # SOLUTION: Price 8 options in parallel
    print("\n=== Exercise 5: 8 Options Parallel ===")
    strikes = [80, 85, 90, 95, 100, 105, 110, 115]
    args_list = [(100, K, 1.0, 0.05, 0.2, 1_000_000) for K in strikes]

    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as pool:
        prices = list(pool.map(price_option, args_list))

    for K, p in zip(strikes, prices):
        print(f"Strike ${K}: ${p:.2f}")
    print(f"Time: {time.time() - start:.2f}s")

    # =============================================================================
    # EXERCISE 6: Numba Parallel (prange)
    # =============================================================================

    from numba import prange

    @njit(parallel=True)
    def estimate_pi_parallel(n):
        inside = 0
        for _ in prange(n):  # prange instead of range!
            x = np.random.random()
            y = np.random.random()
            if x*x + y*y < 1:
                inside += 1
        return 4 * inside / n

    print("\n=== Exercise 6: Numba Parallel ===")
    estimate_pi_parallel(1000)  # Warmup
    start = time.time()
    pi = estimate_pi_parallel(100_000_000)  # 100 million!
    print(f"π ≈ {pi:.6f}")
    print(f"Time: {time.time() - start:.2f}s")

    print("\n=== Bonus: Watch btop ===")
    print("Starting... watch your CPU monitor!")
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as pool:
        list(pool.map(burn_cpu, range(4)))
    print(f"Done! Time: {time.time() - start:.1f}s")
