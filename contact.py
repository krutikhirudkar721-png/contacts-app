import json
import os
# ---------- Contact Class ----------
class Contact:
    def __init__(self, name, phone):
        self.name = name.strip()
        self.phone = phone.strip()

    def to_dict(self):
        return {"name": self.name, "phone": self.phone}

# ---------- Load Contacts ----------
contacts = []

def load_contacts():
    global contacts
    if os.path.exists("contacts.json"):
        try:
            with open("contacts.json", "r") as file:
                data = json.load(file)
                contacts = [Contact(item["name"], item["phone"]) for item in data]
        except json.JSONDecodeError:
            print("Error: File is corrupted. Starting fresh.")
            contacts = []


# ---------- Save Contacts ----------
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump([c.to_dict() for c in contacts], file, indent=4)


# ---------- Validation ----------
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) >= 10


def contact_exists(name):
    return any(c.name.lower() == name.lower() for c in contacts)


# ---------- CRUD Operations ----------
def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()

    if not name:
        print("Name cannot be empty.\n")
        return

    if not is_valid_phone(phone):
        print("Invalid phone number.\n")
        return

    if contact_exists(name):
        print("Contact already exists.\n")
        return

    contacts.append(Contact(name, phone))
    save_contacts()
    print("Contact added successfully!\n")


def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    print("\n--- Contact List ---")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c.name} - {c.phone}")
    print()


def search_contact():
    name = input("Enter name to search: ").strip()

    for c in contacts:
        if c.name.lower() == name.lower():
            print(f"Found: {c.name} - {c.phone}\n")
            return

    print("Contact not found.\n")


def delete_contact():
    name = input("Enter name to delete: ").strip()

    for c in contacts:
        if c.name.lower() == name.lower():
            contacts.remove(c)
            save_contacts()
            print("Contact deleted successfully!\n")
            return

    print("Contact not found.\n")


def update_contact():
    name = input("Enter name to update: ").strip()

    for c in contacts:
        if c.name.lower() == name.lower():
            new_phone = input("Enter new phone: ").strip()

            if not is_valid_phone(new_phone):
                print("Invalid phone number.\n")
                return

            c.phone = new_phone
            save_contacts()
            print("Contact updated successfully!\n")
            return

    print("Contact not found.\n")


# ---------- Main Menu ----------
def main():
    load_contacts()

    while True:
        print("===== CONTACT MENU =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            print("Program closed.")
            break
        else:
            print("Invalid choice.\n")


# ---------- Run Program ----------
if __name__ == "__main__":
    main()
