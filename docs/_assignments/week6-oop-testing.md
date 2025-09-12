---
layout: assignment
title: "Week 6: Object-Oriented Programming & Testing"
assignment_number: 6
due_date: 2025-11-03 23:59:00
points: 120
difficulty: "Intermediate-Advanced"
estimated_time: "6-7 hours"
topics:
  - "Object-Oriented Programming"
  - "Classes and Inheritance"
  - "Testing with pytest"
  - "Debugging Techniques"
  - "Program Efficiency"
status: "open"
---

## Overview

Master object-oriented programming principles, implement robust testing strategies, and optimize program efficiency. This assignment builds a complete library management system using OOP best practices.

## Learning Objectives

By completing this assignment, you will:

- Design and implement class hierarchies with inheritance
- Apply OOP principles (encapsulation, polymorphism, abstraction)
- Write comprehensive unit tests using pytest
- Debug complex programs systematically
- Optimize code for efficiency and performance

## Prerequisites

- Understanding of Python functions and data structures
- Basic knowledge of classes (covered in lecture)
- pytest installed (`pip install pytest`)

## Part 1: Building a Library Management System (40 points)

Create `library_system.py` implementing a complete OOP library system:

### 1.1 Base Media Class (10 points)

```python
class Media:
    """
    Abstract base class for all library media items.
    
    Attributes:
        - title: str
        - author: str
        - year: int
        - is_available: bool
        - isbn/issn: str (unique identifier)
    
    Methods:
        - checkout(): Mark as unavailable
        - return_item(): Mark as available
        - get_info(): Return formatted item information
        - __str__(): String representation
        - __eq__(): Equality comparison by ISBN/ISSN
    """
```

### 1.2 Derived Media Classes (15 points)

Implement at least three subclasses:

```python
class Book(Media):
    """Add pages, genre, edition attributes"""
    
class Magazine(Media):
    """Add issue_number, frequency attributes"""
    
class DigitalMedia(Media):
    """Add file_size, format, download_link attributes"""
```

### 1.3 Library Class (15 points)

```python
class Library:
    """
    Manages collection of media items.
    
    Features:
        - Add/remove items
        - Search by title, author, year
        - Check out/return items
        - Generate inventory reports
        - Track overdue items
        - Export catalog to JSON/CSV
    """
```

## Part 2: Member Management System (25 points)

Extend the system with member tracking:

### 2.1 Member Classes (15 points)

```python
class Member:
    """Base class for library members"""
    
class Student(Member):
    """Student members with borrowing limits"""
    
class Faculty(Member):
    """Faculty with extended privileges"""
    
class Guest(Member):
    """Limited access members"""
```

### 2.2 Borrowing System (10 points)

Implement:
- Borrowing limits by member type
- Due date calculation
- Fine calculation for overdue items
- Borrowing history tracking

## Part 3: Testing Suite (30 points)

Create `test_library_system.py` with comprehensive tests:

### 3.1 Unit Tests (15 points)

Write pytest tests for:
- Media class initialization and methods
- Library add/remove operations
- Search functionality
- Member registration and privileges

Example:
```python
def test_book_creation():
    book = Book("Python Crash Course", "Eric Matthes", 2019, 
                "978-1593279288", pages=544, genre="Programming")
    assert book.title == "Python Crash Course"
    assert book.is_available == True

def test_checkout_system():
    # Test checkout workflow
    pass
```

### 3.2 Integration Tests (10 points)

Test complete workflows:
- Member registers → searches catalog → checks out book → returns book
- Library generates reports with multiple items and members
- Overdue fine calculation across multiple members

### 3.3 Edge Cases & Error Handling (5 points)

Test:
- Invalid inputs (negative years, empty strings)
- Checking out unavailable items
- Member exceeding borrowing limit
- Duplicate ISBN/ISSN handling

## Part 4: Performance Optimization (15 points)

Create `library_optimizer.py`:

### 4.1 Search Optimization (8 points)

Implement efficient search using:
- Indexing by common search fields
- Caching frequent searches
- Binary search for sorted collections

### 4.2 Performance Profiling (7 points)

- Profile your code using cProfile
- Identify bottlenecks
- Document optimization strategies
- Compare before/after performance

## Part 5: Advanced Features (10 points)

Choose ONE to implement:

### Option A: Recommendation System
- Suggest books based on borrowing history
- Find similar items by genre/author
- Popular items tracking

### Option B: Reservation System
- Queue for unavailable items
- Notification when available
- Priority by member type

### Option C: Data Persistence
- Save/load library state to database
- Transaction logging
- Backup and restore functionality

## Submission Requirements

Submit these files:
1. `library_system.py` - Core OOP implementation
2. `test_library_system.py` - Complete test suite
3. `library_optimizer.py` - Optimized version
4. `performance_report.md` - Performance analysis (1-2 pages)
5. `README.md` - Setup and usage instructions

### Directory Structure
```
week6_assignment/
├── library_system.py
├── test_library_system.py
├── library_optimizer.py
├── performance_report.md
├── README.md
└── sample_data.json (optional)
```

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| **OOP Design** | 40 | Proper inheritance, encapsulation, clean interfaces |
| **Member System** | 25 | Complete implementation with all member types |
| **Testing** | 30 | Coverage >80%, edge cases handled |
| **Optimization** | 15 | Measurable performance improvements |
| **Advanced Feature** | 10 | Complete, working implementation |
| **Total** | 120 | |

### Deductions
- No docstrings: -5 points
- Poor code organization: -5 points
- Tests not passing: -10 points
- Missing type hints: -3 points

## Testing Your Code

Run tests:
```bash
pytest test_library_system.py -v
pytest --cov=library_system test_library_system.py  # Coverage report
```

Profile performance:
```bash
python -m cProfile -s cumulative library_optimizer.py
```

## Hints and Tips

1. **Start with the base classes** - Get Media and Member working first
2. **Use `@property` decorators** for controlled attribute access
3. **Implement `__repr__` and `__str__`** for debugging
4. **Test incrementally** - Write tests as you implement features
5. **Use inheritance wisely** - Don't force inheritance where composition works better
6. **Consider using `dataclasses`** for simpler class definitions
7. **Profile before optimizing** - Don't guess what's slow

## Common Pitfalls to Avoid

- Don't modify class attributes directly - use methods
- Remember to handle edge cases in your tests
- Don't optimize prematurely - make it work first
- Avoid circular imports between modules
- Don't forget to test error conditions

## Resources

- [Python OOP Tutorial](https://realpython.com/python3-object-oriented-programming/)
- [pytest Documentation](https://docs.pytest.org/)
- [Python Profiling Guide](https://docs.python.org/3/library/profile.html)
- [Clean Code in Python](https://realpython.com/python-clean-code/)

## Questions?

Post on the course forum or attend office hours. Start early to leave time for testing and optimization!