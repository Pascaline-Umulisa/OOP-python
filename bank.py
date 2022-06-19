from datetime import datetime

# current_time=datetime.now()

class Account:
    def __init__(self,account_number,account_name):
        self.account_number=account_number
        self.account_name=account_name
        self.balance=0
        self.deposits=[]
        self.withrawals=[]
        self.loan_balance=0

    
    def deposit(self,amount):
        if amount<=0:
            return "The amount should be greater than zero"
        else:
            self.balance+=amount
            deposit_details={"date":datetime.now().strftime('%d/%m/%y'),"amount":amount,"narration":f"You have deposited {amount} on {datetime.now} "}
            self.deposits.append(deposit_details)
            # print(deposit_details)
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

            withdrawal_details={"date":datetime.now().strftime('%d/%m/%y'),"amount":amount,"narration":f"You have withdrawn {amount} on {datetime.now()} "}
            self.withrawals.append(withdrawal_details)

            return f"You withdrew {amount} KSH on the account {self.account_number} in the name of {self.account_name}. The balance is {self.balance} KSH"
    def deposit_statement(self):
        for a in self.deposits:
            return a
    
    def withdrawal_statement(self):
        for withdrawal in self.withrawals:
            print(withdrawal)

    def Current_balance(self):
        return f"Your current balance is {self.balance} KSH."
    def full_statement(self):
        statement=self.deposits+self.withrawals
        for a in statement:
            print(a["narration"])
    def borrow(self,amount):
        deposit_sum=0
        for a in self.deposits:
            deposit_sum+=a["amount"]
        if amount<=0:
            return "invalid amount"
        if len(self.deposits)<10:
            return f"You can't borrow money because of few deposits made, make {10-len(self.deposits)} more deposits to qualify"
        if amount<100:
            return "You can only borrow atleast 100"
        if self.balance!=0:
            return f"You have {self.balance} KSH in your balance so can't borrow when you have money"
        if amount> deposit_sum/3:
            return f"You are not qualified to borrow this amount. You can borrow atmost {deposit_sum/3}"
        if self.loan_balance!=0:
            return f"YOu have unpaid loan of {self.loan_balance}, for you to borrow first clear the loan you have"
        else:
            interest=(3/100)*amount
            self.loan_balance+=amount+interest
            return f"You have borrowed {amount} and your loan balance to be paid is equal to {self.loan_balance}"
    def loan_repayment(self,amount):
        if amount<=0:
            return "invalid amount"
        if amount>self.loan_balance:
            remainder=amount-self.loan_balance
            self.loan_balance=0
            return f"Your loan balance is {self.loan_balance} { self.deposit(remainder)}"
        else:
            self.loan_balance-=amount
            return f"You have paid a loan of {amount} KSH and your current loan balance is {self.loan_balance} "
    def transfer(self,amount,instance_name):
        if amount<=0:
            return "invalid amount"
        if amount>=self.balance:
            return "insufficient amount"
        if isinstance(instance_name,Account):
            self.balance-=amount
            instance_name.balance+=amount
            return f"You have transfered {amount} KSH to {instance_name} account with the name of {instance_name.account_name}. Your new balance is {self.balance}"


        




# Update the withdrawal method to store each withdrawal transaction as a dictionary like like this 
# {
#    "date": datetime object,
#    "amount": amount,
#    "narration": deposit or withdrawal
# }

# Update the deposit method to store each deposit transaction as a dictionary like this 
# {
#    "date": datetime object,
#    "amount": amount,
#    "narration": deposit or withdrawal
# }

# Add a new method  full_statement which combines both deposits and withdrawals into one list ordered by date and using a for loop prints each transaction in a new line like this
# 16/06/22 —----- Deposit —---- 1000

# Add a new attribute loan_balance which is zero by default.

# Add a borrow method which allows a customer to borrow if they meet these conditions:
# Customer has made at least 10 deposits.
# Loan amount requested must be more than 100
# A customer qualifies for a loan amount that is less than  or equal to 1/3 of their total sum of deposit history
# Customer account has no has no balance
# Customer has no outstanding loan
# The loan attracts  an interest of 3%.

# Add a loan repayment method with these conditions
# A customer can repay a loan to reduce the current loan balance
# Overpayment of a loan increases a customers current deposit

# Add a new method transfer which accepts two attributes (amount and instance of another account). If the amount is less than the current instances balance, the method transfers the requested amount from the current account to the passed account. The transfer is accomplished by reducing the current account balance and depositing the requested amount to the passed account.

