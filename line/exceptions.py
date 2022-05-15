from point import exceptions as point_exceptions, Point


class LineException(Exception):
    pass


class EqualPoints(LineException, point_exceptions.PointsException):
    def __init__(self, point: Point):
        self.point = point

    def __str__(self) -> str:
        return f"This line segment equal to point: {self.point}"
