from pyconrad import pyCONRAD as pyC
import numpy as np
import jpype as jp
from jpype import nio as nio
import psutil

conrad = pyC.getInstance()
conrad.setup()
conrad.startConrad()

#ar = np.random.randn(5, 5).astype(np.float32)
#x = np.asarray([1,2,3]).astype(np.float32) # java uses 32 bit signed ints
#b=jp.nio.convertToDirectBuffer(ar).asFloatBuffer()
#b = b.order(jp.java.nio.ByteOrder.LITTLE_ENDIAN)
#print(b.get()) # outputs 16777216
#print(b.get()) # 33554432
#print(b.get()) # 50331648
w = 9999
h = 9999
print(psutil.virtual_memory(),"Before anything is allocated")
dBuffer = jp.java.nio.ByteBuffer.allocateDirect(5*5)

grid = conrad.classes.stanford.rsl.conrad.data.numeric.Grid2D(dBuffer.asFloatBuffer)
print(psutil.virtual_memory(),"grid allocated")
#dt = np.dtype(np.float32)
#dt = dt.newbyteorder('>')
#np.frombuffer(jp.java.nio.FloatBuffer.wrap(grid.getBuffer()), dtype=dt)
#print(grid.getBuffer())
print(psutil.virtual_memory(),"grid allocated")
ar = np.ndarray((w,h)).astype(np.float32)#np.random.randn(w,h).astype('float32')
print(psutil.virtual_memory(),"ndarray allocated")
buffer = nio.convertToDirectBuffer(ar)
print(psutil.virtual_memory(),"converted to buffer")
#test = jp.JArray(jp.JByte)(buffer)
#bytebuffer = jp.java.nio.ByteBuffer.wrap(buffer)

buffer.asFloatBuffer().get(grid.getBuffer())
print(psutil.virtual_memory(),"feeded np as buffer to grid")
#print(ar)
#print(grid.getBuffer())

