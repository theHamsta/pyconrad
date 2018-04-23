import pyconrad
import sys
import os
from os.path import basename, isfile, abspath
import numpy as np

_ = pyconrad.ClassGetter()


def start_pyconrad(*args, **kwargs):
    pyconrad.setup_pyconrad()
    pyconrad.start_reconstruction_pipeline_gui()


def start_conrad_imagej(*args, **kwargs):
    pyconrad.setup_pyconrad()
    pyconrad.start_gui()

    for f in sys.argv[1:]:
        try:
            if isfile(f):
                f = abspath(f)
                if str.lower(f).endswith('.vtk') or str.lower(f).endswith('.vti'):
                    _.NumericGrid.from_vtk(f).show()
                elif str.lower(f).endswith('.np') or str.lower(f).endswith('.npz'):
                    file_object = np.load(f)
                    for key in file_object.keys():
                        numpy_array = file_object[key]
                        _.NumericGrid.from_numpy(numpy_array).show(key)

                else:
                    pyconrad.ij().IJ.openImage(
                        f).show(basename(f))

        except Exception as e:
            print(e)


if __name__ == "__main__":
    start_pyconrad()
