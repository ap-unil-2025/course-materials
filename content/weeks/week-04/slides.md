---
marp: true
paginate: true
header: "Session 4: Contact Manager - Part 1"
footer: "Anna Smirnova, October 13, 2025"
style: |
  section {
    font-size: 22px;
  }
  section.lead {
    background: #003aff;
    color: white;
    font-size: 28px;
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
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }
---

<!-- _class: lead -->

# Session 4: Contact Manager - Part 1

**Building Your First Real Program**

---

# Welcome! 🚀

**Last sessions:**
- Git basics & GitHub workflow
- Python fundamentals review

**Today (Week 4):**
- Build Contact Manager from scratch
- Learn functions for organization
- Use lists to store multiple contacts
- Use dictionaries for structured data
- Maybe: simple recursion example

**Let's build something real together!**

---

# Quick Review: Nuvolos Environment Setup

**Important: You DO NOT need to create virtual environments!**

✅ **What you should do:** Use the **base** conda environment (already set up) - just start coding in Python files

❌ **What you should NOT do:** Don't create venv (virtual environments), don't create new conda environments, don't run `python -m venv`

**Why?** Nuvolos already has everything configured in the base environment. Creating additional environments can cause confusion and conflicts. **Just code in base - it's ready to go!**

---

# Quick Review: Running Python Files in VSCode

**1. Using the Play Button ▶️** - Open your `.py` file, click the play button (triangle) in top right, output appears in terminal below

**2. Using the Terminal**
```bash
python your_file.py    # or python3 your_file.py
```

**3. Right-click Method** - Right-click in your code, select "Run Python File in Terminal"

**Pro tip:** Use `print()` statements to see what your code is doing!

---

# What Are We Building Today?

**A Contact Manager Application**

Think of it like a simple phone contacts app:
- Store multiple contacts (name, phone, email)
- Add new contacts
- Search for contacts
- View all contacts
- Delete contacts

**Why this project?**
- Practical and relatable
- Teaches all the key concepts
- You can actually use it!

---

# The Problem: How to Store Multiple Contacts?

**Bad approach:**
```python
contact1_name = "Alice"
contact1_phone = "555-0001"

contact2_name = "Bob"
contact2_phone = "555-0002"

contact3_name = "Charlie"
contact3_phone = "555-0003"
```

**Problems:**
- What if we need 100 contacts?
- Hard to loop through them
- Hard to add/remove contacts

**We need a better way!**

---

# The Solution: Lists!

```python
# contact_manager.py
# Week 4: Building from scratch with proper data structures

contacts = []  # Can store unlimited contacts!

print("="*40)
print("  CONTACT MANAGER v1.0")
print("="*40)
```

**A list can hold many items - perfect for contacts!**

But wait... how do we store name AND phone for each contact?

**Answer: Dictionaries!**

---

# Understanding Dictionaries

**A dictionary stores key-value pairs:**

```python
# One contact as a dictionary
contact = {
    "name": "Alice Smith",
    "phone": "555-0001",
    "email": "alice@email.com"
}

# Access values by key
print(contact["name"])    # "Alice Smith"
print(contact["phone"])   # "555-0001"
```

**Perfect for structured data like contacts!**

---

# Combining Lists and Dictionaries

```python
# A list of dictionaries - our contact database!
contacts = [
    {"name": "Alice", "phone": "555-0001", "email": "alice@email.com"},
    {"name": "Bob", "phone": "555-0002", "email": "bob@email.com"}
]

# Loop through all contacts
for contact in contacts:
    print(f"{contact['name']}: {contact['phone']}")
```

**Output:**
```
Alice: 555-0001
Bob: 555-0002
```

**This is how real programs store data!**

---

# Building Functions: The Thought Process

**Before coding, ask:**
1. What is the function supposed to do?
2. What inputs does it need?
3. What should it return?
4. What are the steps to accomplish this?

**Let's apply this to adding a contact...**

---

# Feature 1: Add a Contact

**Goal:** Add a new contact to our list

**Inputs needed:**
- The list of contacts (where to add)
- Name (required)
- Phone (required)
- Email (optional - might be empty)

**What should happen:**
1. Create a contact dictionary with the data
2. Add it to the list
3. Give feedback to the user
4. Return the contact (so we can use it later)

**Question:** How do we know what ID to give the new contact?

---

# Add Contact: Step-by-Step Thinking

**Step 1: Create the contact**
- We need a dictionary
- Keys: "name", "phone", "email", "id"
- ID can be: current list length + 1 (why?)

**Step 2: Add to list**
- Use `.append()` to add to the end

**Step 3: User feedback**
- Print a message so user knows it worked

**Step 4: Return the contact**
- Why return it? So we can check what we added!

**Now YOU implement it in the starter template!**

---

# Problem: What About Duplicates?

**What happens if we add the same person twice?**
- We'd have duplicate contacts
- Confusing and wastes space

**Solution: Check before adding**

**How to check?**
1. Loop through existing contacts
2. Compare names (case-insensitive!)
3. If found, return True
4. If we finish the loop without finding, return False

**Why case-insensitive?**
- "Alice Smith" and "alice smith" are the same person!
- Use `.lower()` when comparing

---

# Building on Functions

**Good practice: Functions that use other functions**

**Pseudocode:**
```
function add_contact_safe:
    if contact_exists(name):
        print "Already exists!"
        return None
    else:
        call add_contact(name, phone, email)
        return the result
```

**Why separate functions?**
- `contact_exists()` can be reused elsewhere
- Each function has ONE job
- Easier to test and fix

---

# Feature 2: Search Contacts

**Goal:** Find contacts that match a search term

**Think about it:**
- User types "alice" → should find "Alice Smith"
- User types "555" → should find all numbers starting with 555
- Search should work for names AND phone numbers

**The algorithm:**
```
Create empty results list
Convert search term to lowercase (why?)

For each contact in the list:
    If search term is IN the name OR IN the phone:
        Add this contact to results

Return the results list
```

**Key insight:** Use `in` to check if one string is inside another!

---

# Feature 3: Display All Contacts

**Goal:** Show all contacts in a nice format

**Think about formatting:**
- Empty list? Show a message
- Otherwise, show each contact on its own line
- Make it readable!

**Pseudocode:**
```
function display_all_contacts:
    If list is empty:
        print "No contacts"
        return

    Print a header
    For each contact:
        Print name, phone, email in a nice format
```

**Tip:** Use f-strings for nice formatting!

---

# Feature 4: Delete Contact

**Goal:** Remove a contact by name

**The challenge:** How do we find AND remove?

**Approach:**
```
Loop through with enumerate (to get index):
    If this contact's name matches:
        Remove it using pop(index)
        Print success message
        return the removed contact

If we finish loop without finding:
    Print "not found"
    return None
```

**Why `enumerate`?** We need the index to use `pop()`!

---

# Understanding Imports

**What is an import?**
- Python has tons of useful code already written!
- `import` lets you use that code in your program
- Like getting tools from a toolbox

**What's a module?**
- A `.py` file with Python code
- Contains functions, variables, classes
- Examples: `json`, `math`, `random`

**What's a package?**
- A collection of related modules
- A folder with multiple `.py` files
- Example: `os`, `datetime`

---

# How Imports Work

**Option 1: Import the whole module**
```python
import json

# Now use it with the module name first:
json.dump(data, file)     # module.function()
json.load(file)           # module.function()
```

**Why the `json.` prefix?** Tells Python where the function comes from!

**Option 2: Import specific things**
```python
from json import dump, load

# Now use directly (no prefix needed):
dump(data, file)
load(file)
```

**Trade-off:** Shorter to type, but less clear where it came from.

---

# Common Import Examples

**Built-in modules you'll use:**

```python
import json              # For saving/loading data
import random            # For random numbers
import math              # For math functions
from datetime import datetime  # For dates/times
```

**How to call after importing:**
```python
import random
number = random.randint(1, 10)    # random.function()

from random import randint
number = randint(1, 10)           # function() directly
```

**Tip:** When starting, use `import module` - it's clearer!

---

# Bonus: Saving Data

**Why save?** So contacts don't disappear when program closes!

**JSON = JavaScript Object Notation**
- A standard way to store data
- Works with lists and dictionaries!

**The concept:**
```
To save:
    Open a file for writing
    Use json.dump() to write the list
    Close the file

To load:
    Open the file for reading
    Use json.load() to read the list
    Close the file
```

**Hint:** Use `try/except` to handle errors (file not found, etc.)

---

# Putting It Together

**What we covered today:**

1. **Functions** - Organize code into reusable pieces
2. **Lists** - Store multiple items
3. **Dictionaries** - Store structured data
4. **Combining them** - Build real programs!

**You now know how to build complete programs!**

---

# Your Practice Assignment

Download the starter template and implement:

**Core Features (do these first!):**
1. `add_contact()` - Add a contact to the list
2. `display_all_contacts()` - Show all contacts
3. `contact_exists()` - Check for duplicates

**Challenge Features (if time!):**
4. `search_contacts()` - Find contacts by name/phone
5. `delete_contact()` - Remove a contact
6. `save_contacts()` - Save to file

**Starter Template:**
[Download here](https://raw.githubusercontent.com/ap-unil-2025/course-materials/master/content/weeks/week-04/contact_manager_starter.py)

---

# Ideas to Extend (Optional!)

**Once you have the basics working, try:**

1. **Add more fields**
   - Birthday, address, notes...

2. **Better formatting**
   - Colors, tables, nicer output

3. **Input validation**
   - Check if phone number looks valid
   - Check if email has @ symbol

4. **Statistics**
   - Count total contacts
   - Count how many have emails

**Remember: Start simple, then add features!**

---

# Pro Tips from Today

<div class="columns">
<div>

**1. Start with data structure**
- We chose: list of dictionaries
- Why? Easy to search, sort, and extend

**2. Build incrementally**
- Start simple, add features one by one
- Test each feature before moving on

</div>
<div>

**3. Think about the user**
- Clear messages, handle errors gracefully
- Make it actually useful!

**4. Code organization**
- Use clear function and variable names
- One function = one job
- Add docstrings to explain what functions do

</div>
</div>

**Remember**: The best code is code that works and others can understand!

---

<!-- _class: lead -->

# Next Week (Week 5)

## Generative AI & Programming

**Topics:**
- How AI can help you code
- Prompt engineering basics
- Using AI as a learning tool
- Understanding AI-generated code
- When to use AI and when not to

**Week 6**: We'll learn OOP and refactor the Contact Manager!

See you next Monday! 🤖