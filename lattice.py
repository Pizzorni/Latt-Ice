import argparse
from animals import Animal as anml
from simulation import Simulation as sim
import numpy as np

world = []


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-p', '--peng', type=int, 
                    help='initial penguin population size')
  parser.add_argument('-b', '--bear', type=int, 
                    help='initial bear population size')
  parser.add_argument('-d', '--dim', type=int, 
                    help='dimension of square world')
  args = parser.parse_args()

  #Default simulation parameters
  num_peng = 20
  num_bear = 10
  dim = 100
  if(args.peng):
    num_peng = args.penguin
  if(args.bear):
    num_bear = args.bear
  if(args.dim):
    dim = args.dimension
  # Custom dtype for usage with np arrays
  # (species, age, energy, speed)
  # Species: Empty -> 0, Penguin -> 1, Bear ->2
  animal_dt = np.dtype([('species', np.int8), ('age', np.int8),
        ('energy', np.int8), ('speed', np.int8)])
  global world
  world = np.zeros([dim,dim], dtype=animal_dt) 
  world_init(num_peng, num_bear, dim)
  #for t in world:
   # print t
  

def world_init(num_peng, num_bear, dim):
  global world
  to_gen = [0, num_peng, num_bear]
  while(to_gen[anml.PENGUIN] > 0 or to_gen[anml.BEAR] > 0):
    rand_x = np.random.randint(0,(dim -1))
    rand_y = np.random.randint(0,(dim -1))
    #if cell is empty, create new species
    if(world[rand_x][rand_y][0] == 0):
      species = np.random.randint(1,3)
      #print "Species being created: " + str(species)
      if(species == anml.PENGUIN):
        age = np.random.randint(1,(sim.P_AGE -1))
        energy = sim.P_ENERGY
        speed = sim.P_SPEED
      if(species == anml.BEAR):
        age = np.random.randint(1,(sim.B_AGE -1))
        energy = sim.B_ENERGY
        speed = sim.P_SPEED
      world[rand_x][rand_y] = (species, age, energy, speed)
      print world[rand_x][rand_y]
      to_gen[species] -= 1
  
  
 
main()
