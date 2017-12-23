import pyconrad
import sys
import os
from os.path import basename
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
            if os.path.isfile(f):
                if str.lower(f).endswith('.vtk'):
                    import vtk
                    from vtk.util import numpy_support as VN
                    reader = vtk.vtkStructuredPointsReader()
                    reader.SetFileName(f)
                    reader.ReadAllVectorsOn()
                    reader.ReadAllScalarsOn()
                    reader.Update()
                    data = reader.GetOutput()  # type: vtkStruturedPoints
                    shape = [*reversed(data.GetDimensions())]

                    array = True
                    counter = 0
                    while array:
                        array = data.GetPointData().getAbstractArray(counter)
                        if array:
                            pyconrad.ClassGetter().Grid1D.from_numpy(
                                array).show()

                else:
                    pyconrad.ij().IJ.openImage(
                        f).show(basename(f))

        except Exception as e:
            print(e)


def start_conrad_compare(*args, **kwargs):
    pyconrad.setup_pyconrad()
    pyconrad.start_gui()

    arrays = []
    for f in sys.argv[1:]:
        try:
            if os.path.isfile(f):
                arr = np.squeeze(_.Grid1D.from_image(f).as_numpy())
                arrays.append(arr)

        except Exception as e:
            print(e)

    if len(arrays) > 1:
        grid = _.Grid1D.from_numpy(np.stack(arrays))
        grid.show()


if __name__ == "__main__":
    start_pyconrad()
