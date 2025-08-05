import uuid
from datetime import datetime

class Transaction:
    def __init__(self, trans_type, amount, from_account_id=None, to_account_id=None):
        if trans_type not in ['deposit', 'withdraw', 'transfer', 'received']:
            raise ValueError("Invalid transaction type.")
        
        self.transaction_id = str(uuid.uuid4())[:8]
        self.trans_type = trans_type
        self.amount = amount
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.from_account_id = from_account_id
        self.to_account_id = to_account_id

    def __str__(self):
        if self.trans_type == 'transfer':
            return f"[{self.timestamp}] Transfer of ${self.amount:.2f} from {self.from_account_id} to {self.to_account_id}"
        elif self.trans_type == 'received':
            return f"[{self.timestamp}] Received ${self.amount:.2f} from {self.from_account_id}"
        else:
            return f"[{self.timestamp}] {self.trans_type.title()} of ${self.amount:.2f}"
