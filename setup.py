from distutils.core import setup, Extension
from setuptools import find_packages


module1 = Extension("ox2xyzmodule",
            sources = ["ox2xyzmodule.c"])

setup (name = 'oxdnavmd',
       version = '0.1',
       description = 'vmd support for oxdna trajectories',
       author = 'Will T Kaufhold',
       author_email = 'wtk23@cam.ac.uk',
       url = "https://github.com/WillTKaufhold1/will_oxdna_vmd",
       licence = "GPL",
       packages = find_packages()
)

