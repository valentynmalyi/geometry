from __future__ import annotations

from itertools import permutations
from math import isclose
from typing import TYPE_CHECKING

from geometry import FigureValidation
from line import exceptions as line_exception, LineSegment
from point import Point

from . import exceptions

if TYPE_CHECKING:
    from .triangle import Triangle


class TriangleValidation(FigureValidation):
    def __init__(self, triangle: Triangle):
        super().__init__()
        self.triangle = triangle

    def validate(self) -> None:
        self._validate_is_point()
        self._validate_is_line()

    def _validate_is_line(self) -> None:
        for a, b, c in permutations([self.triangle.a, self.triangle.b, self.triangle.c], 3):
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
        if self.triangle.a == self.triangle.b == self.triangle.c:
            raise exceptions.IsPoint(self.triangle.a)


class RightTriangleValidation(TriangleValidation):
    def validate(self) -> None:
        super().validate()
        self._validate_is_right()

    def _validate_is_right(self) -> None:
        side_a, side_b, side_c = sorted([
            LineSegment(self.triangle.a, self.triangle.b).square_length,
            LineSegment(self.triangle.b, self.triangle.c).square_length,
            LineSegment(self.triangle.a, self.triangle.c).square_length,
        ])
        if not isclose(side_c, side_a + side_b):
            raise exceptions.IsNotRight(f'{self}')


class EquilateralTriangleValidation(TriangleValidation):
    def validate(self) -> None:
        super().validate()
        self._validate_is_equilateral()

    def _validate_is_equilateral(self) -> None:
        c = LineSegment(self.triangle.a, self.triangle.b).square_length
        b = LineSegment(self.triangle.a, self.triangle.c).square_length
        a = LineSegment(self.triangle.b, self.triangle.c).square_length
        if not isclose(a, b) and not isclose(a, c):
            raise exceptions.IsNotEquilateral(f'{self}')
