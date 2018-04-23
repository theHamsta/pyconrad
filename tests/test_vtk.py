from __future__ import print_function
import math
import vtk
from os.path import join, dirname
import pyconrad.autoinit


def test_distance_between_points():

    p0 = (0, 0, 0)
    p1 = (1, 1, 1)

    distSquared = vtk.vtkMath.Distance2BetweenPoints(p0, p1)

    dist = math.sqrt(distSquared)

    print("p0 = ", p0)
    print("p1 = ", p1)
    print("distance squared = ", distSquared)
    print("distance = ", dist)


def test_read_vti():
    path = join(dirname(__file__), 'small_domain.vti')
    _ = pyconrad.ClassGetter()
    grid = _.NumericGrid.from_vtk(path)
    print(grid)
    print(grid.origin)
    print(grid.spacing)


if __name__ == "__main__":
    test_distance_between_points()
    test_read_vti()
