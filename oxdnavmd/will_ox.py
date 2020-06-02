#!/home/wtk23/anaconda3/bin/python
import os
import subprocess
from . import psf_maker
from . import process_energies

from ctypes import *

class Trajectory():
    def __init__(self,top_fname,dat_fname,input_fname, dir_name):
        self.top_fname = top_fname
        self.dat_fname = dat_fname
        self.input_fname = input_fname
        self.dir_name = dir_name
    def make_xyz_file(self,xyz_fname):
        libname = os.path.abspath(os.path.dirname(__file__))
        fnames = os.listdir(libname)
        our_fname = list(filter(lambda x : "ox2xyz" in x, fnames))[0]
        libname = os.path.abspath(os.path.join(os.path.dirname(__file__), our_fname))
        print ("call")
        mod = CDLL(libname)
        print ("call2") 
        result = mod.ox2xyz_run(
            str(self.dat_fname).encode("ascii"), 
            str(self.top_fname).encode("ascii"),
                    )
    
    def make_energy_file(self):
        suffix_string = "analysis_data_output_1 = {\nname = stdout\nprint_every = 1\ncol_1 = {\ntype=pair_energy}}"
        os.system(f'echo "{suffix_string}" > {self.dir_name}/suffix_file')
        os.system(f"cat {self.dir_name}/{self.input_fname} {self.dir_name}/suffix_file > {self.dir_name}/input_vmd")
        os.system(f"DNAnalysis ./{self.dir_name}/input_vmd trajectory_file={self.dat_fname} > {self.dir_name}/ENERGIES.dat")

    def process_energy_file(self):
        process_energies.read_stuff(f"{self.dir_name}/ENERGIES.dat",self.dir_name)
    
    def make_psf(self):
        psf_maker.write_psf(self.top_fname,self.dir_name)
        
    def call_vmd(self):
        pass

t = Trajectory("top","dat","input","data")
t.make_xyz_file("test")
t.make_energy_file()
t.process_energy_file()
t.make_psf()

