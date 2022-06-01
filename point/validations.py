from __future__ import annotations

from typing import TYPE_CHECKING

from geometry import FigureValidation

if TYPE_CHECKING:
    from .point import Point


class PointValidation(FigureValidation):
    def __init__(self, point: Point):
        super().__init__()
        self.point = point

    def validate(self) -> None:
        pass
