from pyconrad import PyConrad

# PyConrad is a singleton class
pyconrad = PyConrad()
# setup PyConrad
pyconrad.setup()
# Optional parameters for Java Virtual Machine RAM and own Java projects
# pyconrad.setup(max_ram = '8G', min_ram= '500M', dev_dirs=['path/to/project/with/own/java/classes']

# Create Phantom (edu.stanford.rsl.tutorial.phantoms.MickeyMouseGrid2D)
phantom = pyconrad.classes.stanford.rsl.tutorial.phantoms.MickeyMouseGrid2D(300, 300)
# Some packages can be accessed more easily
phantom2 = pyconrad.get_phantom_package().MickeyMouseGrid2D(200,200)

# Use Java method of class MickeyMouseGrid2D
phantom.show()

# start CONRAD GUI
pyconrad.start_conrad()

