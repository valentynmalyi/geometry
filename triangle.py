from math import isclose

from point import LineSegment, Point


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self) -> str:
        return f"A{self.a}, B{self.b}, C{self.c}"


class RightTriangle(Triangle):
    def __init__(self, a: Point, b: Point, c: Point):
        super().__init__(a=a, b=b, c=c)
        self._validate_is_right(a, b, c)

    def _validate_is_right(self, a: Point, b: Point, c: Point) -> None:
        side = sorted([LineSegment(a, b).length, LineSegment(b, c).length, LineSegment(a, c).length])
        if not isclose(side[2] ** 2, side[1] ** 2 + side[0] ** 2):
            raise Exception(f"triangle {self} isn't a right triangle")
