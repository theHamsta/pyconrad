from pyconrad import PyGrid, PyConrad,GridIndexer
import numpy as np

PyConrad.get_instance().setup(min_ram='400M')

phantom_package = PyConrad.get_instance().classes.stanford.rsl.tutorial.phantoms
shape = [230, 330]

gridIn = phantom_package.MickeyMouseGrid2D(shape[1], shape[0])
grid_indexer = GridIndexer(gridIn)
print(grid_indexer)


from scipy.misc import *


imshow(grid_indexer[2:4])


