#author Bastian Bier

from pyconrad import PyConrad, ImageUtil, PyGrid
import numpy as np
from matplotlib import pyplot as plt

conrad = PyConrad.get_instance()
conrad.setup('8G', '1G')
#conrad.startReconstructionFilterPipeline()
# conrad.startConrad()

package = conrad.classes.stanford.rsl.conrad.data.numeric
packagePhantom = conrad.classes.stanford.rsl.tutorial.phantoms
packageConfig = conrad.classes.stanford.rsl.conrad.utils


gridTest = package.Grid2D(30,30)
print('Print Grid2D object:',gridTest)

# TODO: Conrad has to be started such that confuguration is available. Is loaded by Conrad? Can be done Otherwise?

config = packageConfig.Configuration.getGlobalConfiguration()
print("Print CONRAD config: ",config)
#config.getGeometry();

# Create a 2D and 3D grid with CONRAD
# dimensions
w = 500
h = 300
d = 3

grid2 = packagePhantom.MickeyMouseGrid2D(w,h)
print(grid2)

grid2.show("Test Grid2D")


grid3 = packagePhantom.Sphere3D(w,h,d)
grid3.setSubGrid(0, grid2)
grid3.show("Test Grid3D")
ImageUtil.saveGrid3DAsTiff(grid3,"bsadf.tif")

plt.ion()
outputArray2 = PyGrid.from_grid(grid2).numpy()
plt.imshow(outputArray2, interpolation='nearest')
plt.title("Array2D")
plt.draw()
plt.pause(0.001)

plt.figure()
outputArray3 = PyGrid.from_grid(grid3).numpy()
plt.imshow(outputArray3[0,...], interpolation='nearest')
plt.title("Array 3D")
plt.draw()
plt.pause(0.001)
ImageUtil.saveArray3DAsTiff(outputArray3,"bsadfARRAY.tif")


outputGrid2 = ImageUtil.wrapNumpyArrayToGrid2D(outputArray2)
outputGrid2.show("outputGrid2D")

outputGrid3 = ImageUtil.wrapNumpyArrayToGrid3D(outputArray3)
outputGrid3.show("outputGrid3D")

#loadedGrid = ImageUtil.loadGrid3DfromTif("C:\\StanfordRepo\\CONRADRSL\\bsadf.tif")
#loadedGrid.show("Loaded Grid")

#loadedArray = ImageUtil.loadArray3DfromTif("C:\\StanfordRepo\\CONRADRSL\\bsadf.tif")
#loadedGrid.show("Loaded Grid")

#loadedGrid2 = ImageUtil.loadGrid2DfromTif("C:\\StanfordRepo\\CONRADRSL\\bsadf0000.tif")
#loadedGrid2.show("Loaded Grid2D")

print("End")

