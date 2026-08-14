
class Employee:

    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Maneger(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            employees = []
        else:
            employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('--->', emp.fullname())


emp_1 = Developer('Raj','Thakor', 80000, 'Python')
emp_2 = Developer('Test', 'User', 50000, 'Java')

mgr_1 = Maneger('Dipak', 'Padhiyar', 45000, [emp_1])

print(mgr_1.email)
mgr_1.print_emp()
# print(emp_1.email)
# print(emp_1.prog_lang)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)








# import datetime
# my_date = datetime.date(2026, 8, 9)

# print(Employee.is_workday(my_date))





# emp_str_1 = 'arjun-thakor-40000'
# emp_str_2 = 'vansh-thakor-50000'
# emp_str_3 = 'vishal-thakor-45000'

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)
# Employee.set_raise_amt(1.05)


