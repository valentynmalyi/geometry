import pytest
from itertools import permutations

from point import Point
from triangle.triangle import exceptions, RightTriangle, Triangle


class TestTriangle:
    def test_validate_is_line(self):
        with pytest.raises(exceptions.IsLine):
            for a, b, c in permutations([Point(0, 0), Point(0, 0), Point(0, 1)], 3):
                Triangle(a, b, c)

    def test_validate_is_point(self):
        with pytest.raises(exceptions.IsPoint):
            RightTriangle(Point(0, 0), Point(0, 0), Point(0, 0))


class TestRightTriangle:
    def test_init_triangle(self):
        assert isinstance(RightTriangle(Point(0, 0), Point(1, 0), Point(0, 2)), Triangle)
        with pytest.raises(Exception):
            RightTriangle(Point(3, 3), Point(1, 0), Point(0, 2))
