from geometry import Figure
from point import Point

from . import validations


class Triangle(Figure):
    validation_class = validations.TriangleValidation

    def __init__(self, a: Point, b: Point, c: Point):
        super().__init__(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self) -> str:
        return f"A{self.a}, B{self.b}, C{self.c}"


class RightTriangle(Triangle):
    validation_class = validations.RightTriangleValidation
