#parent class
class Pets:

    dogs = []
    def __init__(self,dogs):
        self.dogs = dogs

    def walk(self):
        for i in self.dogs:
            print(i.walk())



"""
 Remember: the class is just for defining the Dog,
 not actually creating instances of individual dogs with specific names and ages
 (class just the blueprint)
"""
class Dog:
    """
    Use the __init__() method to initialize (e.g., specify)
    an object’s initial attributes by giving them their default value (or state).
    """

    def __init__(self,name,age):
        #instance attributes
        self.name = name
        self.age = age
        self.hungry = True

    # class attributes
    species = "mammal"


    #instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self,sound):
        return "{} says {}".format(self.name,sound)

    def eat(self):
        self.hungry = False

    def walk(self):
        return "%s is walking!"%(self.name)


def get_biggest_number(*args):
    return max(args)



# instatiate(represent) object
chester = Dog("Chester",4)
tomo =Dog("Tomo",5)
pluto = Dog("Pluto",7)
ryuka = Dog("Ryuka",3)
yoko = Dog("Yoko",2)

print( "--------------------")
# instatiate instance methods

print(tomo.description())
print(tomo.speak("woof"))

print("---------------------")


#Access the instance attributes
print ("{} is {} and {} is {}.".format(chester.name,chester.age,tomo.name,tomo.age))

# is chester a mammal ?
if chester.species == "mammal":
    print("{0} is a {1}!".format(chester.name,chester.species))

# determine oldest dog
print("The oldest dog is {} years old.".format(get_biggest_number(tomo.age,pluto.age,ryuka.age,yoko.age)))



print('----------------------')
"""
child class ( inheriting from dog class)
"""
class Bulldog(Dog):
    def run(self,speed):
        return "{} runs {}".format(self.name,speed)


jim = Bulldog("craky",12)
print(jim.description())

print(jim.run("slow"))



"""
another child class
"""

class RussellTerrier(Dog):
    def run(self,run):
        return "{} runs {}".format(self.name,run)

ana = RussellTerrier("ana",7)
print(ana.description())
print(ana.run("medium"))





# instantiating pets class
"""
pets class
"""
print( "******************")


list_dogs = [ Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)]

pets = Pets(list_dogs)

print("I have {} dogs".format(len(pets.dogs)))
for i in pets.dogs:
    print("{} is {}".format(i.name,i.age))
print("and they ae all {}s, of course".format(i.species))






"""
hungry dogs method 
"""
print("------------------------------")
hungry_dogs = [Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9),Dog("Tomo",5)]

hungry_pets = Pets(hungry_dogs)

print("I have {} dogs".format(len(hungry_pets.dogs)))
for i in hungry_pets.dogs:
    print("{} is {}".format(i.name,i.age))
print("and they are all {}s, of course".format(i.species))

are_my_dogs_hungry = False
for i in hungry_pets.dogs:
    if i.hungry:
        are_my_dogs_hungry = True

if are_my_dogs_hungry:
    print("My dogs are Hungry")
else:
    print("My dogs are not Hungry")

print ("xxxxxxxxxxxxxxxxxxx")





"""
walking dogs 
"""
walking_dogs = [Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9),Dog("Tomo",5)]

walking_doggos=Pets(walking_dogs)

print(walking_doggos.walk())