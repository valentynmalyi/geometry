from line import exceptions as line_exceptions, LineSegment


class TriangleException(Exception):
    pass


class IsLine(TriangleException):
    def __init__(self, line: LineSegment):
        self.line = line
        pass

    def __str__(self) -> str:
        return f"This triangle is a line {self.line}"


class IsPoint(line_exceptions.EqualPoints, IsLine):
    def __str__(self) -> str:
        return f"This triangle equal to point: {self.point}"


class IsNotRight(TriangleException):
    def __init__(self, triangle_points: str):
        self.triangle_points = triangle_points

    def __str__(self) -> str:
        return f"{self.triangle_points} is not a right triangle"
