from Account import BankAccount

class Transaction:

    @staticmethod
    def deposit_to_account(account: BankAccount, amount):
        account.deposit(amount)
        return account.balance

    @staticmethod
    def withdraw_to_account(account: BankAccount, amount):
        account.withdraw(amount)
        return account.balance





