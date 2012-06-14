from pinball import *

from scipy import *
from scipy.linalg import norm 
from numpy.testing import assert_array_equal, assert_array_almost_equal
from nose.tools import assert_almost_equal

def test_random_unit_vector_1():
    u = random_unit_vector()
    assert u.size == 2

def test_random_unit_vector_2():
    u = random_unit_vector()
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

def test_ordered_unit_vectors():
    l = ordered_unit_vectors(4)
    assert_array_almost_equal(l.next(), array([1, 0]))
    assert_array_almost_equal(l.next(), array([0, 1]))
    assert_array_almost_equal(l.next(), array([-1, 0]))
    assert_array_almost_equal(l.next(), array([0, -1]))

