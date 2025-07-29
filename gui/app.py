# gui/app.py
import tkinter as tk

class BankApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Banking System")
        self.root.geometry("400x400")
        self.root.configure(bg="#f8f8f8")  # Soft light gray background

        self.create_main_menu()

    def create_main_menu(self):
        # Title label
        title = tk.Label(
            self.root, text="Banking System Simulator",
            font=("Helvetica", 18, "bold"),
            bg="#f8f8f8", fg="#000000"
        )
        title.pack(pady=(40, 30))

        # Button styling
        button_style = {
            "font": ("Helvetica", 14),
            "bg": "#ffffff",
            "fg": "#000000",
            "activebackground": "#e6e6e6",
            "activeforeground": "#000000",
            "width": 20,
            "bd": 0,
            "highlightthickness": 0,
            "relief": "flat",
            "padx": 10,
            "pady": 10
        }

        # Create buttons with consistent spacing
        self.create_btn = tk.Button(self.root, text="Create Account", **button_style)
        self.create_btn.pack(pady=10)

        self.login_btn = tk.Button(self.root, text="Login", **button_style)
        self.login_btn.pack(pady=10)

        self.exit_btn = tk.Button(self.root, text="Exit", command=self.root.quit, **button_style)
        self.exit_btn.pack(pady=10)

    def run(self):
        self.root.mainloop()
