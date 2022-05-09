from math import isclose

import pytest

from point import LineSegment, Point
from triangle import RightTriangle, Triangle
from vector import Vector


class TestLineSegment:
    def test_vector(self):
        assert LineSegment(Point(1, 1), Point(2, 1)).vector == Vector(1, 0)

    def test_square_length(self):
        assert LineSegment(Point(1, 1), Point(2, 2)).square_length == 2

    def test_length(self):
        assert isclose(LineSegment(Point(2, 2), Point(1, 1)).length, 2 ** 0.5)


class TestRightTriangle:
    def test_init_triangle(self):
        assert isinstance(RightTriangle(Point(0, 0), Point(1, 0), Point(0, 2)), Triangle)
        with pytest.raises(Exception):
            RightTriangle(Point(3, 3), Point(1, 0), Point(0, 2))
