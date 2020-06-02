#!/home/wtk23/anaconda3/bin/python

import numpy as np
import pandas as pd
import sys
from functools import reduce
from copy import copy

def double_energy(energy_data):
    sanc_energy = np.array(list(zip(list(energy_data),list(energy_data),))).flatten()
    sanc_energy = np.floor(sanc_energy*10000)/10000 
    return sanc_energy

def write_psf(topfile,dump_dirname,use_energies = False):

    with open(topfile,'r') as f: data = list(map(lambda x :x.replace('\n',''),f.readlines()))

    Nts = int(data[0].split(' ')[0])
    Nstrands = int(data[0].split(' ')[1])

    all_data = np.array(list(map(lambda x : x.split(' '), data[1:])))

    all_dict = {}

    all_dict['atom id'] = np.arange(1,len(all_data)*2+1)
    all_dict['segment name'] = ['U']*Nts*2
    all_dict['residue id'] = np.array(list(zip([i[0] for i in all_data],
                                   [i[0] for i in all_data]))).flatten()
    all_dict['residue name'] = ['MET']*Nts*2
    all_dict['atom name'] = ['C']*Nts*2 #really should make some changes here.
    all_dict['atom type'] = ['C']*Nts*2
    all_dict['charge'] = ['0']*Nts*2
    all_dict['mass'] = ['1']*Nts*2
    all_dict['zeroes'] = ['0']*Nts*2


    if use_energies:
        import pickle as pkl
        energy_data = np.array(pkl.load(open(f'./{dump_dirname}/averaged_data.pkl','rb'))) # list of values
        #id1 id2 FENE BEXC STCK NEXC HB CRSTCK CXSTCK DH total, t = 10000
        #consider applying a standard scaler to the energy_data?
        energy_dict = {}
        for index,name_ in enumerate(["FENE","BEXC","STCK","NEXC","HB","CRSTCK","CXSTACK","DH","total"]):
            energy_dict[name_] = energy_data[:,index]
    else:
        energy_dict = {"RAW": list(np.zeros(Nts))} #energy_data?

    #make sure if i haven't got an energy file to parse from i just parse normal.
    #want to make loads of different kinds of atoms files
    for key in energy_dict:
        new_dict = copy(all_dict)
        new_dict['charge'] = double_energy(energy_dict[key])

        breakpoint()

        df = pd.DataFrame.from_dict(new_dict)
        n = np.array(df)
        np.savetxt(f"ATOMS.{key}.txt", n, fmt = "% 8s% 4s% 5s% 7s% 5s% 5s% 12s% 14s% 12s")


    hydrogen_bonds = [(i,i+1) for i in range(1,Nts*2+1,2)]

    backbone_bonds = []
    for i,val in enumerate(all_data[:,3]):
        val = int(val)
        if val != -1:
            backbone_bonds.append((i*2+1,(i+1)*2+1))

            
    all_bonds = backbone_bonds + hydrogen_bonds

    #need to do some hacky shit to deal with the situation where the number of bonds is not divisible by 4. In principle you can avoid this by clever string parsing, but fuck it...
    extra = len(all_bonds)%4

    if extra != 0:
        all_bonds = all_bonds + [all_bonds[-1]] * (4-extra)
        
    tmp = np.array([all_bonds[i*4:(i+1)*4] for i in range(int(np.ceil(len(all_bonds)/4)))])

    new_hbonds = [i.flatten() for i in tmp]
            
    np.savetxt("BONDS.txt",new_hbonds, fmt = "% 8s% 8s% 8s% 8s% 8s% 8s% 8s% 8s")

    with open("header1","w+") as f:
        f.write(f"{len(df)} !NATOM\n")
    with open("header2","w+") as f:
        f.write(f"{len(all_bonds)} !NBOND\n")

    import os
    for key in energy_dict:
        os.system(f"cat header1 ATOMS.{key}.txt header2 BONDS.txt > {dump_dirname}/traj-{key}.psf")
        os.system(f"rm ATOMS.{key}.txt")
    os.system("rm BONDS.txt")
    os.system("rm header1")
    os.system("rm header2")
