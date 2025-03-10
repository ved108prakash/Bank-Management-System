from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def ifsc_code(self):
        pass

    @abstractmethod
    def Branch_address(self):
        pass

    @abstractmethod
    def Loan(self, Acc, Amount):
        pass

class Customer(Bank):
    def __init__(self):
        self.__bank_data = {}
        self.__loan_data = {}

    def ifsc_code(self):
        return 'SBIC101K'

    def Branch_address(self):
        return 'Karve Nagar, Pune'

    def Loan(self, Acc, Amount):
        if Acc in self.__bank_data:
            self.__loan_data[Acc] = Amount
            self.__bank_data[Acc]['balance'] += Amount
            return f'Loan of {Amount} Rs. approved for Account {Acc}.'
        return f'Account {Acc} not found.'

    def add_customer(self, Name, Acc, Bal):
        self.__bank_data[Acc] = {'Name': Name, 'balance': Bal}
        return f'{Name} Welcome to the Bank.'

    def check_balance(self, Acc):
        if Acc in self.__bank_data:
            return f'{self.__bank_data[Acc]["balance"]} Rs.'
        return f'Account {Acc} not found.'

    def deposit_amount(self, Acc, amount):
        if Acc in self.__bank_data:
            self.__bank_data[Acc]['balance'] += amount
            return f'{amount} Rs. deposited successfully. Total balance: {self.__bank_data[Acc]["balance"]} Rs.'
        return f'Account {Acc} not found.'

    def debit_amount(self, Acc, amount):
        if Acc in self.__bank_data and self.__bank_data[Acc]['balance'] >= amount:
            self.__bank_data[Acc]['balance'] -= amount
            return f'{amount} Rs. debited successfully. Total balance: {self.__bank_data[Acc]["balance"]} Rs.'
        return f'Account {Acc} not found or insufficient balance.'

    @property
    def get_customer_data(self):
        return self.__bank_data

    @property
    def get_loan_data(self):
        return self.__loan_data

class Bank_Emp(Customer):
    def __init__(self):
        super().__init__()
        self.__salary_data = {}

    def add_emp(self, emp_id, Acc, Bal, sal):
        self.add_customer(emp_id, Acc, Bal)  
        self.__salary_data[emp_id] = sal
        return f'{emp_id} Welcome to the Bank.'

    def check_salary(self, emp_id):
        if emp_id in self.__salary_data:
            return f'{self.__salary_data[emp_id]} Rs. is the salary of ID-{emp_id}.'
        return f'Employee {emp_id} not found.'

    @property
    def get_salary_data(self):
        return self.__salary_data

    def increase_salary(self, emp_id, new_sal):
        if emp_id in self.__salary_data:
            self.__salary_data[emp_id] = new_sal
            return f'Salary updated to {new_sal} Rs. for employee {emp_id}'
        return f'Employee {emp_id} not found.'


# Create Customer
customer = Customer()
print(customer.add_customer('Ved', 101, 5000))
print(customer.add_customer('Sumit', 102, 15000))
print(customer.deposit_amount(101, 2000))
print(customer.debit_amount(101, 3000))
print(customer.check_balance(101))
print(customer.Loan(102, 10000))
print(customer.get_customer_data)
print(customer.get_loan_data)

# Create Bank Employee
emp = Bank_Emp()
print(emp.add_emp('emp_01', 201, 15000, 20000))
print(emp.add_emp('emp_02', 202, 17000, 22000))
print(emp.check_salary('emp_01'))
print(emp.Loan(201, 7000))
print(emp.get_customer_data)
print(emp.get_salary_data)
print(emp.check_balance(201))
print(emp.debit_amount(201, 3000))
print(emp.check_balance(201))

print(emp.increase_salary('emp_02', 25000))
print(emp.check_salary('emp_02'))  


