
from jpype import *
from pyconrad import pyIJ
import time

ij = pyIJ.PyIJ()
ij.initJava()
ij.startGui()

imagePath = 'D:/Data/mrt_raw/0016.tif'

print('Load Image')

test = ij.classes.ImagePlus(JString(imagePath))
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
test = ij.classes.ImagePlus(JString(imagePath))
test.show()
print('Image Loaded, python thread closes in 5sec...')
time.sleep(5)
print('Oh crap, there is a GUI running, cant exit main process..... ')
print('Wait on User close imageJ')