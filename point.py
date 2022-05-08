from vector import Vector


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


class LineSegment:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    @property
    def vector(self) -> Vector:
        return Vector(self.b.x - self.a.x, self.b.y - self.a.y)

    @property
    def square_length(self) -> int:
        return self.vector.square_length

    @property
    def length(self) -> float:
        return self.vector.length
