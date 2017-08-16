import sys
sys.path.append('/localhome/local/projects/pyCONRAD/setup')

from jpype import *
from pyCONRAD import *

jvm = PyConrad()
jvm.setup()
#https://github.com/originell/jpype/blob/master/jpype/nio.py
#https://stackoverflow.com/questions/7060215/how-can-i-get-the-memory-location-of-a-object-in-java
#http://www.docjar.com/docs/api/sun/misc/Unsafe.html


jvm.terminate()



