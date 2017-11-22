
# Copyright (C) 2010-2017 - Andreas Maier
# CONRAD is developed as an Open Source project under the GNU General Public License (GPL-3.0)

# all non-underscored names are exported unless __all__ is defined

import pkg_resources

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except:
    __version__ = 'unknown'


from jpype import JDouble, JArray, JInt, JString, JShort, JProxy, JByte, JBoolean, JChar, JLong, JFloat, JClass, JIterator, JavaException, java, JPackage
from ._pygrid import PyGrid, ndarray_to_grid, grid_to_ndarray
from pyconrad._pyconrad import setup_pyconrad, start_imagej, start_reconstruction_pipeline, is_initialized, is_gui_started, stop_gui
from pyconrad._classgetter import ClassGetter
from .constants import java_float_dtype
from .download_conrad import download_conrad, conrad_jar_dir, conrad_jar_path
from ._imageutils import ImageUtil
from ._autocomplete_files.autocomplete_conrad import AutoCompleteConrad
from ._autocomplete import generate_autocomplete_file


def edu():
    if not _pyconrad.PyConrad().is_initialized:
        raise _pyconrad.PyConradNotInitializedError()

    return JPackage('edu')


def ij():

    if not _pyconrad.PyConrad().is_initialized:
        raise _pyconrad.PyConradNotInitializedError()

    return JPackage('edu')

# class pyconrad:
#
#     @property
#     def edu(self):
#         return JPackage('edu')
#
#     @property
#     def ij(self):
#         return JPackage('edu')


class PyConrad(_pyconrad.PyConrad):

    def __init__(self):
        print("Use of class PyConrad deprecated")
