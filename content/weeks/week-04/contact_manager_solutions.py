"""
Contact Manager - Complete Solutions
Session 4: Functions and Data Structures
Anna Smirnova, October 2025

This file contains all the solutions for the Contact Manager project.
Students should try to implement these functions themselves first!
"""

import json
from typing import List, Dict, Optional
from datetime import datetime

# Initialize empty contacts list
contacts = []

# ============================================================================
# FEATURE 1: ADD CONTACTS
# ============================================================================

def add_contact(contacts_list, name, phone, email=""):
    """Add a new contact to our list"""
    # Create a dictionary for this contact
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "id": len(contacts_list) + 1
    }
    
    # Add to our list
    contacts_list.append(contact)
    print(f"✓ Added {name} to contacts")
    return contact


def contact_exists(contacts_list, name):
    """Check if a contact already exists"""
    for contact in contacts_list:
        if contact["name"].lower() == name.lower():
            return True
    return False


def add_contact_safe(contacts_list, name, phone, email=""):
    """Add contact with duplicate prevention"""
    if contact_exists(contacts_list, name):
        print(f"⚠️  {name} already exists!")
        return None
    
    return add_contact(contacts_list, name, phone, email)


# ============================================================================
# FEATURE 2: SEARCH CONTACTS
# ============================================================================

def search_contacts(contacts_list, search_term):
    """Find contacts by name or phone"""
    results = []
    search_lower = search_term.lower()
    
    for contact in contacts_list:
        if (search_lower in contact["name"].lower() or 
            search_lower in contact["phone"]):
            results.append(contact)
    
    return results


def display_search_results(search_term):
    """Display search results in a user-friendly way"""
    results = search_contacts(contacts, search_term)
    
    if not results:
        print(f"No contacts found for '{search_term}'")
    else:
        print(f"\nFound {len(results)} contact(s):")
        for contact in results:
            print(f"  • {contact['name']}: {contact['phone']}")


# ============================================================================
# LIST COMPREHENSIONS
# ============================================================================

def get_all_names_v2(contacts_list):
    """Get all contact names using list comprehension"""
    return [contact["name"] for contact in contacts_list]


def get_contacts_without_email(contacts_list):
    """Get names of contacts without email addresses"""
    return [c["name"] for c in contacts_list if not c["email"]]


def get_555_phones(contacts_list):
    """Challenge: Get all phone numbers starting with 555"""
    return [c["phone"] for c in contacts_list if c["phone"].startswith("555")]


# ============================================================================
# FEATURE 3: BULK OPERATIONS
# ============================================================================

def bulk_add_from_text(contacts_list, text_data):
    """Add multiple contacts from formatted text"""
    lines = text_data.strip().split('\n')
    added = 0
    
    for line in lines:
        parts = line.split(',')
        if len(parts) >= 2:
            name = parts[0].strip()
            phone = parts[1].strip()
            email = parts[2].strip() if len(parts) > 2 else ""
            
            if add_contact_safe(contacts_list, name, phone, email):
                added += 1
    
    return added


# ============================================================================
# STATISTICS
# ============================================================================

def get_contact_stats(contacts_list):
    """Get interesting statistics about contacts"""
    stats = {
        "total": len(contacts_list),
        "with_email": 0,
        "without_email": 0,
        "by_area_code": {}
    }
    
    for contact in contacts_list:
        # Count emails
        if contact["email"]:
            stats["with_email"] += 1
        else:
            stats["without_email"] += 1
        
        # Group by area code
        area_code = contact["phone"][:3]
        if area_code not in stats["by_area_code"]:
            stats["by_area_code"][area_code] = []
        stats["by_area_code"][area_code].append(contact["name"])
    
    return stats


# ============================================================================
# FEATURE 4: SAVE/LOAD
# ============================================================================

def save_contacts(contacts_list, filename="contacts.json"):
    """Save contacts to a file"""
    try:
        with open(filename, 'w') as f:
            json.dump(contacts_list, f, indent=2)
        print(f"✓ Saved {len(contacts_list)} contacts to {filename}")
        return True
    except Exception as e:
        print(f"❌ Error saving: {e}")
        return False


def load_contacts(filename="contacts.json"):
    """Load contacts from a file"""
    try:
        with open(filename, 'r') as f:
            loaded = json.load(f)
        print(f"✓ Loaded {len(loaded)} contacts from {filename}")
        return loaded
    except FileNotFoundError:
        print("No saved contacts found")
        return []
    except Exception as e:
        print(f"❌ Error loading: {e}")
        return []


# ============================================================================
# ADVANCED FEATURES
# ============================================================================

def get_sorted_contacts(contacts_list, sort_by="name"):
    """Return contacts sorted by field"""
    return sorted(contacts_list, key=lambda x: x[sort_by])


def filter_contacts(contacts_list, **criteria):
    """Filter contacts by multiple criteria"""
    results = contacts_list
    
    for field, value in criteria.items():
        results = [c for c in results 
                  if value.lower() in str(c.get(field, '')).lower()]
    
    return results


# ============================================================================
# MENU SYSTEM
# ============================================================================

def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("     CONTACT MANAGER MENU")
    print("="*40)
    print("1. Add contact")
    print("2. Search contacts")
    print("3. Display all contacts")
    print("4. Show statistics")
    print("5. Save contacts")
    print("6. Load contacts")
    print("7. Delete contact")
    print("0. Exit")
    print("="*40)


def display_all_contacts(contacts_list):
    """Display all contacts in a formatted way"""
    if not contacts_list:
        print("No contacts to display")
        return
    
    print(f"\n{'='*50}")
    print(f"{'ID':<5} {'Name':<20} {'Phone':<15} {'Email':<20}")
    print(f"{'='*50}")
    for contact in contacts_list:
        print(f"{contact['id']:<5} {contact['name']:<20} {contact['phone']:<15} {contact.get('email', ''):<20}")
    print(f"{'='*50}")


def run_contact_manager():
    """Main program loop"""
    local_contacts = load_contacts()  # Load on start
    
    while True:
        display_menu()
        choice = input("\nEnter choice: ")
        
        if choice == "0":
            save_contacts(local_contacts)  # Auto-save on exit
            print("Goodbye!")
            break
            
        elif choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email (optional): ")
            add_contact_safe(local_contacts, name, phone, email)
            
        elif choice == "2":
            search_term = input("Search for: ")
            display_search_results(search_term)
            
        elif choice == "3":
            display_all_contacts(local_contacts)
            
        elif choice == "4":
            stats = get_contact_stats(local_contacts)
            print(f"\n📊 Contact Statistics:")
            print(f"Total: {stats['total']} contacts")
            print(f"With email: {stats['with_email']}")
            print(f"Without email: {stats['without_email']}")
            print(f"By area code: {stats['by_area_code']}")
            
        elif choice == "5":
            save_contacts(local_contacts)
            
        elif choice == "6":
            local_contacts = load_contacts()
            
        elif choice == "7":
            name = input("Name to delete: ")
            delete_contact(local_contacts, name)
            
        else:
            print("Invalid choice. Please try again.")


# ============================================================================
# RECURSION EXAMPLES
# ============================================================================

def find_contact_recursive(contacts_list, name, index=0):
    """Find a contact using recursion (just for fun!)"""
    # Base case: reached end of list
    if index >= len(contacts_list):
        return None
    
    # Base case: found the contact
    if contacts_list[index]["name"].lower() == name.lower():
        return contacts_list[index]
    
    # Recursive case: check next contact
    return find_contact_recursive(contacts_list, name, index + 1)


def find_contact_simple(contacts_list, name):
    """Find contact using simple loop"""
    for contact in contacts_list:
        if contact["name"].lower() == name.lower():
            return contact
    return None


# ============================================================================
# CHALLENGE SOLUTIONS
# ============================================================================

def delete_contact(contacts_list, name):
    """Challenge 1: Delete a contact by name"""
    for i, contact in enumerate(contacts_list):
        if contact["name"].lower() == name.lower():
            removed = contacts_list.pop(i)
            print(f"✓ Deleted {removed['name']}")
            return removed
    print(f"Contact {name} not found")
    return None


def find_duplicate_phones(contacts_list):
    """Challenge 2: Find duplicate phone numbers"""
    phone_count = {}
    for contact in contacts_list:
        phone = contact["phone"]
        phone_count[phone] = phone_count.get(phone, 0) + 1
    
    duplicates = [phone for phone, count in phone_count.items() if count > 1]
    return duplicates


def create_backup(contacts_list):
    """Challenge 3: Create backup with timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"contacts_backup_{timestamp}.json"
    
    try:
        with open(backup_filename, 'w') as f:
            json.dump(contacts_list, f, indent=2)
        print(f"✓ Backup created: {backup_filename}")
        return backup_filename
    except Exception as e:
        print(f"❌ Backup failed: {e}")
        return None


def merge_contacts(list1, list2):
    """Challenge 4: Merge two contact lists without duplicates"""
    merged = list1.copy()
    
    for contact in list2:
        if not contact_exists(merged, contact["name"]):
            merged.append(contact)
    
    # Re-number IDs
    for i, contact in enumerate(merged, 1):
        contact["id"] = i
    
    return merged


# ============================================================================
# BONUS: VALIDATION FUNCTIONS
# ============================================================================

def validate_phone(phone):
    """Validate phone number format"""
    # Remove common separators
    clean_phone = phone.replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
    
    # Check if it's all digits and right length
    if not clean_phone.isdigit():
        return False
    
    # Check length (adjust based on your country)
    if len(clean_phone) < 7 or len(clean_phone) > 15:
        return False
    
    return True


def validate_email(email):
    """Basic email validation"""
    if not email:
        return True  # Email is optional
    
    # Very basic check
    if "@" not in email or "." not in email:
        return False
    
    parts = email.split("@")
    if len(parts) != 2:
        return False
    
    return True


# ============================================================================
# PROFESSIONAL VERSION WITH TYPE HINTS
# ============================================================================

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
    # Check for duplicates
    if contact_exists(contacts_list, name):
        print(f"⚠️  Contact '{name}' already exists")
        return None
    
    # Validate phone
    if not validate_phone(phone):
        print(f"❌ Invalid phone number: {phone}")
        return None
    
    # Validate email
    if not validate_email(email):
        print(f"❌ Invalid email address: {email}")
        return None
    
    # Create contact
    contact = {
        "id": len(contacts_list) + 1,
        "name": name,
        "phone": phone,
        "email": email,
        "created_at": datetime.now().isoformat()
    }
    
    contacts_list.append(contact)
    print(f"✓ Successfully added {name}")
    return contact


# ============================================================================
# TEST THE SYSTEM
# ============================================================================

if __name__ == "__main__":
    print("Contact Manager v1.0 - Solutions File")
    print("=" * 50)
    
    # Test adding contacts
    add_contact_safe(contacts, "Alice Smith", "555-0001", "alice@email.com")
    add_contact_safe(contacts, "Bob Jones", "555-0002")
    add_contact_safe(contacts, "Charlie Brown", "555-0003", "charlie@email.com")
    
    # Test duplicate prevention
    print("\nTesting duplicate prevention:")
    add_contact_safe(contacts, "Alice Smith", "555-9999")
    
    # Test search
    print("\nTesting search:")
    display_search_results("alice")
    
    # Test statistics
    print("\nTesting statistics:")
    stats = get_contact_stats(contacts)
    print(f"Total contacts: {stats['total']}")
    print(f"With email: {stats['with_email']}")
    
    # Test save/load
    print("\nTesting save/load:")
    save_contacts(contacts, "test_contacts.json")
    
    # Run the interactive menu (uncomment to test)
    # run_contact_manager()