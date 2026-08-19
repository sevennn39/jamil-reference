import random
import tkinter as tk
from tkinter import messagebox, simpledialog

FUN_FACTS = [
    "Cat urine glows under a blacklight.",
    "A shrimp's heart is in its head.",
    "Dreamt is the only English word that ends in the letters mt.",
    "A dime has 118 ridges around the edge.",
    "A crocodile cannot stick its tongue out."
        ,
    "The 'sixth sick sheik's sixth sheep's sick' is believed to be the toughest tongue twister in the English language.",
]

PREDICTIONS = [
    "You'll have a great day!",
    "Someone will derail your plans...",
    "Things won't work out how you think.",
    "You may end up tired by the end of the day.",
    "It'll just be a day.",
    "You may run into some issues.",
]


def run_quiz():
    total_score = 0

    question_one = simpledialog.askstring("Quiz", "What is the capital of Australia?")
    if question_one and question_one.strip().lower() == "canberra":
        total_score += 1
        messagebox.showinfo("Quiz", "Correct! Canberra is the capital of Australia.")
    else:
        messagebox.showinfo("Quiz", "Not quite. The correct answer is Canberra.")

    question_two = simpledialog.askstring("Quiz", "What is 12 x 29?")
    if question_two and question_two.strip() == "348":
        total_score += 1
        messagebox.showinfo("Quiz", "Correct! 12 x 29 = 348.")
    else:
        messagebox.showinfo("Quiz", "Not quite. The correct answer is 348.")

    question_three = simpledialog.askstring("Quiz", "What is the powerhouse of the cell?")
    if question_three and question_three.strip().lower() == "mitochondria":
        total_score += 1
        messagebox.showinfo("Quiz", "Correct! The mitochondria are the powerhouse of the cell.")
    else:
        messagebox.showinfo("Quiz", "Not quite. The correct answer is Mitochondria.")

    messagebox.showinfo(
        "Quiz Results",
        f"This is the end of the quiz!\nTotal Score: {total_score}\nRerun the app to play something else!",
    )


def run_high_low():
    num = random.randint(1, 12)
    guess = simpledialog.askstring(
        "High Card, Low Card",
        f"Starting number: {num}\nWill the next number be higher or lower?",
    )
    if not guess:
        return

    other = random.randint(1, 12)
    if num < other:
        result = f"It was higher! [{other}]"
    elif num > other:
        result = f"It was lower! [{other}]"
    else:
        result = f"It was the same! [{other}]"

    messagebox.showinfo("High Card, Low Card", result)


def run_coin_flip():
    result = "Heads!" if random.randint(1, 2) == 1 else "Tails!"
    messagebox.showinfo("Coin Flip", result)


def run_fun_facts():
    fact = random.choice(FUN_FACTS)
    messagebox.showinfo("Fun Facts", f"Your fact is: {fact}")


def run_predictions():
    prediction = random.choice(PREDICTIONS)
    messagebox.showinfo("Predictions", f"Here's how your day will go today:\n{prediction}")


def build_menu():
    root = tk.Tk()
    root.title("37039")
    root.geometry("420x360")
    root.resizable(False, False)

    header = tk.Label(root, text="Hello! Welcome to 37039!", font=("Arial", 14, "bold"))
    header.pack(pady=(18, 10))

    subtitle = tk.Label(root, text="Choose a game:")
    subtitle.pack()

    frame = tk.Frame(root, padx=20, pady=10)
    frame.pack()

    options = [
        ("High Card, Low Card", run_high_low),
        ("Coin Flip", run_coin_flip),
        ("Fun Facts", run_fun_facts),
        ("Quiz", run_quiz),
        ("Predictions", run_predictions),
    ]

    for label, command in options:
        button = tk.Button(frame, text=label, width=25, command=command)
        button.pack(pady=6)

    exit_button = tk.Button(root, text="Exit", command=root.destroy, width=15)
    exit_button.pack(pady=(10, 20))

    root.mainloop()


if __name__ == "__main__":
    build_menu()