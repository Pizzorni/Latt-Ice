import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import sys

if(len(sys.argv) > 1):
  infile = sys.argv[1]
  print infile
else:
  infile = "lattice.frames"

f = open(infile, 'r')
frames = f.read().split('\n')
f.close()

info = frames[0].split(':')
gen = int(info[0])
dim = int(info[1])

frames.remove(frames[0])
frames.remove('')

#chunk frames into individual generations
chunked_frames = [frames[i:i+dim] for i in 
                        xrange(0, len(frames), dim)] 


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(0,dim), ax.set_xticks([])
ax.set_ylim(0,dim), ax.set_yticks([])
peng_scat = ax.scatter(None, None, color = 'green')
bear_scat = ax.scatter(None, None, color = 'red')


def update(frame_number):
  frame = chunked_frames[frame_number]
  penguins = []
  bears = []
  for r in range(dim):
    for c in range(dim):
      species = frame[r][c]
      if species == '1':
        penguins.append((r,c))
      elif species == '2':
        bears.append((r,c))
  peng_scat.set_offsets(penguins)
  bear_scat.set_offsets(bears)
  label = "Generation: " + str(frame_number)
  plt.suptitle(label)

animation = FuncAnimation(fig, update, frames = gen, interval = 100)
plt.show()
