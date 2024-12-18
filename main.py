import tkinter as tk
from tkinter import messagebox
import random
import time

class MemoryTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Test App")

        # Initialize variables
        self.sequence = []
        self.user_input = []
        self.current_index = 0
        self.num_digits = 5
        self.start_time = None
        self.end_time = None

        # Create widgets
        self.label = tk.Label(root, text="Press Start to begin!", font=("Arial", 14))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", font=("Arial", 12), command=self.start_game)
        self.start_button.pack(pady=10)

        self.input_entry = tk.Entry(root, font=("Arial", 12), state="disabled")
        self.input_entry.pack(pady=10)
        self.input_entry.bind("<Return>", self.check_input)

        self.num_digits_label = tk.Label(root, text="Number of digits:", font=("Arial", 12))
        self.num_digits_label.pack(pady=10)

        self.num_digits_spinbox = tk.Spinbox(root, from_=3, to=10, font=("Arial", 12), width=5, command=self.update_num_digits)
        self.num_digits_spinbox.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", font=("Arial", 12), command=root.quit)
        self.quit_button.pack(pady=10)

        # Menu setup
        menu = tk.Menu(root)
        root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=root.quit)

        help_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def update_num_digits(self):
        try:
            self.num_digits = int(self.num_digits_spinbox.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid number of digits!")

    def start_game(self):
        self.sequence = [random.randint(1, 9) for _ in range(self.num_digits)]
        self.current_index = 0
        self.user_input = []

        self.label.config(text="Memorize this sequence:")
        self.input_entry.config(state="disabled")
        self.show_sequence()

    def show_sequence(self):
        self.label.config(text=f"{self.sequence}")
        self.root.after(2000, self.clear_label)

    def clear_label(self):
        self.label.config(text="Now, enter the sequence:")
        self.input_entry.config(state="normal")
        self.input_entry.focus()
        self.start_time = time.time()

    def check_input(self, event):
        try:
            self.user_input = list(map(int, self.input_entry.get().strip().split()))
            self.end_time = time.time()

            if self.user_input == self.sequence:
                elapsed_time = self.end_time - self.start_time
                messagebox.showinfo("Success", f"Correct! Time taken: {elapsed_time:.2f} seconds")
            else:
                messagebox.showerror("Error", "Incorrect sequence. Try again!")

            self.input_entry.delete(0, tk.END)
            self.input_entry.config(state="disabled")
            self.label.config(text="Press Start to play again!")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def show_about(self):
        messagebox.showinfo("About", "Memory Test App\nDeveloped using Python and Tkinter.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryTestApp(root)
    root.mainloop()