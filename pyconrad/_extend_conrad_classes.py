
# Copyright (C) 2010-2017 - Andreas Maier
# CONRAD is developed as an Open Source project under the GNU General Public License (GPL-3.0)

import pyconrad
import numpy as np

def _extend_pointnd():
    @classmethod
    def _pointnd_from_numpy(cls, array):
        return cls(pyconrad.JArray(pyconrad.JDouble)(array.tolist()))

    @classmethod
    def _pointnd_from_list(cls, array):
        return cls(pyconrad.JArray(pyconrad.JDouble)(array))

    def numpy_pointnd(self):
        return np.array(self.getCoordinates()[:])

    pointnd_class = pyconrad.PyConrad().classes.stanford.rsl.conrad.geometry.shapes.simple.PointND
    pointnd_class.numpy = numpy_pointnd
    pointnd_class.from_numpy = _pointnd_from_numpy
    pointnd_class.from_list = _pointnd_from_list

def _extend_simple_vector():
    @classmethod
    def _simple_vector_from_numpy(cls, array):
        return cls(pyconrad.JArray(pyconrad.JDouble)(array.tolist()))

    @classmethod
    def _simple_vector_from_list(cls, array):
        return cls(pyconrad.JArray(pyconrad.JDouble)(array))

    def numpy_simple_vector(self):
        return np.array(self.copyAsDoubleArray())

    simple_vector_class = pyconrad.PyConrad().classes.stanford.rsl.conrad.numerics.SimpleVector
    simple_vector_class.numpy = numpy_simple_vector
    simple_vector_class.from_numpy = _simple_vector_from_numpy
    simple_vector_class.from_list = _simple_vector_from_list

def _extend_simple_matrix():
    @classmethod
    def _simple_matrix_from_numpy(cls, array):
        return cls(pyconrad.JArray(pyconrad.JDouble,np.ndim(array))(array.tolist()))

    @classmethod
    def _simple_matrix_from_list(cls, array):
        return cls(pyconrad.JArray(pyconrad.JDouble, np.ndim(array))(array))

    def numpy_simple_matrix(self):
        return np.matrix(self.copyAsDoubleArray())

    simple_matrix_class = pyconrad.PyConrad().classes.stanford.rsl.conrad.numerics.SimpleMatrix
    simple_matrix_class.numpy = numpy_simple_matrix
    simple_matrix_class.from_numpy = _simple_matrix_from_numpy
    simple_matrix_class.from_list = _simple_matrix_from_list

def extend_all_classes():
    _extend_pointnd()
    _extend_simple_vector()
    _extend_simple_matrix()
