# Will's oxDNA scripts for VMD
https://packaging.python.org/tutorials/packaging-projects/

## Introduction

oxDNA visualization in VMD, with energy color coding.

The scripts here take an oxDNA .dat file, and generate a .xyz file and a .psf file. Locations of stacking (S) and phosphate repulsion (BB) sites are placed in the .xyz file, and bond connectivity is placed in the .psf file. Bond connectivity includes one bond between the S site and BB site,and a second bond between BB sites that are connected.

There are also scripts here that extract energy profiles from simulation trajectories, and then colorcode nucleotides in VMD according to energy value. Specifically, nucleotides can be colored according to each the value of each energy component in the oxDNA force field. These components can be: 

1. FENE : Finite extension non-linear elastic potential; backbone stretching. 
1. BEXC : Backbone excluded volume
1. STCK: Stacking energies
1. NEXC: Excluded volume
1. HB: Hydrogen bonding
1. CRSTCK: Cross stacking
1. CXSTACK: Coaxial stacking (i.e. encouraging helicity)
1. DH: Debye-Huckel electrostatic repulsion
1. total: total energy 

## Example rendered images

## Dependencies

1. Linux operating system (or OS X)
1. gcc 
1. Python >= 3.5
1. numpy 
1. scipy
1. oxDNA
1. ctypes

## Instructions for use

The general principle is to use DNAnalysis to generate an energy file detailing pairwise energies as a function of trajectory time, then use this energy file to construct a PSF. vmd can then read the PSF with which contains bond connectivity, and also read a converted xyz file which contains positional information. To trick vmd into color coding energies, the energy values are hidden in the charge attribute of the PSF. In principle this pacakge will eventually integrate fully into vmd as a nicer solution than this ad hoc method.

## Installation

If the given requirements are met, the software can be installed with the Python package manager pip:

``` 
pip install oxdnavmd
```

## Generating .xyz and .psf files



## Visualization

The example trajectory contains a short trajectory, with relevant PSF files. To look at the HB energy distribution,  run "vmd traj-HB.psf test.xyz", which should load the molecule. Subsequently in the vmd visualization menu, the color by section should be set to charge. For each PSF, coloring by strand is also possible. To do this, change the color by section to resid.


## Implementation

Everything is wrapped into a Python package. Bottlenecks in trajectory processing have been written in C, with Python wrappers, using ctypes.



















