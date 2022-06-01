from dataclasses import dataclass

from geometry import Figure
from point import Point

from . import validations


@dataclass()
class Triangle(Figure):
    validation_class = validations.TriangleValidation
    a: Point
    b: Point
    c: Point


class RightTriangle(Triangle):
    validation_class = validations.RightTriangleValidation


class EquilateralTriangle(Triangle):
    validation_class = validations.EquilateralTriangleValidation
