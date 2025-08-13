import sqlite3
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
        # Clear window in case we are returning from dashboard
        for widget in self.root.winfo_children():
            widget.destroy()

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

        tk.Button(self.root, text="Create Account", command=self.show_create_account, **button_style).pack(pady=10)
        tk.Button(self.root, text="Login", command=self.show_login, **button_style).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, **button_style).pack(pady=10)

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

            if not all([fname, lname, email, phone, address, id_number]):
                messagebox.showerror("Error", "Please fill out all fields.")
                return

            full_name = f"{fname} {lname}"
            customer_id = self.bank.create_customer(full_name, email, phone)
            messagebox.showinfo("Success", f"Account created!\nCustomer ID: {customer_id}")
            create_win.destroy()

        tk.Button(create_win, text="Create Account", command=submit_customer, bg="#4CAF50", fg="white", padx=10, pady=5).grid(row=len(labels), column=0, columnspan=2, pady=20)



    def show_dashboard(self, customer_id, name):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Welcome, {name}!", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.root, text=f"Customer ID: {customer_id}", font=("Arial", 12)).pack(pady=5)

        tk.Button(self.root, text="Check Balance", command=self.view_balance).pack(pady=10)
        tk.Button(self.root, text="Deposit Money", command=self.deposit).pack(pady=10)
        tk.Button(self.root, text="Withdraw Money", command=self.withdraw).pack(pady=10)
        tk.Button(self.root, text="Transaction History", command=self.withdraw).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.create_main_menu).pack(pady=20)

    def view_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: $1000.00")

    def deposit(self):
        messagebox.showinfo("Deposit", "Deposit screen coming soon...")

    def withdraw(self):
        messagebox.showinfo("Withdraw", "Withdraw screen coming soon...")

    def transaction_history(self):
        messagebox.showinfo("Transaction History", "Transaction screen coming soon...")




    def show_login(self):
        login_win = tk.Toplevel(self.root)
        login_win.title("Customer Login")
        login_win.geometry("350x250")
        login_win.configure(bg="#f0f0f0")

        tk.Label(login_win, text="Customer ID", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        id_entry = tk.Entry(login_win, width=25)
        id_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(login_win, text="Email Address", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        email_entry = tk.Entry(login_win, width=25)
        email_entry.grid(row=1, column=1, padx=10, pady=10)

        def authenticate():
            customer_id = id_entry.get().strip()
            email = email_entry.get().strip()

            conn = sqlite3.connect("banking.db")
            cursor = conn.cursor()
            cursor.execute("SELECT customer_id, name FROM customers WHERE customer_id=? AND email=?", (customer_id, email))
            result = cursor.fetchone()
            conn.close()

            if result:
                messagebox.showinfo("Login Successful", f"Welcome back, {result[1]}!")
                login_win.destroy()
                self.show_dashboard(result[0], result[1])
            else:
                messagebox.showerror("Login Failed", "Invalid Customer ID or Email.")

        tk.Button(login_win, text="Login", command=authenticate, bg="#4CAF50", fg="white", padx=10, pady=5).grid(row=3, column=0, columnspan=2, pady=20)

    def run(self):
        self.root.mainloop()
