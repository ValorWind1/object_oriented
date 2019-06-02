class Planet:

    shape = "round"     # class level attributes , instances and object have access to

    def __init__(self,name,radius,gravity,system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):            # instance method , inside the class
        return (self.name +" its currtenly orbiting the : " + self.system)


    @classmethod  # class methods have access to all class atributes, such as attributes. unlike instance methods
    def commons(cls):
        return("all planets are"+cls.shape + " because of gravity")


    @staticmethod  # have only accesss to the parameters that itself has
    def spin (speed = "2000 miles per hour"):
        return ("the planet spins at : "+speed)



# hoth = Planet("Hoth",400000,4,"Hoth System")
# print(hoth.name)
# print(f"Name is: {hoth.name}")
# print(f"Radius is:{hoth.radius}",f"Gravity is: {hoth.gravity}",f" System is : {hoth.system}")
# print("radius is : "+ str(hoth.radius)+" gravity is : "+ str(hoth.gravity)+" system is:" + hoth.system)
# print(hoth.orbit())
# naboo = Planet("Naboo",230000,8,"Naboo System")
# print(naboo.name +" has aradius of : " + str(naboo.radius) + " with current gravity of : " +str(naboo.gravity)+ " and is located in the : " + naboo.system)
#
# print("----------------")
#
# print(Planet.shape)
# print(hoth.shape)  # example to show that instances, and objectes have access to class lvl attributes
#
# print("---------")
#
# print(Planet.commons())  # static method
#
# print ("-----")
#
# print(Planet.spin())   # static method

