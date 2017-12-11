# import pyconrad.autoinit
import pyconrad
from pyconrad.opencl import *
import numpy as np

if not pyconrad.is_initialized():
    pyconrad.setup_pyconrad(dev_dirs=['/localhome/local/projects/CONRAD'])

_ = pyconrad.ClassGetter('edu.stanford.rsl.tutorial.cone')


def test_init_cone_beam_backprojector():
    """
    CONRAD crashes on the creation of a OpenCL when using the CONRAD.jar version 1.0.7 on Linux
    (Not only in pyconrad but also when executing the only jar).
    This does not happen if you compile CONRAD from the repository
    """
    _.ConeBeamBackprojector()


def test_get_conrad_cl():
    print(pyconrad.opencl.get_conrad_context())
    print(pyconrad.opencl.get_conrad_command_queue())
    print(pyconrad.opencl.get_conrad_device())


def test_pyopenclgrid():
    ocl_grid = PyOpenClGrid(np.ndarray([10, 10], np.float32))

    print(ocl_grid)

    ctx = ocl_grid.context
    queue = cl.CommandQueue(ctx)


def test_clgrid_classgetter():

    _.OpenCLGrid1D(_.Grid1D(20))
    _.OpenCLGrid2D(_.Grid2D(20, 20))
    _.OpenCLGrid3D(_.Grid3D(20, 20, 40))


def test_clgrid_fromnumpy():

    random = np.random.randn(10, 20)
    cl_grid = opencl_namespaces.OpenCLGrid2D.from_numpy(random)
    print(cl_grid[2, 4])
    assert np.allclose(cl_grid[2, 4],random[4, 2])


def test_clgrid_upload():

    random = np.random.randn(10, 20, 30)
    oclgrid = _.OpenCLGrid1D.form_size(*reversed(random.shape))
    oclgrid.upload(random)

    print(oclgrid[2, 4])
    assert np.allclose(oclgrid[2, 4],random[4, 2])

    downloaded = oclgrid.download()
    assert np.allclose(downloaded, random)


def test_clgrid_upload():

    random = np.random.randn(10, 20)
    cl_grid = opencl_namespaces.OpenCLGrid2D.from_numpy(random)
    print(cl_grid[2, 4])


if __name__ == "__main__":
    pass
    # test_init_cone_beam_backprojector()
    # test_get_conrad_cl()
    # test_pyopenclgrid()
