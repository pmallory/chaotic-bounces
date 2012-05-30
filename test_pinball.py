from pinball import *

from scipy import *
from scipy.linalg import norm 
from numpy.testing import assert_array_equal
from nose.tools import assert_almost_equal

def test_generate_unit_vector_1():
    u = generate_unit_vector()
    assert u.size == 2

def test_generate_unit_vector_2():
    u = generate_unit_vector()
    assert_almost_equal(norm(u), 1)

def test_arrange_circles_1():
    coords = arrange_circles(1)
    test_coords = [(1/2, -1*sqrt(3)/6),
                   (-1/2, -1*sqrt(3)/6),
                   (0, sqrt(3)/3)]
    assert coords == test_coords

def test_reflect():
    velocity = array([1, 0])
    circle_center = array([2, 0])
    circle_edge = array([1,0])
    new_velocity = reflect(circle_center, circle_edge, velocity)
    assert_array_equal(new_velocity, array([-1, 0]))

