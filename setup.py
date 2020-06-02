from setuptools import Extension, setup
from setuptools import find_packages

#there are problems with this.
module1 = Extension("oxdnavmd.ox2xyz",
            sources = ["./oxdnavmd/ox2xyzmodule.c"])

with open("README.md") as f: README = f.read()

setup (name = 'oxdnavmd',
       version = '0.21',
       description = 'vmd support for oxdna trajectories',
       long_description = README,
       long_description_content_type='text/markdown',
       author = 'Will T Kaufhold',
       author_email = 'wtk23@cam.ac.uk',
       url = "https://github.com/WillTKaufhold1/will_oxdna_vmd",
       licence = "GPL",
       packages = find_packages(),
       ext_modules = [module1])
