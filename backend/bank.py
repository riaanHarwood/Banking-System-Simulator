from backend.account import SavingsAccount, CheckingAccount

class Bank():
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner_name, account_type):
        if account_type.lower() == "savings":
            account = SavingsAccount(owner_name)
        elif account_type.lower() == "checking":
            account = CheckingAccount(owner_name)
        else:
            raise ValueError("Invalid account type. Choose 'Savings' or 'Checking'.")
        self.accounts[account.account_id] = account
        return account.account_id


    def get_account(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id]
        else:
            raise ValueError("Account not found. Please try again.")
        

    def deposit(self, account_id, amount): 
        user = self.get_account(account_id)
        if amount <= 0:
            raise ValueError("Invalid amount. Please enter a number greater than zero.")
        user.deposit(amount)
        return "Deposit successful"
    

    def withdraw(self, account_id, amount):
        user = self.get_account(account_id)
        if amount <= 0:
            raise ValueError("Invalid amount. Please enter a number greater than zero.")
        if not user.withdraw(amount):
            raise ValueError("Insufficient funds.")
        return f"Withdrawal successful. Remaining balance: ${user.balance}."


    def transfer(self, from_id, to_id, amount):
        sender = self.get_account(from_id)
        receiver = self.get_account(to_id)
        if amount <= 0:
            raise ValueError("Invalid amount.")
        if not sender.withdraw(amount):
            raise ValueError("Transfer failed. Insufficient funds.")
        receiver.deposit(amount)
        sender.transaction_history.append(f"Transferred ${amount} to account {to_id}")
        receiver.transaction_history.append(f"Received ${amount} from account {from_id}")
        return f"Transfer of ${amount} to account {to_id} complete."


    def get_transaction_history(self, account_id): 
        user = self.get_account(account_id)
        return "\n".join(user.transaction_history)
