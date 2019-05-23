#!/bin/env python
#
# Setup python package
#

from distutils.core import setup

# make the package
setup(name='mediaviz',
      version='0.1',
      description='New media (film, tv, music) recommendation system with Web GUI',
      author='Samuel Rohrer',
      url='https://srohrer32.github.io',
      py_modules = ['impl']
      )
