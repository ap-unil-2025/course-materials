"""
Contact Manager v2.0 - OOP Version
Session 6: Object-Oriented Programming
Anna Smirnova, October 2025

This shows the transformation from Week 4's functional approach
to Week 6's object-oriented approach.
"""

import json
from datetime import datetime
from typing import List, Dict, Optional


# ============================================================================
# CONTACT CLASS (Optional - shows encapsulation)
# ============================================================================

class Contact:
    """Represents a single contact with validation"""

    def __init__(self, name: str, phone: str, email: str = ""):
        self.name = name
        self.phone = phone
        self.email = email
        self.created_at = datetime.now().isoformat()

    def matches_search(self, search_term: str) -> bool:
        """Check if this contact matches a search term"""
        search_lower = search_term.lower()
        return (search_lower in self.name.lower() or
                search_lower in self.phone)

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create Contact from dictionary"""
        contact = cls(data["name"], data["phone"], data.get("email", ""))
        contact.created_at = data.get("created_at", datetime.now().isoformat())
        return contact

    def __str__(self):
        """String representation for display"""
        return f"{self.name}: {self.phone}" + (f" ({self.email})" if self.email else "")


# ============================================================================
# CONTACT MANAGER CLASS - Main Application
# ============================================================================

class ContactManager:
    """
    Manages a collection of contacts with save/load functionality.

    This is the OOP version of our Week 4 Contact Manager!
    Notice how the data (contacts list) and the functions that operate
    on it are now bundled together in a class.
    """

    def __init__(self):
        """Initialize with empty contact list"""
        self.contacts: List[Contact] = []

    # ========================================================================
    # CORE FUNCTIONALITY
    # ========================================================================

    def add_contact(self, name: str, phone: str, email: str = "") -> Optional[Contact]:
        """
        Add a new contact to the manager.

        Week 4 version:
            add_contact(contacts_list, name, phone, email)

        Week 6 version:
            manager.add_contact(name, phone, email)

        Notice: No need to pass contacts_list - it's part of the class!
        """
        # Check for duplicates
        if self.contact_exists(name):
            print(f"⚠️  Contact '{name}' already exists")
            return None

        # Create and add contact
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f"✓ Added {name} to contacts")
        return contact

    def contact_exists(self, name: str) -> bool:
        """Check if a contact with this name already exists"""
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return True
        return False

    def search(self, search_term: str) -> List[Contact]:
        """
        Find contacts matching the search term.

        Week 4: search_contacts(contacts_list, term)
        Week 6: manager.search(term)
        """
        return [c for c in self.contacts if c.matches_search(search_term)]

    def delete_contact(self, name: str) -> Optional[Contact]:
        """Delete a contact by name"""
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                removed = self.contacts.pop(i)
                print(f"✓ Deleted {removed.name}")
                return removed
        print(f"Contact '{name}' not found")
        return None

    def get_all_contacts(self) -> List[Contact]:
        """Return all contacts"""
        return self.contacts.copy()

    # ========================================================================
    # FILE OPERATIONS
    # ========================================================================

    def save(self, filename: str = "contacts.json") -> bool:
        """
        Save contacts to a JSON file.

        Week 4: save_contacts(contacts_list, filename)
        Week 6: manager.save(filename)
        """
        try:
            # Convert Contact objects to dictionaries
            data = [contact.to_dict() for contact in self.contacts]

            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)

            print(f"✓ Saved {len(self.contacts)} contacts to {filename}")
            return True

        except Exception as e:
            print(f"❌ Error saving: {e}")
            return False

    def load(self, filename: str = "contacts.json") -> bool:
        """
        Load contacts from a JSON file.

        Week 4: contacts = load_contacts(filename)
        Week 6: manager.load(filename)

        Notice: We modify self.contacts instead of returning a new list!
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)

            # Convert dictionaries to Contact objects
            self.contacts = [Contact.from_dict(c) for c in data]

            print(f"✓ Loaded {len(self.contacts)} contacts from {filename}")
            return True

        except FileNotFoundError:
            print(f"No file '{filename}' found - starting fresh")
            return False

        except Exception as e:
            print(f"❌ Error loading: {e}")
            return False

    # ========================================================================
    # STATISTICS & UTILITY
    # ========================================================================

    def get_stats(self) -> dict:
        """Get statistics about the contact collection"""
        stats = {
            "total": len(self.contacts),
            "with_email": sum(1 for c in self.contacts if c.email),
            "without_email": sum(1 for c in self.contacts if not c.email),
            "by_area_code": {}
        }

        # Group by area code
        for contact in self.contacts:
            area_code = contact.phone[:3]
            if area_code not in stats["by_area_code"]:
                stats["by_area_code"][area_code] = []
            stats["by_area_code"][area_code].append(contact.name)

        return stats

    def display_all(self):
        """Display all contacts in a formatted table"""
        if not self.contacts:
            print("No contacts to display")
            return

        print(f"\n{'='*60}")
        print(f"{'Name':<20} {'Phone':<15} {'Email':<25}")
        print(f"{'='*60}")
        for contact in self.contacts:
            print(f"{contact.name:<20} {contact.phone:<15} {contact.email:<25}")
        print(f"{'='*60}")

    def __len__(self):
        """Allow len(manager) to get contact count"""
        return len(self.contacts)

    def __str__(self):
        """String representation"""
        return f"ContactManager with {len(self.contacts)} contacts"


# ============================================================================
# COMPARISON: WEEK 4 vs WEEK 6
# ============================================================================

def show_comparison():
    """Demonstrate the difference between functional and OOP approaches"""

    print("=" * 70)
    print("WEEK 4 APPROACH (Functional)")
    print("=" * 70)
    print("""
    # Data and functions are separate
    contacts = []

    # Functions operate on external data
    add_contact(contacts, "Alice", "555-0001")
    search_contacts(contacts, "Alice")
    save_contacts(contacts, "contacts.json")

    # You must pass the list to every function
    """)

    print("\n" + "=" * 70)
    print("WEEK 6 APPROACH (Object-Oriented)")
    print("=" * 70)
    print("""
    # Data and methods are bundled together
    manager = ContactManager()

    # Methods operate on their own data
    manager.add_contact("Alice", "555-0001")
    manager.search("Alice")
    manager.save("contacts.json")

    # The data is encapsulated inside the object
    """)


# ============================================================================
# INTERACTIVE DEMO
# ============================================================================

def run_demo():
    """Run an interactive demo of the OOP contact manager"""
    print("\n" + "="*60)
    print("     CONTACT MANAGER v2.0 - OOP DEMO")
    print("="*60)

    # Create manager instance
    manager = ContactManager()

    # Try to load existing contacts
    manager.load()

    while True:
        print("\n1. Add contact")
        print("2. Search contacts")
        print("3. Display all")
        print("4. Show statistics")
        print("5. Delete contact")
        print("6. Save & Exit")
        print("0. Exit without saving")

        choice = input("\nChoice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email (optional): ")
            manager.add_contact(name, phone, email)

        elif choice == "2":
            term = input("Search for: ")
            results = manager.search(term)
            if results:
                print(f"\nFound {len(results)} contact(s):")
                for contact in results:
                    print(f"  • {contact}")
            else:
                print("No matches found")

        elif choice == "3":
            manager.display_all()

        elif choice == "4":
            stats = manager.get_stats()
            print("\n📊 Contact Statistics:")
            print(f"  Total: {stats['total']}")
            print(f"  With email: {stats['with_email']}")
            print(f"  Without email: {stats['without_email']}")

        elif choice == "5":
            name = input("Name to delete: ")
            manager.delete_contact(name)

        elif choice == "6":
            manager.save()
            print("Saved and exiting. Goodbye!")
            break

        else:
            print("Invalid choice")


# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("Testing OOP Contact Manager\n")

    # Show the comparison first
    show_comparison()

    # Create a manager and test it
    print("\n" + "="*60)
    print("LIVE EXAMPLE:")
    print("="*60)

    manager = ContactManager()

    # Add some contacts
    manager.add_contact("Alice Smith", "555-0001", "alice@email.com")
    manager.add_contact("Bob Jones", "555-0002")
    manager.add_contact("Charlie Brown", "555-0003", "charlie@email.com")

    # Try to add duplicate
    print("\nTrying to add duplicate:")
    manager.add_contact("Alice Smith", "555-9999")

    # Search
    print("\nSearching for 'alice':")
    results = manager.search("alice")
    for contact in results:
        print(f"  Found: {contact}")

    # Display all
    print("\nAll contacts:")
    manager.display_all()

    # Show stats
    print("\nStatistics:")
    stats = manager.get_stats()
    print(f"  Total: {stats['total']}")
    print(f"  With email: {stats['with_email']}")

    # Save
    print("\nSaving...")
    manager.save("demo_contacts.json")

    print(f"\nFinal state: {manager}")
    print(f"Contact count: {len(manager)}")

    # Uncomment to run interactive demo:
    # run_demo()
