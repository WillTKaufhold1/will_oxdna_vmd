#!/home/wtk23/anaconda3/bin/python
import os
import subprocess
from . import psf_maker
from . import process_energies
from pathlib import Path
from ctypes import *

class Trajectory():
    def __init__(self, top_fname, dat_fname , dir_name, 
                 input_fname = None, prefix_name = "out"):
        self.top_fname = top_fname
        self.dat_fname = dat_fname
        self.prefix_name = prefix_name
        self.input_fname = input_fname
        self.dir_name = dir_name
        if not Path(self.dat_fname).is_file():
            raise Exception(f"{self.dat_fname} does not exist")
        if not Path(self.top_fname).is_file():
            raise Exception(f"{self.top_fname} does not exist")
        if self.input_fname != None and not Path(self.input_fname).is_file():
            raise Exception(f"{self.input_fname} does not exist")
        os.system(f"mkdir {dir_name}") 
    def make_xyz_file(self):
        libname = os.path.abspath(os.path.dirname(__file__))
        fnames = os.listdir(libname)
        our_fname = list(filter(lambda x : "ox2xyz" in x, fnames))[0] 
        libname = os.path.abspath(os.path.join(os.path.dirname(__file__), our_fname))
        mod = CDLL(libname)
        print (libname)
        print (os.getcwd())
        self.traj_fname = self.prefix_name+".xyz"

        mod.ox2xyz_run(
            str(self.dat_fname).encode("ascii"),
            str(self.top_fname).encode("ascii"),
            str(self.traj_fname).encode("ascii")
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
        #in principle we should also be able to make a top file which doesn't color code
