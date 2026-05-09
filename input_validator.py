"""
Design Input Validator Class
Problem: Build a registration system where multiple validation rules are applied to user input. 
Each rule is a separate implementation of a Validator interface, and the RegistrationService runs all validators before accepting the registration.

Requirements:

Validator interface with a validate(input) method that returns true if valid, false otherwise
EmailValidator: returns true if the input contains @
PasswordValidator: returns true if the input has 8 or more characters
RegistrationService: takes a list of validators in its constructor. Its register(input) method runs all validators and prints whether the input passed or failed
"""

from abc import abstractmethod, ABC

