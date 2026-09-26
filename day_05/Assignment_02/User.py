from BankApp import Transaction
from CustomeException import AccountNotFoundException, InvalidAmountException, InsufficientBalanceException

class User:

    def __init__(self, accounts):
        self._accounts = accounts
        self._transaction = []

    def find_account(self, account_no):

        for account in self._accounts:

            if account.acc_id == account_no:
                return account
        raise AccountNotFoundException('Account Not Found !!')

    def deposit(self):
        try:
            account_no = int(input('Enter Account No :'))
            account = self.find_account(account_no)

            amount = int(input('Enter Amount For Deposit :'))
            new_balance = Transaction.deposit_to_account(account, amount)

            self._transaction.append(f'Account : {account_no} | Deposit : {amount} | Balance : {new_balance}')

            print('Amount Deposit Successfully !!')
            print(f'New Balance : {new_balance}')

        except AccountNotFoundException as e:
            print(e)

        except InsufficientBalanceException as e:
            print(e)

        except InvalidAmountException as e:
            print(e)

        except ValueError:
            print('Please Enter Valid Number !!')

    def withdraw(self):

        try:
            account_no = int(input('Enter Account No :'))
            account = self.find_account(account_no)

            amount = int(input('Enter Amount For Withdraw :'))

            new_balance = Transaction.withdraw_to_account(account, amount)

            self._transaction.append(f'Account : {account_no} | Withdraw : {amount} | Balance : {new_balance}')

            print('Amount Withdraw Successfully !!')
            print(f'New Balance : {new_balance}')

        except AccountNotFoundException as e:
            print(e)

        except InsufficientBalanceException as e:
            print(e)

        except InvalidAmountException as e:
            print(e)

        except ValueError:
            print('Please Enter Valid Number !!')

    def show_statement(self):

        print('-----Transaction Statement-----')

        if len(self._transaction) == 0:
            print('No Transaction Statement Available !!')
        else:
            for transaction in self._transaction:
                print(transaction)
        print('------------------------------')

    def menu(self):

        while True:
            print('-------Bank-------\n1.Deposite\n2.Withdraw\n'
                  '3.Account Details\n4.Transaction Statement\n5.Exit\n--------------------')

            try:
                choice = int(input('Enter Your Choice :'))

                match choice:

                    case 1:
                        self.deposit()
                    case 2:
                        self.withdraw()

                    case 3:
                        try:
                            account_no = int(input('Enter Account No :'))
                            account = self.find_account(account_no)
                            print('-----Account Details-----')
                            print(account)

                        except ValueError:
                            print('Please Enter Valid Account No !!')

                    case 4:
                        self.show_statement()

                    case 5:
                        self.show_statement()
                        print('Exiting...!!')
                        break

                    case _:
                        print('Invalid Choice...!!')
            except ValueError:
                print('please Enter Valid Choice !!')