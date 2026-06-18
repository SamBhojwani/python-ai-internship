"""
student_manager.py
------------------
A menu-driven program to manage student records.
Records are stored in memory using dictionaries.

Usage:
    python student_manager.py
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# In-memory student database
students: dict[str, dict] = {}


def add_student() -> None:
    """Add a new student record."""
    student_id = input("Enter Student ID: ").strip()

    if student_id in students:
        print(f"Student with ID {student_id} already exists.")
        return

    name = input("Enter Name: ").strip()
    department = input("Enter Department: ").strip()

    try:
        cgpa = float(input("Enter CGPA: ").strip())
        if not (0.0 <= cgpa <= 10.0):
            raise ValueError("CGPA must be between 0.0 and 10.0")
    except ValueError as e:
        print(f"Invalid CGPA: {e}")
        return

    students[student_id] = {
        "name": name,
        "department": department,
        "cgpa": cgpa
    }
    logger.info(f"Student {student_id} added.")
    print(f"Student {name} added successfully.")


def update_student() -> None:
    """Update an existing student record."""
    student_id = input("Enter Student ID to update: ").strip()

    if student_id not in students:
        print(f"No student found with ID {student_id}.")
        return

    print("What would you like to update?")
    print("1. Name")
    print("2. Department")
    print("3. CGPA")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        students[student_id]["name"] = input("Enter new name: ").strip()
        print("Name updated.")
    elif choice == "2":
        students[student_id]["department"] = input("Enter new department: ").strip()
        print("Department updated.")
    elif choice == "3":
        try:
            cgpa = float(input("Enter new CGPA: ").strip())
            if not (0.0 <= cgpa <= 10.0):
                raise ValueError("CGPA must be between 0.0 and 10.0")
            students[student_id]["cgpa"] = cgpa
            print("CGPA updated.")
        except ValueError as e:
            print(f"Invalid CGPA: {e}")
    else:
        print("Invalid choice.")

    logger.info(f"Student {student_id} updated.")


def delete_student() -> None:
    """Delete a student record by ID."""
    student_id = input("Enter Student ID to delete: ").strip()

    if student_id not in students:
        print(f"No student found with ID {student_id}.")
        return

    name = students[student_id]["name"]
    del students[student_id]
    logger.info(f"Student {student_id} deleted.")
    print(f"Student {name} deleted successfully.")


def search_student() -> None:
    """Search and display a student record by ID."""
    student_id = input("Enter Student ID to search: ").strip()

    if student_id not in students:
        print(f"No student found with ID {student_id}.")
        return

    s = students[student_id]
    print("\n" + "-" * 30)
    print(f"ID         : {student_id}")
    print(f"Name       : {s['name']}")
    print(f"Department : {s['department']}")
    print(f"CGPA       : {s['cgpa']}")
    print("-" * 30)


def display_all() -> None:
    """Display all student records."""
    if not students:
        print("No student records found.")
        return

    print("\n" + "=" * 50)
    print(f"{'ID':<10} {'Name':<20} {'Department':<20} {'CGPA'}")
    print("=" * 50)
    for sid, s in students.items():
        print(f"{sid:<10} {s['name']:<20} {s['department']:<20} {s['cgpa']}")
    print("=" * 50)


def main() -> None:
    """Main loop — show menu and handle user input."""
    print("Welcome to Student Record Manager")

    while True:
        print("\n--- Menu ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Display All Students")
        print("6. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            search_student()
        elif choice == "5":
            display_all()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()