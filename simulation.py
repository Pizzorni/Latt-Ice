from random import randint
from animals import Bear
from animals import Penguin
population = []

for i in xrange(10):
  coin = randint(0,1)
  if coin == 1:
    population.append(Penguin(randint(0,20)))
  else:
    population.append(Bear(randint(0,20), randint(0,10)))

for animal in population:
  print animal

