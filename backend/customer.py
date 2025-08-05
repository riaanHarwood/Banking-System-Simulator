import uuid
class Customer():
    def __init__(self, name, email, phone=None): 
        self.customer_id = str(uuid.uuid4())[:8]
        self.name = name
        self.email = email
        self.phone = phone
        self.accounts = [] 

    def add_account(self, account_id):
        self.accounts.append(account_id)

    def get_accounts(self):
        return self.accounts 
    
    def __str__(self):
        return f"Customer {self.name} ({self.customer_id}) - Email: {self.email}"
