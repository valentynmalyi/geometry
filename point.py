from vector import Vector


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class LineSegment:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    @property
    def vector(self) -> Vector:
        return Vector(self.b.x - self.a.x, self.b.y - self.b.y)

    # implement methods square_length and length
