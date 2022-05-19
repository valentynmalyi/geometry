from geometry import FigureValidation
from point import Point

from . import exceptions


class LineSegmentValidation(FigureValidation):
    def __init__(self, a: Point, b: Point):
        super().__init__(a, b)
        self.a = a
        self.b = b

    def validate(self) -> None:
        self._validate_equal_points()

    def _validate_equal_points(self) -> None:
        if self.a == self.b:
            raise exceptions.EqualPoints(self.a)
