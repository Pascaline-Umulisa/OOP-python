class Account:
    def __init__(self,account_number,account_name,balance,phone_number):
        self.account_number=account_number
        self.account_name=account_name
        self.balance=balance
        self.phone_number=phone_number
    
    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
        return f"You deposited{self.amount} on the account {self.accountnumber} in the name of {self.accountname}. The balance is {self.balance} "
    def withdraw(self,amount):
        self.amount=amount
        self.balance-=self.amount
        return f"You withrawn {self.amount} on the account {self.accountnumber} in the name of {self.accountname}. The balance is {self.balance} "
    