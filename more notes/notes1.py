import datetime
"""python object oriented programming """

# main benefits of objected orieented programming :
# they organised data, and functions  easy to reused, or build upon

class Employee:

    raise_amount = 1.04
    num_of_emplos = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+ "." + last +"@company.com"

        Employee.num_of_emplos += 1

    def fullName(self):
        return self.first +" "+ self.last

    def apply_raised(self):
        self.pay = int(self.pay * self.raise_amount)



    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount


    @classmethod
    def from_string(cls,employee_str):
        first, last, pay = employee_str.split("-")
        return Employee(first, last, pay)


    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

        # unanvigous representation of the object (debbuging)
    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

        # readable representation of an object (display to end user)
    def __str__(self):
        return '{}-{}'.format(self.fullName(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullName())

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang= prog_lang



class Manager(Employee):

    def __init__(self,first,last,pay,employees = None): # list of employees
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []  # = to an empty list
        else:
            self.employees = employees



    def add_employee_Manager(self, employeeManaged):
        if employeeManaged not in self.employees:
            self.employees.append(employeeManaged)

    def remove_employee_Manager(self,employeeRemove):
        if employeeRemove in self.employees:
            self.employees.append(employeeRemove)

    def print_current_employees(self):
        for i in self.employees:
            print("--->", i.fullName())

    # unanvigous representation of the object (debbuging)
    def __repr__(self):
         return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

    # readable representation of an object (display to end user)
    def __str__(self):
        return '{}-{}'.format(self.fullName(),self.email)

employe1 = Employee('Corey','armstrong',50000)
employe2 = Employee('teryy','roger',60000)
#using __add__( ) method
print(employe1+employe2)
# using __len__ method
print(len(employe1))
print("-------------")
print(employe1)
print(employe2)
print(employe1.email)
print(employe2.email)
print(employe1.fullName())
print(employe2.fullName())
print("--------------")

Employee.set_raise_amount(1.05)
print("salary")
print(employe1.pay)
print(employe1.apply_raised())
print(employe1.pay)

print("---------------")
print("number of employees : "+str(Employee.num_of_emplos))
print("--------------")


print("--------------")
employee_str_1 = "John-doe-7000"
employee_str_2 = "Steve-Smith-5000"
employee_str_3 = "Jane-Doe-6000"

#separting from a string separated by -

new_employee1 = Employee.from_string(employee_str_1)
new_employee2 = Employee.from_string(employee_str_2)

print(new_employee2.first+ " salary:  "+new_employee2.pay)
print(new_employee1.first+ " salary: "+new_employee1.pay)


print("----------------")
#
my_date = datetime.date(2019,6,15)
print(Employee.is_workday(my_date))

# ************************************************************

print("----------------------------")
print("--------Developers------------")

dev1 = Developer("lams", "wind",9000, "Python")
dev2 = Developer("adams","wood",8000, "Java")

print(dev1.fullName()+" languague : "+dev1.prog_lang)
print(dev2.fullName()+" languague : "+dev2.prog_lang)

# ************************************************************

print ("----------------------------")
print("------Managers---------------")

mgr1 = Manager("Sue","Smith",10000,[dev1])
print(mgr1.email)

mgr1.add_employee_Manager(dev1)

mgr1.print_current_employees()
print(mgr1)


print("============")
# will tells us if an objected is an instance of a class
print(isinstance(mgr1,Manager))

# if an object is a instance of a subclass

print(issubclass(Developer,Employee))



