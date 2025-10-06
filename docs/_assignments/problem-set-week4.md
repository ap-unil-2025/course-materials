---
layout: assignment
title: "Problem Set 4: Lists, Dictionaries, Functions & Imports"
assignment_number: 104
github_classroom_url: "https://classroom.github.com/a/oPeViRDp"
topics:
  - "Lists and list operations"
  - "Dictionaries and nested structures"
  - "Functions"
  - "JSON imports and file I/O"
  - "Recursion (bonus)"
status: "open"
difficulty: "Beginner to Intermediate"
estimated_time: "3-4 hours"
---

# Problem Set 4: Lists, Dictionaries, Functions & Imports

## Overview

This assignment focuses on working with Python data structures (lists and dictionaries), writing functions, using imports, and exploring basic recursion.

**GitHub Classroom Link:** [Accept Assignment](https://classroom.github.com/a/oPeViRDp)

## Learning Objectives

- Master list operations and comprehensions
- Work with dictionaries and nested data structures
- Write functions that process collections
- Use Python modules (json, random, etc.)
- Understand basic recursion concepts

## Assignment Structure

This problem set consists of 4 required problems and 1 optional bonus problem:

### Problem 1: List Operations (8 functions)
Practice working with Python lists - creating, modifying, filtering, and transforming them.

**Functions to implement:**
- `create_number_list(start, end)` - Create a list of numbers
- `filter_even_numbers(numbers)` - Filter even numbers
- `square_numbers(numbers)` - Square each number
- `find_max_min(numbers)` - Find maximum and minimum
- `remove_duplicates(items)` - Remove duplicates while preserving order
- `merge_lists(list1, list2)` - Merge two lists alternating elements
- `list_statistics(numbers)` - Calculate statistics (sum, average, count, etc.)
- `chunk_list(items, chunk_size)` - Split list into chunks

### Problem 2: Dictionary Operations (9 functions)
Practice working with Python dictionaries - creating, accessing, modifying, and nesting them.

**Functions to implement:**
- `create_student_record(name, age, major, gpa)` - Create a student dictionary
- `get_value_safely(dictionary, key, default)` - Safe dictionary access
- `merge_dictionaries(dict1, dict2)` - Merge two dictionaries
- `count_word_frequency(text)` - Count word frequency in text
- `invert_dictionary(dictionary)` - Swap keys and values
- `filter_dictionary(dictionary, keys_to_keep)` - Filter dictionary by keys
- `group_by_first_letter(words)` - Group words by first letter
- `calculate_grades_average(students)` - Calculate grade averages
- `nested_dict_access(data, keys)` - Access nested dictionary values

### Problem 3: Mini Contact Manager (9 functions)
Build a simple contact manager using lists and dictionaries - combines all concepts from Problems 1 & 2.

**Functions to implement:**
- `create_contact(name, phone, email)` - Create a contact dictionary
- `add_contact(contacts, name, phone, email)` - Add contact to list
- `find_contact_by_name(contacts, name)` - Find contact by name
- `search_contacts(contacts, search_term)` - Search by name or phone
- `delete_contact(contacts, name)` - Remove a contact
- `count_contacts_with_email(contacts)` - Count contacts with email
- `get_all_phone_numbers(contacts)` - Extract all phone numbers
- `sort_contacts_by_name(contacts)` - Sort contacts alphabetically
- `contact_exists(contacts, name)` - Check if contact exists

### Problem 4: Data Persistence with JSON (9 functions)
Learn to use Python modules (imports) and save data to files using JSON.

**Functions to implement:**
- `save_to_json(data, filename)` - Save data to JSON file
- `load_from_json(filename)` - Load data from JSON file
- `save_contacts_to_file(contacts, filename)` - Save contacts to JSON
- `load_contacts_from_file(filename)` - Load contacts from JSON
- `append_contact_to_file(contact, filename)` - Add contact to existing file
- `backup_file(source_filename, backup_filename)` - Create backup copy
- `get_file_stats(filename)` - Get file statistics
- `merge_json_files(file1, file2, output_file)` - Merge two JSON files
- `search_json_file(filename, key, value)` - Search JSON file

### Bonus: Introduction to Recursion (8 functions - Optional)
Learn about recursive functions - functions that call themselves!

**Functions to implement:**
- `factorial(n)` - Calculate factorial recursively
- `countdown(n)` - Print countdown using recursion
- `sum_list(numbers)` - Sum list recursively
- `fibonacci(n)` - Calculate Fibonacci number
- `power(base, exponent)` - Calculate power recursively
- `reverse_string(text)` - Reverse string recursively
- `count_down_list(n)` - Create countdown list
- `flatten_list(nested_list)` - Flatten nested list

## Getting Started

1. **Accept the assignment** using the GitHub Classroom link above
2. **Clone your repository** to your local machine or Nuvolos
3. **Complete each problem** in its respective file (`problem1.py`, `problem2.py`, etc.)
4. **Test your solutions** by running each file: `python problem1.py`
5. **Commit and push** your work regularly

## Testing Your Code

Each problem file includes built-in test cases. Run them with:
```bash
python problem1.py
python problem2.py
python problem3.py
python problem4.py
python bonus_recursion.py  # if completed
```

For automated testing:
```bash
pip install pytest
pytest test_assignment.py -v
```

## Submission

Push your completed code to your GitHub repository:
```bash
git add .
git commit -m "Complete Problem Set 4"
git push origin main
```

GitHub Actions will automatically run tests on your code.

## Tips for Success

- **Start early** - Give yourself time to debug
- **Test incrementally** - Test each function as you write it
- **Use print statements** - Debug by printing intermediate values
- **Read error messages** - They tell you what went wrong
- **Ask for help** - Use Discord or office hours if stuck

## Resources

- [Python Functions Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [JSON Module Documentation](https://docs.python.org/3/library/json.html)
- Week 4 Lesson Guide
- Week 4 Practice Slides

## Academic Integrity

This is an **individual assignment**. You may:
- Use Python documentation
- Discuss concepts with classmates
- Ask questions on Discord

You may NOT:
- Copy code from other students
- Use AI to generate complete solutions
- Submit work that is not your own

## Assessment

This is an ungraded practice assignment designed to build your programming skills. Focus on understanding concepts rather than just getting tests to pass.

Good luck! Remember: struggling with problems is part of learning to code.
