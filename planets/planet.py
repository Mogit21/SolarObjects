
import math

class Planet:
    def __init__(self, name, equatorial_radius, avg_orbit_distance, mean_orbit_velocity, equatorial_inclination,
                 volume, density, mass, surface_area, surface_gravity, escape_velocity, atmospheric_constituents):
        self.name = name
        self.equatorial_radius = equatorial_radius
        self.equatorial_circumference = 2 * math.pi * self.equatorial_radius
        self.avg_orbit_distance = avg_orbit_distance
        self.mean_orbit_velocity = mean_orbit_velocity
        self.equatorial_inclination = equatorial_inclination
        self.volume = volume
        self.density = density
        self.mass = mass
        self.surface_area = surface_area
        self.surface_gravity = surface_gravity
        self.escape_velocity = escape_velocity
        self.atmospheric_constituents = atmospheric_constituents



class PlanetLocal:
    def __init__(self, name, equatorial_radius):
        self.name = name
        self.equatorial_radius = equatorial_radius
        self.equatorial_circumference = 2 * math.pi * equatorial_radius



earth = Planet("Earth", 6371, 40030.2)
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