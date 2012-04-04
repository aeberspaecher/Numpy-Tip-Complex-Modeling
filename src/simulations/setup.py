'''
Created on Mar 19, 2012

@author: federicov
'''
## usage: python setup.py build_ext --inplace
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("cython_arc_distance", ["cython_arc_distance.pyx"], include_dirs=[numpy.get_include()])]
)
