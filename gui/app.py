import tkinter as tk
from tkinter import messagebox
from backend.bank import Bank

class BankApp:
    def __init__(self):
        self.bank = Bank()

        self.root = tk.Tk()
        self.root.title("Banking System")
        self.root.geometry("400x400")
        self.root.configure(bg="#f8f8f8")
        self.create_main_menu()

    def create_main_menu(self):
        title = tk.Label(
            self.root, text="Banking System Simulator",
            font=("Helvetica", 18, "bold"),
            bg="#f8f8f8", fg="#000000"
        )
        title.pack(pady=(40, 30))

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

        self.create_btn = tk.Button(self.root, text="Create Account", command=self.show_create_account, **button_style)
        self.create_btn.pack(pady=10)

        self.login_btn = tk.Button(self.root, text="Login", command=self.show_login, **button_style)
        self.login_btn.pack(pady=10)

        self.exit_btn = tk.Button(self.root, text="Exit", command=self.root.quit, **button_style)
        self.exit_btn.pack(pady=10)

    def show_create_account(self):
        create_win = tk.Toplevel(self.root)
        create_win.title("Create New Customer")
        create_win.geometry("400x500")
        create_win.configure(bg="#f0f0f0")

        labels = [
            "First Name", "Surname", "Email Address", "Contact Number",
            "Home Address", "Identification"
        ]
        entries = {}

        for i, label in enumerate(labels):
            tk.Label(create_win, text=label, bg="#f0f0f0").grid(row=i, column=0, padx=10, pady=8, sticky="w")
            entry = tk.Entry(create_win, width=30)
            entry.grid(row=i, column=1, padx=10, pady=8)
            entries[label] = entry

        def submit_customer():
            fname = entries["First Name"].get().strip()
            lname = entries["Surname"].get().strip()
            email = entries["Email Address"].get().strip()
            phone = entries["Contact Number"].get().strip()
            address = entries["Home Address"].get().strip()
            id_number = entries["Identification"].get().strip()

            # Basic validation
            if not all([fname, lname, email, phone, address, id_number]):
                messagebox.showerror("Error", "Please fill out all fields.")
                return

            full_name = f"{fname} {lname}"
            customer_id = self.bank.create_customer(full_name, email, phone)

            # Optionally store other fields like address and ID in a real app
            messagebox.showinfo("Success", f"Account created!\nCustomer ID: {customer_id}")
            create_win.destroy()

        submit_btn = tk.Button(create_win, text="Create Account", command=submit_customer, bg="#4CAF50", fg="white", padx=10, pady=5)
        submit_btn.grid(row=len(labels), column=0, columnspan=2, pady=20)

    def show_login(self):
        messagebox.showinfo("Login", "Login functionality coming soon!")

    def run(self):
        self.root.mainloop()
