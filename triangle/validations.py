from itertools import permutations
from math import isclose

from geometry import FigureValidation
from line import exceptions as line_exception, LineSegment
from point import Point

from . import exceptions


class TriangleValidation(FigureValidation):
    def __init__(self, a: Point, b: Point, c: Point):
        super().__init__(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def validate(self) -> None:
        self._validate_is_point()
        self._validate_is_line()

    def _validate_is_line(self) -> None:
        for a, b, c in permutations([self.a, self.b, self.c], 3):
            self._validate_line_segment(a, b, c)
            self._validate_triangle_inequality(a, b, c)

    @staticmethod
    def _validate_line_segment(a: Point, b: Point, c: Point) -> None:
        try:
            LineSegment(a, b)
        except line_exception.EqualPoints:
            raise exceptions.IsLine(LineSegment(a, c))

    @staticmethod
    def _validate_triangle_inequality(a: Point, b: Point, c: Point) -> None:
        if LineSegment(a, c).length >= (LineSegment(a, b).length + LineSegment(b, c).length):
            raise exceptions.IsLine(LineSegment(a, c))

    def _validate_is_point(self) -> None:
        if self.a == self.b == self.c:
            raise exceptions.IsPoint(self.a)


class RightTriangleValidation(TriangleValidation):
    def validate(self) -> None:
        super().validate()
        self._validate_is_right()

    def _validate_is_right(self) -> None:
        side_a, side_b, side_c = sorted([
            LineSegment(self.a, self.b).square_length,
            LineSegment(self.b, self.c).square_length,
            LineSegment(self.a, self.c).square_length,
        ])
        if not isclose(side_c, side_a + side_b):
            raise exceptions.IsNotRight(f'{self}')
