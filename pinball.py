from scipy import *
from scipy.linalg import norm

def intersect(center, radius, particle_location, particle_velocity):
    """Determine how soon a prticle will hit the circle.

    center: center of the circle
    radius: radius of the circle
    particle_location: vector of particle's position
    particle_velocity: particle's veolcity vector

    returns None if there is no intersection. returns smallest positive time until
    intserstion otherwise.
    """
    intermediate_value = dot(particle_velocity, (center-particle_location))

    if intermediate_value <= 0:
        return 

    D = square(intermediate_value) - dot((center-particle_location), (center-particle_location)) + radius**2

    if D <= 0:
        return

    return intermediate_value - sqrt(D) 

def reflect(center, reflection_point, velocity):
    """Determine the new veolcity of a particle reflecting off of a circle.

    center: center of the circle
    reflection point: point where the particle is hitting the circle.
    velocity: velocity vector of the particle (a unit vector is expected)

    returns a 2 element vector
    """
    intermediate_value = center - reflection_point
    return v-((dot(2*v, intermediate_value))/(dot(intermediate_value, intermediate_value)))*intermediate_value

def arrange_circles(side_length):
    """Given a side length, return the coordinates of the three points of an
       equilateral triangle centered on the origin."""
    return [(side_length/2, -side_length*sqrt(3)/6),
            (-side_length/2, -side_length*sqrt(3)/6),
            (0, side_length*sqrt(3)/3)]

def generate_unit_vector():
    """Generate a random (evenly distributed) unit vector. Used to seed a 
        particle's velocity."""
    vector = random.random((1,2))
    return vector/norm(vector)


if __name__ == '__main__':
    circle_distance = 6
    circle_radius = 1

    u =  generate_unit_vector()
