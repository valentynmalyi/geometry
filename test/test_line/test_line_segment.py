from math import isclose

from line import Vector
from line.line_segment import LineSegment
from point import Point


class TestLineSegment:
    def test_vector(self):
        assert LineSegment(Point(1, 1), Point(2, 1)).vector == Vector(1, 0)

    def test_square_length(self):
        assert LineSegment(Point(1, 1), Point(2, 2)).square_length == 2

    def test_length(self):
        assert isclose(LineSegment(Point(2, 2), Point(1, 1)).length, 2 ** 0.5)
