from pyconrad import pyCONRAD as pyC
import numpy as np
import jpype as jp
from jpype import nio as nio
import psutil
import time

conrad = pyC.getInstance()
conrad.setup()
conrad.startConrad()

w = 9999
h = 9999
dt = np.dtype(">f4")
#np_arr = np.ndarray((w,h),dtype=dt).astype(np.float32)#np.random.randn(w,h).astype('float32')

#Variante 1 :
#We create a ndarray from numpy and the Grid
#We create from the ndarray a directBuffer as the java representation of the ndarray (does not cost additional memory, ndarray and directBuffer are shared/same memory)
#We can update the grid float[] with:
#dBuffer.asFloatBuffer().get(grid.getBuffer())
#We can update the ndarray with:
#dBuffer.asFloatBuffer().put(grid.getBuffer())
print(psutil.virtual_memory(),"Before anything is allocated")
ndarray = np.random.randn(w,h).astype(dt)
print(psutil.virtual_memory(),"ndarray is allocated")
grid = conrad.classes.stanford.rsl.conrad.data.numeric.Grid2D(w,h)
print(psutil.virtual_memory(),"grid is allocated")
dBuffer = nio.convertToDirectBuffer(ndarray)
print(psutil.virtual_memory(),"directBuffer created")

dBuffer.asFloatBuffer().get(grid.getBuffer())



print('ndarray[0][0]: ' , ndarray[0][0] , " Grid.getAtIndex(0,0): " , grid.getAtIndex(0,0))
print('ndarray[0][0] = 10.0 | followed by dBuffer.asFloatBuffer().get(grid.getBuffer())')
ndarray[0][0] = 10.0
before_grid_update = time.process_time()
dBuffer.asFloatBuffer().get(grid.getBuffer())#now grid has 10 at (0,0)
after_grid_update = time.process_time()
print('ndarray[0][0]: ' , ndarray[0][0] , " Grid.getAtIndex(0,0): " , grid.getAtIndex(0,0))
print('grid.setAtIndex(0,0,20.0) | followed by dBuffer.asFloatBuffer().put(grid.getBuffer())')
grid.setAtIndex(0,0,20.0)
before_ndarray_update = time.process_time()
dBuffer.asFloatBuffer().put(grid.getBuffer())#now ndarray has 20 at (0,0)
after_ndarray_update =time.process_time()
print('ndarray[0][0]: ' , ndarray[0][0] , " Grid.getAtIndex(0,0): " , grid.getAtIndex(0,0))
print(psutil.virtual_memory(),"After Tests")
grid_update_time = after_grid_update - before_grid_update
ndarray_update_time = after_ndarray_update - before_ndarray_update
print("Time for update grid in s: ", grid_update_time )
print("Time for update ndarray in s: ", ndarray_update_time)
#ar = np.random.randn(5, 5).astype(np.float32)
#x = np.asarray([1,2,3]).astype(np.float32) # java uses 32 bit signed ints
#b=jp.nio.convertToDirectBuffer(ar).asFloatBuffer()
#b = b.order(jp.java.nio.ByteOrder.LITTLE_ENDIAN)
#print(b.get()) # outputs 16777216
#print(b.get()) # 33554432
#print(b.get()) # 50331648

#print(psutil.virtual_memory(),"Before anything is allocated")
#dBuffer = jp.java.nio.ByteBuffer.allocateDirect(5*5)

#grid = conrad.classes.stanford.rsl.conrad.data.numeric.Grid2D(dBuffer.asFloatBuffer)
#print(psutil.virtual_memory(),"grid allocated")
#dt = np.dtype(np.float32)
#dt = dt.newbyteorder('>')
#np.frombuffer(jp.java.nio.FloatBuffer.wrap(grid.getBuffer()), dtype=dt)
#print(grid.getBuffer())
#print(psutil.virtual_memory(),"grid allocated")
#ar = np.ndarray((w,h)).astype(np.float32)#np.random.randn(w,h).astype('float32')
#print(psutil.virtual_memory(),"ndarray allocated")
#buffer = nio.convertToDirectBuffer(ar)
#print(psutil.virtual_memory(),"converted to buffer")
#test = jp.JArray(jp.JByte)(buffer)
#bytebuffer = jp.java.nio.ByteBuffer.wrap(buffer)

#buffer.asFloatBuffer().get(grid.getBuffer())
#print(psutil.virtual_memory(),"feeded np as buffer to grid")
#print(ar)
#print(grid.getBuffer())
