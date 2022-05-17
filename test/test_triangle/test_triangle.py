from unittest.mock import call, patch

import pytest

from point import Point
from triangle.triangle import exceptions, RightTriangle, Triangle


class TestTriangle:
    def test_validate_is_point(self):
        Triangle._validate_is_point(Point(1, 1), Point(0, 0), Point(1, 0))
        with pytest.raises(exceptions.IsPoint):
            Triangle._validate_is_point(Point(0, 0), Point(0, 0), Point(0, 0))

    @patch.object(Triangle, "_validate_line_segment")
    def test_validate_is_line(self, mock_line_segment):
        Triangle._validate_is_line(Point(1, 1), Point(0, 0), Point(1, 0))
        assert len(mock_line_segment.mock_calls) == 6
        calls = [
            call(Point(1, 1), Point(0, 0), Point(1, 0)),
            call(Point(1, 1), Point(1, 0), Point(0, 0)),
            call(Point(0, 0), Point(1, 1), Point(1, 0)),
            call(Point(0, 0), Point(1, 0), Point(1, 1)),
            call(Point(1, 0), Point(1, 1), Point(0, 0)),
            call(Point(1, 0), Point(0, 0), Point(1, 1)),
        ]
        mock_line_segment.assert_has_calls(calls, any_order=True)

    def test_validate_line_segment(self):
        Triangle._validate_line_segment(Point(1, 1), Point(0, 0), Point(1, 0))
        with pytest.raises(exceptions.IsLine):
            Triangle._validate_line_segment(Point(0, 0), Point(0, 0), Point(1, 1))

    def test_validate_triangle_inequality(self):
        Triangle._validate_triangle_inequality(Point(1, 1), Point(0, 0), Point(1, 0))
        with pytest.raises(exceptions.IsLine):
            Triangle._validate_triangle_inequality(Point(1, 2), Point(2, 4), Point(4, 8))
            Triangle._validate_triangle_inequality(Point(1, 3), Point(2, 6), Point(3, 9))
            Triangle._validate_triangle_inequality(Point(0, 0), Point(0, 1), Point(0, 2))


class TestRightTriangle:
    def test_validate_is_right(self):
        RightTriangle._validate_is_right(Point(0, 0), Point(1, 0), Point(0, 2))
        # assert isinstance(RightTriangle(Point(0, 0), Point(1, 0), Point(0, 2)), Triangle)
        with pytest.raises(exceptions.IsNotRight):
            RightTriangle._validate_is_right(Point(3, 3), Point(1, 0), Point(0, 2))
