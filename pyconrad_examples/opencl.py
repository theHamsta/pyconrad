import pyconrad.autoinit
import pyopencl.clrandom
# import gputools

_ = pyconrad.ClassGetter(
    'edu.stanford.rsl.tutorial.phantoms',
)  # type: pyconrad.AutoCompleteConrad


# create phantom
phantom2d = _.MickeyMouseGrid2D(200, 200)
phantom2d.show()

# to device
phantom_cl = _.OpenCLGrid2D(phantom2d)
# add noise
random_gen = pyopencl.clrandom.ThreefryGenerator(
    pyconrad.opencl.get_conrad_context())
random_gen.fill_normal(phantom_cl.as_clarray())
phantom_cl.show()
