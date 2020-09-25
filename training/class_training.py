
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

