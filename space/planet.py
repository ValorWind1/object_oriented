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
