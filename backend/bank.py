from backend.account import SavingsAccount, CheckingAccount

class Bank():
    def __init__(self):
        self.accounts = {}    # account_id -> Account object
        self.customers = {}   # customer_id -> Customer object

    def create_account(self, owner_name, account_type):
        if account_type.lower() == "savings":
            account = SavingsAccount(owner_name)
        elif account_type.lower() == "checking":
            account = CheckingAccount(owner_name)
        else:
            raise ValueError("Invalid account type. Choose 'Savings' or 'Checking'.")

        self.accounts[account.account_id] = account
        return account.account_id  # Return ID so GUI/user can reference it


    def get_account(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id]
        else:
            raise ValueError("Account not found. Please try again.")

    def deposit(self, account_id, amount): 
        user = self.get_account(account_id)
        if amount >= 1:
            user.balance += amount
            user.transaction_history.append(f"Deposited ${amount}")
            return "Deposit successful"
        elif amount <=0:
            raise ValueError("Invalid Amount. Please enter a valid number greater than zero.")


    def withdraw(self, account_id, amount):
        user = self.get_account(account_id)

        if amount <= 0:
            raise ValueError("Invalid Amount. Please enter a valid number greater than zero.")
        if user.balance < amount:
            raise ValueError("Insufficient funds.")

        user.balance -= amount 
        user.transaction_history.append(f"Withdrew ${amount}")
        return f'Withdrawal successful. Remaining balance: ${user.balance}.'


    def transfer(self, from_id, to_id, amount):
        return 
    


    def get_transaction_history(self, account_id): 
        return 






