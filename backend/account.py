from abc import ABC, abstractmethod
import uuid

class Account(ABC):
    def __init__(self, owner_name, balance=0.0):
        self.account_id = str(uuid.uuid4())[:8]
        self.owner_name = owner_name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
            return True
        return False

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

    @abstractmethod
    def account_type(self):
        pass
class SavingsAccount(Account):
    def account_type(self):
        return "Savings"

class CheckingAccount(Account):
    def account_type(self):
        return "Checking"
