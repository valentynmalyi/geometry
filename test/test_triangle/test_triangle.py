from unittest.mock import patch

import pytest

from point import Point
from triangle.triangle import exceptions, RightTriangle, Triangle


class TestTriangle:
    def test_validate_is_three_dot_line(self):
        Triangle._validate_is_three_dot_line(Point(1, 1), Point(0, 0), Point(1, 0))
        with pytest.raises(exceptions.IsLine):
            Triangle._validate_is_three_dot_line(Point(0, 0), Point(0, 1), Point(0, 2))

    @patch("triangle.Triangle._validate_line_segment")
    def test_validate_is_two_dot_line(self, test_mock):
        Triangle._validate_is_two_dot_line(Point(1, 1), Point(0, 0), Point(1, 0))
        assert len(test_mock.mock_calls) == 6
        """  # can I do two related assert for one test function??? If I want to check specific call input
            calls = [ call(Point(1, 1), Point(0, 0), Point(1, 0)), #noqa W291
            call(Point(1, 1), Point(1, 0), Point(0, 0)),
            call(Point(0, 0), Point(1, 1), Point(1, 0)),
            call(Point(0, 0), Point(1, 0), Point(1, 1)),
            call(Point(1, 0), Point(1, 1), Point(0, 0)),
            call(Point(1, 0), Point(0, 0), Point(1, 1))
        ]
        test_mock.assert_has_calls(calls, any_order=True)
        """

    def test_validate_line_segment(self):
        Triangle._validate_line_segment(Point(1, 1), Point(0, 0), Point(1, 0))
        with pytest.raises(exceptions.IsLine):
            Triangle._validate_line_segment(Point(0, 0), Point(0, 0), Point(1, 0))

    def test_validate_is_point(self):
        Triangle._validate_is_point(Point(1, 1), Point(0, 0), Point(1, 0))
        with pytest.raises(exceptions.IsPoint):
            Triangle._validate_is_point(Point(0, 0), Point(0, 0), Point(0, 0))


class TestRightTriangle:
    def test_validate_is_right(self):
        RightTriangle._validate_is_right(Point(0, 0), Point(1, 0), Point(0, 2))
        # assert isinstance(RightTriangle(Point(0, 0), Point(1, 0), Point(0, 2)), Triangle)
        with pytest.raises(exceptions.IsNotRight):
            RightTriangle._validate_is_right(Point(3, 3), Point(1, 0), Point(0, 2))
