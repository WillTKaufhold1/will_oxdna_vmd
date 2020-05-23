# Will's oxDNA scripts for VMD

## Intro

I wanted to integrate oxDNA effectively into VMD. These are a collection of scripts that perform this integration. The reason I wanted effective integration was that I wanted to lever the VMD package ecosystem when analysing DNA origami. 

The scripts here take an oxDNA .dat file, and generate a .xyz file, and a .psf file. Locations of hydrogen bonding (HB) and phosphate repulsion (BB) sites are placed in the .xyz file, and bond connectivity is placed in the .psf file. Bond connectivity includes one bond between the HB site and BB site,and a second bond between BB sites that are connected.

There are also scripts here that extract energy profiles from simulation trajectories, and then colorcode nucleotdies in VMD according to energy value. Specifically nucleotdies can be colored according to each the value of each energy component in the oxDNA force field. These components can be: 

1. FENE : Finite extension non-linear elastic potential; backbone stretching. 
1. BEXC
1. STCK: Stacking energies
1. NEXC: Excluded volume
1. HB: Hydrogen bonding
1. CRSTCK: Cross stacking
1. CXSTACK: Unused
1. DH: 
1. total: total energy 

## Example rendered images

<img src="/images/strand.png" width="324" height="324">
Fig. 1: A section of DNA origami colored by strand id. The red strand is the scaffold.

<img src="/images/HBs.png" width="324" height="324">
Fig. 2: Colored by mean HB energy. dsDNA is colored red (large negative HB energy); ssDNA is colored blue (0 HB energy). Crossovers and the terminii of strands are colored somewhere between as hydrogen bonding occurs here but not as strongly as in the origami bulk.

<img src="/images/stacking.png" width="324" height="324">
Fig. 3: Colored by stacking energy: red is highly stacked; blue is unstacked. Observe substantial reduction of stacking energy at crossovers in the origami bulk. ssDNA (colored blue in Fig. 2) still stacks strongly, possibly an artefact of the oxDNA force field, or maybe a real effect?

<img src="/images/FENE.png" width="324" height="324">
Fig. 4: Colored by FENE potential (i.e. backbond connectivity cost). Since terminal nucleotides in strands only have one FENE potential instead of 2, these nucleotides have comparatively low FENE interaction energies. Noticce the strain in some of the helices, notably on the left; this indicates either compression or expansion.

## Requirements

In principle I designed these scripts for VMD. However, they may work with any other visualization toolkit that can read and .xyz and .psf file.

Python scripts need Python>=3.5 with numpy and pandas 

F# scripts need an f# compiler

Generation of energy files require the (oxDNA) DNAnalysis package to be in PATH.

And I've only tested this on Linux, although it should probably work on OSX as well.

## Instructions for use

The general principle is to use DNAnalysis to generate an energy file detailing pairwise energies as a function of trajectory time, then use this energy file to construct a PSF. vmd can then read the PSF with which contains bond connectivity, and also read a converted xyz file which contains positional information. To trick vmd into color coding energies, the energy values are hidden in the charge attribute of the PSF. 

TODO: actually write instructions









