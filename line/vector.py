from __future__ import annotations


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: Vector) -> Vector:
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other: Vector) -> int:
        return self.x * other.x + self.y * other.y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y

    @property
    def square_length(self) -> int:
        return self.x ** 2 + self.y ** 2

    @property
    def length(self) -> float:
        return self.square_length ** 0.5
