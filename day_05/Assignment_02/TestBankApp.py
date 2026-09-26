from User import User
from Saving import SavingAccount
from Current import CurrentAccount

class Bank:


    account1 = SavingAccount(101, "Viral", 50000, "personal")
    account2 = SavingAccount(102, "Rahul", 80000, "corporate")
    account3 = CurrentAccount(103, "Amit", 150000)
    account4 = SavingAccount(104, "Vikram", 80000, "personal")
    account5 = CurrentAccount(105, "Priya", 120000, )
    account6 = CurrentAccount(106, "Harsh", 145000)

    accounts = [account1,account2,account3,account4,account5,account6]

    user = User(accounts)
    user.menu()





