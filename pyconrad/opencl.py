import pyopencl as cl
import pyopencl.array
import pyconrad
import numpy as np
import jpype


# from pyopencl docu:
# Interoperability with other OpenCL software

# Just about every object in pyopencl supports the following interface (here shown as an example for pyopencl.MemoryObject, from which pyopencl.Buffer and pyopencl.Image inherit):

#     pyopencl.MemoryObject.from_int_ptr()
#     pyopencl.MemoryObject.int_ptr

# This allows retrieving the C-level pointer to an OpenCL object as a Python integer, which may then be passed to other C libraries whose interfaces expose OpenCL objects. It also allows turning C-level OpenCL objects obtained from other software to be turned into the corresponding pyopencl objects.

opencl_namespaces = pyconrad.ClassGetter(
    'edu.stanford.rsl.conrad.data.numeric.opencl',
    'edu.stanford.rsl.conrad.opencl'
)


def get_conrad_context():
    OpenCLUtil = pyconrad.edu().stanford.rsl.conrad.opencl.OpenCLUtil
    context_java = OpenCLUtil.getStaticContext()
    return cl.Context.from_int_ptr(context_java.ID)


def get_conrad_command_queue() -> cl.CommandQueue:
    OpenCLUtil = pyconrad.edu().stanford.rsl.conrad.opencl.OpenCLUtil
    command_queue_java = OpenCLUtil.getStaticCommandQueue()
    return cl.CommandQueue.from_int_ptr(command_queue_java.ID)


# TODO: does not work yet
def get_conrad_device():
    OpenCLUtil = pyconrad.edu().stanford.rsl.conrad.opencl.OpenCLUtil
    device_java = OpenCLUtil.getStaticCommandQueue().getDevice()
    cl.Device.from_int_ptr(device_java.ID)


# class PyOpenClGrid:

#     def __init__(self, host_array, copy_host_mem=True):
#         # if host_array.dtype != np.float32:
#         #     raise ValueError('Array must be of dtype float32')

#         self._context = get_conrad_context()
#         self._command_queue = get_conrad_command_queue()

#         host_array = host_array.astype(np.float32)

#         # if copy_host_ptr:
#         #     self._cl_buffer = cl.Buffer(
#         #         ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=host_array)
#         # else:
#         #     self._cl_buffer = cl.Buffer(
#         #         ctx, mf.READ_WRITE, hostbuf=host_array)

#         # self._host_array = host_array

#         if copy_host_mem:
#             self._device_array = cl.array.to_device(
#                 self._command_queue, host_array)
#         else:
#             self._device_array = cl.array.Array(
#                 self._command_queue, host_array.shape, host_array.dtype)

#     @property
#     def context(self):
#         return self._context

#     @property
#     def command_queue(self):
#         return self._command_queue

#     @property
#     def device_array(self):
#         return self._device_array

#     def __array__(self):
#         # cl.enqueue_copy(self._command_queue,
#         #                 dest=self._host_array, src=self._cl_buffer)
#         self._device_array.get(self._host_array)
#         return self._host_array

#     def __repr__(self):
#         return self._device_array.__repr__()

#     def __str__(self):
#         return self._device_array.__str__()

#     @property
#     def shape(self):
#         return self._device_array.shape

#     def asopenclgrid(self):

#         rtn = getattr(opencl_namespaces,
#                       "OpenCLGrid{}D".format(len(self.shape)))(*reversed(self.shape))

    # def get(self):
    #     return self.__array__()

    # def clone(self):
    #     pass

    # def notifyBeforeRead(self):
    #     pass

    # def notifyAfterWrite(self):
    #     pass

    # def getGridOperator(self):
    #     pass

    # def initializeDelegate(context_java, device_java):
    #     pass

    # def getDelegate(self):
    #     pass

    # def release(self):
    #     pass

    # def getBuffer(self):
    #     pass


if __name__ == "__main__":
    pass

    # a_np = np.random.rand(50000).astype(np.float32)
    # b_np = np.random.rand(50000).astype(np.float32)
    # mf = cl.mem_flags
    # a_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)
    # b_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b_np)

    # prg = cl.Program(ctx, """
    # __kernel void sum(
    #     __global const float *a_g, __global const float *b_g, __global float *res_g)
    # {
    # int gid = get_global_id(0);
    # res_g[gid] = a_g[gid] + b_g[gid];
    # }
    # """).build()

    # res_g = cl.Buffer(ctx, mf.WRITE_ONLY, a_np.nbytes)
    # prg.sum(queue, a_np.shape, None, a_g, b_g, res_g)

    # res_np = np.empty_like(a_np)
    # cl.enqueue_copy(queue, res_np, res_g)

    # # Check on CPU with Numpy:
    # print(res_np - (a_np + b_np))
    # print((a_np + b_np))
    # print(np.linalg.norm(res_np - (a_np + b_np)))
