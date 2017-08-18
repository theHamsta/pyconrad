from pyconrad import PyGrid2D, PyConrad, ImageUtil
import numpy as np

PyConrad.getInstance().setup()

phantom_package = PyConrad.getInstance().classes.stanford.rsl.tutorial.phantoms
shape = [230, 330]

pygrid = PyGrid2D(shape)
print(pygrid)

try:
    numpyIn = np.random.rand(shape[0],shape[1]).astype(PyGrid2D.java_float_type())
    pygrid2 = PyGrid2D.from_numpy(numpyIn)
    numpyOut = ImageUtil.wrapGrid2D(pygrid2.grid())
    print(pygrid2)
    print(numpyOut)
    print("Test from_numpy passed")
except Exception as ex:
    print(ex)
    print("Test from_numpy failed")

try:
    gridIn = phantom_package.MickeyMouseGrid2D(shape[1], shape[0])
    # gridIn = PyConrad.numeric_package().Grid2D(shape[1], shape[0])
    pygrid = PyGrid2D.from_grid(gridIn)
    numpyOut = pygrid.numpy()


    from scipy.misc import imshow
    imshow(numpyOut)
except Exception as ex:
    print(ex)
    print("Test from_grid failed")



PyConrad.getInstance().terminate()
