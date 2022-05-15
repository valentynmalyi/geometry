from math import isclose

from line.vector import Vector


class TestVector:
    def test__add__(self):
        assert Vector(1, 1) + Vector(1, 2) == Vector(2, 3)

    def test__mul__(self):
        assert Vector(1, 1) * Vector(1, 2) == 3

    def test__eq__(self):
        assert Vector(1, 1) == Vector(1, 1)
        assert Vector(0, 1) != Vector(1, 1)
        assert Vector(0, 1) != object()

    def test_square_length_property(self):
        assert Vector(1, 1).square_length == 2

    def test_length_property(self):
        assert isclose(Vector(1, 1).length, 2 ** 0.5)
