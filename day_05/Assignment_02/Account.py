from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(self, acc_id, name, balance):
        self._acc_id = acc_id
        self._name = name
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @property
    def acc_id(self):
        return self._acc_id

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def __str__(self):
        return f'Account No : {self._acc_id} | Name : {self._name} | Balance : {self._balance}'