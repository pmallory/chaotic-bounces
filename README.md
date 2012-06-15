Chaotic Bounces
===============

This project exists so thet I can explore SciPy and NumPy. The objective is to model a simple chaotic system.

The system:
    Three circles of some radius are placed on the vertices of an equilateral triangle of some size centered on the origin. A particle with an initial position on the origin moving in a random direction will reflect off the circles zero or more times before it escapes. How many bounces it makes depends on its initial direction.

Usage
=====

<pre>
usage: pinball.py [-h] [-d DISTANCE] [-r RADIUS] [-t TRIALS] [-e]

optional arguments:
  -h, --help            show this help message and exit
  -d DISTANCE, --distance DISTANCE
                        The distance between the circles
 -r RADIUS, --radius RADIUS
                        The radius of each circle
  -t TRIALS, --trials TRIALS
                        How many trials should be run
  -e, --even            Use evenly evenly spaced trial velocity. Random
                        velocities used by default.
</pre>
