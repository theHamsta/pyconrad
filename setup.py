#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for pyconrad.

    This file was generated with PyScaffold 2.5.7.post0.dev6+ngcef9d7f, a tool that easily
    puts up a scaffold for your new Python project. Learn more under:
    http://pyscaffold.readthedocs.org/
"""

import sys
from setuptools import setup

import os
from distutils.core import setup
from distutils.command.install import install as _install


def _post_install(dir):
    cwd=os.path.join(dir, 'pyconrad')
    print(cwd)


class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib,),
                     msg="Running post install task")




def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup( name='pyconrad',
        version='0.0.1',
           packages=['pyconrad'],
           author='Andreas Maier',
           author_email='andreas.maier@fau.de',
           install_requires=[
               'jpype1','numpy', 'pathlib', 'pyconrad_java'
           ],
           dependency_links=[
               "git+https://git5.cs.fau.de/PyConrad/pyconrad_java.git#egg=pyconrad-java-0.0.1"
           ],
           cmdclass={'install': install},
           url='https://git5.cs.fau.de/PyConrad/pyCONRAD/',
           download_url='https://git5.cs.fau.de/PyConrad/pyCONRAD/repository/archive.tar.gz?ref=0.0.1')
        #setup_requires=['six', 'pyscaffold>=2.5a0,<2.6a0'] + sphinx,
          #use_pyscaffold=True)



if __name__ == "__main__":
    setup_package()
