from typing import override
from Account import BankAccount
from CustomeException import InsufficientBalanceException, InvalidAmountException


class CurrentAccount(BankAccount):

    def __init__(self, acc_id, name, balance):
        super().__init__(acc_id, name, balance)

    @override
    def deposit(self, amount):

        if amount <= 0:
            raise InvalidAmountException('Amount Must be Greater Than Zero !!')

        if amount > 200000:
            raise InvalidAmountException('Maximum upto 2 lakh can be Deposited in an Account at a Time !!')

        self._balance += amount

    @override
    def withdraw(self, amount):

        if amount <= 0:
            raise InvalidAmountException('Amount Must be Greater Than Zero !!')

        if amount > self._balance:
            raise InsufficientBalanceException('Insufficient Amount')

        if self._balance - amount < 10000:
            raise InsufficientBalanceException('Min balance 10000 must be Maintained For Current Account !!')

        self._balance -= amount

    def __str__(self):
        return super().__str__() + ' | Account :- Current'



