import argparse
from animals import Animal as anml
from simulation import Simulation as sim
import numpy as np
import copy

world = []
population = []
new_pop = []

def main():
  global world
  global population
  global new_pop

  parser = argparse.ArgumentParser()
  parser.add_argument('-p', '--peng', type=int, 
                    help='initial penguin population size')
  parser.add_argument('-b', '--bear', type=int, 
                    help='initial bear population size')
  parser.add_argument('-d', '--dim', type=int, 
                    help='dimension of square world')
  parser.add_argument('-g', '--gen', type=int,
                    help='number of generations')
  args = parser.parse_args()
  #Default simulation parameters
  num_peng = 20
  num_bear = 10
  dim = 20
  gen = 100
  if(args.peng):
    num_peng = args.penguin
  if(args.bear):
    num_bear = args.bear
  if(args.dim):
    dim = args.dimension
  if(args.gen):
    gen = args.gen

  # Custom dtype for usage with np arrays
  # (species, age, energy, speed)
  # Species: Empty -> 0, Penguin -> 1, Bear ->2
  animal_dt = np.dtype([('species', np.int8), ('age', np.int8),
        ('energy', np.int8), ('speed', np.int8)])

  world = np.zeros([dim,dim], dtype=animal_dt) 
  world_init(num_peng, num_bear, dim)
  count = 0

  print "Initial pop size: " + str(len(population))
  for g in range(gen):
    print "Generation: " + str(g)
    print "Pop size: " + str(len(population))
    np.random.shuffle(population)
    while(len(population) > 0):
      animal = population.pop()
      if(world[animal]['species'] == anml.PENGUIN):
        simulate_penguin(animal)
      else:
        simulate_bear(animal)
    print "pop before copy: " + str(len(population))
    print "babies before wipe: " + str(len(new_pop))
    for beasty in new_pop:
      population.append(beasty)
    new_pop = []
    print "pop after babies: " + str(len(population))
  print "Final pop size: " + str(len(population))

  

def world_init(num_peng, num_bear, dim):
  global world
  global population
  while(num_peng > 0):
    x = np.random.randint(0,dim)
    y = np.random.randint(0,dim)
    if(world[x][y][0] == 0):
      age = np.random.randint(1,sim.P_AGE)
      world[x][y] = (anml.PENGUIN, age, sim.P_ENERGY, sim.P_SPEED)
      population.append((x,y))
      num_peng -= 1
  while(num_bear > 0):
    x = np.random.randint(0,dim)
    y = np.random.randint(0,dim)
    if(world[x][y][0] == 0):
      age = np.random.randint(1,sim.B_AGE)
      world[x][y] = (anml.BEAR, age, sim.B_ENERGY, sim.B_SPEED)
      population.append((x,y))
      num_bear -= 1

def simulate_penguin(penguin_coords):
  global world
  global population
  global new_pop
  x = penguin_coords[0]
  y = penguin_coords[1]

  free_cells = get_moves(x,y)
  penguin = world[x][y]
  penguin['age'] += 1
  reproduce = penguin['age']
  penguin['age'] = penguin['age'] % sim.P_AGE

  if(free_cells):
    move_to = free_cells[np.random.randint(len(free_cells))]
    #move and add penguin to simulated population
    new_pop.append(move_to)
    world[move_to] = penguin
    world[x][y] = (anml.EMPTY, 0, 0, 0)

    if(reproduce == sim.P_AGE):
      baby_peng = (anml.PENGUIN, 1, sim.P_ENERGY, sim.P_SPEED)
      #add baby penguin to population yet to be simulated
      new_pop.append((x,y))
      world[x][y] = baby_peng
      print "reproduced!"
  else:
    new_pop.append((x,y))
    world[x][y] = penguin

def simulate_bear(bear_coords):
  global world
  global population
  global new_pop
  x = bear_coords[0]
  y = bear_coords[1]
  new_pop.append((x,y))

def get_moves(x,y):
  dim = world.shape[0]
  new_loc = [(x+i , y+j) for i,j in [(i,j) for 
            i in range(-1,2) for j in range (-1,2)]]
  new_loc = [(x%dim, y%dim) for x,y in new_loc]
  free_loc = []
  for n in new_loc:
    #construct list of free spaces
    if world[n][0] == anml.EMPTY and n != (x,y):
      free_space = True
      free_loc.append(n)
  return free_loc



main()
