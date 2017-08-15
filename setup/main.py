from jpype import *
import time
from setup import pyCONRAD as pyCONRAD

conrad = pyCONRAD.PyConrad()
conrad.setup()
conrad.startReconstructionFilterPipeline()

#ij = pyIJ.PyIJ()
#ij.initJava()
#ij.startGui()

imagePath = 'C:\\Data\\0016.tif'
#
# print('Load Image')
#
test = conrad.ij.ImagePlus(JString(imagePath))
test.show()

#test2 = ij.ijGuiInstance.ImagePlus(JString(imagePath))
#
# time.sleep(2)
# print('10 sec over, closing imagej....')
#
# ij.stopGui()
#
# print('Gui Stoped | JVM still running, wait 2sec until restart....')
# time.sleep(2)
# #ij.stopJava()
# ij.startGui()
# print('Gui Startet, wait 5sec until image will be loaded....')
# time.sleep(5)
# print('Load Image')
# test = ij.classes.ImagePlus(JString(imagePath))
# test.show()
# print('Image Loaded, python thread closes in 5sec...')
# time.sleep(5)
# print('Oh crap, there is a GUI running, cant exit main process..... ')
# print('Wait on User close imageJ')