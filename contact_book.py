import tkinter as tk
from tkinter import messagebox, filedialog
import json
import os

# Load contacts from JSON file
def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as file:
            return json.load(file)
    return {}

# Save contacts to JSON file
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

# Add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        save_contacts()
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showerror("Error", "Name and phone number are required!")

# Update the list of contacts displayed
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"{name} - {info['phone']}")

# Clear the entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Search for a contact
def search_contact():
    search_term = search_entry.get()
    if search_term:
        for name, info in contacts.items():
            if search_term in name or search_term in info['phone']:
                contact_list.delete(0, tk.END)
                contact_list.insert(tk.END, f"{name} - {info['phone']}")
                return
        messagebox.showinfo("Not Found", "No contact found!")
    else:
        messagebox.showerror("Error", "Please enter a name or phone number to search!")

# Select a contact from the list
def select_contact(event):
    try:
        selected_contact = contact_list.get(contact_list.curselection())
        name, phone = selected_contact.split(" - ")
        info = contacts[name]
        
        name_entry.delete(0, tk.END)
        name_entry.insert(tk.END, name)
        phone_entry.delete(0, tk.END)
        phone_entry.insert(tk.END, phone)
        email_entry.delete(0, tk.END)
        email_entry.insert(tk.END, info.get('email', ''))
        address_entry.delete(0, tk.END)
        address_entry.insert(tk.END, info.get('address', ''))
    except:
        pass

# Update an existing contact
def update_contact():
    name = name_entry.get()
    if name in contacts:
        contacts[name] = {
            "phone": phone_entry.get(),
            "email": email_entry.get(),
            "address": address_entry.get()
        }
        save_contacts()
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", "Contact updated successfully!")
    else:
        messagebox.showerror("Error", "Contact not found!")

# Delete a contact
def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        save_contacts()
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showerror("Error", "Contact not found!")

# Initialize contacts
contacts = load_contacts()

# Setup the main application window
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")
root.configure(bg="#e6f2ff")

# Input fields for contact details
tk.Label(root, text="Name", bg="#e6f2ff", fg="#000000", font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root, bg="#ffffff", fg="#000000")
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Phone", bg="#e6f2ff", fg="#000000", font=('Arial', 12, 'bold')).grid(row=1, column=0, padx=10, pady=10)
phone_entry = tk.Entry(root, bg="#ffffff", fg="#000000")
phone_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Email", bg="#e6f2ff", fg="#000000", font=('Arial', 12, 'bold')).grid(row=2, column=0, padx=10, pady=10)
email_entry = tk.Entry(root, bg="#ffffff", fg="#000000")
email_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Address", bg="#e6f2ff", fg="#000000", font=('Arial', 12, 'bold')).grid(row=3, column=0, padx=10, pady=10)
address_entry = tk.Entry(root, bg="#ffffff", fg="#000000")
address_entry.grid(row=3, column=1, padx=10, pady=10)

# Buttons for add, update, and delete
add_button = tk.Button(root, text="Add Contact", command=add_contact, bg="#4CAF50", fg="#ffffff", font=('Arial', 12, 'bold'))
add_button.grid(row=4, column=0, padx=10, pady=10)

update_button = tk.Button(root, text="Update Contact", command=update_contact, bg="#FFC107", fg="#ffffff", font=('Arial', 12, 'bold'))
update_button.grid(row=4, column=1, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, bg="#f44336", fg="#ffffff", font=('Arial', 12, 'bold'))
delete_button.grid(row=4, column=2, padx=10, pady=10)

# Search field
tk.Label(root, text="Search", bg="#e6f2ff", fg="#000000", font=('Arial', 12, 'bold')).grid(row=5, column=0, padx=10, pady=10)
search_entry = tk.Entry(root, bg="#ffffff", fg="#000000")
search_entry.grid(row=5, column=1, padx=10, pady=10)

search_button = tk.Button(root, text="Search", command=search_contact, bg="#2196F3", fg="#ffffff", font=('Arial', 12, 'bold'))
search_button.grid(row=5, column=2, padx=10, pady=10)

# Listbox to display contacts
contact_list = tk.Listbox(root, width=50, bg="#ffffff", fg="#000000")
contact_list.grid(row=6, column=0, columnspan=3, padx=10, pady=10)
contact_list.bind('<<ListboxSelect>>', select_contact)

# Populate the listbox with contacts
update_contact_list()

# Start the application
root.mainloop()
