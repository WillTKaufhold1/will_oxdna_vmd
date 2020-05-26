# dat, top, input are our inputs
cd 1.traj-xyz-generation && ./ox2xyz.exe $1 $2 > test.xyz
echo "generated xyz files"
cd ..
cd 2.energy-file-generation/ && DNAnalysis ./input-anal trajectory_file=../1.traj-xyz-generation/$1 > ENERGIES.dat
echo "generated energy files"
cd ..
cd 3.psf-generation/ && ./create_psf_auxfile ../2.energy-file-generation/ENERGIES.dat
echo "generated auxilary psf file"
./ox2xyz.py top 
echo "generated psf file"
echo "all done"

