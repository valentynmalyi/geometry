from geometry import Figure
from point import Point

from . import validations
from .vector import Vector


class LineSegment(Figure):
    validation_class = validations.LineSegmentValidation

    def __init__(self, a: Point, b: Point):
        super().__init__(a, b)
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
