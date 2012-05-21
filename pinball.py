from scipy import *

def intersect(center, radius, particle_location, particle_velocity):
    intermediate_value = dot(particle_velocity, (center-particle_location))

    if intermediate_value <= 0:
        return 

    D = square(intermediate_value) - dot((center-particle_location), (center-particle_location)) + radius**2

    if D <= 0:
        return

    return intermediate_value - sqrt(D) 

def reflect(center, reflection_point, velocity):
    intermediate_value = center - reflection_point
    return v-((dot(2*v, intermediate_value))/(dot(intermediate_value, intermediate_value)))*intermediate_value


if __name__ == '__main__':
    center = array([1, 0])
    radius = 1 
    particle_location = array([0,0])
    particle_velocity= array([1,0])
    print intersect(center, radius, particle_location, particle_velocity)
