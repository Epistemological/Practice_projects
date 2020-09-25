
# 1
# how to create a simple class,
# initialize attributes for that class,
# how to create methods of that class,
# and how to create instance variables for the class

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Dennis', 'Besseling', '50000')
emp_2 = Employee('Mayra', 'Eriksson', '50000')

print(emp_1)
print(emp_2)

""" manual way of building arguments in class"""

emp_1.first = 'Dennis'
emp_1.last = 'Besseling'
emp_1.email = 'besseling.d@gmail.com'
emp_1.pay = 35000

emp_2.first = 'Mayra'
emp_2.last = 'Eriksson'
emp_2.email = 'mayra.eriksson@gmail.com'
emp_2.pay = 35000

print(emp_1.email)
print(emp_2.email)

# manual way of showing first and last name of emp_1
print('{} {}'.format(emp_1.first, emp_1.last))

# 2
# class variables = same for all instances in a class
# difference between self and class when applying class variables

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Dennis', 'Besseling', '50000')
emp_2 = Employee('Mayra', 'Eriksson', '50000')

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

#3
# class methods and static methods

# CLASS METHODS
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

emp_1 = Employee('Dennis', 'Besseling', '50000')
emp_2 = Employee('Mayra', 'Eriksson', '50000')

Employee.set_raise_amount(1.05)

# what if all the data is coming as strings separated by hiffens?
emp_str_1 = 'Dennis-Besseling-30000'
emp_str_2 = 'Mayra-Eriksson-20000'
emp_str_3 = 'Walter-Dorador-40000'

# add new method as a class method that returns the modification
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
new_emp_1.pay

# STATIC METHODS

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Dennis', 'Besseling', '50000')
emp_2 = Employee('Mayra', 'Eriksson', '50000')

import datetime
my_date = datetime.date(2020, 9, 26)

print(Employee.is_workday(my_date))


# 4 Inheritance - Creating Subclasses

class developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

dev_1 = developer('Dennis', 'Besseling', '50000', 'python')
dev_2 = developer('Mayra', 'Eriksson', '50000', 'java')

print(help(developer))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1.email)
print(dev_1.prog_lang)

class manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

mgr_1 = manager('Sue', 'Smith', 90000, [dev_1])

print(isinstance(mgr_1, manager))
# True
print(isinstance(mgr_1, Employee))
# True
print(isinstance(mgr_1, developer))
# False
print(issubclass(developer,Employee))
# True
print(issubclass(developer,manager))
# False

#5 Special (Magic/Dunder) Methods

# how to change the behavior of these two additions?
print(1+2)
print('a'+'b')

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Dennis', 'Besseling', '50000')
emp_2 = Employee('Mayra', 'Eriksson', '50000')

print(emp_1)
# Dennis Besseling - Dennis.Besseling@gmail.com
repr(emp_1)
# "Employee('Dennis', 'Besseling', 50000)"
str(emp_1)
# 'Dennis Besseling - Dennis.Besseling@gmail.com'

print(emp_1.__repr__())
# Employee('Dennis', 'Besseling', 50000)
print(emp_1.__str__())
# Dennis Besseling - Dennis.Besseling@gmail.com


print(1+2)
#3
print(int.__add__(1,2))
#3
print(str.__add__('a','b'))
#ab

print(emp_1 + emp_2)
# 100000

print(len('test'))
print(len(emp_1))

#6 Property Decorators - Getters, Setters, and Deleters


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')
emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)










