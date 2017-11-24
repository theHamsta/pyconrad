
# Copyright (C) 2010-2017 - Andreas Maier
# CONRAD is developed as an Open Source project under the GNU General Public License (GPL-3.0)

# all non-underscored names are exported unless __all__ is defined

import pkg_resources

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except:
    __version__ = 'unknown'


import jpype
from ._pygrid import PyGrid
from pyconrad._pyconrad import setup_pyconrad, start_gui, start_reconstruction_pipeline_gui, is_initialized, is_gui_started, terminate_pyconrad
from pyconrad._classgetter import ClassGetter
from .constants import java_float_dtype
from ._autocomplete_files.autocomplete_conrad import AutoCompleteConrad
from ._autocomplete import generate_autocomplete_file


def edu():
    if not _pyconrad.PyConrad().is_initialized:
        raise _pyconrad.PyConradNotInitializedError()

    return JPackage('edu')  # type: .AutoCompleteConrad.edu


def ij():

    if not _pyconrad.PyConrad().is_initialized:
        raise _pyconrad.PyConradNotInitializedError()

    return JPackage('ij')

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
