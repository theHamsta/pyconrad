#from jpype import *
from pyconrad import pyCONRAD

conrad = pyCONRAD.getInstance()
conrad.setup('8G','1G')
#conrad.startReconstructionFilterPipeline()
conrad.startConrad()

grid = conrad.classes.stanford.rsl.conrad.data.numeric.Grid2D(30,30)
grid.show("Grid2D Python")

testClass = conrad.classes.stanford.rsl.science.syben.pytonTest.PythonTest
testClassInstance = testClass()

testClass.gridParameterStatic(grid)
returnedGridStatic = testClass.gridParameterStaticWithReturn(grid)
returnedGridStatic.show("gridParameterStaticWithReturn Python")
print("Grid value is increased by 200 in static java method")

testClassInstance.gridParameter(grid)
returnedGrid = testClassInstance.gridParameterWithReturn(grid)
returnedGrid.show("gridParameterWithReturn Python")
print("Grid value is increased by 200 in java method")
