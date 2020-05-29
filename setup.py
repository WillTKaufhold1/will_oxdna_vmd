from setuptools import setup, find_packages, Extension

module1 = Extension('oxdna-vmd',
                    sources = ['oxdna-vmd/ox2xyzmodule.c'])

setup (name = 'oxdna-vmd',
       version = '0.1',
       description = 'vmd support for oxdna trajectories',
       author = 'Will T Kaufhold',
       author_email = 'wtk23@cam.ac.uk',
       url = "https://github.com/WillTKaufhold1/will_oxdna_vmd",
       ext_modules = [module1])
