import argparse
from animals import Animal as anml
from simulation import Simulation as sim
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


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
  dim = 100
  gen = 1000
  if(args.peng):
    num_peng = args.peng
  if(args.bear):
    num_bear = args.bear
  if(args.dim):
    dim = args.dim
  if(args.gen):
    gen = args.gen

  # Custom dtype for usage with np arrays
  # (species, age, energy, speed)
  # Species: Empty -> 0, Penguin -> 1, Bear ->2
  animal_dt = np.dtype([('species', np.int8), ('age', np.int8),
        ('energy', np.int8), ('speed', np.int8), ('eaten', np.int8)])

  world = np.zeros([dim,dim], dtype=animal_dt) 
  world_init(num_peng, num_bear, dim)
  
  #plt.ion()
  #plt.axis('off')
  #fig = plt.figure()
  #ax = fig.add_subplot(111)
  #ax.set_xlim(0,dim)
  #ax.set_ylim(0,dim)
  #ax.get_xaxis().set_visible(False)
  #ax.get_yaxis().set_visible(False)
  peng_x, peng_y, bear_x, bear_y = generate_plot(population)
  #scat1 = ax.scatter(peng_x, peng_y, color = 'green')
  #scat2 = ax.scatter(bear_x, bear_y, color = 'red')
  #fig.canvas.draw()
  print "Initial number of penguins: " + str(num_peng)
  print "Initial number of bears: " + str(num_bear)
  for g in range(gen):
    np.random.shuffle(population)
    while(len(population) > 0):
      animal = population.pop()
      if(world[animal]['species'] == anml.PENGUIN):
        simulate_penguin(animal)
      else:
        simulate_bear(animal)
    new_pop = list(set(new_pop))
    for beasty in new_pop:
      population.append(beasty)
    new_pop = []
    peng_x, peng_y, bear_x, bear_y = generate_plot(population)
    #ax.clear()
    #ax.get_xaxis().set_visible(False)
    #ax.get_yaxis().set_visible(False)
    #scat1 = ax.scatter(peng_x, peng_y, color = 'green')
    #scat2 = ax.scatter(bear_x, bear_y, color = 'red')
    #fig.canvas.draw()
  finbear = 0
  finpeng = 0
  unaccounted = 0
  for beast in population:
    if(world[beast]['species'] == anml.PENGUIN):
      finpeng += 1
    elif(world[beast]['species'] == anml.BEAR):
      finbear += 1
    else:
      unaccounted += 1
  print "Final number of penguins: " + str(finpeng)
  print "Final number of bears: " + str(finbear)
  print "Unaccounted for cells: " + str(unaccounted)


def world_init(num_peng, num_bear, dim):
  global world
  global population
  while(num_peng > 0):
    x = np.random.randint(0,dim)
    y = np.random.randint(0,dim)
    if(world[x][y][0] == 0):
      age = np.random.randint(1,sim.P_AGE)
      world[x][y] = (anml.PENGUIN, age, sim.P_ENERGY, sim.P_SPEED, 0)
      population.append((x,y))
      num_peng -= 1
  while(num_bear > 0):
    x = np.random.randint(0,dim)
    y = np.random.randint(0,dim)
    if(world[x][y][0] == 0):
      age = np.random.randint(1,sim.B_AGE)
      world[x][y] = (anml.BEAR, age, sim.B_ENERGY, sim.B_SPEED, 0)
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
  eaten = penguin['eaten']
  if(eaten == 1):
    world[x][y] = (anml.EMPTY, 0, 0, 0, 0)

  elif(free_cells):
    move_to = free_cells[np.random.randint(len(free_cells))]
    #move and add penguin to simulated population
    new_pop.append(move_to)
    world[move_to] = penguin
    world[x][y] = (anml.EMPTY, 0, 0, 0, 0)

    if(reproduce == sim.P_AGE):
      baby_peng = (anml.PENGUIN, 1, sim.P_ENERGY, sim.P_SPEED, 0)
      #add baby penguin to population yet to be simulated
      new_pop.append((x,y))
      world[x][y] = baby_peng
  else:
    new_pop.append((x,y))
    world[x][y] = penguin

def simulate_bear(bear_coords):
  global world
  global population
  global new_pop
  x = bear_coords[0]
  y = bear_coords[1]

  free_cells = hunt_penguins(x,y)
  bear = world[x][y]
  bear['age'] += 1
  bear['energy'] -= 1
  reproduce = bear['age']
  bear['age'] = bear['age'] % sim.B_AGE
  survive = bear['energy']

  if(survive == 0):
    world[x][y] = (anml.EMPTY, 0, 0, 0, 0)
    print "bear dead"
  elif(free_cells):
    move_to = free_cells[np.random.randint(len(free_cells))]
    world[x][y] = (anml.EMPTY, 0, 0, 0, 0)
    if(world[move_to]['species'] == anml.PENGUIN):
      world[move_to]['eaten'] = 1
      bear['energy'] += 5
    world[move_to] = bear
    new_pop.append(move_to)
    if(reproduce == sim.B_AGE):
      baby_bear = (anml.BEAR, 1, sim.B_ENERGY, sim.B_SPEED, 0)
      new_pop.append((x,y))
      world[x][y] = baby_bear
      print "baby bear"
  else:
    new_pop.append((x,y))
    world[x][y] = bear


def get_moves(x,y):
  dim = world.shape[0]
  new_loc = [(x+i , y+j) for i,j in [(i,j) for 
            i in range(-1,2) for j in range (-1,2)]]
  new_loc = [(x%dim, y%dim) for x,y in new_loc]
  free_loc = []
  for n in new_loc:
    #construct list of free spaces
    if world[n][0] == anml.EMPTY and n != (x,y):
      free_loc.append(n)
  return free_loc

def hunt_penguins(x,y):
  dim = world.shape[0]
  new_loc = [(x+i , y+j) for i,j in [(i,j) for 
            i in range(-1,2) for j in range (-1,2)]]
  new_loc = [(x%dim, y%dim) for x,y in new_loc]
  free_loc = []
  peng_loc = []
  for n in new_loc:
    #construct list of free spaces and spaces with penguins
    if world[n][0] == anml.EMPTY and n!= (x,y):
      free_loc.append(n)
    if world[n][0] == anml.PENGUIN:
      peng_loc.append(n)
  if len(peng_loc) > 0:
    return peng_loc
  else:
    return free_loc


def generate_plot(population):
  bear_x = []
  bear_y = []
  peng_x = []
  peng_y = []
  for point in population:
    if world[point]['species'] == anml.BEAR:
      bear_x.append(point[0])
      bear_y.append(point[1])
    else:
      peng_x.append(point[0])
      peng_y.append(point[1])

  return peng_x, peng_y, bear_x, bear_y








main()
