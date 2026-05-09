"""
Exercise 1: Bank Account
Design Bank Account Class
Problem: Create a BankAccount class that manages a simple bank account with deposit, withdrawal, and balance checking functionality.

Requirements:

Fields: accountNumber, ownerName, balance
Constructor that initializes the account with owner name and account number (balance starts at 0)
deposit(amount): adds money to balance (only positive amounts)
withdraw(amount): removes money if sufficient balance exists, returns success/failure
getBalance(): returns current balance
"""

class BankAccount:
    def __init__(self, owner_name: str, account_number: int, balance: int=0) -> None:
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount: int) -> None:
        if amount > 0:
            self.balance += amount
    
    def withdraw(self, amount: int) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False
    
    def getBalance(self) -> int:
        return self.balance
    

if __name__ == "__main__":
    account = BankAccount("michael", 1)
    account.deposit(1000)
    print(account.getBalance()) # 1000
    

    account.withdraw(900) # success
    print(account.getBalance()) # 100

    account.withdraw(1000) # failure