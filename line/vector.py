from __future__ import annotations

from dataclasses import dataclass


@dataclass()
class Vector:
    x: float
    y: float

    def __add__(self, other: Vector) -> Vector:
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other: Vector) -> float:
        return self.x * other.x + self.y * other.y

    @property
    def square_length(self) -> float:
        return self.x ** 2 + self.y ** 2

    @property
    def length(self) -> float:
        return self.square_length ** 0.5
