import vtk
from os.path import splitext


# def read_vti(file, array_name=0):
#     from vtk import vtkXMLImageDataReader
#     from vtk.util import numpy_support as VN

#     reader = vtk.vtkXMLImageDataReader()
#     reader.SetFileName(file)
#     # reader.ReadAllVectorsOn()
#     # reader.ReadAllScalarsOn()
#     reader.Update()
#     data = reader.GetOutput()  # type: vtkStruturedPoints
#     shape = [*reversed(data.GetDimensions())]

#     # if array_dim > 1:
#     #     shape.append(array_dim)

#     rtn = VN.vtk_to_numpy(data.GetPointData().GetArray(array_name)).reshape(
#         shape), data.GetOrigin(), data.GetSpacing()
#     return rtn


def read_vtk(file, array_name=0):
    """
    Reads a VTK voxel file (*.vtk or *.vti) and return result as numpy array

    Arguments:
        file {[type]} -- [description]

    Keyword Arguments:
        array_name array index or identifier
         (in the case that the VTK-file contains more than one array)

    Raises:
        TypeError -- In case that 'file' does not have a valid extension

    Returns:
        tuple[np.array, tuple[float], tuple[float]] -- array, origin, spacing
    """

    from vtk import vtkStructuredPointsReader, vtkXMLImageDataReader
    from vtk.util import numpy_support as VN

    _, ext = splitext(file)

    if ext.lower() == '.vtk':
        reader = vtkStructuredPointsReader()
        reader.ReadAllVectorsOn()
        reader.ReadAllScalarsOn()
    elif ext.lower() == '.vti':
        reader = vtkXMLImageDataReader()
    else:
        raise TypeError(
            'Not a valid VTK voxel data extension (use *.vtk, or *.vti)')

    reader.SetFileName(file)
    reader.Update()
    data = reader.GetOutput()  # type: vtkStruturedPoints
    shape = [*reversed(data.GetDimensions())]

    rtn = VN.vtk_to_numpy(data.GetPointData().GetArray(array_name)).reshape(
        shape), data.GetOrigin(), data.GetSpacing()
    return rtn
