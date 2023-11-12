import tkinter as tk
from tkinter import ttk
import random


# Your functions here
def get_secret(min_num=1, max_num=9):
    return random.randint(min_num, max_num)


def check_guess(secret_num, guess):
    if guess == secret_num:
        return "Correct"
    elif guess > secret_num:
        return "Guess too high"
    else:
        return "Guess too low"


def get_best_score(best_score, game_guesses):
    if best_score is None:
        return game_guesses
    else:
        return min(best_score, game_guesses)


# Tkinter GUI
class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.secret_num = get_secret()

    def create_widgets(self):
        self.instructions = tk.Text(self, height=4, width=60, bg="light green")
        self.instructions.pack(pady=12)
        self.instructions.insert(
            ttk.END, "Instructions: \nGuess a number between 1 and 9"
        )

        self.entry = ttk.Entry(self, bg="light yellow")
        self.entry.pack(pady=12)
        self.entry.bind('<Return>', self.submit_guess)  # Bind the Enter key

        self.submit = ttk.Button(self, bg="light blue")
        self.submit["text"] = "Submit Guess"
        self.submit["command"] = self.submit_guess
        self.submit.pack(pady=12)

        self.feedback = tk.Text(self, height=2, width=30, bg="light pink")
        self.feedback.pack(pady=12)

        self.quit = ttk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(pady=12)

    '''In this code, event=None makes the event argument optional. If the function is called without an event argument (like when it's called from the button click), event will be None. If the function is called with an event argument (like when it's called from the Enter key press), event will contain the event data. Since the submit_guess function doesn't use the event data, you can ignore this argument in the function body.
    '''
    def submit_guess(self, event=None):  # Add an optional event parameter
        try:
            guess = int(self.entry.get())
            guess_check = check_guess(self.secret_num, guess)
            if guess_check == "Correct":
                self.feedback.delete(1.0, tk.END)
                self.feedback.insert(tk.END, "Correct!")
            else:
                self.feedback.delete(1.0, tk.END)
                self.feedback.insert(tk.END, "Incorrect. Try again.\n" + guess_check)
        except ValueError:
            self.feedback.delete(1.0, tk.END)
            self.feedback.insert(tk.END, "Invalid input. Please enter a number.")
        self.entry.delete(0, tk.END)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
