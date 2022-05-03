class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


def multiply(a: Vector, b: Vector) -> float:
    return a.x * b.x + a.y * b.y
