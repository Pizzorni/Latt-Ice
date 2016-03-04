from random import randint
from animals import *
import argparse
import numpy as np


def main():
  parser = argparse.argumentParser()
  parser.add_argument('-p', '--penguin', type=int, 
                    help='initial penguin population size')
  parser.add_argument('-b', '--bear', type=int, 
                    help='initial bear population size')
  parser.add_argument('-d', '--dimension', type=int, 
                    help='dimension of square world')

  max_peng = 20
  max_bear = 10
  dim = 100

  if(args.penguin):
    max_peng = args.penguin
  if(args.bear):
    max_bear = args.bear
  if(args.dimension):
    dim = args.dimension

  # Custom dtype for usage with np arrays
  #   
  animal_dt = np.dtype([('species', np.int8), ('age', np.int8),
        ('energy', np.int8), ('speed', np.int8)])

  arr = np.empty([dim,dim] dtype=animal_dt) 

def world_init(max_peng, max_bear, world_dim):
  
