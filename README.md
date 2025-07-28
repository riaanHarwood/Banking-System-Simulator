# Banking-System-Simulator
A digital banking system simulator project. Skills addresses include OOP and GUI design 



# 🏦 Banking System Simulator (Python + Tkinter)

A desktop-based banking system simulator built with Python, demonstrating Object-Oriented Programming (OOP) principles and GUI development using Tkinter. This project simulates basic banking operations such as creating accounts, making deposits, withdrawals, and transfers—all within a user-friendly interface.

---

## 🔧 Features

- Create customer accounts (Savings & Checking)
- Deposit, withdraw, and transfer funds
- View account balance and transaction history
- GUI built using Tkinter
- Clean, modular OOP structure
- Error handling for invalid transactions (e.g., overdrafts)

---

## 🧱 OOP Design

This project applies fundamental OOP principles:

- **Encapsulation** – Account and Customer data are managed via dedicated classes
- **Inheritance** – `SavingsAccount` and `CheckingAccount` inherit from a base `Account` class
- **Polymorphism** – Different account types behave differently for certain operations
- **Composition** – A `Bank` contains multiple `Account` and `Customer` objects

---

## 🖥️ GUI Overview

- **Main Menu**: Create new account, login to existing account
- **Account Dashboard**: 
  - View balance
  - Make deposit/withdrawal
  - Transfer between accounts
  - View recent transactions

---

## 🗂️ Project Structure

banking-system/
│
├── main.py # Entry point for the app
├── backend/
│ ├── bank.py # Bank class logic
│ ├── account.py # Account base and subclasses
│ ├── customer.py # Customer-related data
│ └── transaction.py # Handles transaction records
│
├── gui/
│ ├── app.py # GUI control flow
│ ├── screens.py # Tkinter frames/windows
│ └── widgets.py # Custom reusable widgets
│
├── README.md
└── requirements.txt




---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/banking-system.git
   cd banking-system

(Optional) Create a virtual environment 

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

python main.py


📚 **Technologies Used**
Python 3.x

Tkinter (Standard GUI library)

Object-Oriented Programming

Basic file I/O (optional for storing data)


🧠 **What I Learned**
+ Applying OOP concepts to a real-world simulation

+ Structuring multi-file Python projects

+ Building desktop applications using Tkinter

+ Improving usability through GUI design


  

**Acknowledgments**
This project was created to practice and showcase my Python programming and GUI development skills. Feedback and suggestions are welcome!




📌 **Future Improvements**
Add persistent storage (JSON or SQLite)

Add login authentication

Improve transaction history display

Dark/light mode switch for GUI
