"""
    Checking Account
"""

from Account import Account



class CheckingAccount (Account):
    
    def __init__ (self, account_number, balance = 0):
        super().__init__(account_number, balance)