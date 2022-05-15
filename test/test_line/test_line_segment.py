from math import isclose

import pytest

from line import Vector
from line.line_segment import exceptions, LineSegment
from point import Point


class TestLineSegment:
    def test_vector(self):
        assert LineSegment(Point(1, 1), Point(2, 1)).vector == Vector(1, 0)

    def test_square_length(self):
        assert LineSegment(Point(1, 1), Point(2, 2)).square_length == 2

    def test_length(self):
        assert isclose(LineSegment(Point(2, 2), Point(1, 1)).length, 2 ** 0.5)

    def test_validate_equal_points(self):
        LineSegment(Point(0, 0), Point(1, 1))
        with pytest.raises(exceptions.EqualPoints):
            LineSegment(Point(0, 0), Point(0, 0))
