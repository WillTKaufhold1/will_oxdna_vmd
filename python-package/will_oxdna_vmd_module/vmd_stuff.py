#/home/wtk23/anaconda3/bin/python

from ctypes import *

cfile = "ox2xyz.so"

class Trajectory():
    def __init__(self,top_fname,dat_fname,input):
        self.top_fname = top_fname
        self.dat_fname = dat_fname

    def make_xyz_file(self,xyz_fname):
        # how to call a c file from Python
        pass
    
    def make_energy_file(self):
        pass
    
     def read_energy_into_memory(self):
        pass

    def call_vmd(self):
        pass

