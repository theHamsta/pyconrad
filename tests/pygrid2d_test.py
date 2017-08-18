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
    assert np.allclose(numpyIn,numpyOut)

    pygrid2.grid().setAtIndex(3,3, 0.4)
    pygrid2.update_numpy()
    numpyOut = ImageUtil.wrapGrid2D(pygrid2.grid())
    assert np.allclose(pygrid2.numpy(),numpyOut)
    print("Test from_numpy passed")
except Exception as ex:
    print(ex)
    print("Test from_numpy failed")

try:
    gridIn = phantom_package.MickeyMouseGrid2D(shape[1], shape[0])
    # gridIn = PyConrad.numeric_package().Grid2D(shape[1], shape[0])

    pygrid = PyGrid2D.from_grid(gridIn)
    pygrid[3:8,10:20] = 1.
    pygrid.update_grid()
    pygrid.show_grid()
    numpyOut = pygrid.numpy()


    from scipy.misc import imshow
    imshow(numpyOut)

    print(pygrid[1:4,5:8])
except Exception as ex:
    print(ex)
    print("Test from_grid failed")




PyConrad.getInstance().terminate()
