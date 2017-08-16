from pyconrad import pyCONRAD
from pyconrad.ImageUtils import ImageUtil
import numpy as np
from matplotlib import pyplot as plt

conrad = pyCONRAD.getInstance()
conrad.setup('8G', '1G')

def test_grid1d():
    numpyIn = np.random.rand(543)
    grid1 = ImageUtil.wrapNumpyArrayToGrid1D(numpyIn.astype(float))
    numpyOut = ImageUtil.wrapGrid1D(grid1)
    assert np.allclose(numpyIn, numpyOut)

def test_grid2d():
    numpyIn = np.random.rand(44,543)
    grid1 = ImageUtil.wrapNumpyArrayToGrid2D(numpyIn.astype(float))
    numpyOut = ImageUtil.wrapGrid2D(grid1)
    assert np.allclose(numpyIn, numpyOut)

def test_grid3d():
    numpyIn = np.random.rand(6,57,42)
    grid1 = ImageUtil.wrapNumpyArrayToGrid3D(numpyIn.astype(float))
    numpyOut = ImageUtil.wrapGrid3D(grid1)
    assert np.allclose(numpyIn, numpyOut)

def test_grid4():
    numpyIn = np.random.rand(7, 6,57,42)
    grid1 = ImageUtil.wrapNumpyArrayToGrid4D(numpyIn.astype(float))
    numpyOut = ImageUtil.wrapGrid4D(grid1)
    assert np.allclose(numpyIn, numpyOut)
