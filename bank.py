class Account:
    def __init__(self,account_number,account_name,balance,phone_number):
        self.account_number=account_number
        self.account_name=account_name
        self.balance=balance
        self.phone_number=phone_number
    
    def deposit(self,amount):
        self.balance+=amount
        return f"You deposited {amount} on the account {self.account_number} in the name of {self.account_name}. The balance is {self.balance} "
    def withdraw(self,amount):
        self.amount=amount
        self.balance-=amount
        return f"You withrawn {amount} on the account {self.account_number} in the name of {self.account_name}. The balance is {self.balance} "
    