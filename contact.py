import json
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def to_dict(self):
        return {"name": self.name, "phone": self.phone}
        
# Load contacts
contacts = []
try:
    with open("contacts.json", "r") as file:
        data = json.load(file)
        for item in data:
            contacts.append(Contact(item["name"], item["phone"]))
except:
    pass
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump([contact.to_dict() for contact in contacts], file)
        
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    new_contact = Contact(name, phone)
    contacts.append(new_contact)
    save_contacts()
    print("Contact Added Successfully!\n")


def view_contacts():
    if not contacts:
        print("No Contacts Found.\n")
    else:
        for contact in contacts:
            print("Name:", contact.name)
            print("Phone:", contact.phone)
            print("-" * 20)


def search_contact():
    name = input("Enter name to search: ")
    for contact in contacts:
        if contact.name.lower() == name.lower():
            print("Name:", contact.name)
            print("Phone:", contact.phone)
            print("-" * 20)
            return
    print("Contact not found.\n")


def delete_contact():
    name = input("Enter name to delete: ")
    for contact in contacts:
        if contact.name.lower() == name.lower():
            contacts.remove(contact)
            save_contacts()
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")


def update_contact():
    name = input("Enter name to update: ")
    for contact in contacts:
        if contact.name.lower() == name.lower():
            contact.phone = input("Enter new phone number: ")
            save_contacts()
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")


while True:
    print("===== CONTACT LIST MENU =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")
    choice = input("Enter choice: ")

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
        print("Program Closed")
        break
    else:
        print("Invalid Choice\n")




