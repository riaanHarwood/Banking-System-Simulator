from backend.account import SavingsAccount, CheckingAccount
from backend.transaction import Transaction
from backend.customer import Customer


class Bank():
    def __init__(self):
        self.accounts = {}
        self.customers = {}

    def create_customer(self, name, email, phone=None):
        customer = Customer(name, email, phone)
        self.customers[customer.customer_id] = customer
        return customer.customer_id

    def get_customer(self, customer_id):
        if customer_id in self.customers:
            return self.customers[customer_id]
        else:
            raise ValueError("Customer not found.")

    def create_account(self, owner_name, account_type, customer_id):
        if account_type.lower() == "savings":
            account = SavingsAccount(owner_name)
        elif account_type.lower() == "checking":
            account = CheckingAccount(owner_name)
        else:
            raise ValueError("Invalid account type. Choose 'Savings' or 'Checking'.")

        self.accounts[account.account_id] = account

        # Link to customer
        customer = self.get_customer(customer_id)
        customer.add_account(account.account_id)
        return account.account_id

    def get_account(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id]
        else:
            raise ValueError("Account not found. Please try again.")

    def deposit(self, account_id, amount):
        account = self.get_account(account_id)
        if amount <= 0:
            raise ValueError("Invalid amount. Please enter a number greater than zero.")
        account.deposit(amount)
        account.transactions.append(Transaction("deposit", amount))
        return "Deposit successful"

    def withdraw(self, account_id, amount):
        account = self.get_account(account_id)
        if amount <= 0:
            raise ValueError("Invalid amount. Please enter a number greater than zero.")
        if not account.withdraw(amount):
            raise ValueError("Insufficient funds.")
        account.transactions.append(Transaction("withdraw", amount))
        return f"Withdrawal successful. Remaining balance: ${account.balance}."

    def transfer(self, from_id, to_id, amount):
        sender = self.get_account(from_id)
        receiver = self.get_account(to_id)
        if amount <= 0:
            raise ValueError("Invalid amount.")
        if not sender.withdraw(amount):
            raise ValueError("Transfer failed. Insufficient funds.")
        receiver.deposit(amount)

        sender.transactions.append(Transaction("transfer", amount))
        receiver.transactions.append(Transaction("received", amount))
        return f"Transfer of ${amount} to account {to_id} complete."

    def get_transaction_history(self, account_id):
        account = self.get_account(account_id)
        return "\n".join([str(t) for t in account.transactions])
