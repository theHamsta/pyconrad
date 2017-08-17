# import sys
# sys.path.append('/localhome/local/projects/pyCONRAD/setup')

from jpype import *
from pyconrad.pyCONRAD import *
import numpy as np
from pyconrad.ImageUtils import ImageUtil
import struct

## Grid2D.java should have the following method
#
# import java.nio.*;
##
# public static Grid2D createGrid2D(ByteBuffer b, int width, int height ) {
#     float[] fArray = new float[width * height];
#     b.asFloatBuffer().get(fArray);
#     return new Grid2D(fArray, width, height);
##     b.asFloatBuffer().array() does not work since b is not mapped onto a float array
# }


def floatToBits(f):
    s = struct.pack('>f', f)
    return struct.unpack('>l', s)[0]


jvm = PyConrad()
jvm.setup()

numpyIn = np.ones([2, 23], np.float32)
# grid1 =ImageUtil.wrapNumpyArrayToGrid2D(numpyIn)


jByteBuffer = nio.convertToDirectBuffer(numpyIn.data)
grid = jvm.classes.stanford.rsl.conrad.data.numeric.Grid2D.createGrid2D(jByteBuffer, numpyIn.shape[1], numpyIn.shape[0])

numpyOut = ImageUtil.wrapGrid2D(grid)
print('in')
print(numpyIn)
print('out')
print(numpyOut)
# Java uses Big Endian, my machine is Little Endian
print('Python: %x' % floatToBits(numpyIn[0,0]))
print('Java: %x' % floatToBits(numpyOut[0,0]))
# assert np.allclose(numpyIn, numpyOut)

jvm.terminate()
