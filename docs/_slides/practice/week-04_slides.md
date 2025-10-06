---
marp: true
paginate: true
header: "Session 4: Contact Manager - Part 1"
footer: "Anna Smirnova, October 13, 2025"
style: |
  section.lead {
    background: #003aff;
    color: white;
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

# Build Feature 1: Add a Contact

```python
def add_contact(contacts_list, name, phone, email=""):
    """Add a new contact to our list"""
    # TODO: Create a dictionary for this contact with:
    # - name, phone, email fields
    # - auto-generated id (hint: use len(contacts_list) + 1)
    
    # TODO: Add the contact to contacts_list
    
    # TODO: Print success message
    
    # TODO: Return the contact dictionary
    pass

# Test it!
add_contact(contacts, "Alice Smith", "555-0001", "alice@email.com")
add_contact(contacts, "Bob Jones", "555-0002")
print(contacts)
```

**Challenge**: What happens if we add a duplicate? Let's fix that!

---

# Prevent Duplicates

```python
def contact_exists(contacts_list, name):
    """Check if a contact already exists"""
    # TODO: Loop through contacts_list
    # TODO: Check if any contact's name matches (case-insensitive)
    # TODO: Return True if found, False otherwise
    pass

# Improved add_contact
def add_contact_safe(contacts_list, name, phone, email=""):
    # TODO: Check if contact already exists using contact_exists()
    # TODO: If exists, print warning and return None
    # TODO: Otherwise, call add_contact() and return result
    pass

# Test duplicate prevention
add_contact_safe(contacts, "Alice Smith", "555-9999")
```

**Your turn**: Add a function to validate phone numbers!

---

# Build Feature 2: Search Contacts

```python
def search_contacts(contacts_list, search_term):
    """Find contacts by name or phone"""
    results = []
    search_lower = search_term.lower()
    
    # TODO: Loop through contacts_list
    # TODO: Check if search_term is in name OR phone
    # TODO: Add matching contacts to results list
    # TODO: Return results
    pass

# Make it user-friendly
def display_search_results(search_term):
    # TODO: Call search_contacts() to get results
    
    # TODO: If no results, print "not found" message
    # TODO: Otherwise, print each result nicely formatted
    pass

# Test it
display_search_results("alice")
display_search_results("555")
```

---

# Part 2: Power of List Comprehensions

---

# Make Our Search Smarter

```python
# Old way (what we just wrote)
def get_all_names(contacts_list):
    names = []
    for contact in contacts_list:
        names.append(contact["name"])
    return names

# New way with list comprehension - ONE LINE!
def get_all_names_v2(contacts_list):
    # TODO: Return list of all names using list comprehension
    # Hint: [something for contact in contacts_list]
    pass

# Even more powerful
def get_contacts_without_email(contacts_list):
    # TODO: Return names of contacts without email
    # Hint: Add an if condition to list comprehension
    pass

# Test it
print("All names:", get_all_names_v2(contacts))
print("No email:", get_contacts_without_email(contacts))
```

**Challenge**: Write a list comprehension to get all phone numbers starting with "555"

---

# Build Feature 3: Bulk Operations

```python
def bulk_add_from_text(contacts_list, text_data):
    """Add multiple contacts from formatted text"""
    lines = text_data.strip().split('\n')
    added = 0
    
    for line in lines:
        # TODO: Split line by comma
        # TODO: Extract name (required) and phone (required)
        # TODO: Extract email if present (optional)
        # TODO: Use add_contact_safe() to add
        # TODO: Count successful additions
        pass
    
    return added

# Test with sample data
sample_data = """Charlie Brown, 555-0003, charlie@email.com
Diana Prince, 555-0004
Eve Adams, 555-0005, eve@email.com"""

added_count = bulk_add_from_text(contacts, sample_data)
print(f"\n✓ Added {added_count} new contacts")
```

---

# Part 3: Dictionaries - Your Swiss Army Knife

---

# Enhance with Statistics

```python
def get_contact_stats(contacts_list):
    """Get interesting statistics about contacts"""
    stats = {
        "total": len(contacts_list),
        "with_email": 0,
        "without_email": 0,
        "by_area_code": {}
    }
    
    for contact in contacts_list:
        # TODO: Count contacts with/without email
        
        # TODO: Extract area code (first 3 chars of phone)
        # TODO: Group contacts by area code in dictionary
        pass
    
    return stats

# Display stats
stats = get_contact_stats(contacts)
print(f"\n📊 Contact Statistics:")
print(f"Total: {stats['total']} contacts")
print(f"With email: {stats['with_email']}")
print(f"By area code: {stats['by_area_code']}")
```

---

# Build Feature 4: Export/Import

```python
import json

def save_contacts(contacts_list, filename="contacts.json"):
    """Save contacts to a file"""
    try:
        # TODO: Open file in write mode
        # TODO: Use json.dump() to save contacts_list
        # TODO: Print success message
        # TODO: Return True
        pass
    except Exception as e:
        print(f"❌ Error saving: {e}")
        return False

def load_contacts(filename="contacts.json"):
    """Load contacts from a file"""
    try:
        # TODO: Open file in read mode
        # TODO: Use json.load() to read contacts
        # TODO: Print success message
        # TODO: Return loaded contacts
        pass
    except FileNotFoundError:
        print("No saved contacts found")
        return []
    except Exception as e:
        print(f"❌ Error loading: {e}")
        return []

# Test save/load
save_contacts(contacts)
loaded = load_contacts()
```

---

# Part 4: Advanced Features

---

# Sort and Filter

```python
def get_sorted_contacts(contacts_list, sort_by="name"):
    """Return contacts sorted by field"""
    # TODO: Use sorted() with a lambda key function
    # Hint: key=lambda x: x[sort_by]
    pass

def filter_contacts(contacts_list, **criteria):
    """Filter contacts by multiple criteria"""
    results = contacts_list
    
    # TODO: For each field, value in criteria
    # TODO: Filter results to only include matching contacts
    # Hint: Use list comprehension with condition
    pass
    
    return results

# Test advanced features
sorted_contacts = get_sorted_contacts(contacts, "name")
print("\nSorted by name:")
for c in sorted_contacts:
    print(f"  {c['name']}: {c['phone']}")

# Filter with multiple criteria
filtered = filter_contacts(contacts, name="a", phone="555")
print(f"\nFiltered ({len(filtered)} results):")
for c in filtered:
    print(f"  {c['name']}: {c['phone']}")
```

---

# Build a Menu System

```python
def display_menu():
    print("\n" + "="*40)
    print("     CONTACT MANAGER MENU")
    print("="*40)
    print("1. Add contact")
    print("2. Search contacts")
    print("3. Display all contacts")
    print("4. Show statistics")
    print("5. Save contacts")
    print("6. Load contacts")
    print("0. Exit")
    print("="*40)

def run_contact_manager():
    """Main program loop"""
    local_contacts = load_contacts()  # Load on start
    
    while True:
        display_menu()
        choice = input("\nEnter choice: ")
        
        if choice == "0":
            # TODO: Save before exit
            # TODO: Print goodbye
            # TODO: Break the loop
            pass
        elif choice == "1":
            # TODO: Get input for name, phone, email
            # TODO: Call add_contact_safe()
            pass
        elif choice == "2":
            # TODO: Get search term
            # TODO: Call display_search_results()
            pass
        # TODO: Implement other menu choices

# Uncomment to run:
# run_contact_manager()
```

---

# Part 5: Make It Professional

---

# Add Type Hints and Docstrings

```python
from typing import List, Dict, Optional

def add_contact_pro(
    contacts_list: List[Dict[str, any]], 
    name: str, 
    phone: str, 
    email: str = ""
) -> Optional[Dict[str, any]]:
    """
    Add a new contact to the contact list.
    
    Args:
        contacts_list: The list to add the contact to
        name: Contact's full name
        phone: Contact's phone number
        email: Contact's email (optional)
    
    Returns:
        The created contact dict, or None if duplicate
    
    Example:
        >>> contacts = []
        >>> add_contact_pro(contacts, "John Doe", "555-1234")
        {'name': 'John Doe', 'phone': '555-1234', ...}
    """
    # Implementation here
    pass
```

**This is how professionals write Python!**

---

# Bonus: Recursive Contact Search

```python
def find_contact_recursive(contacts_list, name, index=0):
    """Find a contact using recursion (just for fun!)"""
    # TODO: Base case 1 - if index >= len(contacts_list), return None
    
    # TODO: Base case 2 - if current contact matches name, return it
    
    # TODO: Recursive case - call function with index + 1
    pass

# Compare with the simple version
def find_contact_simple(contacts_list, name):
    # TODO: Use a for loop to find contact by name
    pass

# Both work the same!
print(find_contact_recursive(contacts, "alice smith"))
print(find_contact_simple(contacts, "alice smith"))
```

**Question**: Which is better? Why?

---

# Challenge Time! 🏆

---

# 5-Minute Challenges

**Challenge 1**: Add a delete contact function
```python
def delete_contact(contacts_list, name):
    # Your code here
    pass
```

**Challenge 2**: Find duplicate phone numbers
```python
def find_duplicate_phones(contacts_list):
    # Return list of phone numbers that appear more than once
    pass
```

**Challenge 3**: Create a backup system
```python
def create_backup(contacts_list):
    # Save with timestamp in filename
    pass
```

**Challenge 4**: Merge two contact lists
```python
def merge_contacts(list1, list2):
    # Combine without duplicates
    pass
```

---

# Quick Solutions

```python
# Challenge 1 Solution
def delete_contact(contacts_list, name):
    # TODO: Find contact by name and remove it
    # Hint: Use enumerate() to get index
    # Hint: Use pop(index) to remove
    pass

# Challenge 2 Solution
def find_duplicate_phones(contacts_list):
    # TODO: Count occurrences of each phone number
    # TODO: Return list of phones that appear > 1 time
    # Hint: Use a dictionary to count
    pass

# Test them!
test_contacts = contacts.copy()
delete_contact(test_contacts, "Alice Smith")
print(f"Duplicate phones: {find_duplicate_phones(contacts)}")
```

---

# What We Built: v0.1 → v1.0

## Week 3 (v0.1) vs Week 4 (v1.0)

**Week 3 Limitations:**
- ❌ Only 3 contacts (separate variables)
- ❌ Repeated code everywhere
- ❌ No way to save data
- ❌ Hard to maintain

**Week 4 Improvements:**
- ✅ Unlimited contacts (lists!)
- ✅ Reusable functions
- ✅ Save/load with JSON
- ✅ Clean, organized code
- ✅ Professional structure
- ✅ Easy to extend

**From 200 lines → 50 lines of cleaner code!**

---

# Take It Further (Homework)

**Extend your Contact Manager:**

1. **Add birthday tracking**
   - Store birthdays
   - Show upcoming birthdays
   - Calculate age

2. **Groups/Categories**
   - Tag contacts (family, work, friends)
   - Filter by group
   - Group statistics

3. **Import from CSV**
   - Read real contact files
   - Handle different formats
   - Validate data

4. **Search improvements**
   - Fuzzy matching
   - Search by partial phone
   - Recent searches

5. **Data validation**
   - Valid email format
   - Phone number formatting
   - Duplicate checking

**Share your improvements on GitHub!**

---

# Pro Tips from Today

**1. Start with data structure**
```python
# We chose: list of dictionaries
# Why? Easy to search, sort, and extend
```

**2. Build incrementally**
```python
# Start simple, add features one by one
# Test each feature before moving on
```

**3. Think about the user**
```python
# Clear messages, handle errors gracefully
# Make it actually useful!
```

**4. Code organization**
```python
# Group related functions
# Use clear naming
# Add comments for "why", not "what"
```

**Remember**: The best code is code that works and others can understand!

---

<!-- _class: lead -->

# Next Week (Week 5)

## The AI Revolution

**Bring your Contact Manager!**

**Plot twist**: We'll recreate everything in 30 seconds!
- Show AI writing our entire program
- "But wait, there's more..."
- Why you still need to understand the code
- How to effectively prompt AI
- Debugging AI-generated code

**Week 6 Preview**: Turn it into professional OOP code

See you next Monday! 🤖