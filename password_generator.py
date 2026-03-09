import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------- FUNCTIONS ----------

def update_length(val):
    length_value.config(text=str(int(float(val))))

def toggle_password():
    if password_box.cget("show") == "":
        password_box.config(show="*")
        show_btn.config(text="Show")
    else:
        password_box.config(show="")
        show_btn.config(text="Hide")

def generate_password():

    length = int(length_slider.get())

    chars = ""

    if lower_var.get():
        chars += string.ascii_lowercase
    if upper_var.get():
        chars += string.ascii_uppercase
    if num_var.get():
        chars += string.digits
    if sym_var.get():
        chars += string.punctuation

    if chars == "":
        messagebox.showwarning("Warning", "Select at least one option!")
        return

    password = "".join(random.choice(chars) for _ in range(length))

    password_var.set(password)

    check_strength(password)

def check_strength(password):

    score = 0

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        strength_label.config(text="Strength: Weak", fg="red")
    elif score == 3:
        strength_label.config(text="Strength: Medium", fg="orange")
    else:
        strength_label.config(text="Strength: Strong", fg="green")

def copy_password():

    password = password_var.get()

    if password == "":
        messagebox.showwarning("Warning", "Generate password first")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    status_label.config(text="Password copied")

def clear_all():

    password_var.set("")
    strength_label.config(text="")
    status_label.config(text="Cleared")

# ---------- WINDOW ----------

root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("420x620")
root.config(bg="#1e1e2f")
root.resizable(False, False)

# ---------- TITLE ----------

title = tk.Label(
    root,
    text="🔐 Advanced Password Generator",
    font=("Segoe UI",18,"bold"),
    bg="#3f51b5",
    fg="white",
    pady=10
)

title.pack(fill="x")

# ---------- LENGTH SLIDER ----------

length_frame = tk.Frame(root,bg="#1e1e2f")
length_frame.pack(pady=15)

tk.Label(
    length_frame,
    text="Password Length",
    bg="#1e1e2f",
    fg="white",
    font=("Segoe UI",12)
).pack()

length_slider = tk.Scale(
    length_frame,
    from_=4,
    to=30,
    orient="horizontal",
    command=update_length,
    bg="#1e1e2f",
    fg="white",
    troughcolor="#444",
    highlightthickness=0
)

length_slider.set(12)
length_slider.pack()

length_value = tk.Label(
    length_frame,
    text="12",
    bg="#1e1e2f",
    fg="lightgreen",
    font=("Segoe UI",11,"bold")
)

length_value.pack()

# ---------- OPTIONS ----------

options_frame = tk.LabelFrame(
    root,
    text="Password Options",
    bg="#1e1e2f",
    fg="white",
    font=("Segoe UI",11,"bold"),
    padx=10,
    pady=10
)

options_frame.pack(pady=10,fill="x",padx=20)

lower_var = tk.IntVar(value=1)
upper_var = tk.IntVar(value=1)
num_var = tk.IntVar(value=1)
sym_var = tk.IntVar(value=1)

tk.Checkbutton(options_frame,text="Lowercase (a-z)",variable=lower_var,bg="#1e1e2f",fg="white",selectcolor="#333").pack(anchor="w")
tk.Checkbutton(options_frame,text="Uppercase (A-Z)",variable=upper_var,bg="#1e1e2f",fg="white",selectcolor="#333").pack(anchor="w")
tk.Checkbutton(options_frame,text="Numbers (0-9)",variable=num_var,bg="#1e1e2f",fg="white",selectcolor="#333").pack(anchor="w")
tk.Checkbutton(options_frame,text="Symbols (!@#)",variable=sym_var,bg="#1e1e2f",fg="white",selectcolor="#333").pack(anchor="w")

# ---------- GENERATE BUTTON ----------

tk.Button(
    root,
    text="Generate Password",
    font=("Segoe UI",12,"bold"),
    bg="#4CAF50",
    fg="white",
    width=22,
    height=2,
    command=generate_password
).pack(pady=10)

# ---------- PASSWORD DISPLAY ----------

password_var = tk.StringVar()

password_frame = tk.Frame(root,bg="#1e1e2f")
password_frame.pack(pady=10)

password_box = tk.Entry(
    password_frame,
    textvariable=password_var,
    font=("Consolas",16),
    width=20,
    justify="center",
    bd=3,
    relief="ridge"
)

password_box.grid(row=0,column=0,padx=5)

show_btn = tk.Button(
    password_frame,
    text="Show",
    command=toggle_password,
    bg="#2196F3",
    fg="white"
)

show_btn.grid(row=0,column=1)

# ---------- STRENGTH ----------

strength_label = tk.Label(
    root,
    text="",
    bg="#1e1e2f",
    font=("Segoe UI",11,"bold")
)

strength_label.pack(pady=5)

# ---------- BUTTONS ----------

btn_frame = tk.Frame(root,bg="#1e1e2f")
btn_frame.pack(pady=15)

tk.Button(
    btn_frame,
    text="Copy",
    width=14,
    height=2,
    bg="#009688",
    fg="white",
    command=copy_password
).grid(row=0,column=0,padx=10)

tk.Button(
    btn_frame,
    text="Clear",
    width=14,
    height=2,
    bg="#f44336",
    fg="white",
    command=clear_all
).grid(row=0,column=1,padx=10)

# ---------- STATUS ----------

status_label = tk.Label(
    root,
    text="Select options and generate password",
    bg="#1e1e2f",
    fg="lightgray",
    font=("Segoe UI",10)
)

status_label.pack(pady=10)

# ---------- RUN ----------

root.mainloop()
