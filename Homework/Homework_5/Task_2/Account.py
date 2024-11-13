"""
    Account
"""

class Account:
    
    def __init__ (self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance


    def deposit (self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is: {self.balance}.")
        else:
            print("Deposited amount must be positive.")


    def withdraw (self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is: {self.balance}.")
        else:
            print("Insufficient funds or invalid amount.")
