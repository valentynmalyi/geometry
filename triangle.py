from point import Point


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self) -> str:
        return f"A{self.a}, B{self.b}, C{self.c}"
