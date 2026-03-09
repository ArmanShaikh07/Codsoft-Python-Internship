import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import webbrowser

# ---------- WINDOW ----------
root = tk.Tk()
root.title("Smart Contact Book")
root.geometry("900x580")
root.config(bg="#f5f7fa")

contacts = []

# ---------- VARIABLES ----------
name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()
search_var = tk.StringVar()

file_name = "contacts.json"

# ---------- FUNCTIONS ----------

def save_contacts():
    with open(file_name, "w") as f:
        json.dump(contacts, f)

def load_contacts():
    global contacts
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            contacts = json.load(f)
        show_contacts()

def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")

def add_contact():

    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    address = address_var.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Name & Phone Required")
        return

    contacts.append([name, phone, email, address])
    save_contacts()
    show_contacts()
    clear_fields()

def show_contacts():

    table.delete(*table.get_children())

    for contact in contacts:
        table.insert("", tk.END, values=contact)

def select_contact(event):

    selected = table.focus()
    data = table.item(selected, "values")

    if data:
        name_var.set(data[0])
        phone_var.set(data[1])
        email_var.set(data[2])
        address_var.set(data[3])

def update_contact():

    selected = table.focus()

    if selected:
        index = table.index(selected)

        contacts[index] = [
            name_var.get(),
            phone_var.get(),
            email_var.get(),
            address_var.get()
        ]

        save_contacts()
        show_contacts()
        clear_fields()

def delete_contact():

    selected = table.focus()

    if selected:
        index = table.index(selected)

        contacts.pop(index)

        save_contacts()
        show_contacts()
        clear_fields()

def search_contact():

    keyword = search_var.get().lower()

    table.delete(*table.get_children())

    for contact in contacts:

        if keyword in contact[0].lower() or keyword in contact[1]:
            table.insert("", tk.END, values=contact)

# ---------- CALL ----------
def call_contact():

    phone = phone_var.get()

    if phone == "":
        messagebox.showwarning("Warning", "Select contact first")
        return

    webbrowser.open(f"tel:{phone}")

# ---------- WHATSAPP ----------
def whatsapp_contact():

    phone = phone_var.get()

    if phone == "":
        messagebox.showwarning("Warning", "Select contact first")
        return

    webbrowser.open(f"https://wa.me/{phone}")

# ---------- TITLE ----------
title = tk.Label(
    root,
    text="📒 Smart Contact Book",
    font=("Segoe UI",22,"bold"),
    bg="#1976d2",
    fg="white",
    pady=12
)

title.pack(fill="x")

# ---------- INPUT FRAME ----------
frame = tk.Frame(root, bg="#f5f7fa")
frame.pack(pady=15)

tk.Label(frame,text="Name",bg="#f5f7fa").grid(row=0,column=0,padx=10)
tk.Entry(frame,textvariable=name_var,width=25).grid(row=0,column=1)

tk.Label(frame,text="Phone",bg="#f5f7fa").grid(row=0,column=2)
tk.Entry(frame,textvariable=phone_var,width=25).grid(row=0,column=3)

tk.Label(frame,text="Email",bg="#f5f7fa").grid(row=1,column=0)
tk.Entry(frame,textvariable=email_var,width=25).grid(row=1,column=1)

tk.Label(frame,text="Address",bg="#f5f7fa").grid(row=1,column=2)
tk.Entry(frame,textvariable=address_var,width=25).grid(row=1,column=3)

# ---------- SEARCH ----------
search_frame = tk.Frame(root, bg="#f5f7fa")
search_frame.pack()

tk.Entry(search_frame,textvariable=search_var,width=35).grid(row=0,column=0,padx=5)

tk.Button(search_frame,text="Search",
          bg="#ff9800",fg="white",
          command=search_contact).grid(row=0,column=1)

tk.Button(search_frame,text="View All",
          bg="#2196f3",fg="white",
          command=show_contacts).grid(row=0,column=2,padx=5)

# ---------- BUTTONS ----------
btn_frame = tk.Frame(root, bg="#f5f7fa")
btn_frame.pack(pady=10)

tk.Button(btn_frame,text="Add",width=10,
          bg="#4caf50",fg="white",
          command=add_contact).grid(row=0,column=0,padx=5)

tk.Button(btn_frame,text="Update",width=10,
          bg="#9c27b0",fg="white",
          command=update_contact).grid(row=0,column=1,padx=5)

tk.Button(btn_frame,text="Delete",width=10,
          bg="#f44336",fg="white",
          command=delete_contact).grid(row=0,column=2,padx=5)

tk.Button(btn_frame,text="Clear",width=10,
          command=clear_fields).grid(row=0,column=3,padx=5)

tk.Button(btn_frame,text="📞 Call",width=10,
          bg="#009688",fg="white",
          command=call_contact).grid(row=0,column=4,padx=5)

tk.Button(btn_frame,text="💬 WhatsApp",width=12,
          bg="#25D366",fg="white",
          command=whatsapp_contact).grid(row=0,column=5,padx=5)

# ---------- TABLE ----------
columns=("Name","Phone","Email","Address")

table=ttk.Treeview(root,columns=columns,show="headings",height=12)

for col in columns:
    table.heading(col,text=col)
    table.column(col,width=200)

table.pack(pady=15)

table.bind("<<TreeviewSelect>>",select_contact)

# ---------- LOAD DATA ----------
load_contacts()

# ---------- RUN ----------
root.mainloop()
