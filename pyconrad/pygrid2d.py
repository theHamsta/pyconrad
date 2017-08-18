import numpy as np
from . import PyConrad
import jpype


float_dtype = np.dtype(">f4")

class PyGrid2D:
    def __init__(self, shape):
        self.__numericpackage = PyConrad.getInstance().classes.stanford.rsl.conrad.data.numeric
        self.__grid = self.__numericpackage.Grid2D(shape[1], shape[0])
        self.__numpy = np.zeros( shape, float_dtype )
        self.__dbuffer = jpype.nio.convertToDirectBuffer(self.__numpy)
        self.shape = shape

    @staticmethod
    def from_numpy(array):
        instance = PyConrad([0,0])
        instance.__grid = instance.__numericpackage.Grid2D(array.shape[1], array.shape[0])
        instance.__numpy = array
        instance.__dbuffer = jpype.nio.convertToDirectBuffer(array)
        instance.shape = array.shape
        instance.update_grid

    @staticmethod
    def from_conrad_grid(grid):
        instance = PyConrad([0,0])
        instance.__grid = grid
        instance.__numpy = np.array(grid.getSize[1], grid.getSize[0])
        instance.__dbuffer = jpype.nio.convertToDirectBuffer(instance.__numpy)
        instance.shape = instance.__numpy.shape
        instance.update_numpy

    def grid(self):
        return self.__grid

    def numpy(self):
        return self.__numpy

    def update_numpy(self):
        assert (self.__numpy.shape == self.shape)
        self.__dbuffer.asFloatBuffer().put(self.__grid.getBuffer())

    def update_grid(self):
        self.__dbuffer.asFloatBuffer().get(self.__grid.getBuffer())

    def save_numpy(self, name):
        from scipy.misc import imsave
        imsave(name, self.__numpy)

    def shape(self):
        return self.shape


