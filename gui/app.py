import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
from backend.bank import Bank


class BankApp:
    def __init__(self):
        self.bank = Bank()

        self.root = tk.Tk()
        self.root.title("Banking System")
        self.root.geometry("500x500")
        self.root.configure(bg="#f8f9fa")  # soft gray background
        self.style = ttk.Style()
        self.style.theme_use("clam")  # modern built-in theme
        self.create_main_menu()

    # ---------------- Main Menu ----------------
    def create_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title
        title = tk.Label(
            self.root,
            text="🏦 Banking System Simulator",
            font=("Helvetica", 20, "bold"),
            bg="#f8f9fa",
            fg="#212529"
        )
        title.pack(pady=(40, 30))

        # Button style
        button_style = {
            "font": ("Helvetica", 13, "bold"),
            "bg": "#ffffff",
            "fg": "#212529",
            "activebackground": "#e9ecef",
            "activeforeground": "#212529",
            "width": 25,
            "bd": 0,
            "relief": "flat",
            "pady": 12
        }

        tk.Button(self.root, text="➕ Create Account", command=self.show_create_account, **button_style).pack(pady=10)
        tk.Button(self.root, text="🔑 Login", command=self.show_login, **button_style).pack(pady=10)
        tk.Button(self.root, text="❌ Exit", command=self.root.quit, **button_style).pack(pady=10)

    # ---------------- Create Account ----------------
    def show_create_account(self):
        create_win = tk.Toplevel(self.root)
        create_win.title("Create New Customer")
        create_win.geometry("450x550")
        create_win.configure(bg="#ffffff")  # White background

        # Header
        header = tk.Label(
            create_win, text="📝 Create Account",
            font=("Helvetica", 16, "bold"),
            bg="#ffffff",  # white background
            fg="#000000"   # black text
        )
        header.grid(row=0, column=0, columnspan=2, pady=20)

        labels = [
            "First Name", "Surname", "Email Address", "Contact Number",
            "Home Address", "Identification"
        ]
        entries = {}

        for i, label in enumerate(labels, start=1):
            tk.Label(
                create_win,
                text=label,
                bg="#ffffff",  # white background
                fg="#000000",  # black text
                font=("Helvetica", 11)
            ).grid(row=i, column=0, padx=10, pady=8, sticky="w")

            entry = tk.Entry(
                create_win,
                width=30,
                bg="#ffffff",    # white inside
                fg="#000000",    # black text
                highlightthickness=1,  # enable outline
                highlightbackground="#000000",  # outline color (normal)
                highlightcolor="#000000"  # outline color (on focus)
            )
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
            messagebox.showinfo("Success", f"✅ Account created!\nCustomer ID: {customer_id}")
            create_win.destroy()

        submit_btn = tk.Button(
            create_win,
            text="Create Account",
            command=submit_customer,
            bg="#28a745", fg="black",
            font=("Helvetica", 12, "bold"),
            padx=25, pady=10
        )
        submit_btn.grid(row=len(labels) + 1, column=0, columnspan=2, pady=20)


    # ---------------- Dashboard ----------------
    def show_dashboard(self, customer_id, name):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"👋 Welcome, {name}!", font=("Helvetica", 18, "bold"), bg="#ffffff", fg="#000000").pack(pady=15)
        tk.Label(self.root, text=f"Customer ID: {customer_id}", font=("Helvetica", 12, "bold"), bg="#f8f9fa", fg="#000000").pack(pady=5)

        # Dashboard frame
        dash_frame = tk.Frame(self.root, bg="#f8f9fa")
        dash_frame.pack(pady=30)

        def dash_button(text, command, color="#007bff"):
            return tk.Button(
                dash_frame, text=text, command=command,
                bg=color, fg="black",
                font=("Helvetica", 12, "bold"),
                activebackground="#0056b3", width=20, pady=10, relief="flat"
            )

        dash_button("💰 Check Balance", self.view_balance, "#17a2b8").pack(pady=8)
        dash_button("➕ Deposit Money", self.deposit, "#28a745").pack(pady=8)
        dash_button("💳 Withdraw Money", self.withdraw, "#ffc107").pack(pady=8)
        dash_button("📜 Transaction History", self.transaction_history, "#6f42c1").pack(pady=8)

        tk.Button(
            self.root, text="🚪 Logout", command=self.create_main_menu,
            bg="#dc3545", fg="black",
            font=("Helvetica", 12, "bold"),
            activebackground="#a71d2a", width=20, pady=10, relief="flat"
        ).pack(pady=25)

    def view_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: $1000.00")

    def deposit(self):
        messagebox.showinfo("Deposit", "Deposit screen coming soon...")

    def withdraw(self):
        messagebox.showinfo("Withdraw", "Withdraw screen coming soon...")

    def transaction_history(self):
        messagebox.showinfo("Transaction History", "Transaction screen coming soon...")

    # ---------------- Login ----------------
    def show_login(self):
        login_win = tk.Toplevel(self.root)
        login_win.title("Customer Login")
        login_win.geometry("400x300")
        login_win.configure(bg="#ffffff")  # white background

        # Header
        header = tk.Label(
            login_win, text="🔑 Login",
            font=("Helvetica", 16, "bold"),
            bg="#ffffff", fg="#000000"
        )
        header.grid(row=0, column=0, columnspan=2, pady=20)

        # Customer ID
        tk.Label(
            login_win,
            text="Customer ID",
            bg="#ffffff", fg="#000000",
            font=("Helvetica", 11)
        ).grid(row=1, column=0, padx=10, pady=10, sticky="w")

        id_entry = tk.Entry(
            login_win,
            width=30,
            bg="#ffffff", fg="#000000",
            highlightthickness=1,
            highlightbackground="#000000",
            highlightcolor="#000000"
        )
        id_entry.grid(row=1, column=1, padx=10, pady=10)

        # Email Address
        tk.Label(
            login_win,
            text="Email Address",
            bg="#ffffff", fg="#000000",
            font=("Helvetica", 11)
        ).grid(row=2, column=0, padx=10, pady=10, sticky="w")

        email_entry = tk.Entry(
            login_win,
            width=30,
            bg="#ffffff", fg="#000000",
            highlightthickness=1,
            highlightbackground="#000000",
            highlightcolor="#000000"
        )
        email_entry.grid(row=2, column=1, padx=10, pady=10)

        # Authentication function
        def authenticate():
            customer_id = id_entry.get().strip()
            email = email_entry.get().strip()

            conn = sqlite3.connect("banking.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT customer_id, name FROM customers WHERE customer_id=? AND email=?",
                (customer_id, email)
            )
            result = cursor.fetchone()
            conn.close()

            if result:
                messagebox.showinfo("Login Successful", f"🎉 Welcome back, {result[1]}!")
                login_win.destroy()
                self.show_dashboard(result[0], result[1])
            else:
                messagebox.showerror("Login Failed", "❌ Invalid Customer ID or Email.")

        # Login button
        login_btn = tk.Button(
            login_win,
            text="Login",
            command=authenticate,
            bg="#007bff", fg="white",
            font=("Helvetica", 12, "bold"),
            padx=15, pady=8,
            relief="flat"
        )
        login_btn.grid(row=3, column=0, columnspan=2, pady=25)


    def run(self):
        self.root.mainloop()
