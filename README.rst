========
pyConrad
========


A python wrapper for the CONRAD framework (https://www5.cs.fau.de/conrad/)

========
CONRAD
========

CONRAD is a state-of-the-art software platform with extensive documentation. It is based on platform-independent technologies. Special libraries offer access to hardware acceleration such as CUDA and OpenCL. There is an easy interface for parallel processing. The software package includes different simulation tools that are able to generate 4-D projection and volume data and respective vector motion fields. Well known reconstruction algorithms such as FBP, DBP, and ART are included. All algorithms in the package are referenced to a scientific source. Please visit http://conrad.stanford.edu for more information.

========
Installation
========

Install via pip:

    pip install pyconrad

This will automatically install CONRAD and all python dependencies. You can use the following python code to get the installation directory of CONRAD:

.. code:: python
    import pyconrad_java
    print( pyconrad_java.conrad_jar_dir )

========
Usage
========

The Python
