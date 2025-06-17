"""
Test if points are in a given bounding polygon using shapely.

Zachary Katz
zachary_katz@mines.edu
June 2025

Functions
---------
inPolygon
    Return true if point is in polygon, not including the boundary.
"""

import shapely.geometry


class BoundingShape:
    """Bounding shape parent class."""

    def __init__(self) -> None:
        """Initialize anything common to all bounding shapes."""
        self.shape = shapely.geometry.Polygon()

    def inShape(self, points: list[tuple]) -> list[bool]:
        """Determine if points are in (not on the boundary) of the shape.

        Parameters
        ----------
        points : list[tuple]
            List of tuples representing points to check.

        Returns
        -------
        list[bool]
            List of bools, true if point is in box.
        """
        assert len(points) > 0, "List of points must not be empty."
        return self.shape.contains(shapely.points(points))


class Polygon(BoundingShape):
    """Polygonal bounding box given by its corners."""

    def __init__(self, box: list[tuple]) -> None:
        """Initialize a bounding polygon.

        Parameters
        ----------
        box : list[tuple]
            List of tuples representing the vertices of the polygon.
            The last vertex should be the same as the first.
        """
        assert box[0] == box[-1], "First and last vertices must be the same."
        self.shape = shapely.geometry.Polygon(box)


class Circle(BoundingShape):
    """Circular boudning box given by its center and radius."""

    def __init__(self, center: tuple, radius: float) -> None:
        """Initialize a bounding circle.

        Parameters
        ----------
        center : tuple
            Tuple representing the center of the circle (x, y).
        radius : float
            Radius of the circle.

        """
        assert radius > 0, "Radius must be positive"
        assert len(center) == 2, "Center must be a tuple of (x, y)"
        self.shape = shapely.geometry.Point(center).buffer(radius)
