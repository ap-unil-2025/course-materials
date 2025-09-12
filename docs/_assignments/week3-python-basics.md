---
layout: assignment
title: "Week 3: Python Basics & Control Flow"
assignment_number: 3
due_date: 2025-10-06 23:59:00
points: 100
difficulty: "Beginner"
estimated_time: "4-5 hours"
topics:
  - "Variables and data types"
  - "Control flow (if/else, loops)"
  - "String manipulation"
  - "Basic input/output"
status: "open"
---

## Overview

Practice fundamental Python programming concepts including variables, control flow structures, and string manipulation. This assignment reinforces the concepts covered in Week 3 lectures.

## Learning Objectives

By completing this assignment, you will:

- Master Python's basic data types (int, float, str, bool)
- Implement control flow with if/else statements and loops
- Practice string manipulation techniques
- Handle user input and format output
- Apply programming best practices and style guidelines

## Part 1: Variable Manipulation (20 points)

Create a Python script `variables_practice.py` that demonstrates:

1. **Type Conversion** (10 points)
   - Convert between int, float, and string types
   - Handle potential conversion errors gracefully
   - Demonstrate understanding of type checking with `isinstance()`

2. **Variable Scoping** (10 points)
   - Show the difference between local and global variables
   - Demonstrate variable shadowing
   - Use the `global` keyword appropriately

## Part 2: Control Flow Challenges (30 points)

Create `control_flow.py` with the following functions:

1. **FizzBuzz Variation** (10 points)
   ```python
   def custom_fizzbuzz(n, div1=3, div2=5, word1="Fizz", word2="Buzz"):
       """
       Customizable FizzBuzz from 1 to n
       Returns a list of results
       """
       # Your implementation here
   ```

2. **Pattern Printer** (10 points)
   ```python
   def print_pattern(n, pattern_type="triangle"):
       """
       Print various patterns based on type:
       - triangle: right-angled triangle of stars
       - diamond: diamond shape with stars
       - pyramid: centered pyramid
       """
       # Your implementation here
   ```

3. **Number Guessing Game** (10 points)
   ```python
   def guessing_game(max_num=100, max_attempts=7):
       """
       Interactive number guessing game
       Returns True if player wins, False otherwise
       """
       # Your implementation here
   ```

## Part 3: String Manipulation (25 points)

Create `string_operations.py` with:

1. **Palindrome Checker** (8 points)
   - Check if a string is a palindrome (ignore case and spaces)
   - Handle both regular and phrase palindromes

2. **Word Statistics** (9 points)
   - Count words, characters, and sentences in a text
   - Find the most common words
   - Calculate average word length

3. **Text Formatter** (8 points)
   - Convert between camelCase, snake_case, and kebab-case
   - Implement title case with proper article handling
   - Create a simple text wrapper (line breaks at word boundaries)

## Part 4: Practical Application (25 points)

Create a **Simple Calculator** program (`calculator.py`) that:

1. **Basic Operations** (10 points)
   - Addition, subtraction, multiplication, division
   - Handle division by zero
   - Support decimal numbers

2. **Advanced Features** (10 points)
   - Memory functions (store, recall, clear)
   - History of last 10 calculations
   - Parentheses support (bonus: +5 points)

3. **User Interface** (5 points)
   - Clear menu system
   - Input validation
   - Helpful error messages

## Submission Requirements

Your submission should include:

```
week3-assignment/
├── variables_practice.py
├── control_flow.py
├── string_operations.py
├── calculator.py
├── test_solutions.py  # Basic tests for your functions
└── README.md          # Brief description of your approach
```

## Testing Your Code

We provide a test file to help you verify your solutions:

```bash
python test_solutions.py
```

All tests should pass before submission.

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Correctness | 60 | Functions work as specified |
| Code Style | 15 | Follows PEP 8, meaningful variable names |
| Documentation | 15 | Clear comments and docstrings |
| Error Handling | 10 | Graceful handling of edge cases |

## Tips for Success

- Start early and test frequently
- Use meaningful variable and function names
- Add comments to explain complex logic
- Test edge cases (empty strings, zero, negative numbers)
- Ask for help during office hours if stuck

## Resources

- [Python Official Tutorial - Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [String Methods Documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

---

*Due: {{ page.due_date | date: "%B %d, %Y at %I:%M %p" }} • Points: {{ page.points }} • Difficulty: {{ page.difficulty }}*