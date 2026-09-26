from abc import abstractmethod, ABC
from typing import override


class Employee(ABC):
    def __init__(self,emp_id, name):
        self._emp_id = emp_id
        self._name = name

    @abstractmethod
    def calculate_gross(self):
        pass

    def __str__(self):
        return f"Employee Data Id :- {self._emp_id}, name :- {self._name}"

class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, basic):
        # self._emp_id = emp_id
        # self._name = name
        super().__init__(emp_id,name)
        self._basic = basic

    @override
    def calculate_gross(self):
        hra = self._basic * 0.4
        da = self._basic * 0.15
        return self._basic + hra + da

    def calculate_net(self):
        gross = self.calculate_gross()
        tax = gross * 0.1
        return gross - tax

class Manager(SalariedEmployee):

    def __init__(self, emp_id, name, basic,allowance):
        super().__init__(emp_id,name,basic)
        self._allowance = allowance

    def calculate_net(self):
        return super().calculate_gross() + self._allowance

class ContractEmployee(Employee):

    def __init__(self, emp_id, name,hrs,wage):
        super().__init__(emp_id,name)
        self._hrs = hrs
        self._wage = wage

    @override
    def calculate_gross(self):
        return self._wage * self._hrs


class Payroll:

    @staticmethod
    def display_gross(e:Employee):
        print(f'Gross sal for the month : {e.calculate_gross()}')

    @staticmethod
    def display_net(e:SalariedEmployee):
        print(f'Net sal for the month : {e.calculate_net()}')

    @staticmethod
    def display_tax(payer : TaxPayer):
        print(f'Tax :- {payer.calculate_tax()}')

if __name__ == '__main__':
    e1 = SalariedEmployee(101,'Viral',10000)
    e2 = ContractEmployee(102,'Vikram',10,100)
    e3 = Manager(103,'Krish',20000,5000)


    print(e1)
    Payroll.display_gross(e1)
    Payroll.display_net(e1)

    print(e2)
    Payroll.display_gross(e2)

    print(e3)
    Payroll.display_gross(e3)
    Payroll.display_net(e3)

