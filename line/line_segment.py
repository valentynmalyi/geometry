from dataclasses import dataclass

from geometry import Figure
from point import Point

from . import validations
from .vector import Vector


@dataclass()
class LineSegment(Figure):
    validation_class = validations.LineSegmentValidation
    a: Point
    b: Point

    @property
    def vector(self) -> Vector:
        return Vector(self.b.x - self.a.x, self.b.y - self.a.y)

    @property
    def square_length(self) -> float:
        return self.vector.square_length

    @property
    def length(self) -> float:
        return self.vector.length
