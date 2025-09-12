---
marp: true
theme: unil-theme
paginate: true
backgroundColor: #f5f9ff
header: "Session 3: Contact Manager - Part 1"
footer: "Anna Smirnova, October 6, 2025"
---

<!-- _class: lead -->

# Session 3: Contact Manager - Part 1

**Building the Foundation with Python Basics**

---

# Our 3-Week Project Journey 🚀

**Week 3 (Today)**: Foundation
- Variables and basic data
- Control flow (if/else)
- Loops for repetition
- String manipulation
- Simple contact storage

**Week 4**: Power Features
- Functions for organization
- Lists and dictionaries
- File save/load
- Professional structure

**Week 6**: Going Pro
- Classes and objects
- Error handling
- Debugging techniques

**Let's build something real!**

---

# Project Setup: Simple Contact Storage

```python
# contact_manager_v1.py
# Week 3: Building the foundation

print("="*40)
print("  CONTACT MANAGER v0.1 (Basic)")
print("="*40)

# We'll build this step by step!
```

**Follow along - create this file now!**

---

# Part 1: Storing Contact Data

---

# Variables for One Contact

```python
# Store a single contact's information
# TODO: Create variables for:
# - contact_name (string)
# - contact_phone (string)  
# - contact_age (integer)
# - is_favorite (boolean)

# TODO: Print a welcome message using the contact's name

# TODO: Calculate and print their age next year
```

**Try it yourself first!**

---

# Getting User Input

```python
# Let's make it interactive!
print("\n--- Add New Contact ---")

# TODO: Get contact information from user
# Remember: input() always returns a string!

contact_name = input("Enter contact name: ")
# TODO: Get phone number
# TODO: Get age (hint: convert to int!)
# TODO: Ask if favorite (y/n)

# TODO: Display the contact info nicely
```

**Common mistake**: Forgetting to convert input to numbers!

---

# Building a Contact Display

```python
# Format contact information nicely
contact_name = "Alice Smith"
contact_phone = "555-0001"
contact_age = 25
is_favorite = True

# TODO: Create a formatted display string
# Should look like:
# =====================================
# Contact: Alice Smith
# Phone: 555-0001
# Age: 25 years old
# Favorite: Yes
# =====================================

# Hint: Use string concatenation or f-strings
```

---

# Part 2: Making Decisions

---

# Add Contact Validation

```python
# Validate contact information before storing
contact_name = input("Enter name: ")
contact_phone = input("Enter phone: ")

# TODO: Check if name is not empty
# If empty, print error and set to "Unknown"

# TODO: Check if phone has at least 7 digits
# If too short, print warning

# TODO: Only mark as valid contact if both checks pass
```

**Real programs validate input!**

---

# Contact Categories with If/Elif/Else

```python
# Categorize contacts by age
contact_age = int(input("Contact's age: "))

# TODO: Determine category:
# - Under 18: "Minor"
# - 18-30: "Young Adult"
# - 31-60: "Adult"
# - Over 60: "Senior"

# TODO: Print category and special notes
# E.g., "Minor - Requires parental consent"
```

**Think about the order of conditions!**

---

# Menu System with Conditions

```python
print("\n--- Contact Manager Menu ---")
print("1. Add contact")
print("2. View contact")
print("3. Exit")

choice = input("\nChoose option: ")

# TODO: Use if/elif/else to handle menu choices
# - If "1": Print "Adding contact..."
# - If "2": Print "Viewing contact..."
# - If "3": Print "Goodbye!"
# - Else: Print "Invalid option!"
```

**This is the start of our interface!**

---

# Part 3: Storing Multiple Contacts

---

# Using Loops for Multiple Contacts

```python
# Store up to 3 contacts
max_contacts = 3
contact_count = 0

print(f"\nYou can add up to {max_contacts} contacts")

# TODO: Use a while loop to:
# - Keep asking for contacts until max_contacts reached
# - Or until user types "done"
# - Track how many contacts added

# TODO: After loop, print summary
# "Added X contacts to your manager"
```

---

# Display All Contacts with For Loop

```python
# Simulate having 3 contacts
# (Next week we'll use lists for this!)
contact1_name = "Alice"
contact2_name = "Bob"
contact3_name = "Charlie"

print("\n--- All Contacts ---")

# TODO: Use a for loop with range(3) to:
# - Print contact number (1, 2, 3)
# - Print contact name
# Format: "Contact #1: Alice"

# Hint: You'll need if/elif to pick the right variable
```

**Preview: Lists will make this much easier!**

---

# Search Contacts with String Methods

```python
# Search for a contact
contact1_name = "Alice Smith"
contact2_name = "Bob Jones"
contact3_name = "Charlie Smith"

search_term = input("Search for: ")

# TODO: Check each contact name
# - Convert both to lowercase for case-insensitive search
# - Use 'in' to check if search_term is in name
# - Print matching contacts

# Example: Searching for "smith" finds Alice and Charlie
```

---

# Part 4: String Formatting

---

# Format Contact Cards

```python
# Create nice contact cards
name = "Alice Smith"
phone = "555-0001"
age = 25

# TODO: Create a contact card using f-strings:
# ╔════════════════════════════╗
# ║  CONTACT CARD              ║
# ║  Name: Alice Smith         ║
# ║  Phone: 555-0001           ║
# ║  Age: 25                   ║
# ╚════════════════════════════╝

# Hint: Use f-strings for formatting
# card = f"Name: {name}"
```

**Make it look professional!**

---

# String Operations for Contacts

```python
contact_name = "  alice SMITH  "
contact_phone = "5550001"

# TODO: Clean up the contact data:
# - Remove extra spaces with strip()
# - Capitalize name properly with title()
# - Format phone as "555-0001"

# TODO: Validate the cleaned data:
# - Check if name has at least 2 characters
# - Check if phone has exactly 7 digits
```

**Clean data is happy data!**

---

# Build a Complete Mini Contact Manager

```python
# Put it all together!
print("\n" + "="*40)
print("  CONTACT MANAGER v0.1")
print("="*40)

running = True
contact_count = 0
max_contacts = 3

while running:
    # TODO: Show menu
    # TODO: Get user choice
    # TODO: Handle each option:
    #   1. Add contact (if not at max)
    #   2. View all contacts
    #   3. Search contacts
    #   4. Exit
    
    pass  # Remove this when you add code

print("Thank you for using Contact Manager!")
```

**This is your Week 3 project!**

---

# Challenge: Add Features

**Enhance your Contact Manager:**

1. **Contact Counter**: Show "X of 3 contacts used"

2. **Duplicate Check**: Don't add same name twice

3. **Phone Formatting**: Auto-format as XXX-XXXX

4. **Favorite Marking**: Mark contacts with ⭐

5. **Statistics**: Show total contacts, favorites count

**Try these on your own!**

---

# What We Built Today

## Contact Manager v0.1 ✅

**Features implemented:**
- ✅ Store contact information
- ✅ Input validation
- ✅ Menu system
- ✅ Add multiple contacts
- ✅ Search by name
- ✅ Display all contacts
- ✅ Nice formatting

**Skills learned:**
- Variables and data types
- User input
- If/else decisions
- Loops (for and while)
- String manipulation
- Basic program structure

**Next week: We'll make it powerful with functions and lists!**

---

# Homework: Extend Your Contact Manager

**Required features to add:**

1. **Contact limit**: Maximum 10 contacts
2. **Delete contact**: Remove by name
3. **Update contact**: Change phone number
4. **Contact types**: Friend/Family/Work
5. **Pretty display**: Numbered list with formatting

**Bonus challenges:**
- Sort contacts alphabetically
- Export to text file (we'll learn this properly next week)
- Birthday tracking (calculate age)

**Submit on GitHub!**

---

# Pro Tips from Week 3

**1. Start simple**
```python
# Build step by step, test each part
```

**2. Use meaningful names**
```python
# Bad: n, p, a
# Good: contact_name, phone_number, age
```

**3. Validate input**
```python
# Always check user input before using it
```

**4. Test edge cases**
```python
# What if user enters nothing?
# What if they enter invalid data?
```

**Remember**: Every expert was once a beginner!

---

<!-- _class: lead -->

# Next Week

## Contact Manager Part 2

**We'll add:**
- Functions to organize code
- Lists to store unlimited contacts
- Dictionaries for better data structure
- File save/load capability
- Professional code organization

**Bring your Week 3 code!**

See you next Monday! 🚀






