pyconrad
========


.. image:: https://badge.fury.io/py/pyconrad.svg
   :target: https://badge.fury.io/py/pyconrad
   :alt: PyPI version


.. image:: https://travis-ci.org/theHamsta/pyconrad.svg?branch=master
   :target: https://travis-ci.org/theHamsta/pyconrad
   :alt: Build Status

.. image:: https://codecov.io/gh/theHamsta/pyconrad/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/theHamsta/pyconrad

A python wrapper for the CONRAD framework (https://www5.cs.fau.de/conrad/)

CONRAD
======

CONRAD is a state-of-the-art software platform with extensive documentation. It is based on platform-independent technologies. Special libraries offer access to hardware acceleration such as CUDA and OpenCL. There is an easy interface for parallel processing. The software package includes different simulation tools that are able to generate 4-D projection and volume data and respective vector motion fields. Well known reconstruction algorithms such as FBP, DBP, and ART are included. All algorithms in the package are referenced to a scientific source. Please visit http://conrad.stanford.edu for more information.

Installation
============

Install via pip (``vtk``, ``opencl`` is optional):

.. code-block:: bash

   pip install pyconrad[vtk,opencl]

or if you downloaded this repository (https://git5.cs.fau.de/PyConrad/pyCONRAD) using:

.. code-block:: bash

   pip install -e .

This will automatically install CONRAD and all python dependencies. Requirements for proper functioning are at Python of version 3.6 or newer and Java 8.

If you encounter a problem during the installation have a look at our wiki: https://git5.cs.fau.de/PyConrad/pyCONRAD/wikis/home


.. warning::

    If installation of JPype fails under Python 3.9 try my branch:

    .. code-block:: bash
          
          pip3 install git+https://github.com/theHamsta/jpype@pyconrad --verbose

Tests
=====

If you want to test whether pyconrad is working correctly on your computer you may execute all tests included in this repo via:

.. code-block:: bash

   python setup.py test

Changelog
=========

Can be found `CHANGELOG.md <https://git5.cs.fau.de/PyConrad/pyCONRAD/blob/master/CHANGELOG.md>`_.

Usage
=====

You can start CONRAD in Python like this:

.. code-block:: python

   import pyconrad

   pyconrad.setup_pyconrad()
   pyconrad.start_gui()  # start ImageJ
   pyconrad.start_reconstruction_pipeline_gui() # if you want to start CONRAD's reconstruction filter pipeline

Or you can run CONRAD Reconstruction Pipeline from command line:

.. code-block:: bash

   conrad
   # or: conrad_imagej

ImageJ Commands
---------------

You can access all classes of ImageJ and Conrad after you initialized the JVM.

.. code-block:: python

    import pyconrad.autoinit
    import ij
    from edu.stanford.rsl.conrad.data.numeric import NumericGrid
    import numpy as np

    pyconrad.start_gui()

    a = np.random.rand(20, 30)
    grid = NumericGrid.from_numpy(a)
    grid.show()

    ij.IJ.run('FFT')

imshow
------

You can also use `pyconrad` to view NumPy arrays in ImageJ.

.. code-block:: python

    import pyconrad.autoinit
    import numpy as np
    import time

    a = np.random.rand(20, 30)
    luts = ['Fire', 'Spectrum', 'Ice', 'Cyan']

    for lut in luts:
        pyconrad.imshow(a, lut, lut=lut)

    print('Enjoy white noise!')
    for i in range(300):
        noise = np.random.rand(200, 200)
        pyconrad.imshow(noise, 'White noise', spacing=(3, 2), origin=(0, 2))
        time.sleep(0.01)

    pyconrad.close_all_windows()

Basic example
-------------

You can access CONRAD's Java classes via pyconrad.edu() or using the convinience class ClassGetter.

.. code-block:: python

    import pyconrad.autoinit
    import edu.stanford.rsl.tutorial.phantoms
    from edu.stanford.rsl.conrad.phantom import NumericalSheppLogan3D

    phantom2d = edu.stanford.rsl.tutorial.phantoms.MickeyMouseGrid2D(100, 100)
    phantom3d = NumericalSheppLogan3D(
        100, 100, 100).getNumericalSheppLoganPhantom()

    # You can also group Java packages an access all classes that are contained (import * does not work)
    # Access more easily using ClassGetter (
    _ = pyconrad.ClassGetter(
        'edu.stanford.rsl.tutorial.phantoms',
        'edu.stanford.rsl.conrad.phantom'
    )

    print('This is a Java class: ' + str(_.NumericalSheppLogan3D))

    # Shape is for dimensions (z,y,x), size for (x,y,z) 
    print(grid.shape)
    print(grid.size)

    # Use Java method of class MickeyMouseGrid2D
    phantom2d.show()
    phantom3d.show()

Also memory transfers to numpy.ndarray are possible. Numeric grids have the additional methods `from_numpy` and `as_numpy`:

.. code-block:: python

    _ = pyconrad.ClassGetter()

    array = np.random.rand(4, 2, 3).astype(pyconrad.java_float_dtype)
    grid = _.NumericGrid.from_numpy(array)

    

    # Manipulate data in using CONRAD at Position (x,y,z) = (0,1,3)
    grid.setValue(5.0, [0, 1, 3])
    # or easier with Python indices (reversed)
    grid[3,1,0] = 5

    # Shape 
    print(grid.shape)
    print(grid.size)

    # Get modified array
    new_array = grid.as_numpy()

    # Attention: Python has a different indexing (z,y,x)
    print('Old value: %f' % array[3, 1, 0])
    print('New value: %f' % new_array[3, 1, 0])

More Examples
-------------

More examples can be found `here <https://git5.cs.fau.de/PyConrad/pyCONRAD/tree/master/pyconrad_examples>`_

Extension methods for java classes
----------------------------------

For easy transition between Java and Python we extended some important Java classes in Python to convert between the respective Java class and the respective numpy structure.
The following java classes are extended:


* PointND
* SimpleVector
* SimpleMatrix
* Numeric Grid(therefore all Grid1D - Grid4D)

with the methods:


* as_numpy (array or matrix depending on the class representation)
* from_numpy
* from_list
* from_tif
* save_tif
* save_vtk

Frequently encountered problems
-------------------------------

.. code-block:: python

   # Creating a PointND
   _.PointND(3,3)  # does not work
   _.PointND([3,3])  # this does work
   _.PointND(JArray(JDouble)([3,2]))  # works
   _.PointND.from_numpy(np.array([2.1,3.1])) #works, uses extension method
   _.PointND.from_list([2.1,3.1]) #works, uses extension method

   # Getting PointND as numpy array
   numpy_point = java_point.as_numpy()

   # the same applies for SimpleVector
   _.SimpleVector([3,2])  # does not work. pyconrad does not know whether you want to call SimpleVector(final double... otherBuffer) or public SimpleVector(final float... otherBuffer)
   _.SimpleVector(JArray(JDouble)([3,2]))  # works
   _.SimpleVector.from_numpy(np.array([2.1,3.1])) #works, uses extension method
   _.SimpleVector.from_list([2.1,3.1]) #works, uses extension method

   #Getting SimpleVector as numpy array
   numpy_vector = java_vector.as_numpy()

   #the same applies for SimpleMatrix
   _.SimpleMatrix(JArray(JDouble,2)([[1.1,2.2,3.3],[4.4,5.5,6.6]]))  # works
   _.SimpleMatrix.from_numpy(np.matrix([[1.1,2.2,3.3],[4.4,5.5,6.6]])) #works, uses extension method
   _.SimpleMatrix.from_list([[1.1,2.2,3.3],[4.4,5.5,6.6]]) #works, uses extension method

   #Getting SimpleMatrix as numpy matrix
   numpy_matrix = java_matrix.as_numpy()

   # Grid.setOrigin(...), setSpacing
   _.Grid2D(3,2).setOrigin(JArray(JDouble)([2,3]))

   # Creating nested enums
   traj = _.HelicalTrajectory()
   print(traj.getDetectorOffsetU())  # returns a float
   enumval = _.['Projection$CameraAxisDirection'].values()[int(traj.getDetectorOffsetU())] # Convert back to enum
   enumval = jvm.enumval_from_int('Projection$CameraAxisDirection', traj.getDetectorOffsetU())  # or like that
