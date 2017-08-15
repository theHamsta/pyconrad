#author Bastian Bier

import pyrad
from ImageUtils import ImageUtil
import numpy as np
from matplotlib import pyplot as plt

conrad = pyrad.getInstance()
conrad.setup()
#conrad.startReconstructionFilterPipeline()
conrad.startConrad()

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

try:
    numpyIn = np.random.rand(543)
    grid1 = ImageUtil.wrapNumpyArrayToGrid1D(numpyIn.astype(float))
    numpyOut = ImageUtil.wrapGrid1D(grid1)
    assert np.allclose(numpyIn, numpyOut)
    print("Test Grid1D passed")
except Exception as ex:
    print("Test Grid1D failed with exception:",ex)

try:
    numpyIn = np.random.rand(44,543)
    grid1 = ImageUtil.wrapNumpyArrayToGrid2D(numpyIn.astype(float))
    numpyOut = ImageUtil.wrapGrid2D(grid1)
    assert np.allclose(numpyIn, numpyOut)
    print("Test Grid2D passed")
except Exception as ex:
    print("Test Grid2D failed with exception:",ex)

try:
    numpyIn = np.random.rand(6,57,42)
    grid1 = ImageUtil.wrapNumpyArrayToGrid3D(numpyIn.astype(float))
    numpyOut = ImageUtil.wrapGrid3D(grid1)
    assert np.allclose(numpyIn, numpyOut)
    print("Test Grid3D passed")
except Exception as ex:
    print("Test Grid3D failed with exception:",ex)

try:
    numpyIn = np.random.rand(7, 6,57,42)
    grid1 = ImageUtil.wrapNumpyArrayToGrid4D(numpyIn.astype(float))
    numpyOut = ImageUtil.wrapGrid4D(grid1)
    assert np.allclose(numpyIn, numpyOut)
    print("Test Grid4D passed")
except Exception as ex:
    print("Test Grid4D failed with exception:",ex)

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
plt.imshow(outputArray3[0,...], interpolation='nearest')
plt.title("Array 3D")
plt.draw()
plt.pause(0.001)
ImageUtil.saveArrayAsTiff(outputArray3,"bsadfARRAY.tif")


outputGrid2 = ImageUtil.wrapNumpyArrayToGrid2D(outputArray2)
outputGrid2.show("outputGrid2D")

outputGrid3 = ImageUtil.wrapNumpyArrayToGrid3D(outputArray3)
outputGrid3.show("outputGrid3D")

print("End")