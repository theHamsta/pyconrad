# pyConrad

A python wrapper for the CONRAD framework (https://www5.cs.fau.de/conrad/)

# CONRAD

CONRAD is a state-of-the-art software platform with extensive documentation. It is based on platform-independent technologies. Special libraries offer access to hardware acceleration such as CUDA and OpenCL. There is an easy interface for parallel processing. The software package includes different simulation tools that are able to generate 4-D projection and volume data and respective vector motion fields. Well known reconstruction algorithms such as FBP, DBP, and ART are included. All algorithms in the package are referenced to a scientific source. Please visit http://conrad.stanford.edu for more information.

# Installation

Install via pip:

```bash
pip install pyconrad
```

This will automatically install CONRAD and all python dependencies.
Start the CONRAD reconstruction pipeline using (from bash or Windows cmd):
```bash
pyconrad
```
You can use the following python code to get the installation directory of CONRAD:
```python
import pyconrad

print("CONRAD installation directory is:")
print(pyconrad.conrad_jar_dir())
```

If you encounter any problems during installtion please have a look at our [wiki](https://git5.cs.fau.de/PyConrad/pyCONRAD/wikis/home)!

# Usage

You can start CONRAD like this:
```python
from pyconrad import PyConrad

pyconrad = PyConrad()  # PyConrad is a singleton class
pyconrad.setup()  # Setup PyConrad
pyconrad.start_conrad()  # Or pyconrad.start_reconstruction_filter_pipeline() to start CONRAD
```

The central class of the pyconrad package is PyConrad. You can use it to access all Java classes of CONRAD and start the graphical user interface:
``` python
from pyconrad import PyConrad

pyconrad = PyConrad()
pyconrad.setup()
# Optional parameters for Java Virtual Machine RAM and own Java projects
# pyconrad.setup(max_ram='8G', min_ram='500M', dev_dirs=['path/to/project/with/own/java/classes'])
pyconrad.start_conrad()

# Create Phantom (edu.stanford.rsl.tutorial.phantoms.MickeyMouseGrid2D)
phantom = pyconrad.classes.stanford.rsl.tutorial.phantoms.MickeyMouseGrid2D(300, 300)
# Access more easily using imports
pyconrad.add_import('edu.stanford.rsl.tutorial.phantoms')
phantom2 = pyconrad['MickeyMouseGrid2D'](200, 200)

# Use Java method of class MickeyMouseGrid2D
phantom.show()
```
To transfer data from NumPy to CONRAD use the class PyGrid:
```python
from pyconrad import PyConrad, PyGrid, java_float_dtype
import numpy as np

pyconrad = PyConrad()
pyconrad.setup()

phantom = pyconrad.get_phantom_package().MickeyMouseGrid2D(200, 200)

pygrid1 = PyGrid.from_grid(phantom)  # Create PyGrid from Grid2D
pygrid1.grid().show()  # Use Java method

from scipy.misc import imshow
imshow(pygrid1()) # or imshow(pygrid1) to use a Python method
```
Data changes have to be synchronized:
``` python
...

# Create PyGrid from numpy array (must be of type pyconrad.java_float_dtype)
array = np.random.rand(4,2,3).astype(java_float_dtype)
pygrid2 = PyGrid.from_numpy(array)

# Manipulate data in using CONRAD at Position (x,y,z) = (1,2,4)
pygrid2.grid().setValue(5.0, [0,1,3])

# Print this pixel using Python indexes [z,y,x]
print("Before update: %f" % pygrid2[3,1,0])
# Python data must be synchronized with CONRAD
pygrid2.update_numpy()
print("After update: %f" % pygrid2[3,1,0])

# Manipulate pixel using python
pygrid2[1,1,1] = 3.0
# Update CONRAD data
pygrid2.update_grid()

# Print
print(pygrid2)
```

More examples can be found [here](examples)

## Extension methods for java classes
For easy transition between java and python we extent the java classes in python to convert easiliy between the respective java class and the respective numpy structure.
The following java classes are extended:
- PointND
- SimpleVector
- SimpleMatrix
- Numeric Grid(therefore all Grid1D - Grid4D)

with the methods:
- as_numpy (array or matrix depending on the class representation)
- from_numpy
- from_list

## Frequently encountered problems
```python
# Creating a PointND
jvm['PointND'](3,3)  # does not work
jvm['PointND']([3,3])  # neither does this
jvm['PointND'](JArray(JDouble)([3,2]))  # works
jvm['PointND'].from_numpy(np.array([2.1,3.1])) #works, uses extension method
jvm['PointND'].from_list([2.1,3.1]) #works, uses extension method

# Getting PointND as numpy array
numpy_point = java_point.as_numpy()

# the same applies for SimpleVector
jvm['SimpleVector'](JArray(JDouble)([3,2]))  # works
jvm['SimpleVector'].from_numpy(np.array([2.1,3.1])) #works, uses extension method
jvm['SimpleVector'].from_list([2.1,3.1]) #works, uses extension method

#Getting SimpleVector as numpy array
numpy_vector = java_vector.as_numpy()

#the same applies for SimpleMatrix
jvm['SimpleMatrix'](JArray(JDouble,2)([[1.1,2.2,3.3],[4.4,5.5,6.6]]))  # works
jvm['SimpleMatrix'].from_numpy(np.matrix([[1.1,2.2,3.3],[4.4,5.5,6.6]])) #works, uses extension method
jvm['SimpleMatrix'].from_list([[1.1,2.2,3.3],[4.4,5.5,6.6]]) #works, uses extension method

#Getting SimpleMatrix as numpy matrix
numpy_matrix = java_matrix.as_numpy()

# Grid.setOrigin(...), setSpacing
jvm['Grid2D'](3,2).setOrigin(JArray(JDouble)([2,3]))
PyGrid.from_grid(jvm['Grid2D'](3,2)).set_origin([2,3])
PyGrid.from_grid(jvm['Grid2D'](3,2)).set_spacing([2,3])

# Creating nested enums
traj = jvm['HelicalTrajectory']()
print(traj.getDetectorOffsetU())  # returns a float
enumval = jvm['Projection$CameraAxisDirection'].values()[int(traj.getDetectorOffsetU())] # Convert back to enum
enumval = jvm.enumval_from_int('Projection$CameraAxisDirection', traj.getDetectorOffsetU())  # or like that
```
