from typing import override
from Account import BankAccount
from CustomeException import InsufficientBalanceException, InvalidAmountException

class SavingAccount(BankAccount):

    def __init__(self, acc_id, name, balance, type):
        super().__init__(acc_id, name, balance)
        self._type = type

    @override
    def deposit(self, amount):

        if amount <= 0:
            raise InvalidAmountException('Amount Must be Greater Than Zero !!')

        if amount > 100000:
            raise InvalidAmountException('Maximum upto 1 lakh can be Deposited in an Account at a Time !!')

        self._balance += amount

    @override
    def withdraw(self, amount):

        if amount <= 0:
            raise InvalidAmountException('Amount Must be Greater Than Zero !!')

        if amount > self._balance:
            raise InsufficientBalanceException('Insufficient Amount')

        if self._type.lower() == 'personal':

            if self._balance - amount < 5000:
                raise InsufficientBalanceException('Min balance 5000 must be maintained For Personal Account !!')

        self._balance -= amount

    def __str__(self):
        return super().__str__() + f' | Account :- Saving | Type : {self._type}'


