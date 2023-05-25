
import math

class Planet:
    def __init__(self, name, equatorial_radius):
        self.name = name
        self.equatorial_radius = equatorial_radius
        self.equatorial_circumference = 2 * math.pi * self.equatorial_radius

class PlanetLocal:
    def __init__(self, name, equatorial_radius):
        self.name = name
        self.equatorial_radius = equatorial_radius
        self.equatorial_circumference = 2 * math.pi * equatorial_radius



#earth = Planet("Earth", 6371, 40030.2)
#mars = Planet("Mars", 3389.5, 21296.9)
earth = Planet("Earth", 6371)
mars = Planet("Mars", 3389.5)

try:
    print (earth.name)
    #print (earth.diameter)
    print (earth.equatorial_radius)
    print (earth.equatorial_circumference)
except AttributeError as e:
    print ("Error occured:", e)

print (earth.equatorial_circumference > mars.equatorial_circumference)