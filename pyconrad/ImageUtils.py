# author Bastian Bier

import numpy as np
from . import pyCONRAD
from jpype import  *
from PIL import Image
from matplotlib import pyplot as plt

#startJVM(getDefaultJVMPath(),
#"-Djava.class.path=/localhome/local/projects/CONRAD 1.0.6/conrad_1.0.6.jar", "-Xmx8G", "-Xmn7G")
#package = JPackage("edu").stanford.rsl.conrad.data.numeric
#packageUtil = JPackage("edu").stanford.rsl.conrad.utils

# Add Save / Load functions?

class ImageUtil:
    
    ###################
    ## Image Wrapper ##
    ###################

    @staticmethod
    def wrapGrid1D(grid1D):
        array = np.asarray(grid1D.getBuffer())
        return array
    
    @staticmethod
    def wrapGrid2D(grid2D):
        w = grid2D.getWidth()
        h = grid2D.getHeight()
        array = np.array(grid2D.getBuffer()[:])
        array = np.reshape(array, (h, w))
        return array
    
    @staticmethod
    def wrapGrid3D(grid3D):
        size = grid3D.getSize()
        array = np.zeros((size[2],size[1],size[0]))
        for id in range(size[2]):
            subgrid = grid3D.getSubGrid(id)
            array[id, ...] = ImageUtil.wrapGrid2D(subgrid)
        return array

    @staticmethod
    def wrapGrid4D(grid4D):
        size = grid4D.getSize()
        array = np.zeros([size[3],size[2],size[1],size[0]])
        for f in range(size[3]):
            subgrid = grid4D.getSubGrid(f)
            array[f, ...] = ImageUtil.wrapGrid3D(subgrid)
        return array

    @staticmethod
    def wrapNumpyArrayToGrid1D(array):
        grid = pyCONRAD.getInstance().classes.stanford.rsl.conrad.data.numeric.Grid1D(array)
        return grid

    @staticmethod
    def wrapNumpyArrayToGrid2D(array):
        dim = array.shape
        flattened = array.flatten()
        grid = pyCONRAD.getInstance().classes.stanford.rsl.conrad.data.numeric.Grid2D(flattened, dim[1], dim[0])
        return grid
    
    @staticmethod
    def wrapNumpyArrayToGrid3D(array):
        dim = array.shape
        grid = pyCONRAD.getInstance().classes.stanford.rsl.conrad.data.numeric.Grid3D(dim[2], dim[1], dim[0])
        for id in range(dim[0]):
            subgrid = ImageUtil.wrapNumpyArrayToGrid2D(array[id, ...])
            grid.setSubGrid(id, subgrid)
        return grid

    @staticmethod
    def wrapNumpyArrayToGrid4D(array):
        dim = array.shape
        grid = pyCONRAD.getInstance().classes.stanford.rsl.conrad.data.numeric.Grid4D(dim[3], dim[2], dim[1], dim[0], False)
        for id in range(dim[0]):
            subgrid = ImageUtil.wrapNumpyArrayToGrid3D(array[id, ...])
            grid.setSubGrid(id, subgrid)
        return grid

    #################
    ## Save Images ##
    #################
    
    @staticmethod
    def saveGridAsTiff(grid, path):
        pyCONRAD.getInstance().classes.stanford.rsl.conrad.utils.ImageUtil.saveAs(grid, path)
        print("To be implemented")
    
    @staticmethod
    def saveArrayAsTiff(array, path):
        dim = array.shape
        if(len(dim) == 3):
            grid = ImageUtil.wrapNumpyArrayToGrid3D(array)
            ImageUtil.saveGridAsTiff(grid, path)
        else:
            print("Did not save, only available for 3D arrays")
            
     #################
     ## Load Images ##
     #################      
    
    @staticmethod
    def loadGrid2DfromTif(path):
        print("Nothing loaded: to be implemented")
    @staticmethod 
    def loadGrid3DfromTif(path):
        print("Nothing Loaded: to be implemented")    