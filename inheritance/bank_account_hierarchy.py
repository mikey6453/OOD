"""
Exercise 1: Bank Account Hierarchy
Design Bank Account Hierarchy Class
Problem: Build a bank account system using inheritance. The base BankAccount class has common fields and methods for deposits and withdrawals. 
Specialized account types have different withdrawal rules.

Requirements:

Base BankAccount class with ownerName, accountNumber, and balance (protected). 
A deposit(amount) method that adds to the balance if the amount is positive. 
A withdraw(amount) method that subtracts from the balance if funds are sufficient and returns true/false. 
A displayAccount() method that prints the owner's name, account number, and formatted balance.

SavingsAccount: adds an interestRate field. Overrides withdraw() to enforce a minimum balance of $100 (the withdrawal fails if it would drop the balance below $100). 
Adds an applyInterest() method that increases the balance by balance * interestRate / 100.

CheckingAccount: adds an overdraftLimit field. Overrides withdraw() to allow withdrawals up to balance + overdraftLimit.
displayAccount() should work correctly for all account types without any changes to the base class.
"""

class BankAccount:
    def __init__(self, owner_name: str, account_number: int, balance: float) -> None:
        self.owner_name = owner_name
        self.account_number = account_number
        self._balance = balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
    
    def withdraw(self, amount: float) -> bool:
        if amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False
    
    def display_account(self) -> None:
        print(f"{self.owner_name}, {self.account_number}, ${self._balance}")

    
class SavingsAccount(BankAccount):
    def __init__(self, owner_name: str, account_number: int, balance: float, interest_rate: float) -> None:
        super().__init__(owner_name, account_number, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount: float) -> bool:
        if 100 + amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False
    
    def apply_interest(self) -> None:
        self._balance += self._balance * self.interest_rate / 100


class CheckingAccount(BankAccount):
    def __init__(self, owner_name: str, account_number: int, balance: float, overdraft_limit: float) -> None:
        super().__init__(owner_name, account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount: float) -> bool:
        if amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            return True
        else:
            return False
        
bank = BankAccount("Michael", 1, 1000)
savings = SavingsAccount("Michael", 2, 1000, 3)
checkings = CheckingAccount("Michael", 3, 1000, 500)

bank.display_account()
savings.display_account()
checkings.display_account()

savings.withdraw(950)
savings.display_account() # $1000

checkings.withdraw(1500)
checkings.display_account() # $-500