#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for pyconrad.

    This file was generated with PyScaffold 2.5.7.post0.dev6+ngcef9d7f, a tool that easily
    puts up a scaffold for your new Python project. Learn more under:
    http://pyscaffold.readthedocs.org/
"""

import os
import sys
from distutils.command.install import install as _install
from distutils.core import setup

from setuptools import setup

# post install hint from:
# https://stackoverflow.com/questions/17806485/execute-a-python-script-post-install-using-distutils-setuptools
def _post_install(dir):
    cwd=os.path.join(dir, 'pyconrad')
    #os.path.append(os.path.join( os.path.dirname(__file__), 'pyconrad'))
    sys.path.append(cwd)
    import download_conrad
    download_conrad.download_conrad(cwd)
    print("CONRAD has been installed to %s" % download_conrad.conrad_jar_dir())


class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib,),
                     msg="Installing Java dependencies...")




def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup( name='pyconrad',
           version='change_version_manually_in_setup.py_when_uploading_via_twine',
           packages=['pyconrad'],
           author='Andreas Maier',
           author_email='andreas.maier@fau.de',
           install_requires=[
               'jpype1','numpy', 'pathlib', 'urllib3'
           ],
           cmdclass={'install': install},
           url='https://git5.cs.fau.de/PyConrad/pyCONRAD/'
           )
        #setup_requires=['six', 'pyscaffold>=2.5a0,<2.6a0'] + sphinx,
          #use_pyscaffold=True)



if __name__ == "__main__":
    setup_package()
