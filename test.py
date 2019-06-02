from space.planet import Planet                # importing the class Planet from planet file inside package
from space.math import planet_mass,planet_volume


Earth = Planet("Earth",777,10,"Milky way")

Earth_Mass = planet_mass(Earth.gravity,Earth.radius)

Earth_Volume = planet_volume(Earth.radius)

print("Earth Mass is : " + str(Earth_Mass))

print("Earth Volume is :" + str(Earth_Volume))
