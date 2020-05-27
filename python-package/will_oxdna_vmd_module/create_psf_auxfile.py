#!/home/wtk23/anaconda3/bin/python

import numpy as np
import pandas as pd
import sys

def get_energies(lines):

    energy_dict = {}
    for line in lines:
        if line[0]+1 not in energy_dict:
            energy_dict[line[0]+1] = np.zeros(len(line)-2)
        if line[1]+1 not in energy_dict:
            energy_dict[line[1]+1] = np.zeros(len(line)-2)
        energy_dict[line[0]+1] += np.array(line[2:]) 
        energy_dict[line[1]+1] += np.array(line[2:]) 
    energy = []
    for key in np.arange(1,len(energy_dict)+1):
        energy.append(energy_dict[key])
    return np.array(energy)


def read_stuff(fname):
    NFRAMES = 0
    with open(fname,"r") as f :
        
        all_data = []
        local = []
        
        for i in f:

            if i[:2] == "#T":
                if local != []: 
                    energies = get_energies(local)
                    if all_data == []:
                        all_data = energies
                    else:
                        all_data += energies
                    local = []
                    NFRAMES += 1
            elif i[:2] == "#i":
                pass
            else:
                local.append(list(map(float,i.replace('\n','').split())))

    #id1 id2 FENE BEXC STCK NEXC HB CRSTCK CXSTCK DH total, t = 10000

    all_data = all_data / NFRAMES #normalization

    import pickle as pkl

    pkl.dump(all_data, open("averaged_data.pkl",'w+b'))








































