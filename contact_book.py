CONTACTS_FILE = "contacts.txt"


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    with open(CONTACTS_FILE, "a") as f:
        f.write(f"{name},{phone},{email}\n")

    print(f"Contact '{name}' added successfully!\n")


def view_contacts():
    try:
        with open(CONTACTS_FILE, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No contacts found yet.\n")
        return

    if not lines:
        print("No contacts found yet.\n")
        return

    print("\n--- Contact List ---")
    for i, line in enumerate(lines, start=1):
        name, phone, email = line.strip().split(",")
        print(f"{i}. Name: {name} | Phone: {phone} | Email: {email}")
    print()


def search_contact():
    keyword = input("Enter name to search: ").strip().lower()

    try:
        with open(CONTACTS_FILE, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No contacts found yet.\n")
        return

    found = False
    for line in lines:
        name, phone, email = line.strip().split(",")
        if keyword in name.lower():
            print(f"Found -> Name: {name} | Phone: {phone} | Email: {email}")
            found = True

    if not found:
        print(f"No contact matching '{keyword}' found.")
    print()


def main_menu():
    while True:
        print("===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main_menu()