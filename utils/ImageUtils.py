# author Bastian Bier

import numpy as np
from setup import pyCONRAD as pyCONRAD
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

    def wrapGrid1D(self, grid1D):
        array = np.asarray(grid1D.getBuffer())
        return array

    def wrapGrid2D(self, grid2D):
        w = grid2D.getWidth()
        h = grid2D.getHeight()
        array = np.asarray(grid2D.getBuffer())
        array = np.reshape(array, (h, w))
        return array

    def wrapGrid3D(self, grid3D):
        size = grid3D.getSize()
        array = np.zeros((size[2],size[1],size[0]))
        for id in range(size[2]):
            subgrid = grid3D.getSubGrid(id)
            array[id, ...] = ImageUtil.wrapGrid2D(subgrid)
        return array

    def wrapGrid4D(self, grid4D):
        size = grid4D.getSize()
        array = np.zeros([size[3],size[2],size[1],size[0]])
        for f in range(size[3]):
            subgrid = grid4D.getSubGrid(f)
            array[f, ...] = ImageUtil.wrapGrid3D(subgrid)
        return array

    def wrapNumpyArrayToGrid1D(self, array):
        grid = pyCONRAD.getInstance().classes.stanford.rsl.conrad.data.numeric.Grid1D(array)
        return grid

    def wrapNumpyArrayToGrid2D(self, array):
        dim = array.shape
        flattened = array.flatten()
        grid = pyCONRAD.getInstance().classes.stanford.rsl.conrad.data.numeric.Grid2D(flattened, dim[1], dim[0])
        return grid

    def wrapNumpyArrayToGrid3D(self, array):
        dim = array.shape
        grid = pyCONRAD.getInstance().classes.stanford.rsl.conrad.data.numeric.Grid3D(dim[2], dim[1], dim[0])
        for id in range(dim[0]):
            subgrid = ImageUtil.wrapNumpyArrayToGrid2D(array[id, ...])
            grid.setSubGrid(id, subgrid)
        return grid

    def wrapNumpyArrayToGrid4D(self, array):
        dim = array.shape
        grid = pyCONRAD.getInstance().classes.stanford.rsl.conrad.data.numeric.Grid4D(dim[3], dim[2], dim[1], dim[0], False)
        for id in range(dim[0]):
            subgrid = ImageUtil.wrapNumpyArrayToGrid3D(array[id, ...])
            grid.setSubGrid(id, subgrid)
        return grid

    #################
    ## Save Images ##
    #################
    
    def saveGridAsTiff(self, grid, path):
        pyCONRAD.getInstance().classes.stanford.rsl.conrad.utils.ImageUtil.saveAs(grid, path)
        print("To be implemented")
        
    def saveArrayAsTiff(self, array, path):
        dim = array.shape
        if(len(dim) == 3):
            grid = ImageUtil.wrapNumpyArrayToGrid3D(array)
            ImageUtil.saveGridAsTiff(grid, path)
        else:
            print("Did not save, only available for 3D arrays")
            
     #################
     ## Load Images ##
     #################      
    
    def loadGrid2DfromTif(self, path):
        print("Nothing loaded: to be implemented")
        
    def loadGrid3DfromTif(self, path):
        print("Nothing Loaded: to be implemented")
    