
pyconrad
========


.. image:: https://badge.fury.io/py/pyconrad.svg
   :target: https://badge.fury.io/py/pyconrad
   :alt: PyPI version


.. image:: https://travis-ci.org/theHamsta/pyconrad.svg?branch=develop
   :target: https://travis-ci.org/theHamsta/pyconrad
   :alt: Build Status


A python wrapper for the CONRAD framework (https://www5.cs.fau.de/conrad/)


* `pyConrad <#pyconrad>`_
* `CONRAD <#conrad>`_
* `Installation <#installation>`_
* `Tests <#tests>`_
* `Changelog <#changelog>`_
* `Usage <#usage>`_

  * `Basic example <#basic-example>`_
  * `More Examples <#more-examples>`_
  * `Autocomplete <#autocomplete>`_
  * `Extension methods for java classes <#extension-methods-for-java-classes>`_
  * `Frequently encountered problems <#frequently-encountered-problems>`_

CONRAD
======

CONRAD is a state-of-the-art software platform with extensive documentation. It is based on platform-independent technologies. Special libraries offer access to hardware acceleration such as CUDA and OpenCL. There is an easy interface for parallel processing. The software package includes different simulation tools that are able to generate 4-D projection and volume data and respective vector motion fields. Well known reconstruction algorithms such as FBP, DBP, and ART are included. All algorithms in the package are referenced to a scientific source. Please visit http://conrad.stanford.edu for more information.

Installation
============

Install via pip :

.. code-block:: bash

   pip install pyconrad

or if you downloaded this repository (https://git5.cs.fau.de/PyConrad/pyCONRAD) using:

.. code-block:: bash

   pip install -e .

This will automatically install CONRAD and all python dependencies. Requirements for proper functioning are at Python of version 3.5 or newer and Java 8.

If you encounter a problem during the installation have a look at our wiki: https://git5.cs.fau.de/PyConrad/pyCONRAD/wikis/home

Tests
=====

If you want to test whether pyconrad is working correctly on your computer you may execute all tests included in this repo via:

.. code-block:: bash

   python setup.py test

Changelog
=========

 Can be found `CHANGELOG.md <https://git5.cs.fau.de/PyConrad/pyCONRAD/blob/master/CHANGELOG.md>`_.

If you encounter any problems during installtion please have a look at our `wiki <https://git5.cs.fau.de/PyConrad/pyCONRAD/wikis/home>`_\ !

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

Basic example
-------------

You can access CONRAD's Java classes via pyconrad.edu() or using the convinience class ClassGetter.

.. code-block:: python

   import pyconrad

   # setup PyConrad
   pyconrad.setup_pyconrad(min_ram='500M', max_ram='8G')
   # Optional parameters for Java Virtual Machine RAM

   pyconrad.start_gui()

   # Create Phantom (edu.stanford.rsl.tutorial.phantoms.MickeyMouseGrid2D)
   phantom = pyconrad.edu().stanford.rsl.tutorial.phantoms.MickeyMouseGrid2D(300, 300)


   # Access more easily using ClassGetter (# type: pyconrad.AutoCompleteConrad adds static auto-complete feature for ClassGetter.edu)
   _ = pyconrad.ClassGetter(
       'edu.stanford.rsl.tutorial.phantoms',
       'edu.stanford.rsl.conrad.phantom'
   )  # type: pyconrad.AutoCompleteConrad

   # You can add more namespaces also later
   _.add_namespaces('edu.stanford.rsl.tutorial.dmip')

   phantom2d = _.MickeyMouseGrid2D(200, 200)
   phantom3d = _.NumericalSheppLogan3D(
       200, 200, 200).getNumericalSheppLoganPhantom()

   # Use Java method of class MickeyMouseGrid2D
   phantom.show()
   phantom3d.show()

Also memory transfers to numpy.ndarray are possible. Numeric grids have the additional methods `from_numpy` and `as_numpy`:

.. code-block:: python

    _ = pyconrad.ClassGetter()

    # Create PyGrid from numpy array (more efficient if using Java float type pyconrad.java_float_dtype)
    array = np.random.rand(4, 2, 3).astype(pyconrad.java_float_dtype)
    grid = _.NumericGrid.from_numpy(array)

    # Manipulate data in using CONRAD at Position (x,y,z) = (0,1,3)
    grid.setValue(5.0, [0, 1, 3])

    # Get modified array
    new_array = grid.as_numpy()

    # Attention: Python has a different indexing (z,y,x)
    print('Old value: %f' % array[3, 1, 0])
    print('New value: %f' % new_array[3, 1, 0])

More Examples
-------------

More examples can be found `here <https://git5.cs.fau.de/PyConrad/pyCONRAD/tree/master/pyconrad_examples>`_

Autocomplete
------------

As it might be difficult to remember the exact names of Java functions and classes, pyconrad provides basic autocomplete feature for CONRAD classes.
Just give your IDE a type hint that a object represents a certain Java namespace or class (\ ``# type: pyconrad.AutoCompleteConrad.edu.standford...``\ ).

Works with pycharm:


.. image:: README.md_files/autocomplete.webm
   :target: README.md_files/autocomplete.webm
   :alt: autocomplete_video


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
   _.PointND([3,3])  # neither does this
   _.PointND(JArray(JDouble)([3,2]))  # works
   _.PointND.from_numpy(np.array([2.1,3.1])) #works, uses extension method
   _.PointND.from_list([2.1,3.1]) #works, uses extension method

   # Getting PointND as numpy array
   numpy_point = java_point.as_numpy()

   # the same applies for SimpleVector
   _.SimpleVector(JArray(JDouble)([3,2]))  # works
   _.SimpleVector.from_numpy(np.array([2.1,3.1])) #works, uses extension method
   _.SimpleVector.from_list([2.1,3.1]) #works, uses extension method

   #Getting SimpleVector as numpy array
   numpy_vector = java_vector.as_numpy()

   #the same applies for SimpleMatrix
   SimpleMatrix(JArray(JDouble,2)([[1.1,2.2,3.3],[4.4,5.5,6.6]]))  # works
   SimpleMatrix.from_numpy(np.matrix([[1.1,2.2,3.3],[4.4,5.5,6.6]])) #works, uses extension method
   SimpleMatrix.from_list([[1.1,2.2,3.3],[4.4,5.5,6.6]]) #works, uses extension method

   #Getting SimpleMatrix as numpy matrix
   numpy_matrix = java_matrix.as_numpy()

   # Grid.setOrigin(...), setSpacing
   _.Grid2D(3,2).setOrigin(JArray(JDouble)([2,3]))
   PyGrid.from_grid(_.Grid2D(3,2)).set_origin([2,3])
   PyGrid.from_grid(_.Grid2D(3,2)).set_spacing([2,3])

   # Creating nested enums
   traj = _.HelicalTrajectory()
   print(traj.getDetectorOffsetU())  # returns a float
   enumval = _.['Projection$CameraAxisDirection'].values()[int(traj.getDetectorOffsetU())] # Convert back to enum
   enumval = jvm.enumval_from_int('Projection$CameraAxisDirection', traj.getDetectorOffsetU())  # or like that