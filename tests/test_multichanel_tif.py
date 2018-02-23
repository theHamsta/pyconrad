import pyconrad.autoinit

_ = pyconrad.ClassGetter()
pyconrad.start_gui()

grid = _.NumericGrid.from_tiff('/localhome/local/multichannel_tif.tif')

grid.show()
print(type(grid))
print(grid.size)

print(isinstance(grid, _.edu.stanford.rsl.conrad.data.numeric.Grid4D))
print(grid.getSize())
print(type(grid.getSubGrid(0)))
grid2 = _.NumericGrid.from_numpy(grid.as_numpy())

grid2.show("grid2")
