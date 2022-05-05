from point import LineSegment, Point
from vector import Vector


class TestLineSegment:
    def test_vector_property(self):
        a = Point(1, 1)
        b = Point(2, 1)
        vector = LineSegment(a, b).vector
        assert vector == Vector(1, 0)
