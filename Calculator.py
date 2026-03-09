import tkinter as tk
from tkinter import messagebox

# ---------- WINDOW ----------
root = tk.Tk()
root.title("Calculator")
root.geometry("380x650")
root.configure(bg="#222831")
root.resizable(False, False)

# ---------- VARIABLE ----------
display_var = tk.StringVar()

# ---------- FUNCTIONS ----------
def click(value):
    display_var.set(display_var.get() + str(value))

def clear_all():
    display_var.set("")

def backspace():
    display_var.set(display_var.get()[:-1])

def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except:
        messagebox.showerror("Error", "Invalid Calculation")
        display_var.set("")

# Popup answer
def show_answer():
    try:
        result = eval(display_var.get())
        messagebox.showinfo("Result", f"Answer = {result}")
    except:
        messagebox.showerror("Error", "Invalid Calculation")

# ---------- TITLE ----------
title = tk.Label(root,
                 text="Simple Calculator",
                 font=("Arial", 20, "bold"),
                 bg="#00ADB5",
                 fg="white",
                 pady=10)
title.pack(fill="x")

# ---------- DISPLAY ----------
display = tk.Entry(root,
                   textvariable=display_var,
                   font=("Arial", 22),
                   justify="right",
                   bd=5,
                   relief="sunken")
display.pack(fill="x", padx=15, pady=20, ipady=10)

# ---------- BUTTON FRAME ----------
frame = tk.Frame(root, bg="#222831")
frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '%', '+']
]

# Number & operator buttons
for r in range(4):
    for c in range(4):
        btn = tk.Button(frame,
                        text=buttons[r][c],
                        font=("Arial", 16, "bold"),
                        width=5,
                        height=2,
                        bg="#393E46",
                        fg="white",
                        command=lambda ch=buttons[r][c]: click(ch))
        btn.grid(row=r, column=c, padx=8, pady=8)

# Clear Button
clear_btn = tk.Button(frame,
                      text="Clear",
                      font=("Arial", 14, "bold"),
                      width=11,
                      height=2,
                      bg="#FF5722",
                      fg="white",
                      command=clear_all)
clear_btn.grid(row=4, column=0, columnspan=2, padx=8, pady=8)

# Backspace Button
back_btn = tk.Button(frame,
                     text="Backspace",
                     font=("Arial", 14, "bold"),
                     width=11,
                     height=2,
                     bg="#3F51B5",
                     fg="white",
                     command=backspace)
back_btn.grid(row=4, column=2, columnspan=2, padx=8, pady=8)

# Equal Button
equal_btn = tk.Button(frame,
                      text="=",
                      font=("Arial", 18, "bold"),
                      width=24,
                      height=2,
                      bg="#4CAF50",
                      fg="white",
                      command=calculate)
equal_btn.grid(row=5, column=0, columnspan=4, padx=8, pady=15)

# Show Answer Button
show_btn = tk.Button(frame,
                     text="Show Answer =",
                     font=("Arial", 16, "bold"),
                     width=24,
                     height=2,
                     bg="#009688",
                     fg="white",
                     command=show_answer)

show_btn.grid(row=6, column=0, columnspan=4, padx=8, pady=5)

# ---------- RUN ----------
root.mainloop()
