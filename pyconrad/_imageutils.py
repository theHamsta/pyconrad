# author Bastian Bier


class ImageUtil:

    #################
    ## Save Images ##
    #################

    @staticmethod
    def saveGrid3DAsTiff(grid, path):
        PyConrad.get_instance().classes.stanford.rsl.conrad.utils.ImageUtil.saveAs(grid, path)

    @staticmethod
    def saveGrid2DAsTiff(grid, path):
        tmp = PyConrad.get_instance().ij.IJ.ImagePlus("image", ImageUtil.wrapGrid2D(grid))
        PyConrad.get_instance().ij.IJ.saveAsTiff(tmp, path)

    @staticmethod
    def saveArray2DAsTiff(array, path):
        grid = ImageUtil.wrapNumpyArrayToGrid2D(array)
        ImageUtil.saveGri2DdAsTiff(grid, path)

    @staticmethod
    def saveArray3DAsTiff(array, path):
        grid = ImageUtil.wrapNumpyArrayToGrid3D(array)
        ImageUtil.saveGrid3DAsTiff(grid, path)

     #################
     ## Load Images ##
     #################

    def loadGrid2DfromTif(path):
        grid2D = PyConrad.get_instance().classes.stanford.rsl.conrad.utils.ImageUtil.wrapImagePlus(PyConrad.get_instance().ij.IJ.openImage(path))
        return grid2D

    def loadGrid3DfromTif(path):
        grid3D = PyConrad.get_instance().classes.stanford.rsl.conrad.utils.ImageUtil.wrapImagePlus(PyConrad.get_instance().ij.IJ.openImage(path))
        return grid3D

    def loadArray2DfromTif(path):
        grid2D = PyConrad.get_instance().classes.stanford.rsl.conrad.utils.ImageUtil.wrapImagePlus(PyConrad.get_instance().ij.IJ.openImage(path))
        array2D = ImageUtil.wrapGrid2D(grid2D)
        return array2D

    def loadArray3DfromTif(path):
        grid3D = PyConrad.get_instance().classes.stanford.rsl.conrad.utils.ImageUtil.wrapImagePlus(PyConrad.get_instance().ij.IJ.openImage(path))
        array3D = ImageUtil.wrapGrid3D(grid3D)
        return array3D
