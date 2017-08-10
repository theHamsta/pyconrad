from jpype import *
import pyIJ
import time

ij = pyIJ.PyIJ()
ij.initJava()
ij.startGui()
ij.initJava()

print('Load Image')

test = ij.classes.ImagePlus(JString('D:\\Data\\Electra_MRscans_reco_raw\\DICOMS\\0018\\0018.tif'))
test.show()

time.sleep(2)
print('10 sec over, closing imagej....')

ij.stopGui()

print('Gui Stoped | JVM still running, wait 2sec until restart....')
time.sleep(2)
#ij.stopJava()
ij.startGui()
print('Gui Startet, wait 5sec until image will be loaded....')
time.sleep(5)
print('Load Image')
test = ij.classes.ImagePlus(JString('D:\\Data\\Electra_MRscans_reco_raw\\DICOMS\\0018\\0018.tif'))
test.show()
print('Image Loaded, python thread closes in 5sec...')
time.sleep(5)