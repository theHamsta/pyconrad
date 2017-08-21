import numpy as np
from .constants import java_float_dtype



class GridIndexer:
    def __init__(self, grid, slice = Ellipsis ):
        self.__grid = grid
        self.shape = list(reversed(grid.getSize()[:]))
        self.__slice = slice
        self.__gridshape = self.shape = list(reversed(grid.getSize()[:]))

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


        if self.__slice == Ellipsis:
            start = np.zeros(len(self.shape))
            end = self.shape
            step = np.ones(len(self.shape))
        else:
            start= []
            end = []
            step = []
            if len(self.shape)!=1:
                for s in self.__slice:
                    start.append(s.start or 0)
                    end.append(s.stop)
                    step.append(s.step or 1)
                end = end or self.shape

        out = np.zeros( int((end-start) / step) , dtype )
        if len(self.shape) == 1:
            for x in range(self.__slice.start, self.__slice.stop, self.__slice.step):
                out[ x-start[0]] = self.__grid.getBuffer[x]

        elif len(self.shape) == 2:
            for y in range(start[0], end[0], step[0]):
                for x in range(start[1], end[1], step[1]):
                    out[y-start[0], x-start[1]] = self.__grid.getAtIndex(x,y)
        elif len(self.shape) == 3:
            for z in range(start[0], end[0], step[0]):
                for y in range(start[1], end[1], step[1]):
                    for x in range(start[2], end[2], step[2]):
                        out[ [z,y,x]-start ] = self.__grid.getValue([x,y,z])

        elif len(self.shape) == 4:
            for f in range(start[0], end[0], step[0]):
                for z in range(start[1], end[1], step[1]):
                    for y in range(start[2], end[2], step[2]):
                        for x in range(start[3], end[3], step[3]):
                            out[ [f,z,y,x]-start ] = self.__grid.getValue([x,y,z,f])

        else:
            raise Exception('Only dimensions from 1 to 4 supported!')
        return out.__array__()

    def __str__(self):
        return "GridIndexer " + self.shape.__str__()


    def grid(self):
        return self.__grid

    @staticmethod
    def java_float_type():
        return java_float_dtype


