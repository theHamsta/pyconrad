from __future__ import print_function
import math
import vtk


def test_distance_between_points():

    p0 = (0, 0, 0)
    p1 = (1, 1, 1)

    distSquared = vtk.vtkMath.Distance2BetweenPoints(p0, p1)

    dist = math.sqrt(distSquared)

    print("p0 = ", p0)
    print("p1 = ", p1)
    print("distance squared = ", distSquared)
    print("distance = ", dist)


if __name__ == "__main__":
    test_distance_between_points()
