from hashlib import new


class Account:
    def __init__(self,account_number,account_name):
        self.account_number=account_number
        self.account_name=account_name
        self.balance=0
        self.deposits=[]
        self.withrawals=[]
        # self.phone_number=phone_number
    
    def deposit(self,amount):
        if amount<=0:
            return "The amount should be greater than zero"
        else:
            self.balance+=amount
            deposit_details=f"You deposited {amount} KSH and the new balance was {self.balance} KSH"
            self.deposits.append(deposit_details)
            return f"You deposited {amount} KSH on the account {self.account_number} in the name of {self.account_name}. The balance is {self.balance} KSH"
    
    def withdraw(self,amount):
        transaction_fees=100
        withrawable_amount=self.balance-transaction_fees
        
        if amount>withrawable_amount:
            return f"insufficient funds"
        elif amount<=0:
            return f"The amount must be greater than zero"
        else:
            self.balance-=amount + transaction_fees

            withdrawal_details=f"You withdrew {amount} and the new balance was {self.balance}"
            self.withrawals.append(withdrawal_details)

            return f"You withdrew {amount} KSH on the account {self.account_number} in the name of {self.account_name}. The balance is {self.balance} KSH"
    def deposit_statement(self):
        for a in self.deposits:
            print(a)
    
    def withdrawal_statement(self):
        for withdrawal in self.withrawals:
            print(withdrawal)

    def Current_balance(self):
        return f"Your current balance is {self.balance} KSH."


# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which using a for loop prints each deposit in a new line
# Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance.
