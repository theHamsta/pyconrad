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

time.sleep(100)
print('10 sec over, closing imagej....')

#ij.stopJava()
#ij.startGui()
print('Java Stoped, wait 10sec until restart....')
#time.sleep(10)

