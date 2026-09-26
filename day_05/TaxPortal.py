from abc import ABC,abstractmethod
from typing import override
from EmployeePortal import Employee

class TaxPayer(ABC):

    def __init__(self,pan):
        self._pan = pan

    @abstractmethod
    def calculate_tax(self):
        pass

    def __str__(self):
        return f'{self._pan}'

class Consultant(TaxPayer):

    def __init__(self,pan):
        super().__init__(pan)

    def calculate_tax(self):
        return 1000

class SalariedEmployee(Employee,TaxPayer):

    def __init__(self,emp_id,name,basic,pan):
        Employee.__init__(self,emp_id,name)
        TaxPayer.__init__(self,pan)
        self._basic = basic

    @override
    def calculate_tax(self):
        gross = self.calculate_gross()
        tax = gross * 0.1
        return tax

    @override
    def calculate_gross(self):
        hra = self._basic * 0.4
        da = self._basic * 0.15
        return self._basic + hra + da

    def calculate_net(self):
        gross = self.calculate_gross()
        tax = gross * 0.1
        return gross - tax

class Manager(SalariedEmployee,TaxPayer):

    def __init__(self,emp_id,name,basic,allowance,pan):
        SalariedEmployee.__init__(self,emp_id,name,basic,pan)
        TaxPayer.__init__(self,pan)
        self._basic = basic
        self._allowance = allowance

    @override
    def calculate_gross(self):
        return  super().calculate_gross() + self._allowance

    @override
    def calculate_tax(self):
        return super().calculate_tax()

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

e1 = SalariedEmployee(1,'Viral',15000,10)
print(e1)
Payroll.display_tax(e1)

m1 = Manager(101,'Krish',10000,5000,20)
print(m1)
Payroll.display_tax(m1)

c = Consultant('TURF896N')
print(c)
Payroll.display_tax(c)