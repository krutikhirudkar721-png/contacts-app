import json
import os
import tkinter as tk
from tkinter import messagebox

# ---------- Contact Class ----------
class Contact:
    def __init__(self, name, phone):
        self.name = name.strip()
        self.phone = phone.strip()

    def to_dict(self):
        return {"name": self.name, "phone": self.phone}


# ---------- Data Handling ----------
contacts = []

def load_contacts():
    global contacts
    if os.path.exists("contacts.json"):
        try:
            with open("contacts.json", "r") as file:
                data = json.load(file)
                contacts = [Contact(i["name"], i["phone"]) for i in data]
        except:
            contacts = []

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump([c.to_dict() for c in contacts], file, indent=4)


# ---------- Validation ----------
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) >= 10

def contact_exists(name):
    return any(c.name.lower() == name.lower() for c in contacts)


# ---------- Functions ----------
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()

    if not name:
        messagebox.showerror("Error", "Name cannot be empty")
        return

    if not is_valid_phone(phone):
        messagebox.showerror("Error", "Invalid phone number")
        return

    if contact_exists(name):
        messagebox.showerror("Error", "Contact already exists")
        return

    contacts.append(Contact(name, phone))
    save_contacts()
    update_listbox()
    clear_fields()
    messagebox.showinfo("Success", "Contact Added")

def view_contacts():
    update_listbox()

def search_contact():
    name = name_entry.get()
    listbox.delete(0, tk.END)

    for c in contacts:
        if c.name.lower() == name.lower():
            listbox.insert(tk.END, f"{c.name} - {c.phone}")
            return

    messagebox.showinfo("Result", "Contact not found")

def delete_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a contact")
        return

    index = selected[0]
    del contacts[index]
    save_contacts()
    update_listbox()

def update_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a contact")
        return

    index = selected[0]
    new_phone = phone_entry.get()

    if not is_valid_phone(new_phone):
        messagebox.showerror("Error", "Invalid phone")
        return

    contacts[index].phone = new_phone
    save_contacts()
    update_listbox()
    messagebox.showinfo("Success", "Updated")

def update_listbox():
    listbox.delete(0, tk.END)
    for c in contacts:
        listbox.insert(tk.END, f"{c.name} - {c.phone}")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)


# ---------- GUI Setup ----------
root = tk.Tk()
root.title("Contact Manager")
root.geometry("400x500")

# Labels & Entries
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

# Buttons
tk.Button(root, text="Add", command=add_contact).pack(pady=5)
tk.Button(root, text="View", command=view_contacts).pack(pady=5)
tk.Button(root, text="Search", command=search_contact).pack(pady=5)
tk.Button(root, text="Delete", command=delete_contact).pack(pady=5)
tk.Button(root, text="Update", command=update_contact).pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

# Load data and start
load_contacts()
update_listbox()

root.mainloop()
