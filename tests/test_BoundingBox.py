"""Tests for BoundingPolygon.py."""

import src.BoundingPolygon as BoundingPolygon
import numpy as np
import pytest


def test_inPolygon():
    """Test cases for inPolygon as an axes-aligned box."""
    # Multiple Points
    box = BoundingPolygon.BoundingPolygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])
    points = [(0.5, 0.5), (2, 2), (-4, -4)]
    np.testing.assert_array_equal(box.inPolygon(points), [True, False, False])

    # Empty list
    box = BoundingPolygon.BoundingPolygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])
    points = []
    with pytest.raises(AssertionError, match="List of points must not be empty."):
        box.inPolygon(points)

    # On Edge, Single Point
    box = BoundingPolygon.BoundingPolygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])
    points = [(0, 0)]
    print(box.inPolygon(points))
    np.testing.assert_array_equal(box.inPolygon(points), [False])
