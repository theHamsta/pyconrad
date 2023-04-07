#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for pyconrad.

    This file was generated with PyScaffold 2.5.7.post0.dev6+ngcef9d7f, a tool that easily
    puts up a scaffold for your new Python project. Learn more under:
    http://pyscaffold.readthedocs.org/
"""

__author__ = "Stephan Seitz <stephan.seitz@fau.de>"
__copyright__ = "Andreas Maier <andreas.maier@fau.de> et al."
__license__ = """
pyCONRAD, python framework for cone beam radiology
Copyright (C) 2017 Stephan Seitz <stephan.seitz@fau.de>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import os
import sys

from pkg_resources import VersionConflict, require
from setuptools import setup
from setuptools.command.install import _install

# post install hint from:
# https://stackoverflow.com/questions/17806485/execute-a-python-script-post-install-using-distutils-setuptools

try:
    require('setuptools>=38.3')
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)


def _post_install(dir):
    cwd = os.path.join(dir, 'pyconrad')
    # os.path.append(os.path.join( os.path.dirname(__file__), 'pyconrad'))
    sys.path.append(cwd)
    import _download_conrad
    _download_conrad.download_conrad(cwd)
    print("CONRAD has been installed to %s" %
          _download_conrad.conrad_jar_dir())


class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib,),
                     msg="Installing Java dependencies...")


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def setup_package():
    setup(name='pyconrad',
          packages=['pyconrad', 'pyconrad_examples'
                    ],
          version="0.7.10",
          author='Andreas Maier',
          author_email='andreas.maier@fau.de',
          license='GPL 3.0',
          use_pyscaffold=True,
          install_requires=['jpype1 @ git+https://github.com/theHamsta/jpype@pyconrad',
              'numpy',
              'nibabel',
              'pathlib',
              'urllib3',
              'pyevtk',
              'setuptools',
              'procbridge',
              'cppimport',
              'joblib',
              'appdirs',
              'pydicom',
              'tqdm',
              ],
          extras_require={
              'opencl': ['pyopencl'],
              'vtk': ['vtk'],
              },
          cmdclass={'install': install},
          url='https://git5.cs.fau.de/PyConrad/pyCONRAD/',
          description='Python wrapper for CONRAD (https://www5.cs.fau.de/conrad/), a framework for cone beam radiography',  # noqa
          long_description=read('README.rst'),
          entry_points={
              'gui_scripts': [
                  'conrad = pyconrad._scripts:start_pyconrad',
                  'conrad_imagej = pyconrad._scripts:start_conrad_imagej',
                  'pyconrad_run = pyconrad._pyconrad_run:main'
              ],
          },
          setup_requires=['pytest-runner'],
          tests_require=['pytest', 'pytest-cov'],
          data_files=[
              ('share/applications', ['data_files/5.cs.fau.conrad.desktop',
                                      'data_files/5.cs.fau.conrad_imagej.desktop'])]
          )
    # setup_requires=['six', 'pyscaffold>=2.5a0,<2.6a0'] + sphinx,
    # use_pyscaffold=True)


if __name__ == "__main__":
    setup_package()
