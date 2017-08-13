from jpype import *
import pyrad

conrad = pyrad.PyConrad()
conrad.setup()
conrad.startReconstructionFilterPipeline()


imagePath = 'C:\\Data\\0016.tif'
#
# print('Load Image')
#
test = conrad.ij.ImagePlus(JString(imagePath))
test.show()
