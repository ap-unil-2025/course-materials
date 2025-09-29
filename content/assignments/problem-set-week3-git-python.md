---
layout: assignment
title: "Problem Set Week 3: Git & Python Fundamentals"
assignment_number: 103
github_classroom_url: "https://classroom.github.com/a/week3-git-python"
topics:
  - "Git version control"
  - "Python basics"
  - "Control flow"
  - "Functions"
  - "File I/O"
status: "closed"
difficulty: "Beginner"
estimated_time: "3-4 hours"
---

# Problem Set 3: Git & Python Fundamentals

## Objectives
- Practice essential Git commands and workflow
- Write Python programs using variables, control flow, and functions
- Handle user input and file operations
- Debug and test simple Python programs

## Setup Instructions

### Part 1: Git Setup (30 minutes)

1. **Accept the GitHub Classroom Assignment**
   ```bash
   # Click the GitHub Classroom link above
   # This will create your personal repository
   ```

2. **Clone Your Repository**
   ```bash
   git clone https://github.com/ap-unil-2025/ps3-YOUR-USERNAME.git
   cd ps3-YOUR-USERNAME
   ```

3. **Configure Git (if not already done)**
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@unil.ch"
   ```

4. **Create Required Files**
   ```bash
   touch README.md
   touch .gitignore
   touch problem1.py problem2.py problem3.py problem4.py
   ```

5. **Set Up .gitignore**
   Create a `.gitignore` file with:
   ```
   __pycache__/
   *.pyc
   .venv/
   venv/
   .DS_Store
   *.log
   test_outputs/
   ```

---

## Problems

### Problem 1: Git Workflow Practice

Complete the following Git tasks and document them in `git_log.txt`:

1. **Initial Commit**
   - Add README.md with your name and date
   - Commit with message: "Initial commit: Add README"

2. **Python File Commit**
   - Create `hello_git.py` with a simple print statement
   - Add and commit with message: "Add hello_git.py"

3. **Modification**
   - Modify `hello_git.py` to include your name
   - View the diff before committing
   - Commit with message: "Personalize hello message"

4. **Create Git Log**
   ```bash
   git log --oneline > git_log.txt
   git add git_log.txt
   git commit -m "Add git history"
   ```

**Deliverable**: Your repository should have at least 4 commits with clear messages.

---

### Problem 2: Temperature Converter

Create `problem2.py` with the following functions:

```python
def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32
    """
    # Your code here
    pass

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9
    """
    # Your code here
    pass

def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    # Your code here
    pass

# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    print("All tests passed!")

    # Run interactive converter
    temperature_converter()
```

**Requirements**:
- Handle invalid input gracefully
- Round results to 2 decimal places
- Support both uppercase and lowercase unit inputs

---

### Problem 3: Number Analysis

Create `problem3.py` with a program that analyzes a list of numbers:

```python
def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.
    """
    numbers = []
    # Your code here
    return numbers

def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers
    """
    if not numbers:
        return None

    analysis = {}
    # Your code here
    return analysis

def display_analysis(analysis):
    """
    Display the analysis in a formatted way.
    """
    # Your code here
    pass

def main():
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")

    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    analysis = analyze_numbers(numbers)
    display_analysis(analysis)

if __name__ == "__main__":
    main()
```

**Example Output**:
```
Number Analyzer
Enter numbers one at a time. Type 'done' when finished.
Enter a number: 5
Enter a number: 10
Enter a number: 3
Enter a number: 8
Enter a number: done

Analysis Results:
-----------------
Count: 4
Sum: 26
Average: 6.50
Minimum: 3
Maximum: 10
Even numbers: 2
Odd numbers: 2
```

---

### Problem 4: File Word Counter

Create `problem4.py` that processes text files:

```python
def create_sample_file(filename="sample.txt"):
    """
    Create a sample text file for testing.
    """
    content = """Python is a powerful programming language.
It is widely used in web development, data science, and automation.
Python's simple syntax makes it great for beginners.
Many companies use Python for their projects."""

    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")

def count_words(filename):
    """
    Count total words in the file.
    """
    # Your code here
    pass

def count_lines(filename):
    """
    Count total lines in the file.
    """
    # Your code here
    pass

def count_characters(filename, include_spaces=True):
    """
    Count characters in the file.
    If include_spaces is False, don't count spaces.
    """
    # Your code here
    pass

def find_longest_word(filename):
    """
    Find and return the longest word in the file.
    """
    # Your code here
    pass

def word_frequency(filename):
    """
    Return a dictionary of word frequencies.
    Convert words to lowercase and remove punctuation.
    """
    import string
    # Your code here
    pass

def analyze_file(filename):
    """
    Perform complete analysis of the file.
    """
    print(f"\nAnalyzing: {filename}")
    print("-" * 40)

    try:
        print(f"Lines: {count_lines(filename)}")
        print(f"Words: {count_words(filename)}")
        print(f"Characters (with spaces): {count_characters(filename, True)}")
        print(f"Characters (without spaces): {count_characters(filename, False)}")
        print(f"Longest word: {find_longest_word(filename)}")

        print("\nTop 5 most common words:")
        freq = word_frequency(filename)
        # Sort by frequency and get top 5
        top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
        for word, count in top_words:
            print(f"  '{word}': {count} times")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Create sample file
    create_sample_file()

    # Analyze the sample file
    analyze_file("sample.txt")

    # Allow user to analyze their own file
    print("\n" + "="*40)
    user_file = input("Enter a filename to analyze (or press Enter to skip): ").strip()
    if user_file:
        analyze_file(user_file)

if __name__ == "__main__":
    main()
```

**Expected Output for Sample File**:
```
Created sample.txt

Analyzing: sample.txt
----------------------------------------
Lines: 4
Words: 28
Characters (with spaces): 184
Characters (without spaces): 157
Longest word: programming

Top 5 most common words:
  'python': 3 times
  'is': 2 times
  'it': 2 times
  'for': 2 times
  'a': 1 times
```

---

## Bonus Challenge (Optional)

Create `bonus_password_generator.py` that generates secure passwords:

**Requirements:**
1. Create a function `generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)`
2. Build a character set based on the parameters
3. Ensure at least one character from each selected type appears in the password
4. Create a function `password_strength(password)` that rates password strength
5. Allow user to specify password length
6. Generate multiple password options for the user to choose from

**Example Output:**
```
Password Generator
------------------------------
Password length (default 12): 16

Generated Password: Kj9@mN#pL2xQ!vR4
Strength: Very Strong

Alternative passwords:
1. bT7$wE@nM3hK&zX9 (Very Strong)
2. pQ2!aF8#dG5*jL6m (Very Strong)
3. vN4@kR7$tY9#wS2x (Very Strong)
```

**Hints:**
- Use `string.ascii_lowercase`, `string.ascii_uppercase`, `string.digits`, `string.punctuation`
- Use `random.choice()` to select random characters
- Use `random.shuffle()` to mix the password
- Check password length, and presence of different character types for strength rating

---

## Submission Requirements

1. **Repository Structure**:
   ```
   ps3-YOUR-USERNAME/
   ├── README.md
   ├── .gitignore
   ├── git_log.txt
   ├── problem2.py
   ├── problem3.py
   ├── problem4.py
   ├── bonus_password_generator.py (optional)
   └── sample.txt (created by problem4.py)
   ```

2. **Testing Your Code**:
   ```bash
   python problem2.py
   python problem3.py
   python problem4.py
   python bonus_password_generator.py  # if completed
   ```

3. **Final Commit and Push**:
   ```bash
   git add .
   git commit -m "Complete Problem Set 3"
   git push origin main
   ```

## Assessment Notes

This is an **ungraded practice assignment** designed to help you learn Git and Python fundamentals. While not graded, completing these exercises is essential for building the skills needed in future weeks.

### Focus Areas:
- **Correctness**: Code should produce expected output
- **Code Quality**: Use clear variable names and proper indentation
- **Error Handling**: Gracefully handle invalid input
- **Git Usage**: Practice meaningful commits and proper repository structure

## Tips

1. **Start Early**: Give yourself time to debug and test
2. **Test Incrementally**: Test each function as you write it
3. **Use Print Statements**: Debug by printing intermediate values
4. **Read Error Messages**: Python error messages are helpful
5. **Commit Often**: Make regular commits as you progress

## Academic Integrity

This is an individual assignment. You may:
- Discuss concepts with classmates
- Use Python documentation and tutorials
- Ask for help on Discord

You may NOT:
- Copy code from other students
- Use AI to generate complete solutions
- Submit work that is not your own

Good luck! Remember, the goal is to learn by doing. If you get stuck, that's normal - debugging is part of programming!