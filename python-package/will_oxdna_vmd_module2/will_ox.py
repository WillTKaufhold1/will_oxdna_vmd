#!/home/wtk23/anaconda3/bin/python
import os
import subprocess
import psf_maker
import process_energies

from ctypes import *

class Trajectory():
    def __init__(self,top_fname,dat_fname,input_fname, dir_name,energy_fname):
        self.top_fname = top_fname
        self.dat_fname = dat_fname
        self.input_fname = input_fname
        self.dir_name = dir_name
        self.energy_fname = energy_fname

    def make_xyz_file(self,xyz_fname):
        adder = CDLL("./ox2xyzmodule.so")
        
        result = adder.ox2xyz_run(
            str(self.dat_fname).encode("ascii"), str(self.top_fname).encode("ascii"),
str(self.energy_fname).encode("ascii")
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

t = Trajectory("top","dat","input","data","energy")
t.make_xyz_file("test")
t.make_energy_file()
t.process_energy_file()
t.make_psf()

#would be convenient to do all this in a new directory
