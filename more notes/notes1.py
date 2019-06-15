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



employe1 = Employee("Corey","armstrong",50000)
employe2 = Employee("teryy","roger",60000)

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
print(employe1.raise_amount)
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