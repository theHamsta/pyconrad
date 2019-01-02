# %% [markdown]
# # Example Use in a Jupyter Notebook
# This code can be run as normal Python file or as Jupyter Notebook in [Visual Studio Code](https://code.visualstudio.com/) using the [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
# Follow the instructions [here](https://code.visualstudio.com/docs/python/editing#_jupyter-code-cells)
#
# Matplotlib sucks in real Python but is kind of okish in a Jupyter notebook. So `pyconrad.imshow` will use `matplotlib.pyplot.imshow` if it is running inside a Jupyter notebook.

# # Detect if Running in a Jupyter Notebook

# %%

import numpy as np
import time
import pyconrad.autoinit


def in_ipynb():
    """ Detects if running inside a Jupyter notebook.
    Modified from: https://stackoverflow.com/questions/15411967/how-can-i-check-if-code-is-executed-in-the-ipython-notebook
    """
    try:
        import IPython
        IPython.get_ipython().config
        return True
    except Exception as ex:
        return False


print(in_ipynb())
# %% [markdown]
# # Display Images with `pyconrad.imshow`
# Here you can see that pyconrad uses matplotlib when in Jupyter kernel

# %%

print('Enjoy white noise!')
for i in range(10):
    noise = np.random.rand(200, 200)
    pyconrad.imshow(noise, 'White noise')
    time.sleep(0.01)

pyconrad.close_all_windows()
