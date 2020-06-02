#/home/wtk23/anaconda3/bin/python

from oxdnavmd import Trajectory
import sys
#lets do this properly with argparser later

if len(sys.argv[1:]) != 2:
    raise Exception("fuck you")

dat,top = sys.argv[1:]

t = Trajectory(top,dat,"data")
t.make_xyz_file()
t.make_psf()

