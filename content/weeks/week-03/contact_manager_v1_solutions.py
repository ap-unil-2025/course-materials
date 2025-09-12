"""
Contact Manager v0.1 - Complete Solutions
Session 3: Python Fundamentals
Anna Smirnova, October 2025

Week 3: Building the foundation with basic Python
This version uses only basic Python concepts (no functions or lists yet!)
"""

# ============================================================================
# COMPLETE CONTACT MANAGER v0.1
# ============================================================================

print("="*40)
print("  CONTACT MANAGER v0.1 (Basic)")
print("="*40)

# Initialize variables for storing contacts
# Since we don't know lists yet, we'll use separate variables
contact1_name = ""
contact1_phone = ""
contact1_age = 0
contact1_favorite = False

contact2_name = ""
contact2_phone = ""
contact2_age = 0
contact2_favorite = False

contact3_name = ""
contact3_phone = ""
contact3_age = 0
contact3_favorite = False

# Track how many contacts we have
contact_count = 0
max_contacts = 3

# Main program loop
running = True

while running:
    # Display menu
    print("\n" + "-"*30)
    print("CONTACT MANAGER MENU")
    print("-"*30)
    print("1. Add new contact")
    print("2. View all contacts")
    print("3. Search contacts")
    print("4. View statistics")
    print("5. Exit")
    print("-"*30)
    print(f"Contacts: {contact_count}/{max_contacts}")
    
    # Get user choice
    choice = input("\nEnter your choice (1-5): ")
    
    # Handle menu choices
    if choice == "1":
        # Add new contact
        if contact_count >= max_contacts:
            print(f"\n❌ Contact list is full! Maximum {max_contacts} contacts.")
        else:
            print("\n--- ADD NEW CONTACT ---")
            
            # Get contact information
            name = input("Enter contact name: ").strip()
            
            # Validate name
            if len(name) < 2:
                print("❌ Name must be at least 2 characters!")
            else:
                # Check for duplicates
                is_duplicate = False
                if contact_count >= 1 and contact1_name.lower() == name.lower():
                    is_duplicate = True
                elif contact_count >= 2 and contact2_name.lower() == name.lower():
                    is_duplicate = True
                elif contact_count >= 3 and contact3_name.lower() == name.lower():
                    is_duplicate = True
                
                if is_duplicate:
                    print(f"❌ Contact '{name}' already exists!")
                else:
                    # Get rest of contact info
                    phone = input("Enter phone number: ").strip()
                    
                    # Validate phone
                    if len(phone) < 7:
                        print("❌ Phone number must be at least 7 digits!")
                    else:
                        # Format phone number (if 7 digits)
                        if len(phone) == 7 and phone.isdigit():
                            phone = phone[:3] + "-" + phone[3:]
                        
                        # Get age
                        age_str = input("Enter age: ")
                        try:
                            age = int(age_str)
                            if age < 0 or age > 150:
                                print("⚠️ Invalid age, setting to 0")
                                age = 0
                        except:
                            print("⚠️ Invalid age, setting to 0")
                            age = 0
                        
                        # Ask if favorite
                        fav_input = input("Is this a favorite contact? (y/n): ").lower()
                        is_favorite = fav_input == 'y' or fav_input == 'yes'
                        
                        # Store in the next available slot
                        if contact_count == 0:
                            contact1_name = name.title()
                            contact1_phone = phone
                            contact1_age = age
                            contact1_favorite = is_favorite
                        elif contact_count == 1:
                            contact2_name = name.title()
                            contact2_phone = phone
                            contact2_age = age
                            contact2_favorite = is_favorite
                        else:  # contact_count == 2
                            contact3_name = name.title()
                            contact3_phone = phone
                            contact3_age = age
                            contact3_favorite = is_favorite
                        
                        contact_count += 1
                        
                        # Display confirmation
                        print(f"\n✓ Contact added successfully!")
                        print("╔" + "═"*30 + "╗")
                        print("║  CONTACT CARD" + " "*16 + "║")
                        print("║" + "-"*30 + "║")
                        print(f"║  Name: {name.title():<21} ║")
                        print(f"║  Phone: {phone:<20} ║")
                        print(f"║  Age: {age:<22} ║")
                        if is_favorite:
                            print("║  ⭐ FAVORITE CONTACT ⭐" + " "*6 + "║")
                        print("╚" + "═"*30 + "╝")
    
    elif choice == "2":
        # View all contacts
        print("\n--- ALL CONTACTS ---")
        
        if contact_count == 0:
            print("No contacts to display.")
        else:
            # Display contact 1
            if contact_count >= 1:
                print(f"\nContact #1:")
                print(f"  Name: {contact1_name}", end="")
                if contact1_favorite:
                    print(" ⭐", end="")
                print()
                print(f"  Phone: {contact1_phone}")
                print(f"  Age: {contact1_age}")
                
                # Determine age category
                if contact1_age < 18:
                    print("  Category: Minor")
                elif contact1_age <= 30:
                    print("  Category: Young Adult")
                elif contact1_age <= 60:
                    print("  Category: Adult")
                else:
                    print("  Category: Senior")
            
            # Display contact 2
            if contact_count >= 2:
                print(f"\nContact #2:")
                print(f"  Name: {contact2_name}", end="")
                if contact2_favorite:
                    print(" ⭐", end="")
                print()
                print(f"  Phone: {contact2_phone}")
                print(f"  Age: {contact2_age}")
                
                # Determine age category
                if contact2_age < 18:
                    print("  Category: Minor")
                elif contact2_age <= 30:
                    print("  Category: Young Adult")
                elif contact2_age <= 60:
                    print("  Category: Adult")
                else:
                    print("  Category: Senior")
            
            # Display contact 3
            if contact_count >= 3:
                print(f"\nContact #3:")
                print(f"  Name: {contact3_name}", end="")
                if contact3_favorite:
                    print(" ⭐", end="")
                print()
                print(f"  Phone: {contact3_phone}")
                print(f"  Age: {contact3_age}")
                
                # Determine age category
                if contact3_age < 18:
                    print("  Category: Minor")
                elif contact3_age <= 30:
                    print("  Category: Young Adult")
                elif contact3_age <= 60:
                    print("  Category: Adult")
                else:
                    print("  Category: Senior")
    
    elif choice == "3":
        # Search contacts
        if contact_count == 0:
            print("\n❌ No contacts to search.")
        else:
            print("\n--- SEARCH CONTACTS ---")
            search_term = input("Enter search term: ").lower()
            
            found_count = 0
            print("\nSearch Results:")
            
            # Search contact 1
            if contact_count >= 1:
                if search_term in contact1_name.lower() or search_term in contact1_phone:
                    print(f"  ✓ {contact1_name}: {contact1_phone}")
                    found_count += 1
            
            # Search contact 2
            if contact_count >= 2:
                if search_term in contact2_name.lower() or search_term in contact2_phone:
                    print(f"  ✓ {contact2_name}: {contact2_phone}")
                    found_count += 1
            
            # Search contact 3
            if contact_count >= 3:
                if search_term in contact3_name.lower() or search_term in contact3_phone:
                    print(f"  ✓ {contact3_name}: {contact3_phone}")
                    found_count += 1
            
            if found_count == 0:
                print(f"  No contacts found matching '{search_term}'")
            else:
                print(f"\nFound {found_count} matching contact(s)")
    
    elif choice == "4":
        # View statistics
        print("\n--- CONTACT STATISTICS ---")
        print(f"Total contacts: {contact_count}/{max_contacts}")
        
        if contact_count > 0:
            # Count favorites
            favorite_count = 0
            if contact_count >= 1 and contact1_favorite:
                favorite_count += 1
            if contact_count >= 2 and contact2_favorite:
                favorite_count += 1
            if contact_count >= 3 and contact3_favorite:
                favorite_count += 1
            
            print(f"Favorite contacts: {favorite_count}")
            
            # Calculate average age
            total_age = 0
            if contact_count >= 1:
                total_age += contact1_age
            if contact_count >= 2:
                total_age += contact2_age
            if contact_count >= 3:
                total_age += contact3_age
            
            average_age = total_age / contact_count
            print(f"Average age: {average_age:.1f} years")
            
            # Count age categories
            minor_count = 0
            young_adult_count = 0
            adult_count = 0
            senior_count = 0
            
            if contact_count >= 1:
                if contact1_age < 18:
                    minor_count += 1
                elif contact1_age <= 30:
                    young_adult_count += 1
                elif contact1_age <= 60:
                    adult_count += 1
                else:
                    senior_count += 1
            
            if contact_count >= 2:
                if contact2_age < 18:
                    minor_count += 1
                elif contact2_age <= 30:
                    young_adult_count += 1
                elif contact2_age <= 60:
                    adult_count += 1
                else:
                    senior_count += 1
            
            if contact_count >= 3:
                if contact3_age < 18:
                    minor_count += 1
                elif contact3_age <= 30:
                    young_adult_count += 1
                elif contact3_age <= 60:
                    adult_count += 1
                else:
                    senior_count += 1
            
            print("\nAge Categories:")
            if minor_count > 0:
                print(f"  Minors: {minor_count}")
            if young_adult_count > 0:
                print(f"  Young Adults: {young_adult_count}")
            if adult_count > 0:
                print(f"  Adults: {adult_count}")
            if senior_count > 0:
                print(f"  Seniors: {senior_count}")
    
    elif choice == "5":
        # Exit
        print("\n" + "="*40)
        print("Thank you for using Contact Manager!")
        print(f"You created {contact_count} contact(s)")
        print("="*40)
        running = False
    
    else:
        print("\n❌ Invalid choice! Please enter 1-5.")

# ============================================================================
# INDIVIDUAL FEATURE SOLUTIONS
# ============================================================================

# Solution 1: Storing a single contact
"""
contact_name = "Alice Smith"
contact_phone = "555-0001"
contact_age = 25
is_favorite = True

print(f"Welcome, {contact_name}!")
print(f"Next year you'll be {contact_age + 1} years old")
"""

# Solution 2: Getting user input with validation
"""
contact_name = input("Enter contact name: ")
contact_phone = input("Enter phone number: ")
age_text = input("Enter age: ")
contact_age = int(age_text)
favorite_input = input("Is this a favorite? (y/n): ")
is_favorite = favorite_input.lower() == 'y'

print(f"Contact: {contact_name}")
print(f"Phone: {contact_phone}")
print(f"Age: {contact_age}")
if is_favorite:
    print("⭐ This is a favorite contact!")
"""

# Solution 3: Input validation
"""
contact_name = input("Enter name: ")
contact_phone = input("Enter phone: ")

# Check if name is not empty
if contact_name == "":
    print("❌ Error: Name cannot be empty!")
    contact_name = "Unknown"

# Check if phone has at least 7 digits
if len(contact_phone) < 7:
    print("⚠️ Warning: Phone number seems too short")

# Only mark as valid if both checks pass
is_valid = contact_name != "Unknown" and len(contact_phone) >= 7
if is_valid:
    print("✓ Contact is valid!")
"""

# Solution 4: Age categorization
"""
contact_age = int(input("Contact's age: "))

if contact_age < 18:
    category = "Minor"
    note = "Requires parental consent"
elif contact_age <= 30:
    category = "Young Adult"
    note = "Digital native generation"
elif contact_age <= 60:
    category = "Adult"
    note = "Primary contact demographic"
else:
    category = "Senior"
    note = "May prefer phone calls"

print(f"Category: {category}")
print(f"Note: {note}")
"""

# Solution 5: Menu system
"""
print("\\n--- Contact Manager Menu ---")
print("1. Add contact")
print("2. View contact")
print("3. Exit")

choice = input("\\nChoose option: ")

if choice == "1":
    print("Adding contact...")
elif choice == "2":
    print("Viewing contact...")
elif choice == "3":
    print("Goodbye!")
else:
    print("Invalid option!")
"""

# Solution 6: Contact card formatting
"""
name = "Alice Smith"
phone = "555-0001"
age = 25

# Using f-strings for formatting
card = f\"\"\"
╔════════════════════════════╗
║  CONTACT CARD              ║
║  Name: {name:<20} ║
║  Phone: {phone:<19} ║
║  Age: {age:<21} ║
╚════════════════════════════╝
\"\"\"
print(card)
"""

# Solution 7: String operations
"""
contact_name = "  alice SMITH  "
contact_phone = "5550001"

# Clean up the contact data
contact_name = contact_name.strip()  # Remove extra spaces
contact_name = contact_name.title()  # Capitalize properly
print(f"Cleaned name: {contact_name}")

# Format phone number
if len(contact_phone) == 7:
    formatted_phone = contact_phone[:3] + "-" + contact_phone[3:]
    print(f"Formatted phone: {formatted_phone}")

# Validate the cleaned data
if len(contact_name) >= 2:
    print("✓ Name is valid")
else:
    print("❌ Name too short")

if len(contact_phone) == 7 and contact_phone.isdigit():
    print("✓ Phone is valid")
else:
    print("❌ Invalid phone number")
"""