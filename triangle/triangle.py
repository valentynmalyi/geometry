from itertools import permutations
from math import isclose

from line import exceptions as line_exception, LineSegment
from point import Point

from . import exceptions


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self._validate(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self) -> str:
        return f"A{self.a}, B{self.b}, C{self.c}"

    @classmethod
    def _validate(cls, a: Point, b: Point, c: Point) -> None:
        cls._validate_is_point(a, b, c)
        cls._validate_is_line(a, b, c)

    @classmethod
    def _validate_is_line(cls, a: Point, b: Point, c: Point) -> None:
        for a, b, c in permutations([a, b, c], 3):
            cls._validate_line_segment(a, b, c)
            cls._validate_triangle_inequality(a, b, c)

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

    @staticmethod
    def _validate_is_point(a: Point, b: Point, c: Point) -> None:
        if a == b == c:
            raise exceptions.IsPoint(a)


class RightTriangle(Triangle):
    def __init__(self, a: Point, b: Point, c: Point):
        super().__init__(a, b, c)
        self._validate_is_right(a, b, c)

    @classmethod
    def _validate_is_right(cls, a: Point, b: Point, c: Point) -> None:
        side_a, side_b, side_c = sorted([
            LineSegment(a, b).square_length, LineSegment(b, c).square_length, LineSegment(a, c).square_length
        ])
        if not isclose(side_c, side_a + side_b):
            raise exceptions.IsNotRight(f'{cls}')
