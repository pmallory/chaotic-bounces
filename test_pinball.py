from pinball import *
from scipy.linalg import norm 

def test_generate_unit_vector_1():
    u = generate_unit_vector()
    assert u.size == 2

def test_generate_unit_vector_2():
    u = generate_unit_vector()
    assert norm(u) == 1

def test_arrange_circles_1():
    coords = arrange_circles(1)
    test_coords = [(1/2, -1*sqrt(3)/6),
                   (-1/2, -1*sqrt(3)/6),
                   (0, sqrt(3)/3)]
    assert coords == test_coords

