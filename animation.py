import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure()
#ax = fig.add_axes(frameon = False)
#ax.set_xlim(0,dim), ax.set_xticks([])
#ax.set_ylim(0,dim), ax.set_yticks([])

f = open('test.out')
frames = f.read().split('\n')
info = frames[0].split(':')
gen = int(info[0])
dim = int(info[1])
f.close()



#def update(frame_number):
 # print "stuff"


#animation = FuncAnimation(fig, update, interval = 10)
#plt.show()
