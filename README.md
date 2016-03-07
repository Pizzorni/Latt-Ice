# Latt-Ice
#### A population dynamic simulator inspired by Wa-Tor

## Usage
### Simulator
python lattice.py [-h] [-p PENG] [-b BEAR] [-d DIM] [-g GEN] [-o OUT]

For example, if I wanted to run a simulation with 100 penguins and 50 bears on a 5x5 lattice for 100 generations and write the output to a file called "mysim.out" I would type

python lattice.py -p 100 -b 50 -d 5 -g 100 -o mysim.out

### Visualization

pythong animation.py [filename]

If no filename, reads from "lattice.frames"

