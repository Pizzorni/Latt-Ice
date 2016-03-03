class Animal(object):
  def __init__(self, age, energy):
    self.age = age
    self.energy = energy

class Bear(Animal):
  def __init__(self, age, energy):
    super(Bear, self).__init__(age, energy)

class Penguin(Animal):
  def __init__(self, age):
    super(Penguin, self).__init__(age, 0)
