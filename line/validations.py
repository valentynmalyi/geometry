from __future__ import annotations

from typing import TYPE_CHECKING

from geometry import FigureValidation

from . import exceptions

if TYPE_CHECKING:
    from .line_segment import LineSegment


class LineSegmentValidation(FigureValidation):
    def __init__(self, line_segment: LineSegment):
        super().__init__()
        self.line_segment = line_segment

    def validate(self) -> None:
        self._validate_equal_points()

    def _validate_equal_points(self) -> None:
        if self.line_segment.a == self.line_segment.b:
            raise exceptions.EqualPoints(self.line_segment.a)
