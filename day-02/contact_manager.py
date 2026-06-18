"""
contact_manager.py
------------------
A CLI-based program to manage contact records.
Records are stored in memory using dictionaries.

Usage:
    python contact_manager.py
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# In-memory contact database
contacts: dict[str, dict] = {}


def add_contact() -> None:
    """Add a new contact record."""
    name = input("Enter Name: ").strip()

    if name in contacts:
        print(f"Contact with name {name} already exists.")
        return

    phone = input("Enter Phone Number: ").strip()
    if not phone.isdigit() or len(phone) != 10:
        print("Invalid phone number. Must be 10 digits.")
        return

    email = input("Enter Email Address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }
    logger.info(f"Contact {name} added.")
    print(f"Contact {name} added successfully.")


def search_contact() -> None:
    """Search for a contact by name."""
    name = input("Enter Name to search: ").strip()

    if name not in contacts:
        print(f"No contact found with name {name}.")
        return

    c = contacts[name]
    print("\n" + "-" * 30)
    print(f"Name  : {name}")
    print(f"Phone : {c['phone']}")
    print(f"Email : {c['email']}")
    print("-" * 30)


def update_contact() -> None:
    """Update an existing contact record."""
    name = input("Enter Name of contact to update: ").strip()

    if name not in contacts:
        print(f"No contact found with name {name}.")
        return

    print("What would you like to update?")
    print("1. Phone Number")
    print("2. Email Address")
    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "1":
        new_phone = input("Enter new Phone Number: ").strip()
        if not new_phone.isdigit() or len(new_phone) != 10:
            print("Invalid phone number. Must be 10 digits.")
            return
        contacts[name]["phone"] = new_phone
        logger.info(f"Contact {name} phone number updated.")
        print(f"Phone number updated successfully.")
    elif choice == "2":
        new_email = input("Enter new Email Address: ").strip()
        contacts[name]["email"] = new_email
        logger.info(f"Contact {name} email address updated.")
        print(f"Email address updated successfully.")
    else:
        print("Invalid choice. Please select 1 or 2.")


def delete_contact() -> None:
    """Delete a contact by name."""
    name = input("Enter Name to delete: ").strip()

    if name not in contacts:
        print(f"No contact found with name {name}.")
        return

    del contacts[name]
    logger.info(f"Contact {name} deleted.")
    print(f"Contact {name} deleted successfully.")


def display_contacts() -> None:
    """Display all contact records."""
    if not contacts:
        print("No contacts to display.")
        return

    print("\n" + "=" * 45)
    print(f"{'Name':<20} {'Phone':<15} {'Email'}")
    print("=" * 45)
    for name, details in contacts.items():
        print(f"{name:<20} {details['phone']:<15} {details['email']}")
    print("=" * 45)


def main() -> None:
    """Main loop — show menu and handle user input."""
    print("Welcome to Contact Manager")

    while True:
        print("\n--- Menu ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display Contacts")
        print("6. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            display_contacts()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()