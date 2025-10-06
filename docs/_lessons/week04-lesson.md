---
layout: lesson
title: "Functions & Data Structures"
week: 4
date: 2025-10-06
type: "programming"
topics:
  - Functions and code organization
  - Lists for storing collections
  - Dictionaries for structured data
  - Building real programs
slides: "/slides/practice/week04_slides.html"
summary: "Learn to build real programs using functions, lists, and dictionaries through a hands-on Contact Manager project."
---

# Functions & Data Structures

This lesson teaches you how to build real, useful programs by organizing code with functions and storing data with lists and dictionaries.

## Learning Objectives

By the end of this lesson, you will:

- Write functions to organize and reuse code
- Use lists to store multiple items
- Use dictionaries to store structured data
- Combine lists and dictionaries for real programs
- Build a complete Contact Manager application

## Why Build a Contact Manager?

A Contact Manager is:
- **Practical**: Like a real phone contacts app
- **Relatable**: Everyone understands contacts
- **Complete**: Uses all the key concepts
- **Extensible**: Easy to add features

## Functions: Organizing Your Code

### What Are Functions?

Functions are reusable blocks of code that:
- Perform specific tasks
- Can take inputs (parameters)
- Can return outputs
- Make code organized and maintainable

```python
def add_contact(contacts_list, name, phone, email=""):
    """Add a new contact to our list"""
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "id": len(contacts_list) + 1
    }

    contacts_list.append(contact)
    print(f"✓ Added {name} to contacts")
    return contact
```

### Key Function Concepts

**1. Parameters and Arguments**
```python
# Parameters: name, phone, email
# email has a default value of ""
def add_contact(contacts_list, name, phone, email=""):
    pass

# Calling with arguments:
add_contact(contacts, "Alice", "555-0001", "alice@email.com")
add_contact(contacts, "Bob", "555-0002")  # email uses default
```

**2. Return Values**
```python
def contact_exists(contacts_list, name):
    """Check if contact already exists"""
    for contact in contacts_list:
        if contact["name"].lower() == name.lower():
            return True  # Found it!
    return False  # Not found
```

**3. Docstrings**
```python
def search_contacts(contacts_list, search_term):
    """
    Find contacts by name or phone.

    This function searches through all contacts and returns
    those that match the search term.
    """
    # Function code here...
```

## Lists: Storing Multiple Items

### Why Lists?

**Bad approach:**
```python
contact1_name = "Alice"
contact2_name = "Bob"
contact3_name = "Charlie"
# What if we need 100 contacts?!
```

**Good approach:**
```python
contacts = []  # Can store unlimited items!
```

### List Operations

```python
# Create empty list
contacts = []

# Add items
contacts.append({"name": "Alice", "phone": "555-0001"})

# Access items
first_contact = contacts[0]

# Loop through items
for contact in contacts:
    print(contact["name"])

# Check length
num_contacts = len(contacts)

# Remove items
contacts.pop(0)  # Remove first item
```

## Dictionaries: Storing Structured Data

### Why Dictionaries?

Dictionaries store key-value pairs, perfect for structured data:

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

# Check if key exists
if "email" in contact:
    print(contact["email"])
```

### Dictionary Operations

```python
# Create dictionary
person = {"name": "Alice", "age": 25}

# Add new key-value pair
person["email"] = "alice@email.com"

# Update value
person["age"] = 26

# Get all keys
keys = person.keys()

# Get all values
values = person.values()

# Loop through dictionary
for key, value in person.items():
    print(f"{key}: {value}")
```

## Combining Lists and Dictionaries

This is the secret to building real programs!

```python
# A list of dictionaries - our contact database
contacts = [
    {"name": "Alice", "phone": "555-0001", "email": "alice@email.com"},
    {"name": "Bob", "phone": "555-0002", "email": "bob@email.com"},
    {"name": "Charlie", "phone": "555-0003", "email": ""}
]

# Loop through all contacts
for contact in contacts:
    print(f"{contact['name']}: {contact['phone']}")

# Find specific contact
def find_contact(contacts_list, name):
    for contact in contacts_list:
        if contact["name"].lower() == name.lower():
            return contact
    return None

# Search contacts
def search_contacts(contacts_list, search_term):
    results = []
    for contact in contacts_list:
        if search_term in contact["name"] or search_term in contact["phone"]:
            results.append(contact)
    return results
```

## Building Features Step by Step

### Feature 1: Add Contact

```python
def add_contact(contacts_list, name, phone, email=""):
    """Add a new contact to our list"""
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "id": len(contacts_list) + 1
    }

    contacts_list.append(contact)
    print(f"✓ Added {name} to contacts")
    return contact
```

### Feature 2: Display All Contacts

```python
def display_all_contacts(contacts_list):
    """Show all contacts in a nice format"""
    if not contacts_list:
        print("No contacts to display")
        return

    print("\n" + "="*50)
    print(f"{'Name':<20} {'Phone':<15} {'Email':<20}")
    print("="*50)

    for contact in contacts_list:
        print(f"{contact['name']:<20} {contact['phone']:<15} {contact.get('email', ''):<20}")

    print("="*50)
```

### Feature 3: Search Contacts

```python
def search_contacts(contacts_list, search_term):
    """Find contacts by name or phone"""
    results = []
    search_lower = search_term.lower()

    for contact in contacts_list:
        if (search_lower in contact["name"].lower() or
            search_lower in contact["phone"]):
            results.append(contact)

    return results
```

### Feature 4: Delete Contact

```python
def delete_contact(contacts_list, name):
    """Remove a contact by name"""
    for i, contact in enumerate(contacts_list):
        if contact["name"].lower() == name.lower():
            removed = contacts_list.pop(i)
            print(f"✓ Deleted {removed['name']}")
            return removed

    print(f"Contact {name} not found")
    return None
```

## Saving and Loading Data

Real programs need to save data!

```python
import json

def save_contacts(contacts_list, filename="contacts.json"):
    """Save contacts to a file"""
    try:
        with open(filename, 'w') as f:
            json.dump(contacts_list, f, indent=2)
        print(f"✓ Saved {len(contacts_list)} contacts")
        return True
    except Exception as e:
        print(f"❌ Error saving: {e}")
        return False

def load_contacts(filename="contacts.json"):
    """Load contacts from a file"""
    try:
        with open(filename, 'r') as f:
            contacts = json.load(f)
        print(f"✓ Loaded {len(contacts)} contacts")
        return contacts
    except FileNotFoundError:
        print("No saved contacts found")
        return []
```

## Building a Menu System

Put it all together with a menu:

```python
def display_menu():
    """Show the menu"""
    print("\n" + "="*40)
    print("     CONTACT MANAGER MENU")
    print("="*40)
    print("1. Add contact")
    print("2. Search contacts")
    print("3. Display all contacts")
    print("4. Delete contact")
    print("5. Save contacts")
    print("6. Load contacts")
    print("0. Exit")
    print("="*40)

def run_contact_manager():
    """Main program loop"""
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("\nEnter choice: ")

        if choice == "0":
            save_contacts(contacts)
            print("Goodbye!")
            break

        elif choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email (optional): ")
            add_contact(contacts, name, phone, email)

        elif choice == "2":
            search_term = input("Search for: ")
            results = search_contacts(contacts, search_term)
            for contact in results:
                print(f"  • {contact['name']}: {contact['phone']}")

        # Add other menu options...
```

## Best Practices

### 1. Write Clear Function Names
```python
# Good
def add_contact(contacts_list, name, phone):
    pass

# Bad
def ac(cl, n, p):
    pass
```

### 2. One Function, One Task
```python
# Good: Each function does one thing
def contact_exists(contacts_list, name):
    # Just check existence
    pass

def add_contact_safe(contacts_list, name, phone):
    # Check, then add
    if contact_exists(contacts_list, name):
        return None
    return add_contact(contacts_list, name, phone)
```

### 3. Use Docstrings
```python
def search_contacts(contacts_list, search_term):
    """
    Find contacts matching the search term.

    Searches both name and phone fields.
    Case-insensitive.
    """
    pass
```

### 4. Handle Edge Cases
```python
def display_all_contacts(contacts_list):
    """Display all contacts"""
    if not contacts_list:  # Empty list?
        print("No contacts to display")
        return

    # Continue with display...
```

## Hands-on Activities

### Activity 1: Basic Contact Manager
Build these features:
1. Add a contact
2. Display all contacts
3. Search for a contact

### Activity 2: Enhanced Features
Add:
1. Delete contact functionality
2. Edit contact information
3. Count statistics (total, with/without email)

### Activity 3: Data Persistence
Implement:
1. Save contacts to a file
2. Load contacts from a file
3. Auto-save on exit

### Activity 4: Advanced Features
Try:
1. Sort contacts by name
2. Find duplicate phone numbers
3. Export contacts to different format

## Common Pitfalls

### 1. Forgetting to Return
```python
# Bad: No return statement
def add_contact(contacts_list, name, phone):
    contact = {"name": name, "phone": phone}
    contacts_list.append(contact)
    # Oops! Should return contact

# Good: Returns the contact
def add_contact(contacts_list, name, phone):
    contact = {"name": name, "phone": phone}
    contacts_list.append(contact)
    return contact
```

### 2. Not Checking Empty Lists
```python
# Bad: Will fail on empty list
first_contact = contacts[0]

# Good: Check first
if contacts:
    first_contact = contacts[0]
else:
    print("No contacts")
```

### 3. Case-Sensitive Comparison
```python
# Bad: Won't find "alice" if stored as "Alice"
if name == contact["name"]:
    pass

# Good: Case-insensitive
if name.lower() == contact["name"].lower():
    pass
```

## Project Template

Download the Contact Manager starter template:
[Contact Manager Starter Template](https://raw.githubusercontent.com/ap-unil-2025/course-materials/master/content/weeks/week-04/contact_manager_starter.py)

The template includes:
- Function stubs with TODOs
- Clear instructions
- Suggested implementation order
- Test code

## Assessment

This lesson helps you build:
- Function design and implementation skills
- Understanding of data structures
- Ability to build complete programs
- Problem-solving with code organization

## Next Steps

Next week (Week 5) we'll explore Generative AI and how it can assist in programming tasks. Week 6 will introduce Object-Oriented Programming (OOP) where we'll refactor our Contact Manager using classes.
