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

