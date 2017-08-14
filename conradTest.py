from jpype import *
import pyrad

conrad = pyrad.getInstance()
conrad.setup()
conrad.startReconstructionFilterPipeline()
#conrad.startConrad()

imagePath = 'D:\\Data\\mrt_raw\\0016.tif'
#
# print('Load Image')
#
test = conrad.ij.ImagePlus(JString(imagePath))
test.show()

#Test for Singleton
conradSecondInstance = pyrad.getInstance()
conradThirdInstance = pyrad.PyConrad()

if conrad is conradSecondInstance is conradThirdInstance:
    print('Singleton test: passed')
else:
    print('Singleton test: failed')
