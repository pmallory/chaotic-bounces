import sys
import argparse
from collections import defaultdict 

import numpy
from scipy import *
from scipy.linalg import norm

import turtle

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
    v = velocity
    return v-((dot(2*v, intermediate_value))/(dot(intermediate_value, intermediate_value)))*intermediate_value

def arrange_circles(side_length):
    """Given a side length, return the coordinates of the three points of an
       equilateral triangle centered on the origin.
    """
    return [(side_length/2, -side_length*sqrt(3)/6),
            (-side_length/2, -side_length*sqrt(3)/6),
            (0, side_length*sqrt(3)/3)]

def random_unit_vector():
    """Generate a random (evenly distributed) unit vector. Used to seed a 
    particle's velocity.
    """
    angle = rand()*2*pi
    return array([cos(angle), sin(angle)])


def ordered_unit_vectors(n):
    """A generator that yields n evenly spaced unit vectors."""
    increment_size = (2*pi)/n

    for angle in arange(0, 2*pi, increment_size):
        yield array([cos(angle), sin(angle)])

def run_trial(circles, circle_radius, initial_velocity):
    """Determine the path of a bouncing particle.

    circles: a list of the center points of the circles
    circle_radius: the radii of the circles
    initial_velocity: the initial velocity of the particle. if None, a random
                      unit vector is used
    """
    particle_position = array([0,0])
    particle_velocity = initial_velocity

    collision_list = [particle_position]
    
    # the previously collided with circle. Don't check for collisions with it.
    prev_circ = None

    # we don't need to reevaluate this reference on every iteration 
    append_method = collision_list.append

    while True:
        for circle in filter(lambda c: c!=prev_circ, circles):
            t = intersect(circle, circle_radius,
                          particle_position, particle_velocity)
            if t:
                new_position = particle_position + t*particle_velocity
                new_velocity = reflect(circle, new_position, particle_velocity)
                particle_position = new_position
                particle_velocity = new_velocity
                append_method(new_position)
                prev_circ = circle
            else:
                return collision_list

def draw_trial(circle_distance, circle_radius, collision_list):
    """Display a graphical representation of a trial.

    All units multiplied by 10 for clarity.
    """
    turtle.penup()
    turtle.hideturtle()
    turtle.speed('fastest')

    circles = arrange_circles(circle_distance)

    # draw the circles
    for circle in circles:
        turtle.setpos(circle[0]*40, circle[1]*40)
        turtle.dot(2*circle_radius*40)

    # draw the particle's path
    turtle.setpos(collision_list[0])
    turtle.pendown()

    for n in collision_list:
        turtle.setpos(n*40)

    turtle.Screen().exitonclick()

def generate_report(filename, results):
    """Write out the reflection pts of the ten bounciest particles."""
    if len(results) < 10:
        return

    paths = sorted(results, key=len, reverse=True)[:10]

    report = """Best Bouncers Report:
    #1:{}
    #2:{}
    #3:{}
    #4:{}
    #5:{}
    #6:{}
    #7:{}
    #8:{}
    #9:{}
    #10:{}
    """.format(paths[0], paths[1], paths[2], paths[3], paths[4], paths[5], paths[6], paths[7], paths[8], paths[9])

    with open(filename, 'w') as f:
        f.write(report)

if __name__ == '__main__':
    # Set command line options
    parser = argparse.ArgumentParser(description='Model a simple chaotic system.')

    parser.add_argument('-d', '--distance', type=int, default=6, help='The distance \
                        between the circles')
    parser.add_argument('-r', '--radius', type=int, default=1, help='The radius \
                        of each circle')
    parser.add_argument('-t', '--trials', type=int, default=1000, help='How many \
                        trials should be run')
    parser.add_argument('-e', '--even', action='store_true', help='Use evenly \
                        evenly spaced trial velocity. Random velocities used by \
                        default.')
    parser.add_argument('-o', '--output', type=str, help='Specify a file to \
                        output a report to.')

    # Set model conditions
    args = parser.parse_args()
    circle_distance = args.distance
    circle_radius = args.radius
    trials = args.trials
    if args.even:
        angles = ordered_unit_vectors(trials)
    circles = arrange_circles(circle_distance)

    # retain the reflection points of the 10 trials with the most bounces
    results = []
    # count the frequencies of the bounce counts
    counter = defaultdict(int)

    # Run tials
    for i in xrange(trials):
        if args.even:
            initial_velocity =  angles.next()
        else:
            initial_velocity = random_unit_vector()

        result = run_trial(circles, circle_radius, initial_velocity)
    
        results.append(result)
        # Only retain the bounce records of the 10 bounciest particles.
        if len(results) > 10:
            results.remove(min(results, key=len))

        # count how many times this number of bounces has happened
        counter[len(result)-1] += 1

        # progress indicator
        sys.stdout.write('\r{0}% complete'.format(100*i/float(trials)))
        sys.stdout.flush()
    else:
        # overwrite progess indicator after the loop
        sys.stdout.write('\rTrials complete!    ')
        print '\nRelative Frequencies:'

    # determine relative frequencies
    for bounce_count in counter:
        print '\t{} bounces: {}%'.format(bounce_count,
                counter.get(bounce_count)/float(trials)*100)

    # write report to output.
    if args.output:
        generate_report(args.output, results)

    # display the trial with the most bounces.
    draw_trial(circle_distance, circle_radius, max(results, key=len))

