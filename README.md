# Will's oxDNA scripts for VMD

## Intro

I wanted to integrate oxDNA effectively into VMD. These are a collection of scripts that perform this integration. The reason I wanted effective integration was that I wanted to lever the VMD package ecosystem when analysing DNA origami. 

The scripts here take an oxDNA .dat file, and generate a .xyz file, and a .psf file. Locations of hydrogen bonding (HB) and phosphate repulsion (BB) sites are placed in the .xyz file, and bond connectivity is placed in the .psf file. Bond connectivity includes one bond between the HB site and BB site,and a second bond between BB sites that are connected.

There are also scripts here that extract energy profiles from simulation trajectories, and then colorcode nucleotdies in VMD according to energy value. Specifically nucleotdies can be colored according to each the value of each energy component in the oxDNA force field. These components can be: 

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

<img src="/images/2/CHAIN2.png" width="324" height="324">
Fig. 1: A section of DNA origami colored by strand id. The red strand is the scaffold.

<img src="/images/2/HB2.png" width="324" height="324">
Fig. 2: Colored by mean HB energy. dsDNA is colored red (large negative HB energy); ssDNA is colored blue (0 HB energy). Crossovers and the terminii of strands are colored somewhere between as hydrogen bonding occurs here but not as strongly as in the origami bulk.

<img src="/images/2/STCK2.png" width="324" height="324">
Fig. 3: Colored by stacking energy: red is highly stacked; blue is unstacked. Observe substantial reduction of stacking energy at crossovers in the origami bulk. ssDNA (colored blue in Fig. 2) still stacks strongly, possibly an artefact of the oxDNA force field, or maybe a real effect?

<img src="/images/2/CTSTACK2.png" width="324" height="324">
Fig. 4: Cross stacking 

<img src="/images/2/CXSTACK2.png" width="324" height="324">
Fig. 5: Co-axial stacking 
<img src="/images/2/FENE2.png" width="324" height="324">
Fig. 6: Colored by FENE potential (i.e. backbond connectivity cost). Since terminal nucleotides in strands only have one FENE potential instead of 2, these nucleotides have comparatively low FENE interaction energies. Noticce the strain in some of the helices, notably on the left; this indicates either compression or expansion.
<img src="/images/2/DH2.png" width="324" height="324">
Fig. 7: Debye-Huckel potential (i.e. electrostatic repulsion)
<img src="/images/2/TOTAL2.png" width="324" height="324">
Fig. 8: Total energy

## Requirements

In principle I designed these scripts for VMD. However, they may work with any other visualization toolkit that can read and .xyz and .psf file.

Python scripts need Python>=3.5 with numpy and pandas 

Generation of energy files require the (oxDNA) DNAnalysis package to be in PATH.

And I've only tested this on Linux, although it should probably work on OSX as well.

## Instructions for use

The general principle is to use DNAnalysis to generate an energy file detailing pairwise energies as a function of trajectory time, then use this energy file to construct a PSF. vmd can then read the PSF with which contains bond connectivity, and also read a converted xyz file which contains positional information. To trick vmd into color coding energies, the energy values are hidden in the charge attribute of the PSF. 

In the src directory, running the RUN.sh followed by the location of the the trajectory file and topology file should generate the relevant PSF files and XYZ files. Since energy is also generated, the input file which was used to run oxDNA is also needed.

The XYZ files are placed in 1.traj-xyz-generation directory, and the PSF files are placed in the 3.psf-generation directory.

## Example 

The example trajectory contains a short trajectory, with relevant PSF files. To look at the HB energy distribution,  run "vmd traj-HB.psf test.xyz", which should load the molecule. Subsequently in the vmd visualization menu, the color by section should be set to charge. For each PSF, coloring by strand is also possible. To do this, change the color by section to resid.






















