import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Smart Task Manager")
root.geometry("650x700")
root.configure(bg="#f4f6f9")
root.resizable(False, False)

# ---------------- ACTIVITY LOG FUNCTION ----------------
def log_activity(message):
    time = datetime.now().strftime("%H:%M:%S")
    activity_box.insert(tk.END, f"[{time}] {message}\n")
    activity_box.see(tk.END)

# ---------------- ADD TASK ----------------
def add_task():
    text = entry.get().strip()

    if text == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return

    create_task_card(text)
    log_activity(f"Task Added: {text}")
    entry.delete(0, tk.END)

# ---------------- CREATE TASK CARD ----------------
def create_task_card(text):
    card = tk.Frame(task_container, bg="white", bd=1, relief="solid")
    card.pack(fill="x", padx=15, pady=8)

    task_var = tk.StringVar(value=text)

    task_label = tk.Label(
        card,
        textvariable=task_var,
        font=("Segoe UI", 12),
        bg="white",
        anchor="w"
    )
    task_label.pack(fill="x", padx=10, pady=5)

    # -------- BUTTON FUNCTIONS --------
    def mark_done():
        task_label.config(fg="gray", font=("Segoe UI", 12, "overstrike"))
        log_activity(f"Marked as Done: {task_var.get()}")

    def delete_task():
        log_activity(f"Deleted Task: {task_var.get()}")
        card.destroy()

    def update_task():
        new_text = simpledialog.askstring("Update Task", "Enter new task:")
        if new_text:
            log_activity(f"Updated Task: {task_var.get()} → {new_text}")
            task_var.set(new_text)
            task_label.config(fg="black", font=("Segoe UI", 12))

    def mark_important():
        task_label.config(fg="red", font=("Segoe UI", 12, "bold"))
        log_activity(f"Marked Important: {task_var.get()}")

    # -------- BUTTON FRAME --------
    btn_frame = tk.Frame(card, bg="white")
    btn_frame.pack(pady=5)

    tk.Button(btn_frame, text="Mark As Done", width=15,
              bg="#22c55e", fg="white",
              command=mark_done).grid(row=0, column=0, padx=5, pady=5)

    tk.Button(btn_frame, text="Update", width=10,
              bg="#3b82f6", fg="white",
              command=update_task).grid(row=0, column=1, padx=5, pady=5)

    tk.Button(btn_frame, text="Delete", width=10,
              bg="#ef4444", fg="white",
              command=delete_task).grid(row=0, column=2, padx=5, pady=5)

    tk.Button(btn_frame, text="Important", width=10,
              bg="#f59e0b", fg="white",
              command=mark_important).grid(row=0, column=3, padx=5, pady=5)

# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="Smart Task Manager",
    font=("Segoe UI", 22, "bold"),
    bg="#1e40af",
    fg="white",
    pady=15
)
title.pack(fill="x")

# ---------------- INPUT ----------------
input_frame = tk.Frame(root, bg="#f4f6f9")
input_frame.pack(pady=15)

entry = tk.Entry(input_frame, font=("Segoe UI", 14), width=35)
entry.grid(row=0, column=0, padx=10)

tk.Button(
    input_frame,
    text="Add Task",
    bg="#1e40af",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    command=add_task
).grid(row=0, column=1)

# ---------------- TASK AREA ----------------
canvas = tk.Canvas(root, bg="#f4f6f9", highlightthickness=0, height=300)
canvas.pack(side="top", fill="both", expand=False)

scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

task_container = tk.Frame(canvas, bg="#f4f6f9")
canvas.create_window((0, 0), window=task_container, anchor="nw")

def configure_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

task_container.bind("<Configure>", configure_scroll)

# ---------------- ACTIVITY LOG BOX ----------------
log_label = tk.Label(root, text="Activity Log",
                     font=("Segoe UI", 14, "bold"),
                     bg="#f4f6f9")
log_label.pack(pady=(15, 5))

activity_box = tk.Text(root, height=8, width=75,
                       font=("Consolas", 10),
                       bg="black", fg="lime")
activity_box.pack(padx=15, pady=5)

# ---------------- RUN ----------------
root.mainloop()
