from multiply import Vector


class TestVector:
    def test__add__(self):
        v1 = Vector(1, 1)
        v2 = Vector(1, 2)
        v3 = v1 + v2
        assert v3.x == 2
        assert v3.y == 3

    def test__mul__(self):
        v1 = Vector(1, 1)
        v2 = Vector(1, 2)
        res = v1 * v2
        assert res == 3
