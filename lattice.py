import argparse
import simulator as sim
import visualizer as vis

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-p', '--peng', type=int, 
                    help='initial penguin population size')
  parser.add_argument('-b', '--bear', type=int, 
                    help='initial bear population size')
  parser.add_argument('-d', '--dim', type=int, 
                    help='dimension of square world')
  parser.add_argument('-g', '--gen', type=int,
                    help='number of generations')
  parser.add_argument('-o', '--out', type=str,
                    help='frame output file')
  args = parser.parse_args()
  #Default simulation parameters
  num_peng = 50
  num_bear = 10
  dim = 10
  gen = 100
  outfile = "lattice.frames"
  if(args.peng):
    num_peng = args.peng
  if(args.bear):
    num_bear = args.bear
  if(args.dim):
    dim = args.dim
  if(args.gen):
    gen = args.gen
  if(args.out):
    outfile = args.out

  sim.run_simulation(num_peng, num_bear, dim, gen, outfile)
  vis.run_visualizer(outfile)

main()
