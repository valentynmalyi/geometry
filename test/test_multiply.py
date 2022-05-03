from multiply import multiply, Vector


def test_multiply():
    v1 = Vector(1, 1)
    v2 = Vector(1, 2)
    assert multiply(v1, v2) == 3
