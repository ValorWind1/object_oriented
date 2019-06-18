"""property decorator: get set attributes  """

class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        # self.email = first + "." +last + "@email.com"

    @property
    def fullName(self):
        return '{} {}'.format(self.first,self.last)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    #setter
    @fullName.setter
    def fullName(self,name):
        first,last = name.split(" ")
        self.first = first
        self.last = last

    #deletter
    @fullName.deleter
    def fullName(self):
        print("Delete Name!")
        self.first = None
        self.last = None



employee1 = Employee("sam","bridges")

employee1.fullName = "fragile bridges"

print(employee1.first)
print(employee1.last)
print(employee1.fullName)# we dont need to put () method. because of @property
print(employee1.email) # we dont need to put () method. because of @property

del employee1.fullName