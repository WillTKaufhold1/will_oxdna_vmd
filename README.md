# Will's oxDNA scripts for VMD

## Intro

I wanted to integrate oxDNA effectively into VMD. These are a collection of scripts that perform this integration. The reason I wanted effective integration was that I wanted to lever the VMD package ecosystem when analysing DNA origami. 

The scripts here take an oxDNA .dat file, and generate a .xyz file, and a .psf file. Locations of hydrogen bonding (HB) and phosphate repulsion (BB) sites are placed in the .xyz file, and bond connectivity is placed in the .psf file. Bond connectivity includes one bond between the HB site and BB site,and a second bond between BB sites that are connected.

There are also scripts here that extract energy profiles from simulation trajectories, and then colorcode nucleotdies in VMD according to energy value. Specifically nucleotdies can be colored according to each the value of each energy component in the oxDNA force field. These components can be: 

(1) FENE : Finite extension non-linear elastic potential; backbone stretching. 
(2) BEXC
(3) STCK: Stacking energies
(4) NEXC: Excluded volume
(5) HB: Hydrogen bonding
(6) CRSTCK: Cross stacking
(7) CXSTACK: Unused
(8) DH: 
(9) total: total energy 

## Requirements

In principle I designed these scripts for VMD. However, they may work with any other visualization toolkit that can read and .xyz and .psf file.

Python scripts need Python>=3.5 with numpy and pandas 

F# scripts need an f# compiler

Generation of energy files require the (oxDNA) DNAnalysis package to be in PATH.

And I've only tested this on Linux, although it should probably work on OSX as well.

## Instructions for use











