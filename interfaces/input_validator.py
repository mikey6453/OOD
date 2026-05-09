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

class Validator(ABC):
    @abstractmethod
    def validate(self, input: str) -> bool:
        pass


class EmailValidator(Validator):
    def validate(self, input: str) -> bool:
        return "@" in input


class PasswordValidator(Validator):
    def validate(self, input) -> bool:
        return len(input) >= 8
    

class RegistrationService:
    def __init__(self, validators: list[Validator]):
        self._validators = validators

    
    def register(self, input: str) -> None:
        for validator in self._validators:
            if not validator.validate(input):
                print("Registration failed")
                return
    

if __name__ == "__main__":
    email_reg = RegistrationService([EmailValidator()])
    email_reg.register("a.bcd@gmail.com")


    password_reg = RegistrationService([PasswordValidator()])
    password_reg.register("Password1234")

