
# Copyright (C) 2010-2017 - Andreas Maier
# CONRAD is developed as an Open Source project under the GNU General Public License (GPL-3.0)

from jpype import JPackage, JArray, JDouble, JClass
from .constants import java_float_dtype
from ._imageutils import ImageUtil
from ._pygrid import PyGrid
import pyconrad

import numpy as np
import warnings

import pyopencl as cl


def _not_implemented_function(self):
    raise NotImplementedError('Not implemented yet')


def _extend_pointnd():
    @classmethod
    def _pointnd_from_numpy(cls, array):
        return cls(JArray(JDouble)(array.tolist()))

    @classmethod
    def _pointnd_from_list(cls, array):
        return cls(JArray(JDouble)(array))

    def _numpy_pointnd(self):
        return np.array(self.getCoordinates()[:])

    pointnd_class = JPackage(
        'edu').stanford.rsl.conrad.geometry.shapes.simple.PointND
    pointnd_class.as_numpy = _numpy_pointnd
    pointnd_class.from_numpy = _pointnd_from_numpy
    pointnd_class.from_list = _pointnd_from_list


def _extend_simple_vector():
    @classmethod
    def _simple_vector_from_numpy(cls, array):
        return cls(JArray(JDouble)(array.tolist()))

    @classmethod
    def _simple_vector_from_list(cls, array):
        return cls(JArray(JDouble)(array))

    def _numpy_simple_vector(self):
        return np.array(self.copyAsDoubleArray())

    simple_vector_class = JPackage(
        'edu').stanford.rsl.conrad.numerics.SimpleVector
    simple_vector_class.as_numpy = _numpy_simple_vector
    simple_vector_class.from_numpy = _simple_vector_from_numpy
    simple_vector_class.from_list = _simple_vector_from_list


def _extend_simple_matrix():
    @classmethod
    def _simple_matrix_from_numpy(cls, array):
        return cls(JArray(JDouble, np.ndim(array))(array.tolist()))

    @classmethod
    def _simple_matrix_from_list(cls, array):
        return cls(JArray(JDouble, np.ndim(array))(array))

    def _numpy_simple_matrix(self):
        return np.matrix(self.copyAsDoubleArray())

    simple_matrix_class = JPackage(
        'edu').stanford.rsl.conrad.numerics.SimpleMatrix
    simple_matrix_class.as_numpy = _numpy_simple_matrix
    simple_matrix_class.from_numpy = _simple_matrix_from_numpy
    simple_matrix_class.from_list = _simple_matrix_from_list


def _extend_numeric_grid():

    @classmethod
    def _numeric_grid_from_numpy(cls, array):
        if array.dtype != java_float_dtype:
            warnings.warn(
                'Array type is not java_float_dtype. Additional copy was needed for conversion')
            return PyGrid.from_numpy(array).grid
        else:
            return PyGrid.from_numpy(np.array(array, java_float_dtype)).grid

    @classmethod
    def _numeric_grid_from_list(cls, input_list):
        return PyGrid.from_numpy(np.array(input_list, java_float_dtype)).grid

    @classmethod
    def _numeric_grid_from_size(cls, *size):
        return PyGrid(list(size)).grid

    def _numpy_grid(self):
        return np.array(PyGrid.from_grid(self))

    def _numeric_grid_getitem(self, idxs):
        if isinstance(idxs, int) and not isinstance(self, JPackage('edu').stanford.rsl.conrad.data.numeric.Grid1D):
            return self.getSubGrid(idxs)
        elif isinstance(idxs, slice) and (isinstance(self, JPackage('edu').stanford.rsl.conrad.data.numeric.Grid3D) or (isinstance(self, pyconrad.PyConrad().classes.stanford.rsl.conrad.data.numeric.Grid4D))):
            start = idxs.start or 0
            end = idxs.stop or self.getSize()[2]
            assert idxs.step == 1 or not idxs.step, "Only step==1 is supported"

            rtn = self.type(
                reversed(*self.getSize()[:]), self.getsize()[1], end - start, False)
            # rtn = pyconrad.PyConrad().classes.stanford.rsl.conrad.data.numeric.Grid3D(self.getSize()[0],self.getSize()[1], end - start, False)
            rtn.setOrigin(self.getOrigin())
            rtn.setSpacing(self.getSpacing())
            for i in range(start, end):
                rtn.setSubGrid(i - start, self.getSubGrid(i))
            return rtn
        else:
            return self.getValue(idxs)

    def _numeric_grid_setitem(self, idxs, value):
        if isinstance(idxs, int) and not isinstance(self, JPackage('edu').stanford.rsl.conrad.data.numeric.Grid1D):
            return self.setSubGrid(idxs, value)
        else:
            return self.setValue(idxs, value)

    @property
    def _numeric_grid_shape(self):
        return list(reversed(self.getSize()[:]))

    @property
    def _numeric_grid_ndim(self):
        return len(self.getSize()[:])

    @property
    def _pygrid(self):
        return PyGrid.from_grid(self)

    def _save_as_tiff(self, path):
        ImageUtil.save_grid_as_tiff(self, path)

    def _as_device_array(self):
        return cl.MemoryObject.from_cl_mem_as_int(self.getDelegate().ID)

    @staticmethod
    def _from_tiff(path):
        return ImageUtil.grid_from_tiff(path)

    grid_class = JPackage('edu').stanford.rsl.conrad.data.numeric.NumericGrid
    grid_class.as_numpy = _numpy_grid
    grid_class.from_numpy = _numeric_grid_from_numpy
    grid_class.from_list = _numeric_grid_from_list
    grid_class.from_size = _numeric_grid_from_size
    grid_class.from_tiff = _from_tiff
    grid_class.save_tiff = _save_as_tiff
    grid_class.__getitem__ = _numeric_grid_getitem
    grid_class.__setitem__ = _numeric_grid_setitem
    grid_class.shape = _numeric_grid_shape
    grid_class.ndim = _numeric_grid_ndim
    grid_class.pygrid = _pygrid
    grid_class.__array__ = _numpy_grid

    @staticmethod
    def _oclgrid_from_numpy(numpy):
        grid = getattr(JPackage('edu').stanford.rsl.conrad.data.numeric,
                       'Grid%iD' % numpy.ndim)(*reversed(numpy.shape))
        oclgrid = getattr(JPackage('edu').stanford.rsl.conrad.data.numeric.opencl,
                          'OpenCLGrid%iD' % numpy.ndim)(grid)
        oclgrid.getDelegate().hostChanged = False
        oclgrid.getDelegate().deviceChanged = True

        numpy = numpy.astype(np.float32)

        queue = pyconrad.opencl.get_conrad_command_queue()
        cl_buffer = cl.MemoryObject.from_int_ptr(
            oclgrid.getDelegate().getCLBuffer().ID)
        cl.enqueue_copy(queue, cl_buffer, numpy)
        return oclgrid

    def _oclgrid_upload_numpy(self, numpy):

        numpy = numpy.astype(np.float32)

        queue = pyconrad.opencl.get_conrad_command_queue()
        cl_buffer = cl.MemoryObject.from_int_ptr(
            self.getDelegate().getCLBuffer().ID)
        self.getDelegate().hostChanged = False
        self.getDelegate().deviceChanged = True
        cl.enqueue_copy(queue, cl_buffer, numpy)

    def _oclgrid_download_numpy(self, numpy=None):

        if numpy is None:
            if not numpy.dtype == np.float32:
                raise TypeError('ndarray must be of dtype float32')
            if not numpy.shape == self.shape:
                raise TypeError(
                    'ndarray must have the same shape as the OCL grid')
        else:
            numpy = np.ndarray(self.shape, np.float32)

        queue = pyconrad.opencl.get_conrad_command_queue()
        cl_buffer = cl.MemoryObject.from_int_ptr(
            self.getDelegate().getCLBuffer().ID)
        cl.enqueue_copy(queue, numpy, cl_buffer)

        return numpy

    @staticmethod
    def _oclgrid_from_tiff(path):
        grid = ImageUtil.grid_from_tiff(path)
        clgrid_class = JClass(
            'edu.stanford.rsl.conrad.data.numeric.opencl.OpenCLGrid%iD' % grid.ndim)
        clgrid = clgrid_class(grid)
        return clgrid

    @staticmethod
    def _oclgrid_from_size(*size):
        grid = _numeric_grid_from_size(size)
        return getattr(_, 'OpenCLGrid%iD' % grid.ndim)(grid)

    for i in range(1, 4):
        clgrid_class = JClass(
            'edu.stanford.rsl.conrad.data.numeric.opencl.OpenCLGrid%iD' % i)
        clgrid_class.from_numpy = _oclgrid_from_numpy
        clgrid_class.from_tiff = _oclgrid_from_tiff
        clgrid_class.download = _oclgrid_download_numpy
        clgrid_class.upload = _oclgrid_upload_numpy
        clgrid_class.from_list = _not_implemented_function
        clgrid_class.from_size = _oclgrid_from_size


def extend_all_classes():
    _extend_pointnd()
    _extend_simple_vector()
    _extend_simple_matrix()
    _extend_numeric_grid()
