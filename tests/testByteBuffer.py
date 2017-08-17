#import sys
#sys.path.append('/localhome/local/projects/pyCONRAD/setup')

from jpype import *
from pyconrad.pyCONRAD import *
import numpy as np
from pyconrad.ImageUtils import ImageUtil

jvm = PyConrad()
jvm.setup()

numpyIn = np.random.rand(423,23)
numpyIn = numpyIn.astype(np.float32)

# grid1 =ImageUtil.wrapNumpyArrayToGrid2D(numpyIn)


jByteBuffer = nio.convertToDirectBuffer(numpyIn.data)
# grid = jvm.classes.stanford.rsl.conrad.data.numeric.Grid2D(numpyIn.shape[1],numpyIn.shape[0])
grid = jvm.classes.stanford.rsl.conrad.data.numeric.Grid2D(jByteBuffer, JArray(JInt,1)(numpyIn.shape))

numpyOut = ImageUtil.wrapGrid2D(grid)
assert np.allclose(numpyIn, numpyOut)


jvm.terminate()



