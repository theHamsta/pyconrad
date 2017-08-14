from jpype import *
import pyrad

conrad = pyrad.PyConrad()
conrad.setup()
conrad.startReconstructionFilterPipeline()
#conrad.startConrad()

imagePath = 'D:\\Data\\mrt_raw\\0016.tif'
#
# print('Load Image')
#
test = conrad.ij.ImagePlus(JString(imagePath))
test.show()
