class Bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw = 10000
    def get_balance(self):
        return f'total amount of money you have {self.balance}'
    def deposit(self,amount):
        self.balance=self.balance+amount
        return f'{amount} money is depositi successfully'
    def withdraw(self,amount):
        if amount<self.min_withdraw:
            return f'minimum withdraw amount is:{self.min_withdraw}'
        elif amount>self.max_withdraw:
            return f'maximum you can withdraw :{self.max_withdraw}'
        elif amount>self.balance:
            return f'You have only {self.balance} balance,please try to withdraw less then {self.balance}'
        else:
            self.balance=self.balance-amount
            return f'Here is your money: {amount}'
        
my_bank = Bank(20000)
reply = my_bank.withdraw(300)
print(reply)
deposit_reply = my_bank.deposit(700)
print(deposit_reply)
print(my_bank.balance)
