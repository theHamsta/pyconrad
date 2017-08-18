import numpy as np
from .constants import java_float_dtype




class GridIndexer:
    def __init__(self, grid, slice = Ellipsis ):
        self.__grid = grid
        self.shape = list(reversed(grid.getSize()[:]))
        self.__slice = slice

    def __getitem__(self, idx):
        return self.__class__(self.__grid, idx)

    # TODO matrix values
    def __setitem__(self, slice, value):
        for y in range(slice[0].start or 0, slice[0].stop or self.shape[0], slice[0].step or 1 ):
            for x in range(slice[1].start or 0, slice[1].stop or self.shape[1], slice[1].step or 1 ):
                self.__grid.setAtIndex(x,y,value)

    def __iter__(self):
        for y in range(self.__slice[0].start or 0, self.__slice[0].stop or self.shape[0], self.__slice[0].step or 1 ):
            for x in range(self.__slice[1].start or 0, self.__slice[1].stop or self.shape[1], self.__slice[1].step or 1 ):
                yield self.__grid.getAtIndex(x,y)

    def __array__(self, dtype = java_float_dtype):
        start = [self.__slice[0].start or 0, self.__slice[1].start or 0 ]
        end = [self.__slice[0].stop or self.shape[0], self.__slice[1].stop or self.shape[1] ]
        step = [self.__slice[0].step or 1, self.__slice[1].step or 1 ]
        out = np.zeros( [int((end[1]-start[1]) / step[1]),int((end[1]-start[1]) / step[1])] , dtype )
        for y in range(self.__slice[0].start or 0, self.__slice[0].stop or self.shape[0], self.__slice[0].step or 1 ):
            for x in range(self.__slice[1].start or 0, self.__slice[1].stop or self.shape[1], self.__slice[1].step or 1 ):
                out[y,x] = self.__grid.getAtIndex(x,y)
        return out

    # def __str__(self):
    #     return self.__array__().__str__()

    def grid(self):
        return self.__grid

    @staticmethod
    def java_float_type():
        return java_float_dtype


