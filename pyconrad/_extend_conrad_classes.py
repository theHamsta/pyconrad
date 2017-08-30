from jpype import *
import pyconrad
import numpy as np

def numpy_pointnd(self):
    return np.array(self.getCoordinates()[:])


def extend_all_classes():
   pointnd_class = pyconrad.PyConrad().classes.stanford.rsl.conrad.geometry.shapes.simple.PointND
   pointnd_class.numpy = numpy_pointnd