import tkinter as tk
import random

# ---------- VARIABLES ----------
choices = ["Rock", "Paper", "Scissors"]
emojis = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂"}

user_score = 0
computer_score = 0
rounds = 0
max_rounds = 5

# ---------- COUNTDOWN ----------
def countdown(user_choice, count=3):

    if count > 0:
        result_label.config(text=f"Computer thinking... {count}")
        root.after(1000, countdown, user_choice, count-1)
    else:
        play_game(user_choice)

# ---------- GAME LOGIC ----------
def play(user_choice):
    countdown(user_choice)

def play_game(user_choice):

    global user_score, computer_score, rounds

    computer_choice = random.choice(choices)
    rounds += 1

    user_label.config(text=f"You: {emojis[user_choice]} {user_choice}")
    comp_label.config(text=f"Computer: {emojis[computer_choice]} {computer_choice}")

    if user_choice == computer_choice:
        result = "Tie 🤝"

    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):

        result = "You Win 🎉"
        user_score += 1
    else:
        result = "Computer Wins 💻"
        computer_score += 1

    animate_result(result)

    score_label.config(
        text=f"Score → You: {user_score} | Computer: {computer_score}"
    )

    round_label.config(
        text=f"Round: {rounds}/{max_rounds}"
    )

    check_winner()

# ---------- RESULT ANIMATION ----------
colors = ["#ff5252","#ff9800","#4caf50","#2196f3","#9c27b0"]

def animate_result(text, i=0):

    result_label.config(text=text, fg=colors[i % len(colors)])

    if i < 10:
        root.after(150, animate_result, text, i+1)

# ---------- GAME WINNER ----------
def check_winner():

    if rounds >= max_rounds:

        if user_score > computer_score:
            result_label.config(text="🏆 You Won The Game!")
        elif computer_score > user_score:
            result_label.config(text="💻 Computer Won The Game!")
        else:
            result_label.config(text="🤝 Game Tie!")

# ---------- RESET ----------
def reset_game():

    global user_score, computer_score, rounds

    user_score = 0
    computer_score = 0
    rounds = 0

    user_label.config(text="You:")
    comp_label.config(text="Computer:")
    result_label.config(text="Choose your move")

    score_label.config(text="Score → You: 0 | Computer: 0")
    round_label.config(text=f"Round: 0/{max_rounds}")

# ---------- MODE CHANGE ----------
def change_mode():

    global max_rounds

    mode = mode_var.get()

    if mode == "Best of 5":
        max_rounds = 5
    else:
        max_rounds = 10

    reset_game()

# ---------- WINDOW ----------
root = tk.Tk()
root.title("Rock Paper Scissors Pro")
root.geometry("440x520")
root.config(bg="#1e1e2f")
root.resizable(False, False)

# ---------- TITLE ----------
title = tk.Label(
    root,
    text="🎮 Rock Paper Scissors",
    font=("Segoe UI",20,"bold"),
    bg="#3949ab",
    fg="white",
    pady=12
)

title.pack(fill="x")

# ---------- MODE ----------
mode_var = tk.StringVar(value="Best of 5")

mode_frame = tk.Frame(root,bg="#1e1e2f")
mode_frame.pack(pady=10)

tk.Label(mode_frame,text="Game Mode:",
         bg="#1e1e2f",fg="white",
         font=("Segoe UI",11)).grid(row=0,column=0)

mode_menu = tk.OptionMenu(mode_frame,mode_var,"Best of 5","Best of 10",
                          command=lambda x: change_mode())

mode_menu.config(width=10)
mode_menu.grid(row=0,column=1,padx=10)

# ---------- ROUND ----------
round_label = tk.Label(
    root,
    text="Round: 0/5",
    font=("Segoe UI",12,"bold"),
    bg="#1e1e2f",
    fg="white"
)

round_label.pack()

# ---------- BUTTONS ----------
btn_frame = tk.Frame(root,bg="#1e1e2f")
btn_frame.pack(pady=20)

tk.Button(btn_frame,text="🪨 Rock",
          width=12,height=2,
          bg="#444",fg="white",
          font=("Segoe UI",11,"bold"),
          command=lambda: play("Rock")).grid(row=0,column=0,padx=8)

tk.Button(btn_frame,text="📄 Paper",
          width=12,height=2,
          bg="#444",fg="white",
          font=("Segoe UI",11,"bold"),
          command=lambda: play("Paper")).grid(row=0,column=1,padx=8)

tk.Button(btn_frame,text="✂ Scissors",
          width=12,height=2,
          bg="#444",fg="white",
          font=("Segoe UI",11,"bold"),
          command=lambda: play("Scissors")).grid(row=0,column=2,padx=8)

# ---------- DISPLAY ----------
user_label = tk.Label(root,text="You:",
                      font=("Segoe UI",13),
                      bg="#1e1e2f",fg="white")

user_label.pack(pady=10)

comp_label = tk.Label(root,text="Computer:",
                      font=("Segoe UI",13),
                      bg="#1e1e2f",fg="white")

comp_label.pack()

result_label = tk.Label(root,
                        text="Choose your move",
                        font=("Segoe UI",15,"bold"),
                        bg="#1e1e2f",
                        fg="lightgreen")

result_label.pack(pady=15)

# ---------- SCORE ----------
score_label = tk.Label(root,
                       text="Score → You: 0 | Computer: 0",
                       font=("Segoe UI",12,"bold"),
                       bg="#1e1e2f",
                       fg="white")

score_label.pack(pady=10)

# ---------- RESET ----------
tk.Button(root,
          text="🔄 Reset Game",
          width=18,
          height=2,
          bg="#e53935",
          fg="white",
          font=("Segoe UI",11,"bold"),
          command=reset_game).pack(pady=20)

# ---------- RUN ----------
root.mainloop()
