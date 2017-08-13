#author Bastian Bier

from jpype import  *
from ImageUtils import ImageUtil
import numpy as np
from matplotlib import pyplot as plt

#can be removed using saibenz method
package = JPackage("edu").stanford.rsl.conrad.data.numeric
packagePhantom = JPackage("edu").stanford.rsl.tutorial.phantoms
packageConfig = JPackage("edu").stanford.rsl.conrad.utils


gridTest = package.Grid2D(30,30)
print(gridTest)

# TODO: Conrad has to be started such that confuguration is available. Is loaded by Conrad? Can be done Otherwise?

config = packageConfig.Configuration.getGlobalConfiguration()
print(config)
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
ImageUtil.saveGridAsTiff(grid3,"bsadf.tif")

plt.ion()
outputArray2 = ImageUtil.wrapGrid2D(grid2)
plt.imshow(outputArray2, interpolation='nearest')
plt.title("Array2D")
plt.draw()
plt.pause(0.001)

plt.figure()
outputArray3 = ImageUtil.wrapGrid3D(grid3)
plt.imshow(outputArray3, interpolation='nearest')
plt.title("Array 3D")
plt.draw()
plt.pause(0.001)
ImageUtil.saveArrayAsTiff(outputArray3,"bsadfARRAY.tif")


outputGrid2 = ImageUtil.wrapNumpyArrayToGrid2D(outputArray2)
outputGrid2.show("outputGrid2D")

outputGrid3 = ImageUtil.wrapNumpyArrayToGrid3D(outputArray3)
outputGrid3.show("outputGrid3D")

print("End")

while True:
    a = 2