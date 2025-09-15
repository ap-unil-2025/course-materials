---
layout: assignment
title: "Problem Set Week 12: High-Performance Computing"
assignment_number: 112
due_date: 2025-12-08 23:59:00
difficulty: "Advanced"
estimated_time: "6-7 hours"
github_classroom_url: "https://classroom.github.com/a/rT7pN3mQ-ps-week12"
topics:
  - "Parallel programming"
  - "GPU computing"
  - "Vectorization"
  - "Memory optimization"
  - "Distributed computing"
status: "active"
description: "Accelerate Python code to production-level performance using HPC techniques"
---

# Problem Set 12: High-Performance Computing in Python

Time to make Python fast! This week you'll learn to accelerate code from seconds to microseconds.

## Exercise 1: CPU Optimization Techniques 🚀

Transform slow Python into blazing-fast code!

### Part A: NumPy Vectorization (25 points)
Replace loops with vectorized operations:

```python
import numpy as np
import time

class MatrixOperations:
    @staticmethod
    def slow_matrix_multiply(A, B):
        """Naive triple-loop matrix multiplication"""
        n, m = A.shape
        m2, p = B.shape
        C = np.zeros((n, p))
        for i in range(n):
            for j in range(p):
                for k in range(m):
                    C[i,j] += A[i,k] * B[k,j]
        return C
    
    @staticmethod
    def vectorized_matrix_multiply(A, B):
        """Vectorized matrix multiplication"""
        # TODO: Implement using NumPy operations
        pass
    
    @staticmethod
    def slow_distance_matrix(points):
        """Calculate pairwise distances slowly"""
        n = len(points)
        distances = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                distances[i,j] = np.sqrt(sum((points[i] - points[j])**2))
        return distances
    
    @staticmethod
    def vectorized_distance_matrix(points):
        """Vectorized pairwise distance calculation"""
        # TODO: Use broadcasting for efficiency
        pass
    
    @staticmethod
    def benchmark(func, *args, runs=100):
        """Benchmark function performance"""
        times = []
        for _ in range(runs):
            start = time.perf_counter()
            func(*args)
            times.append(time.perf_counter() - start)
        return {
            'mean': np.mean(times),
            'std': np.std(times),
            'min': np.min(times),
            'max': np.max(times)
        }
```

### Part B: Numba JIT Compilation (30 points)
Compile Python to machine code:

```python
from numba import jit, njit, prange, cuda
import numpy as np

class NumbaAcceleration:
    @staticmethod
    def slow_mandelbrot(height, width, max_iter=256):
        """Calculate Mandelbrot set slowly"""
        result = np.zeros((height, width))
        for i in range(height):
            for j in range(width):
                c = complex(-2 + 3*j/width, -1 + 2*i/height)
                z = 0
                for n in range(max_iter):
                    if abs(z) > 2:
                        result[i,j] = n
                        break
                    z = z*z + c
        return result
    
    @staticmethod
    @njit(parallel=True)
    def fast_mandelbrot(height, width, max_iter=256):
        """JIT-compiled Mandelbrot with parallelization"""
        # TODO: Implement with Numba decorators
        # TODO: Use prange for parallel loops
        pass
    
    @staticmethod
    @njit
    def monte_carlo_pi(n_samples):
        """Estimate π using Monte Carlo"""
        # TODO: Fast random sampling
        # TODO: Count points inside circle
        pass
    
    @staticmethod
    @njit(parallel=True)
    def parallel_statistics(data):
        """
        Calculate statistics in parallel:
        - Mean, variance, skewness, kurtosis
        - Percentiles
        - Correlation matrix
        """
        # TODO: Implement parallel statistics
        pass
```

### Part C: Cython Implementation (30 points)
Write C-speed Python extensions:

```python
# save as matrix_ops.pyx
import numpy as np
cimport numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def fast_convolution(np.ndarray[double, ndim=2] image,
                     np.ndarray[double, ndim=2] kernel):
    """
    Fast 2D convolution using Cython
    """
    cdef int h = image.shape[0]
    cdef int w = image.shape[1]
    cdef int kh = kernel.shape[0]
    cdef int kw = kernel.shape[1]
    cdef int i, j, m, n
    cdef double s
    
    # TODO: Implement efficient convolution
    pass

@cython.boundscheck(False)
def fast_edit_distance(str s1, str s2):
    """
    Levenshtein distance with Cython
    """
    # TODO: Dynamic programming implementation
    pass

# Setup.py for compilation
from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    ext_modules=cythonize("matrix_ops.pyx"),
    include_dirs=[numpy.get_include()]
)
```

### Part D: Memory Optimization (15 points)
```python
class MemoryOptimizer:
    @staticmethod
    def profile_memory(func):
        """Decorator to profile memory usage"""
        import tracemalloc
        def wrapper(*args, **kwargs):
            tracemalloc.start()
            result = func(*args, **kwargs)
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            print(f"Current: {current/1024/1024:.2f} MB")
            print(f"Peak: {peak/1024/1024:.2f} MB")
            return result
        return wrapper
    
    @staticmethod
    def optimize_dataframe(df):
        """
        Reduce pandas DataFrame memory usage:
        - Downcast numeric types
        - Convert strings to categories
        - Use sparse arrays
        """
        # TODO: Implement memory optimization
        pass
```

## Exercise 2: GPU Computing with CUDA 🎮

Harness the power of thousands of cores!

### Part A: CuPy - NumPy on GPU (25 points)
```python
import cupy as cp
import numpy as np

class GPUArrayOperations:
    @staticmethod
    def gpu_matrix_operations():
        """
        Implement on GPU:
        - Matrix multiplication
        - Element-wise operations
        - Reductions (sum, mean, etc.)
        """
        # TODO: Use CuPy for GPU operations
        pass
    
    @staticmethod
    def gpu_fft(signal):
        """Fast Fourier Transform on GPU"""
        # TODO: Implement GPU FFT
        pass
    
    @staticmethod
    def benchmark_gpu_vs_cpu(operation, size):
        """
        Compare GPU vs CPU performance:
        - Data transfer overhead
        - Computation time
        - Total time
        """
        # TODO: Comprehensive benchmark
        pass
```

### Part B: Custom CUDA Kernels (35 points)
Write raw CUDA kernels:

```python
from numba import cuda
import numpy as np

class CUDAKernels:
    @staticmethod
    @cuda.jit
    def vector_add_kernel(a, b, c):
        """CUDA kernel for vector addition"""
        idx = cuda.grid(1)
        if idx < a.size:
            c[idx] = a[idx] + b[idx]
    
    @staticmethod
    @cuda.jit
    def matrix_multiply_kernel(A, B, C):
        """
        Tiled matrix multiplication kernel:
        - Use shared memory
        - Coalesced memory access
        - Minimize global memory reads
        """
        # TODO: Implement tiled matmul
        pass
    
    @staticmethod
    @cuda.jit
    def reduction_kernel(input_array, output):
        """
        Parallel reduction (sum):
        - Tree-based reduction
        - Shared memory optimization
        """
        # TODO: Implement reduction
        pass
    
    @staticmethod
    def launch_kernel(kernel, data, threads_per_block=256):
        """Configure and launch CUDA kernel"""
        # TODO: Calculate grid dimensions
        # TODO: Transfer data to GPU
        # TODO: Launch kernel
        # TODO: Synchronize and return
        pass
```

### Part C: Deep Learning on GPU (40 points)
Accelerate neural networks:

```python
class GPUNeuralNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.weights = []
        self.biases = []
        self._init_on_gpu()
    
    @cuda.jit
    def forward_kernel(input_data, weights, bias, output, activation):
        """GPU kernel for forward pass"""
        # TODO: Parallel forward propagation
        pass
    
    @cuda.jit
    def backward_kernel(grad_output, weights, input_data, grad_weights, grad_input):
        """GPU kernel for backpropagation"""
        # TODO: Parallel gradient computation
        pass
    
    def train_on_gpu(self, X, y, epochs=100, batch_size=32):
        """
        GPU-accelerated training:
        - Batch processing on GPU
        - Parallel gradient updates
        - Optimized memory transfers
        """
        # TODO: Implement GPU training
        pass
    
    def benchmark_speedup(self, cpu_nn):
        """Compare GPU vs CPU training time"""
        # TODO: Measure speedup
        pass
```

## Exercise 3: Parallel & Distributed Computing 🌐

Scale across multiple cores and machines!

### Part A: Multiprocessing & Threading (30 points)
```python
import multiprocessing as mp
import threading
import concurrent.futures
from queue import Queue

class ParallelProcessor:
    @staticmethod
    def parallel_map(func, data, n_workers=None):
        """
        Parallel map implementation:
        - Use multiprocessing.Pool
        - Handle chunking
        - Aggregate results
        """
        # TODO: Implement parallel map
        pass
    
    @staticmethod
    def producer_consumer_pattern(producers, consumers, queue_size=100):
        """
        Implement producer-consumer:
        - Multiple producer threads
        - Multiple consumer threads
        - Thread-safe queue
        """
        # TODO: Producer-consumer pattern
        pass
    
    @staticmethod
    def parallel_monte_carlo(simulation_func, n_simulations, n_processes=None):
        """
        Run Monte Carlo simulations in parallel:
        - Distribute simulations
        - Combine results
        - Calculate statistics
        """
        # TODO: Parallel Monte Carlo
        pass
    
    @staticmethod
    def parallel_hyperparameter_search(model, param_grid, cv_folds=5):
        """
        Parallel grid search for ML:
        - Distribute parameter combinations
        - Parallel cross-validation
        - Find best parameters
        """
        # TODO: Parallel hyperparameter tuning
        pass
```

### Part B: Dask - Distributed DataFrames (35 points)
```python
import dask.dataframe as dd
import dask.array as da
from dask.distributed import Client

class DaskComputing:
    def __init__(self):
        self.client = Client(n_workers=4, threads_per_worker=2)
    
    def process_large_dataset(self, filepath):
        """
        Process dataset larger than RAM:
        - Read in chunks
        - Parallel processing
        - Out-of-core computation
        """
        # TODO: Dask DataFrame operations
        pass
    
    def distributed_ml_training(self, X, y):
        """
        Train ML model on distributed data:
        - Distributed preprocessing
        - Parallel model training
        - Aggregate predictions
        """
        # TODO: Distributed ML
        pass
    
    def parallel_image_processing(self, image_paths):
        """
        Process thousands of images:
        - Lazy loading
        - Parallel transformations
        - Efficient storage
        """
        # TODO: Dask delayed operations
        pass
```

### Part C: Ray - Distributed Computing (35 points)
```python
import ray

@ray.remote
class DistributedWorker:
    def __init__(self, worker_id):
        self.worker_id = worker_id
        self.data = None
    
    def load_data(self, data_chunk):
        """Load data partition"""
        self.data = data_chunk
    
    def process(self):
        """Process data partition"""
        # TODO: Worker processing logic
        pass

class RayDistributed:
    def __init__(self, n_workers=4):
        ray.init()
        self.workers = [DistributedWorker.remote(i) for i in range(n_workers)]
    
    def distributed_training(self, model_class, data):
        """
        Distributed model training:
        - Data parallelism
        - Model parallelism
        - Parameter server
        """
        # TODO: Implement distributed training
        pass
    
    def parallel_hyperparameter_tuning(self):
        """Use Ray Tune for hyperparameter search"""
        # TODO: Ray Tune implementation
        pass
```

## Exercise 4: Performance Profiling & Optimization 📊

Profile and optimize real applications!

### Part A: Profiling Tools (25 points)
```python
class PerformanceProfiler:
    @staticmethod
    def profile_code(func):
        """
        Comprehensive profiling:
        - Time profiling (cProfile)
        - Memory profiling (memory_profiler)
        - Line profiling (line_profiler)
        """
        import cProfile
        import pstats
        from memory_profiler import profile
        
        # TODO: Implement profiling decorator
        pass
    
    @staticmethod
    def visualize_profile(profile_data):
        """
        Create visualizations:
        - Flame graphs
        - Call graphs
        - Memory timeline
        """
        # TODO: Profile visualization
        pass
    
    @staticmethod
    def identify_bottlenecks(code):
        """
        Automatic bottleneck detection:
        - Hot spots
        - Memory leaks
        - I/O bounds
        """
        # TODO: Bottleneck analysis
        pass
```

### Part B: Optimization Case Studies (40 points)
Optimize real-world scenarios:

```python
class OptimizationCases:
    @staticmethod
    def optimize_web_scraper(urls):
        """
        Speed up web scraping:
        - Async requests (aiohttp)
        - Connection pooling
        - Parallel processing
        - Caching
        """
        # TODO: Optimized scraper
        pass
    
    @staticmethod
    def optimize_data_pipeline(input_file, transformations):
        """
        ETL pipeline optimization:
        - Streaming processing
        - Parallel transformations
        - Memory-efficient operations
        - Optimized I/O
        """
        # TODO: Fast data pipeline
        pass
    
    @staticmethod
    def optimize_ml_inference(model, batch_data):
        """
        Production ML optimization:
        - Model quantization
        - Batch processing
        - GPU inference
        - Result caching
        """
        # TODO: Fast inference
        pass
```

### Part C: Benchmark Suite (35 points)
```python
class BenchmarkSuite:
    def __init__(self):
        self.results = {}
    
    def benchmark_numpy_operations(self):
        """
        Benchmark NumPy operations:
        - Different array sizes
        - Various operations
        - Memory vs compute bound
        """
        # TODO: NumPy benchmarks
        pass
    
    def benchmark_parallel_scaling(self):
        """
        Test parallel scaling:
        - Strong scaling (fixed problem size)
        - Weak scaling (fixed size per processor)
        - Amdahl's Law validation
        """
        # TODO: Scaling analysis
        pass
    
    def generate_report(self):
        """
        Generate performance report:
        - Speedup graphs
        - Efficiency metrics
        - Recommendations
        """
        # TODO: Report generation
        pass
```

## Real-World HPC Project 🏭

Choose ONE production-level project:

### Option A: Real-Time Video Processing
```python
class VideoProcessor:
    """
    Process video streams in real-time:
    - GPU-accelerated filters
    - Parallel frame processing
    - Stream optimization
    """
    pass
```

### Option B: Large-Scale Data Analytics
```python
class BigDataAnalytics:
    """
    Analyze TB-scale datasets:
    - Distributed processing
    - Incremental algorithms
    - Result aggregation
    """
    pass
```

### Option C: Scientific Simulation
```python
class ParticleSimulator:
    """
    N-body particle simulation:
    - GPU acceleration
    - Spatial indexing
    - Parallel collision detection
    """
    pass
```

## Bonus Challenges 🌟

### Challenge 1: Custom Memory Pool (30 points)
```python
class MemoryPool:
    """
    Implement memory pool for zero-copy operations:
    - Pre-allocated buffers
    - Lock-free allocation
    - Memory recycling
    """
    pass
```

### Challenge 2: SIMD Operations (30 points)
```python
class SIMDOperations:
    """
    Use SIMD instructions:
    - Vector operations
    - Packed arithmetic
    - CPU intrinsics
    """
    pass
```

### Challenge 3: Distributed Training (30 points)
```python
class DistributedDL:
    """
    Multi-GPU deep learning:
    - Data parallelism
    - Model parallelism
    - Gradient aggregation
    """
    pass
```

## Performance Targets 🎯

Your implementations should achieve:
- **10x speedup** with NumPy vectorization
- **100x speedup** with Numba JIT
- **1000x speedup** with GPU acceleration
- **Linear scaling** up to 8 cores
- **Sub-second** processing for GB-scale data

## Submission Requirements

Your submission should include:
1. `cpu_optimization.py` - CPU acceleration techniques
2. `gpu_computing.py` - CUDA/GPU implementations
3. `parallel_computing.py` - Multiprocessing/distributed
4. `profiling.py` - Performance analysis tools
5. `benchmarks/` - Benchmark results and graphs
6. `hpc_project/` - Your chosen project
7. `README.md` - Performance analysis and insights

## Grading Rubric

- **Performance Gains (40%)**: Achieving speedup targets
- **Implementation Quality (25%)**: Correct, efficient code
- **Benchmarking (20%)**: Thorough performance analysis
- **Documentation (15%)**: Clear explanations of optimizations

## Tips for Success

1. **Profile First**: Never optimize without profiling
2. **Measure Everything**: Track time, memory, and resources
3. **Start Simple**: Optimize incrementally
4. **Avoid Premature Optimization**: Focus on bottlenecks
5. **Test Correctness**: Fast but wrong is useless

## Common Pitfalls

- Forgetting Amdahl's Law limitations
- Not accounting for data transfer overhead
- Race conditions in parallel code
- Memory leaks in long-running processes
- Ignoring cache effects

## Resources

- [High Performance Python](https://www.oreilly.com/library/view/high-performance-python/9781492055013/)
- [CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)
- [Dask Documentation](https://docs.dask.org/)
- [Numba Documentation](https://numba.readthedocs.io/)

## Fun Facts 🤓

- Modern GPUs have >10,000 cores
- Top supercomputers exceed 1 exaFLOP (10^18 operations/second)
- Python's GIL doesn't affect multiprocessing
- NumPy operations release the GIL
- A single GPU can outperform 100 CPU cores for parallel tasks

Remember: The best optimization is often a better algorithm, but when you need speed, HPC delivers! ⚡