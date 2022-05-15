from point.point import Point


class TestPoint:
    def test__eq__(self):
        assert Point(1, 1) == Point(1, 1)
        assert Point(0, 1) != Point(1, 1)
        assert Point(0, 1) != object()
