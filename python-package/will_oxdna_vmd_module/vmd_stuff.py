#!/home/wtk23/anaconda3/bin/python
import os
import psf_maker
import create_psf_auxfile
#from ctypes import cdll
#cfile = "ox2xyz.so"
#lib = cdll.LoadLibrary(cfile)
#lib.main("top", "dat", "test")


class Trajectory():
    def __init__(self,top_fname,dat_fname,input):
        self.top_fname = top_fname
        self.dat_fname = dat_fname

    def make_xyz_file(self,xyz_fname):
        # how to call a c file from Python
        os.system("./a.out > xyz.xyz")
        pass
    
    def make_energy_file(self):
        os.system("DNAnalysis ./input-anal trajectory_file=dat > ENERGIES.dat")

    def do_stuff(self):
        create_psf_auxfile.read_stuff("ENERGIES.dat")
    
    def make_psf(self):
        psf_maker.write_psf(self.top_fname)
        
    def read_energy_into_memory(self):
        pass

    def call_vmd(self):
        pass

t = Trajectory("top","dat","input")
t.make_xyz_file("test")
t.do_stuff()
t.make_psf()
