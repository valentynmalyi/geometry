from point import Point

from . import exceptions
from .vector import Vector


class LineSegment:
    def __init__(self, a: Point, b: Point):
        self._validate_equal_points(a, b)
        self.a = a
        self.b = b

    def __repr__(self) -> str:
        return f"A({self.a}), B({self.b})"

    @property
    def vector(self) -> Vector:
        return Vector(self.b.x - self.a.x, self.b.y - self.a.y)

    @property
    def square_length(self) -> int:
        return self.vector.square_length

    @property
    def length(self) -> float:
        return self.vector.length

    @staticmethod
    def _validate_equal_points(a: Point, b: Point) -> None:
        if a == b:
            raise exceptions.EqualPoints(a)
