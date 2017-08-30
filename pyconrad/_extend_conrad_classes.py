from jpype import *
import pyconrad
import numpy as np

def _extend_pointnd():
    @classmethod
    def _pointnd_from_numpy(cls, array):
        return cls(JArray(JDouble)(array))

    def _pointnd_numpy(self):
        return np.array(self.getCoordinates()[:])

    pointnd_class = pyconrad.PyConrad().classes.stanford.rsl.conrad.geometry.shapes.simple.PointND
    pointnd_class.numpy = _pointnd_numpy
    pointnd_class.from_numpy = _pointnd_from_numpy

def extend_all_classes():
    _extend_pointnd()


