"""python object oriented programming """
# main benefits of objected orieented programming :
# they organised data, and functions  easy to reused, or build upon

class Employee:
    pass

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+ "." + last +"@company.com"

    def fullName(self):
        return self.first +" "+ self.last



employe1 = Employee("Corey","armstrong",50000)
employe2 = Employee("teryy","roger",60000)
print(employe1)
print(employe2)
print(employe1.email)
print(employe2.email)
print(employe1.fullName())
print(employe2.fullName())
