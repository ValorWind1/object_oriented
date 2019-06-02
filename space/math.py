def planet_mass(gravity,radius):
    mass = (gravity*radius**2) / (6.67*10**-1)
    return mass

def planet_volume(radius):
    volume = ( 4*3.142*radius**2)/3
    return volume

