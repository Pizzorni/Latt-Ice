# Latt-Ice
#### A population dynamic simulator inspired by Wa-Tor

## Usage
### Simulator
python lattice.py [-h] [-p PENG] [-b BEAR] [-d DIM] [-g GEN] [-o OUT]

For example, if I wanted to run a simulation with 100 penguins and 50 bears on a 5x5 lattice for 100 generations and write the output to a file called "mysim.out" I would type

python lattice.py -p 100 -b 50 -d 5 -g 100 -o mysim.out

#### Defaults
Penguins: 5  
Bears: 5  
Dimensions: 5  
Generations: 100  
Out: lattice.frames  

### Visualization

python animation.py [filename]

If no filename, reads from "lattice.frames"

### Flags

| Short 	| Long          	| Description                              	|
|-------	|---------------	|------------------------------------------	|
| -p    	| --peng         	| number of penguins                      	|
| -b    	| --bear        	| number of bears                          	|
| -d    	| --dim         	| size of lattice (dim x dim)              	|
| -g    	| --gen         	| number of generations                   	|
| -o    	| --out         	| file to write frames to                 	|
| -h    	| --help        	| help I need somebody                     	| 

### Dependencies
  * Python 2.7
  * matplotlib
  * numpy

### TODO
 * organize code 
 * profile performance
 * add multiple algorithms for bear/penguin movement
  * evolutionary 
  * MCTS
 * build tool for batch simulation for different algorithm combinations 
 * 
