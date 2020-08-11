#!/bin/env python
#
# Setup python package
#

from distutils.core import setup

# make the package
setup(name='mediaviz',
      version='1.1',
      description='New media (film, tv, music) recommendation system with Web GUI',
      author='Samuel Rohrer',
      url='https://srohrer32.github.io',
      license='GPL-3.0',
      py_modules = ['impl']
      )
